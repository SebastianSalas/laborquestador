require 'sinatra'
require 'json'

set :bind, '0.0.0.0'

get '/' do
  content_type :json
  {mensaje: "Aplicación Ruby funcionando correctament"}.to_json

end

get '/servicio-marce' do
  content_type :json
  { mensaje: "¡Hola! soy Marcelo, estudiante de Ingeniería de Sistemas y entusiasta del tenis" }.to_json
end
