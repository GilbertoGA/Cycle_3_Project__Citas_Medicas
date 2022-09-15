from c3pAPP.models.usuario import User
from rest_framework import serializers

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id_usuario', 'username', 'password', 
                  'nombre', 'apellido', 'email', 'tipo_documento', 
                  'numero_documento', 'direccion']