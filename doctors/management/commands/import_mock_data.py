from django.core.management.base import BaseCommand
from doctors.models import Doctor

class Command(BaseCommand):
    help = 'Import mock data into the Doctor model'

    def handle(self, *args, **kwargs):
        # Dados dos médicos que você quer importar
        doctors = [
            {
                "id": 1,
                "valor_consulta": 340,
                "nome": "Dr. Ricardo Freire Gurgel",
                "especialidade": "Clínico Geral",
                "imagem": "https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Ricardo_Gurgel.jpeg",
                "visualizacoes": 407,
                "avaliacao": 4.8,
                "crm": "103621",
                "cidade": "São Paulo, SP",
                "descricao": "Médico formado pela UFRJ, com especializações em Oncologia Ocular, Uso Medicinal da Cannabis e Nutrologia Esportiva pela Unifesp.",
                "patologias": "Epilepsia, Alzheimer, Parkinson, Dores crônicas, Ansiedade, Insônia, Obesidade, Perda de Apetite, Câncer, Autismo, TDAH, Endometriose, Medicina do Esporte, Fibromialgia",
                "atendimento": "Crianças, Adolescentes, Adultos e Idosos",
                "convenio": "Não",
                "retorno": "Até 60 dias",
                "experiencia": "Ampla experiência em Saúde Integrativa, combinando abordagens convencionais e complementares para promover o bem-estar integral dos pacientes.",
                "formacao": [
                    {"instituicao": "Universidade Federal do Rio de Janeiro (UFRJ)", "curso": "Medicina"},
                    {"instituicao": "Universidade Federal de São Paulo (UNIFESP)", "curso": "Uso Medicinal da Cannabis"}
                ],
                "video_url": "https://www.youtube-nocookie.com/embed/U1x1AUxhqEs?si=-FR1g-c6WbchIWY8"
            },
            {
                "id": 2,
                "valor_consulta": 230,
                "nome": "Dra. Mariana Costa",
                "especialidade": "Neurologista",
                "imagem": "https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Dra._Isabela_Junqueira.jpeg",
                "avaliacao": 4.8,
                "visualizacoes": 512,
                "crm": "209876",
                "cidade": "Rio de Janeiro, RJ",
                "descricao": "Neurologista com experiência em tratamentos alternativos, incluindo o uso medicinal da cannabis.",
                "patologias": "Epilepsia, Alzheimer, Parkinson, Ansiedade",
                "atendimento": "Adultos e Idosos",
                "convenio": "Sim",
                "retorno": "30 dias",
                "experiencia": "Especialista em neurologia e tratamento de doenças neurodegenerativas com cannabis medicinal.",
                "formacao": [
                    {"instituicao": "Universidade de São Paulo (USP)", "curso": "Medicina"},
                    {"instituicao": "Harvard Medical School", "curso": "Pesquisa em Cannabis Medicinal"}
                ],
                "video_url": "https://www.youtube-nocookie.com/embed/U1x1AUxhqEs?si=-FR1g-c6WbchIWY8"
            },
            {
                "id": 3,
                "nome": "Dr. João Mendes",
                "valor_consulta": 230,
                "especialidade": "Psiquiatra",
                "imagem": "https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Dr._Arailton_Neto.png",
                "visualizacoes": 389,
                "avaliacao": 4.8,
                "crm": "305432",
                "cidade": "Belo Horizonte, MG",
                "descricao": "Psiquiatra com foco em transtornos de ansiedade e depressão, utilizando cannabis medicinal.",
                "patologias": "Depressão, Ansiedade, TDAH, Insônia",
                "atendimento": "Adolescentes e Adultos",
                "convenio": "Não",
                "retorno": "45 dias",
                "experiencia": "Experiência com pacientes psiquiátricos e tratamentos alternativos.",
                "formacao": [
                    {"instituicao": "Universidade Federal de Minas Gerais (UFMG)", "curso": "Psiquiatria"}
                ],
                "video_url": "https://www.youtube-nocookie.com/embed/U1x1AUxhqEs?si=-FR1g-c6WbchIWY8"
            },
                {
                "id": 4,
                "valor_consulta": 900,
                "nome": "Dr. Ricardo Nunes Andreozzi",
                "especialidade": "Clínico Geral",
                "imagem": "https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Ricardo_Gurgel.jpeg",
                "visualizacoes": 407,
                "avaliacao": 4.8,
                "crm": "103621",
                "cidade": "São Paulo, SP",
                "descricao": "Médico formado pela UFRJ, com especializações em Oncologia Ocular, Uso Medicinal da Cannabis e Nutrologia Esportiva pela Unifesp.",
                "patologias": "Epilepsia, Alzheimer, Parkinson, Dores crônicas, Ansiedade, Insônia, Obesidade, Perda de Apetite, Câncer, Autismo, TDAH, Endometriose, Medicina do Esporte, Fibromialgia",
                "atendimento": "Crianças, Adolescentes, Adultos e Idosos",
                "convenio": "Não",
                "retorno": "Até 60 dias",
                "experiencia": "Ampla experiência em Saúde Integrativa, combinando abordagens convencionais e complementares para promover o bem-estar integral dos pacientes.",
                "formacao": [
                    {"instituicao": "Universidade Federal do Rio de Janeiro (UFRJ)", "curso": "Medicina"},
                    {"instituicao": "Universidade Federal de São Paulo (UNIFESP)", "curso": "Uso Medicinal da Cannabis"}
                ],
                "video_url": "https://www.youtube-nocookie.com/embed/U1x1AUxhqEs?si=-FR1g-c6WbchIWY8"
            },
            {
                "id": 5,
                "valor_consulta": 920,
                "nome": "Dra. Marcela Ribeiro",
                "especialidade": "Neurologista",
                "imagem": "https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Dra._Luisa_de_Freitas_Ramos.jpg",
                "avaliacao": 4.8,
                "visualizacoes": 512,
                "crm": "209876",
                "cidade": "Rio de Janeiro, RJ",
                "descricao": "Neurologista com experiência em tratamentos alternativos, incluindo o uso medicinal da cannabis.",
                "patologias": "Epilepsia, Alzheimer, Parkinson, Ansiedade",
                "atendimento": "Adultos e Idosos",
                "convenio": "Sim",
                "retorno": "30 dias",
                "experiencia": "Especialista em neurologia e tratamento de doenças neurodegenerativas com cannabis medicinal.",
                "formacao": [
                    {"instituicao": "Universidade de São Paulo (USP)", "curso": "Medicina"},
                    {"instituicao": "Harvard Medical School", "curso": "Pesquisa em Cannabis Medicinal"}
                ],
                "video_url": "https://www.youtube-nocookie.com/embed/U1x1AUxhqEs?si=-FR1g-c6WbchIWY8"
            },
            {
                "id": 6,
                "valor_consulta": 830,
                "nome": "Dr. João Brandão",
                "especialidade": "Psiquiatra",
                "imagem": "https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/FOTO.jpg",
                "visualizacoes": 389,
                "avaliacao": 4.8,
                "crm": "305432",
                "cidade": "Belo Horizonte, MG",
                "descricao": "Psiquiatra com foco em transtornos de ansiedade e depressão, utilizando cannabis medicinal.",
                "patologias": "Depressão, Ansiedade, TDAH, Insônia",
                "atendimento": "Adolescentes e Adultos",
                "convenio": "Não",
                "retorno": "45 dias",
                "experiencia": "Experiência com pacientes psiquiátricos e tratamentos alternativos.",
                "formacao": [
                    {"instituicao": "Universidade Federal de Minas Gerais (UFMG)", "curso": "Psiquiatria"}
                ],
                "video_url": "https://www.youtube-nocookie.com/embed/U1x1AUxhqEs?si=-FR1g-c6WbchIWY8"
            },
            {
                "id": 7,
                "valor_consulta": 530,
                "nome": "Dr. Lyoto Machida",
                "especialidade": "Médico do esporte",
                "imagem": "https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/FOTO.jpg",
                "visualizacoes": 389,
                "avaliacao": 4.8,
                "crm": "305432",
                "cidade": "Belo Horizonte, MG",
                "descricao": "Psiquiatra com foco em transtornos de ansiedade e depressão, utilizando cannabis medicinal.",
                "patologias": "Depressão, Ansiedade, TDAH, Insônia",
                "atendimento": "Adolescentes e Adultos",
                "convenio": "Não",
                "retorno": "45 dias",
                "experiencia": "Experiência com pacientes psiquiátricos e tratamentos alternativos.",
                "formacao": [
                    {"instituicao": "Universidade Federal de Minas Gerais (UFMG)", "curso": "Psiquiatria"}
                ],
                "video_url": "https://www.youtube-nocookie.com/embed/U1x1AUxhqEs?si=-FR1g-c6WbchIWY8"
            },
            {
                "id": 8,
                "valor_consulta": 330,
                "nome": "Dr. Anderson Silva",
                "especialidade": "Médico do Esporte",
                "imagem": "https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/FOTO.jpg",
                "visualizacoes": 389,
                "avaliacao": 4.8,
                "crm": "305432",
                "cidade": "Belo Horizonte, MG",
                "descricao": "Psiquiatra com foco em transtornos de ansiedade e depressão, utilizando cannabis medicinal.",
                "patologias": "Depressão, Ansiedade, TDAH, Insônia",
                "atendimento": "Adolescentes e Adultos",
                "convenio": "Não",
                "retorno": "45 dias",
                "experiencia": "Experiência com pacientes psiquiátricos e tratamentos alternativos.",
                "formacao": [
                    {"instituicao": "Universidade Federal de Minas Gerais (UFMG)", "curso": "Psiquiatria"}
                ],
                "video_url": "https://www.youtube-nocookie.com/embed/U1x1AUxhqEs?si=-FR1g-c6WbchIWY8"
            }
        ]
        try:
            new_doctors = [
                Doctor(
                    id=doctor_data['id'],
                    name=doctor_data['nome'],
                    specialty=doctor_data['especialidade'],
                    image=doctor_data['imagem'],
                    views=doctor_data['visualizacoes'],
                    rating=doctor_data['avaliacao'],
                    crm=doctor_data['crm'],
                    city=doctor_data['cidade'],
                    description=doctor_data['descricao'],
                    conditions=doctor_data['patologias'],
                    patient_groups=doctor_data['atendimento'],
                    insurance=doctor_data['convenio'],
                    follow_up=doctor_data['retorno'],
                    experience=doctor_data['experiencia'],
                    education=doctor_data['formacao'],
                    video_url=doctor_data['video_url'],
                    consultation_fee=doctor_data['valor_consulta'],
                ) for doctor_data in doctors
            ]
            Doctor.objects.bulk_create(new_doctors)

            self.stdout.write(self.style.SUCCESS('Mock data inserted successfully!'))
        except Exception as e:
            self.stderr.write(self.style.SUCCESS(f'Error inserting mock data: {str(e)}'))
