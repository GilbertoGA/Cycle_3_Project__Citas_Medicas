from rest_framework import serializers
from c3pAPP.models.asignacion_paciente import asignacion_paciente
from c3pAPP.serializers.pacienteSerializer import GETpacienteSerializer
from c3pAPP.serializers.personal_saludSerializer import personal_saludSerializer
from c3pAPP.serializers.familiarSerializer import familiarSerializer


class asignacion_pacienteSerializer(serializers.ModelSerializer):
    id_paciente = GETpacienteSerializer()
    id_personal = personal_saludSerializer()
    id_familiar = familiarSerializer()
    class Meta:
        model = asignacion_paciente
        fields = ['id', 'id_paciente', 'id_familiar', 'id_personal']
