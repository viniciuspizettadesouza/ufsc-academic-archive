from sys import modules
from .parser.cmmParser import cmmParser
from .parser.cmmVisitor import cmmVisitor
from typing import List
import ast

class astVisitor(cmmVisitor):
    def __init__(self, file_name):
        self.file_name = file_name
        self.func_table = {}

    def visitStart(self, ctx:cmmParser.StartContext):
        main_call = ast.Call(func=ast.Name(id='main', ctx=ast.Load()), args=[], keywords=[]) 
        main = ast.Expr(value=main_call)
        body = [self.visit(func) for func in ctx.func()]
        body.append(main)
        module = ast.Module(body=body, type_ignores=[])
        ast.fix_missing_locations(module)
        return module
    
    def visitFunc(self, ctx:cmmParser.FuncContext):
        name = ctx.name.text
        args = self.visit(ctx.args()) if ctx.args() else [] # List or arguments

        self.func_table[name] = ast.Name(id=name, ctx=ast.Load())

        self.id_table = {} # Function id table
        for arg in args:
            self.id_table[arg.arg] = ast.Name(id=arg.arg, ctx=ast.Load())


        body = self.visit(ctx.statms())

        return ast.FunctionDef(name=name, args=ast.arguments(posonlyargs=[], args=args,
                                                             kwonlyargs=[],
                                                             kw_defaults=[],
                                                             defaults=[]),
                              body=body, decorator_list=[])

    def visitStatms(self, ctx:cmmParser.StatmsContext):
        return [self.visit(stmt) for stmt in ctx.statm()]

    def visitWhile(self, ctx:cmmParser.WhileContext):
        test = self.visit(ctx.cond)
        body = self.visit(ctx.statms())
        return ast.While(test=test, body=body, orelse=[])

    def visitIf(self, ctx:cmmParser.IfContext):
        test = self.visit(ctx.cond)
        body = self.visit(ctx.then)
        orelse = self.visit(ctx.otherwise) if ctx.ELSE() else []
        return ast.If(test=test, body=body, orelse=orelse)
        
    def visitArgs(self, ctx:cmmParser.ArgsContext):
        return [ast.arg(arg=str(id)) for id in ctx.ID()]

    def visitCall(self, ctx:cmmParser.CallContext):
        id = ctx.name.text
        if id not in self.func_table:
            raise KeyError(self.file_name+':'+str(ctx.name.line)+':'+str(ctx.name.column)+' function '+id+' is not defined')
        return ast.Call(func=self.func_table[id], 
                        args=self.visit(ctx.exprs()), keywords=[])

    def visitExprs(self, ctx:cmmParser.ExprsContext):
        return [self.visit(x) for x in ctx.expr()]

    def visitAssign(self, ctx:cmmParser.AssignContext):
        expr = self.visit(ctx.expr())
        id = str(ctx.ID())
        if id not in self.id_table: # Create table entry if variable is not defined
            self.id_table[id] = ast.Name(id=id, ctx=ast.Load())
        return ast.Assign(targets=[ast.Name(id=id, ctx=ast.Store())], value=expr)

    def visitReturn(self, ctx:cmmParser.ReturnContext):
        return ast.Return(value=self.visit(ctx.expr()))

    def visitAtom(self, ctx:cmmParser.AtomContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.ID():
            id = str(ctx.ID())
            if id not in self.id_table:
                symbol = ctx.ID().getSymbol()
                raise KeyError(self.file_name+':'+str(symbol.line)+':'+str(symbol.column)+' variable '+id+' is not defined')
            return ast.Name(id=id, ctx=ast.Load())
        elif ctx.INT():
            return ast.Constant(value=int(str(ctx.INT())))
        elif ctx.call():
            return self.visit(ctx.call())
        elif ctx.INPUT():
            input_call = ast.Call(func=ast.Name(id='input', ctx=ast.Load()), 
                                  args=[], keywords=[])
            return ast.Call(func=ast.Name(id='int', ctx=ast.Load()), 
                            args=[input_call], keywords=[])

    def visitExpr(self, ctx:cmmParser.ExprContext):
        left = self.visit(ctx.left)
        if ctx.right: # >, <, >=, <=, ==, != 
            right = self.visit(ctx.right)

            op_map = {'<' : ast.Lt,
                      '>' : ast.Gt,
                      '>=': ast.LtE,
                      '<=': ast.GtE,
                      '==': ast.Eq,
                      '!=': ast.NotEq}

            op = op_map[ctx.op.text]()
            
            return ast.Compare(left=left, ops=[op], comparators=[right])
        else: # higher priority expsetion 
             return left 

    def visitSumm(self, ctx:cmmParser.SummContext):
        left = self.visit(ctx.left)
        if ctx.right:
            right = self.visit(ctx.right)
            if ctx.op.text == '+':
                op = ast.Add()
            elif ctx.op.text == '-':
                op = ast.Sub()
            
            return ast.BinOp(left=left, op=op, right=right)
        return left

    def visitMult(self, ctx:cmmParser.MultContext):
        left = self.visit(ctx.left)
        if ctx.right:
            right = self.visit(ctx.right)
            if ctx.op.text == '*':
                op = ast.Mult()
            elif ctx.op.text == '/':
                op = ast.FloorDiv()
            
            return ast.BinOp(left=left, op=op, right=right)
        return left

    def visitPrint(self, ctx:cmmParser.PrintContext):
        print_call = ast.Call(func=ast.Name(id='print', ctx=ast.Load()),
                              args=[self.visit(ctx.expr())], keywords=[])
        return ast.Expr(value=print_call)

