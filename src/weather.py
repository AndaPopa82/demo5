from tkinter import *
from tkinter import messagebox
import requests
from api_key import key
import logging

# Configurarea logurilor;
# Un fisier logs.log se va genera in care sunt vizualizate log-urile de la INFO level in sus
logging.basicConfig(filename="C:/Users/Ysa/PycharmProjects/src/logs.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()


def get_weather(city):
    # se face request-ul in functie de oras si key
    result = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + key)
    if result:
        result_json = result.json()  # se stocheaza info primita in variabila result_json
        # se extrage din json: orasul, tara, weather, temperatura, vantul
        city = result_json["name"]
        tara = result_json["sys"]["country"]
        weather = result_json["weather"][0]["main"]
        temp_kelvin = result_json["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15
        imagine = result_json["weather"][0]["icon"]
        vant = result_json["wind"]["speed"]
        rezultat_final = [city, tara, temp_celsius, weather, imagine, vant]
        logging.info("The request for data was made and successfully received!")
        return rezultat_final  # se returneaza rezultat_final
    else:
        return None


def search():
    city = user_input.get()  # infomatia din functia input (de la tastatura) se atribuie variabilei city
    if not user_input.get():
        # pop up message in cazul in care nu se introduce nimic de la tastatura
        messagebox.showinfo(title="Error", message="Please enter a city!")
        logging.warning("No city name was provided!")
    else:
        # se apeleaza functia get_weather si se stocheaza in variabila vremea_final care este o lista
        try:   # try/except pt sitatia in care nu este conexiune la internet sau nu functioneaza site-ul
            vremea_final = get_weather(city)
            if vremea_final:
                # am actualizat atibutele din labels cu informatiile primite cu ajutorul functiei get_weather
                location_city_country["text"] = f"{vremea_final[0]}, {vremea_final[1]}"
                temp_lbl["text"] = f" {vremea_final[2]:.0f}°C"
                temp_lbl["bg"] = "azure3"
                vremea_lbl["text"] = vremea_final[3]
                vremea_lbl["bg"] = "azure3"
                poza_vreme["file"] = f"icons_vreme/{vremea_final[4]}.png"
                vant_lbl["text"] = f" {vremea_final[5]} m/s"
                vant_lbl["image"] = pic_vant
                vant_lbl["bg"] = "azure3"
                label_background_color["bg"] = "azure3"
                poza_termometru["file"] = f"icons_vreme/termometru.png"
            else:
                # pop up message in cazul in care se introduce de la tastatura un text care nu recunoscut ca oras
                messagebox.showinfo(title="Error", message=f"No city with the name {city} was found!")
                logging.warning("A wrong city name was provided!")
        except:
            messagebox.showinfo(title="Error", message=f"Technical problem, please check!")
            logging.error("There are some technical problems, please check!")


# am creeat fereasta aplicatiei
root = Tk()
root.geometry("700x350")
root.resizable(True, False)
root.title("Weather")
root.iconbitmap("icons_vreme/logo_api.ico")


# am creeat un widget de tip Label pentru textul "Insert the city name:"
city_head = Label(root, text='Insert the city name:', font='Calibri 12 bold')
city_head.pack(padx=20, pady=5)

# am creeat un widget de tip Entry pentru orasul ce urmeaza sa fie scris de la tastatura
user_input = StringVar()
city_entry = Entry(root, width=36, textvariable=user_input,
                   justify=CENTER, foreground="black",
                   font='Calibri 12 bold')
city_entry.pack(padx=20, pady=7)

# am creeat un widget de tip Button pentru functia de Search, am atribuit si o poza "deget.png
deget_pic = PhotoImage(file="icons_vreme/deget.png")
search_btn = Button(root,
                    text="Search",
                    width=92,
                    bg="azure3",
                    font="Calibri 16 bold",
                    command=search,
                    relief="ridge",
                    borderwidth=7,
                    padx=15,
                    pady=6,
                    image=deget_pic,
                    compound="left")
search_btn.pack()

# am creeat un widget de tip Label pentru backgroundul gri din partea de jos a aplicatiei
# backgroundul apare numai dupa folosirea butonului de Search
label_background_color = Label(root, width=700, height=30)
label_background_color.place(x=0, y=230)

# am creeat un widget de tip Label pentru textul afisarea orasului si tarii
location_city_country = Label(root, text="", font=("Calibri", 36))
location_city_country.pack()

# am creeat un widget de tip Label pentru afisarea temperaturii, am atribuie si poza poza_termometru.png
poza_termometru = PhotoImage(file="")
temp_lbl = Label(root,
                 text="",
                 font=("bold", 17),
                 image=poza_termometru,
                 compound="left")
temp_lbl.place(x=45, y=250)

# am creeat un widget de tip Label pentru afisarea valorii vantului, am atribuie si poza pic_vant.png
pic_vant = PhotoImage(file="icons_vreme/pic_vreme.png")
vant_lbl = Label(root,
                 text="",
                 font=("bold", 17),
                 compound="left")
vant_lbl.place(x=270, y=265)

# am creeat un widget de tip Label pentru afisarea incarcarii atmosferice, am atribuie si poza poza_vreme.png
poza_vreme = PhotoImage(file="")
vremea_lbl = Label(root,
                   text="",
                   font=("bold", 17),
                   foreground="black",
                   image=poza_vreme,
                   compound="left")
vremea_lbl.place(x=480, y=230)


root.mainloop()
