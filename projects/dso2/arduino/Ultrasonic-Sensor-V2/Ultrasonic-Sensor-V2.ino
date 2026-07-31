#include <Ultrasonic.h>
#include <ESP8266WiFi.h>

// Define o nome do sensor(ultrassom) e onde esta ligado o trig(12) e o echo(13) respectivamente
Ultrasonic ultrassom(12,13);  
WiFiServer server(80);

long distancia;

const char* ssid = "(((H)))";
const char* password = "vinips62";
 
void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
 
  server.begin();
  Serial.println("Server started");
 
  Serial.print("Use this URL : ");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/"); 
}
 
void loop() {

  distancia = ultrassom.Ranging(CM);  //  ultrassom.Ranging(CM) retorna a distancia em centimetros 
  
  Serial.print(distancia);  //  Imprime o valor da variável distancia 
  Serial.println("cm");

  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client) {
    return;
  }
 
  // Wait until the client sends some data
  Serial.println("new client");
  while(!client.available()){
    delay(100);
  }
 
  // Read the first line of the request
  String request = client.readStringUntil('\r');
  Serial.println(request);
  client.flush();
   
  // Return the response
  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html");
  client.println(""); //  do not forget this one
  client.println("<!DOCTYPE HTML>");
  client.println("<html>");  

  client.println("<h1>Testa se esta muito perto.</h1>");

  if(distancia < 10 ) {
    client.println("<p>Perto demais !</p>");
    client.println("<p>Valor percebido: </p>");    
    client.println("<p>");
    client.println(distancia);
    client.println("</p>");
  } else {
    client.println("<p>Nenhum perigo.</p>");
    client.println("<p>Valor percebido: </p>");
    client.println("<p>");
    client.println(distancia);
    client.println("</p>");
  }
  client.println("<a href=\"/test\">Clique aqui para testar!</a><br>");
  client.println("</html>");
   
  delay(100);
  Serial.println("Client disconnected");
  Serial.println("");
}
