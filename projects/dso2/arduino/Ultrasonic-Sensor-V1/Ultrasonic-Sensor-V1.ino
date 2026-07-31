#include <Ultrasonic.h>
#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>

// Define o nome do sensor(ultrassom) e onde esta ligado o trig(12) e o echo(13) respectivamente
Ultrasonic ultrassom(12,13);  
WiFiServer server(80);

long distancia;

const char* ssid = "(((H)))";
const char* password = "vinips62";

void setup() {        
  Serial.begin(9600); //  Habilita Comunicação Serial a uma taxa de 9600 bauds.
  
  Serial.println();
  Serial.println();
  Serial.print("Conectando a rede ");
  Serial.println(ssid);
 
  WiFi.begin(ssid, password);  //  Inicia conexão com a rede wifi

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi conectado"); 
}

void loop(){
    
  distancia = ultrassom.Ranging(CM);  //  ultrassom.Ranging(CM) retorna a distancia em centimetros 
  
  Serial.print(distancia);  //  Imprime o valor da variável distancia 
  Serial.println("cm");
  delay(1000);
  
  //Check WiFi connection status
  if(WiFi.status()== WL_CONNECTED){  
    
    HTTPClient http;  // Declara objeto da classe HTTPClient
 
    http.begin("http://192.168.0.15:3333/sensor");  //  Destino da requisição
    http.addHeader("Content-Type", "text/plain");  //  Especifice content-type header
    
    //Send the request
    int httpCode = http.POST(distancia);   //  Envia a requisição
    String payload = http.getString();  //  Get the response payload
 
    Serial.println(payload);  //  Printa o conteudo da requisição
 
    http.end();  //  Fecha a conexão 
  }
}