import discord
import os
from dotenv import load_dotenv
import random

load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'✅ Bot conectado como {self.user}')
        print(f'ID: {self.user.id}')
        print('------')
    
    async def on_message(self, message):
        # No responder a sí mismo
        if message.author == self.user:
            return
        
        # Comando !hola
        if message.content == '!hola':
            await message.channel.send(f'¡Hola {message.author.mention}! 👋')
        
        # Comando !ping
        elif message.content == '!ping':
            await message.channel.send('🏓 Pong!')
        
        # Comando !say
        elif message.content.startswith('!say '):
            texto = message.content[5:]
            await message.channel.send(texto)
        
        # Comando !dado
        elif message.content == '!dado':
            dado = random.randint(1, 6)
            await message.channel.send(f'🎲 Has sacado un {dado} en el dado.')
        
        # Comando !moneda
        elif message.content == '!moneda':
            moneda = random.choice(['Cara', 'Cruz'])
            await message.channel.send(f'🪙 Ha salido {moneda}.')
        
        # Comando !8ball
        elif message.content == '!8ball':
            respuestas = [
                "Sí.",
                "No.",
                "Tal vez.",
                "Definitivamente.",
                "Pregunta de nuevo más tarde.",
                "No cuentes con ello.",
                "¡Claro que sí!",
                "Mis fuentes dicen que no."
            ]
            respuesta = random.choice(respuestas)
            await message.channel.send(f'🎱 La bola mágica dice: {respuesta}')
        
        # Comando !prediccion
        elif message.content == '!prediccion':
            nombre = message.author.display_name
            
            predicciones_amor = [
                "💕 Conocerás a alguien especial en un lugar inesperado",
                "💑 Una amistad se convertirá en algo más",
                "💖 Tu relación actual se fortalecerá enormemente",
                "🌹 Este año es para enfocarte en amarte a ti mismo/a",
                "💘 Alguien del pasado podría regresar a tu vida",
                "❤️ Vivirás una historia de amor como de película"
            ]
            
            predicciones_dinero = [
                "💰 Recibirás un aumento o promoción inesperada",
                "💸 Una inversión que hiciste dará frutos",
                "💵 Aprenderás a administrar mejor tu dinero",
                "🤑 Una oportunidad de negocio llegará a tu puerta",
                "💎 Deberás ahorrar en la primera mitad del año",
                "🏆 Tu trabajo duro será recompensado financieramente"
            ]
            
            predicciones_carrera = [
                "🚀 Cambiarás de trabajo o de carrera",
                "📈 Lograrás un proyecto importante que te dará reconocimiento",
                "🎓 Aprenderás una nueva habilidad que cambiará tu vida",
                "💼 Te convertirás en líder de un equipo",
                "🌟 Recibirás una oferta que no esperabas",
                "👨‍💻 Iniciarás tu propio emprendimiento"
            ]
            
            predicciones_viaje = [
                "✈️ Viajarás a un lugar que siempre soñaste visitar",
                "🗺️ Una aventura inesperada te espera en el verano",
                "🏖️ Harás un viaje que cambiará tu perspectiva de vida",
                "🌍 Conocerás una cultura completamente nueva",
                "🎒 Un viaje con amigos será inolvidable",
                "🚗 Una escapada de fin de semana traerá grandes sorpresas"
            ]
            
            predicciones_salud = [
                "🏃 Encontrarás la motivación para cuidar tu salud",
                "🧘 Descubrirás la meditación o yoga y te encantará",
                "💪 Alcanzarás una meta física que te propusiste",
                "🥗 Cambiarás tus hábitos alimenticios para mejor",
                "😴 Aprenderás a priorizar tu descanso y bienestar",
                "🌱 Tu energía estará en su punto más alto"
            ]
            
            predicciones_extra = [
                "🎉 Celebrarás un logro importante con los que amas",
                "📱 Conocerás a alguien influyente en redes sociales",
                "🎨 Descubrirás un talento oculto que tienes",
                "📚 Leerás un libro que cambiará tu forma de pensar",
                "🎵 La música jugará un papel importante este año",
                "🐕 Una mascota podría llegar a tu vida"
            ]
            
            consejos = [
                "Recuerda: todo lo que quieres está del otro lado del miedo.",
                "Este año, atrévete a hacer lo que te asusta.",
                "La magia sucede fuera de tu zona de confort.",
                "No esperes el momento perfecto, créalo tú.",
                "Las mejores cosas de la vida suceden cuando menos las esperas.",
                "Confía en el proceso, todo llega en el momento indicado."
            ]
            
            numero_suerte = random.randint(1, 100)
            meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                     "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
            mes_importante = random.choice(meses)
            
            prediccion = f"""
✨ **PREDICCIONES PARA {nombre} EN 2026** ✨
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔮 Mirando el futuro de **{nombre}**...

💕 **AMOR:**
   {random.choice(predicciones_amor)}

💰 **DINERO:**
   {random.choice(predicciones_dinero)}

🚀 **CARRERA:**
   {random.choice(predicciones_carrera)}

✈️ **VIAJES:**
   {random.choice(predicciones_viaje)}

💪 **SALUD:**
   {random.choice(predicciones_salud)}

🎁 **EXTRA:**
   {random.choice(predicciones_extra)}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🍀 Tu número de la suerte: **{numero_suerte}**
📅 Tu mes más importante: **{mes_importante}**

💭 **Consejo para 2026:** {random.choice(consejos)}

✨ ¡Que tengas un increíble 2026! ✨
            """
            await message.channel.send(prediccion)
        
        # Comando !server
        elif message.content == '!server':
            await message.channel.send(f'Servidor: {message.guild.name}\nMiembros: {message.guild.member_count}')
        
        # Comando !ayuda
        elif message.content == '!ayuda':
            ayuda = """
📋 **Comandos disponibles:**
`!hola` - Saluda al bot
`!ping` - Verifica que el bot funciona
`!say <mensaje>` - El bot repite tu mensaje
`!dado` - Lanza un dado 🎲
`!moneda` - Lanza una moneda 🪙
`!8ball` - Pregunta a la bola mágica 🎱
`!prediccion` - Obtén tu predicción para 2026 🔮
`!server` - Información del servidor
`!ayuda` - Muestra este menú
            """
            await message.channel.send(ayuda)

# Configurar intents
intents = discord.Intents.default()
intents.message_content = True

# Crear y ejecutar el bot
client = MyClient(intents=intents)
client.run(os.getenv('DISCORD_TOKEN'))
