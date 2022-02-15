import json
import sys

def successOutput (data):
  output = { "state": "success", "data": data }
  print(json.dumps(output))
  pass

def failureOutput (error):
  output = {
    "state": "failure",
    "data": {
      "message": str(error),
      "type": str(type(error))
    }
  }
  print(json.dumps(output))
  pass

# captura global de los errores
# si tu script falla en cualquier momento , tenes que capturar el error y devolverlo con la funcion 
# failureOutput(err)

def main (args):
  return args

try:
  result = main(sys.argv)
  successOutput(result)

except Exception as error:
  failureOutput(error)
