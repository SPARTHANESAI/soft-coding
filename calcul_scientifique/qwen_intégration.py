import requests, subprocess, json 


"""  
    PROBLEME PRINCIPAL: On veut essayer d'intégrer dans notre code le model qwen2.5:0.5b de ollama pour l'utiliser en local.
    Maintenant deux possibilités: soit onutilise l'Api de ollama, soit on utiise le subprocess pour lancer le model en local.
    Récupérons d'abord la question de l'utilisateur.  
"""
"""question = input("utilisateur : ")

 # Maintenant, on va utiliser via requests l'API  generate de ollama pour générer la réponse du model qwen. 
reponse = requests.post(
    "http://localhost:11434/api/generate", 
    json = {
        "model" : "qwen2.5:0.5b", 
        "prompt" : question,
        "stream" : True 
    }, stream = True
)
print("assistant : ", end="", flush=True)
for line in reponse.iter_lines():
    if line: 
        data = json.loads(line.decode("utf-8"))
        print(data["response"], end="", flush = True)
        
# Ici, apparaît notre deuxième méthode pour gérer la situation : Subprocess
result = subprocess.run(["ollama", "run", "qwen2.5:0.5b", question], capture_output = True, text = True, encoding = 'utf-8')
print("\n\nassistant subprocess : ", result.stdout)
 """
 
 
"""  
    Maintenant, notons que jusqu'ici, nous ne donnons que de prompts simoles au modèle et lui il ne fait que répondre 
    ponctuellement. Mais, on aurait bien voulu que le modèle garde en mémoire les questions et qu'il puisse répondre en fonction 
    de l'historique de la conversation un peu comme ça se passe avec chatgpt. 
    
    Pour ce faire nous allons utiliser donc l'api "chat" de ollama que nous avons trouvé dans la documentation de ollama. 
    
"""

try : 
    with open("conversation.json", "r", encoding = 'utf-8') as fichier : 
        messages = json.load(fichier)
except FileNotFoundError : 
    messages = []
    print("une erreur s'est produite")

try : 
    while True: 
        question = input("\nvous : ")
        if question.lower() in ["exit", "quit"]: 
            break
        messages.append({
            "role" : 'user', 
            "content" : question
        })
        
        
        try : 
            
            api_answer = requests.post(
                "http://localhost:11434/api/chat", 
                json = {
                    "model" : "qwen2.5:0.5b", 
                    "messages" : messages
                }, 
                stream = True, 
                timeout=120
            )
        except requests.exceptions.ConnectionError: 
            print("Erreur de connexion. Pense à lancer ollama")    
            continue
        except requests.exceptions.Timeout:
            print("La requête a dépassé le temps limite. Veuillez réessayer plus tard.") 
            continue
        except requests.exceptions.RequestException as e:
            print(f"Une erreur s'est produite lors de la requête : {e}") 
            continue
            

        print("assistant : ", end="")
        reponse_totale = ""
        try : 
            for line in api_answer.iter_lines(): 
                if line : 
                    reponse_en_fragment = json.loads(line.decode(encoding = 'utf-8'))
                    reponse_en_fragment = reponse_en_fragment["message"]['content']
                    reponse_totale += reponse_en_fragment
                    print(reponse_en_fragment, end="", flush = True)
        except json.decoder.JSONDecodeError:
            print("\nErreur de décodage JSON. La réponse du modèle pourrait être incomplète ou mal formée.")
                        
        messages.append(
            {
                "role" : 'assistant', 
                "content" : reponse_totale
            }
        )
        with open("conversation.json", "w", encoding= 'utf-8') as fichier: 
            json.dump(
                messages, 
                fichier, 
                ensure_ascii = False, 
                indent = 4
            )
except KeyboardInterrupt:    
    print("conversation interrompue par l'utilisateur.")     
        
        
"""
    NOTES IMPORTANTES : 
    1. L'utilisation de stream = True dans la requête permet de recevoir la réponses du modèle en temps réel, 
    ce qui est très utile pour les longues réponses. le seul point négatif est que la réponses en fragmentée et 
    qu'il va falloir à chaque fois utiliser 
    un print pour que l'affichage soit aussi en temps réel. Il faudra aussi
    par ailleurs reconstituer le le message total à la fin de la réponse pour pouvoir l'ajouter à l'historique de la conversation. 
    
    2. L'utilisation de flush = True dans le print permet d'affiher les réponses du modèle en temps réel, sans attendre la fin de la réponse. 
    c'est un peu comme si on disait à python d'afficher rapideent ce qu'il a reçu. car par défaut, puthon attend que le buffer soit prêt 
    à être affiché pour l'afficher. 
    
    3. Subprocess nous permet d'interagir directement avec nore propre ordinateur comme si nous voulions exécuter directement une commande dans le terminal. 
    Cela nous permet d'utiliser le modèle qwen2.5:0.5b de ollama en local et plus rapidement sans passer par l'API  de ollama. Cependant, 
    son usage peut devenir plus complexe à certains niveaux, notamment si nous voulions gérer l'historique de la conversation. 
    
    4. La subtilité pour obtenir des messages basés sur l'historique de la conversation avec les IAs repose sur le fait que nous devons envoyer à chaque fois 
    l'historique complet de la conversation au modèle. Cela signifie que nous devons stocker les messages de l'utilisateur et de l'assistant à 
    chaque étape de la conversation et les renvoyer au modèle à chaque nouvelle question. Cela permet au odèle de comprendre le contexte de la
    conversation de manière plus efficace et de fournir des réponses plus pertinentes. Ici nous utilisaons l'API Chat de ollama pour y arriver. 
    
    5. Maintenant, il y a aussi une nuance importante à noter : 
    
    
    6. Il est aussi important de noter que ce que nous recevons de l'api n'est pas du json direct mais un objet response
    
    
    prochaine etape a completer c'est de dauvegarder la conversation dans un fichier et aussi de verifier di je peux utiliser lal'api de chat gpt enn direct du r la web 
"""