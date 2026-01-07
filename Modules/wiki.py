import wikipedia

# Buscar información sobre un tema
topic = "Python (programming language)"

try:
    # Obtener resumen con 3 oraciones
    summary = wikipedia.summary(topic, sentences=3)
    
    print(f"📚 Searching for: {topic}\n")
    print(summary)
    
    # Obtener la página completa para más detalles
    page = wikipedia.page(topic)
    print(f"\n🔗 Read more: {page.url}")
    
except wikipedia.exceptions.DisambiguationError as e:
    print("⚠️ The term is ambiguous. Options include:")
    for option in e.options[:5]:  # Mostrar solo las primeras 5 opciones
        print(f"  - {option}")
        
except wikipedia.exceptions.PageError:
    print(f"❌ No Wikipedia page found for '{topic}'")