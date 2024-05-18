import tkinter as tk
from buttons import OpButton, PauseButton
from PIL import ImageTk, Image
from cars import Car
from pedestrians import Pedestrian
from traffic_lights import TrafficLights
from lights_controller import LightsController

# Σχετικές διευθύνσεις που βρίσκονται οι φωτογραφίες
# του φόντου και του κουμπιού λειτουργίας των
# φωτεινών σηματοδοτών
BG_IMAGE = "../images/double_intersection.jpg"
PAUSE_IMAGE = "../images/buttons/pause_btn.png"
ON_OFF_RED = "../images/buttons/on_off_red.png"
ON_OFF_GRN = "../images/buttons/on_off_grn.png"


# Δημιουργία παραθύρου
root = tk.Tk()
# Τίτλος παραθύρου
root.title("Traffic Simulator")
# Φόρτωση εικόνων φόντου και κουμπιών
bg = ImageTk.PhotoImage(Image.open(BG_IMAGE))
pause_img = ImageTk.PhotoImage(Image.open(PAUSE_IMAGE))
on_off_red = ImageTk.PhotoImage(Image.open(ON_OFF_RED))
on_off_green = ImageTk.PhotoImage(Image.open(ON_OFF_GRN))

# Μέγεθος παραθύρου'
root.geometry(f"{bg.width()}x{bg.height()}")
# Δημιουργία καμβά όπου θα τρέχει η προσομοίωση
canvas = tk.Canvas(root, width=bg.width(), height=bg.height())
canvas.pack(fill="both", expand=True)
# Ορισμός φόντου στον καμβά
back_ground = canvas.create_image(bg.width()/2, bg.height()/2, image=bg)
# Κλήση της μεθόδου που δημιουργεί τους φωτεινούς σηματοδότες
TrafficLights.traffic_lights_creator(lights_images=TrafficLights.create_images(), canvas=canvas, root=root)
# Κλήση της μεθόδου που ξεκινάει τη λειτουργία των φωτεινών σηματοδοτών
LightsController()
# Κλήση της συνάρτησης που δημιουργεί συνεχώς αυτοκίνητα
Car.car_creator(car_images=Car.create_images(), canvas=canvas, root=root)
# Κλήση της συνάρτησης που δημιουργεί συνεχώς πεζούς
Pedestrian.pedestrian_creator(ped_images=Pedestrian.create_images(), canvas=canvas, root=root)
# Δημιουργία του κουμπιού για την εναλλαγή των λειτουργιών των φωτεινών σηματοδοτών
PauseButton(x=1200, y=50, image=pause_img, window=root)
OpButton(x=1300, y=50, images=(on_off_green, on_off_red), window=root)

root.mainloop()
