import tkinter as tk 
from PIL import ImageTk,Image
from tkinter import colorchooser as cc
from tkinter import font
from tkinter.ttk import Combobox


# Basic Config for Calculator Window
Calc_window = tk.Tk()
Calc_window.title('Normal Calculator')
Calc_window.geometry('263x630')
Calc_window.resizable(width = 0 ,height = 0)
Calc_window.configure(background = 'sky blue')


# Basic Variables
default_bg_color = 'sky blue'
default_bg_digits_color = 'purple'
default_font_style = 'Times New Roman'
Normal_button_size = (53,53)
Clear_button_size = (180,100)
Image_path = 'C:\\Users\\Priyanshu\\Desktop\\Button Images\\' 

# All Images Initialize
All_Comboboxes = ()
    
One_third_button_values = ()
Button_1_images_initialize = ()
Button_2_images_initialize = ()
Button_3_images_initialize = ()
Button_4_images_initialize = ()
Button_5_images_initialize = ()
Button_6_images_initialize = ()
Button_7_images_initialize = ()
Button_8_images_initialize = ()
Button_9_images_initialize = ()
Button_0_images_initialize = ()
Button_Plus_images_initialize = ()
Button_Minus_images_initialize = ()
Button_Multiply_images_initialize = ()
Button_Divide_images_initialize = ()
Button_Decimal_images_initialize = ()
Button_Square_images_initialize = ()
Button_Underoot_images_initialize = ()
Button_Clear_images_initialize = ()
Button_Equal_to_images_initialize = ()

Button_9_values = ()
for i in range(1,34):
    Button_9_values+=(f'Nine Image {i}',)
One_third_button_values+=Button_9_values,

Button_8_values = ()
for i in range(1,33):
    Button_8_values+=(f'Eight Image {i}',)
One_third_button_values+=Button_8_values,

Button_7_values = ()
for i in range(1,33):
    Button_7_values+=(f'Seven Image {i}',)
One_third_button_values+=Button_7_values,

Button_6_values = ()
for i in range(1,28):
    Button_6_values+=(f'Six Image {i}',)
One_third_button_values+=Button_6_values,

Button_5_values = ()
for i in range(1,44):
    Button_5_values+=(f'Five Image {i}',)
One_third_button_values+=Button_5_values,

Button_4_values = ()
for i in range(1,30):
    Button_4_values+=(f'Four Image {i}',)
One_third_button_values+=Button_4_values,



two_third_button_values = ()

Button_3_values = ()
for i in range(1,29):
    Button_3_values+=(f'Three Image {i}',)
two_third_button_values+=Button_3_values,

Button_2_values = ()
for i in range(1,37):
    Button_2_values+=(f'Two Image {i}',)
two_third_button_values+=Button_2_values,

Button_1_values = ()
for i in range(1,29):
    Button_1_values+=(f'One Image {i}',)
two_third_button_values+=Button_1_values,

Button_0_values = ()
for i in range(1,30):
    Button_0_values+=(f'Zero Image {i}',)
two_third_button_values+=Button_0_values,

Button_plus_values = ()
for i in range(1,58):
    Button_plus_values+=(f'Plus Image {i}',)
two_third_button_values+=Button_plus_values,

Button_minus_values = ()
for i in range(1,28):
    Button_minus_values+=(f'Minus Image {i}',)
two_third_button_values+=Button_minus_values,


remaining_Buttons_values = ()

Button_multiply_values = ()
for i in range(1,70):
    Button_multiply_values+=(f'Multiply Image {i}',)
remaining_Buttons_values+=Button_multiply_values,

Button_Decimal_values = ()
for i in range(1,4):
    Button_Decimal_values+=(f'Decimal Image {i}',)
remaining_Buttons_values+=Button_Decimal_values,

Button_Divide_values = ()
for i in range(1,61):
    Button_Divide_values+=(f'Divide Image {i}',)
remaining_Buttons_values+=Button_Divide_values,

Button_square_values = ()
for i in range(1,7):
    Button_square_values+=(f'Square Image {i}',)
remaining_Buttons_values+=Button_square_values,

Button_squareroot_values = ()
for i in range(1,71):
    Button_squareroot_values+=(f'Underoot Image {i}',)
remaining_Buttons_values+=Button_squareroot_values,

Button_Equal_to_values = ()
for i in range(1,30):
    Button_Equal_to_values+=(f'Equal To Image {i}',)
remaining_Buttons_values += Button_Equal_to_values,


Button_Clear_all_values = ()
for i in range(1,8):
    Button_Clear_all_values+=(f'Clear All Image {i}',)


for i in range(75):
    try:
        Image_initialize_Underoot = ImageTk.PhotoImage(Image.open(Image_path + Button_squareroot_values[i]+'.jpg').resize(Normal_button_size))
        Button_Underoot_images_initialize += Image_initialize_Underoot,
        
        Image_initialize_Multiply = ImageTk.PhotoImage(Image.open(Image_path + Button_multiply_values[i]+'.jpg').resize(Normal_button_size))
        Button_Multiply_images_initialize += Image_initialize_Multiply,
        
        Image_initialize_Divide = ImageTk.PhotoImage(Image.open(Image_path + Button_Divide_values[i]+'.jpg').resize(Normal_button_size))
        Button_Divide_images_initialize += Image_initialize_Divide,
        
        Image_initialize_Plus = ImageTk.PhotoImage(Image.open(Image_path + Button_plus_values[i]+'.jpg').resize(Normal_button_size))
        Button_Plus_images_initialize += Image_initialize_Plus,
        
        Image_initialize_5 = ImageTk.PhotoImage(Image.open(Image_path + Button_5_values[i] + '.jpg').resize(Normal_button_size))
        Button_5_images_initialize += Image_initialize_5,
        
        Image_initialize_2 = ImageTk.PhotoImage(Image.open(Image_path + Button_2_values[i] + '.jpg').resize(Normal_button_size))
        Button_2_images_initialize += Image_initialize_2,
        
        
        Image_initialize_9 = ImageTk.PhotoImage(Image.open(Image_path + Button_9_values[i] + '.jpg').resize(Normal_button_size))
        Button_9_images_initialize += Image_initialize_9,
        
        Image_initialize_7 = ImageTk.PhotoImage(Image.open(Image_path + Button_7_values[i] + '.jpg').resize(Normal_button_size))
        Button_7_images_initialize += Image_initialize_7,
        
        Image_initialize_8 = ImageTk.PhotoImage(Image.open(Image_path + Button_8_values[i] + '.jpg').resize(Normal_button_size))
        Button_8_images_initialize += Image_initialize_8,
        
        Image_initialize_4 = ImageTk.PhotoImage(Image.open(Image_path + Button_4_values[i] + '.jpg').resize(Normal_button_size))
        Button_4_images_initialize += Image_initialize_4,
        
        Image_initialize_0 = ImageTk.PhotoImage(Image.open(Image_path + Button_0_values[i] + '.jpg').resize(Normal_button_size))
        Button_0_images_initialize += Image_initialize_0,
        
        Image_initialize_Equal_to = ImageTk.PhotoImage(Image.open(Image_path + Button_Equal_to_values[i] + '.jpg').resize(Normal_button_size))
        Button_Equal_to_images_initialize += Image_initialize_Equal_to,
        
        Image_initialize_1 = ImageTk.PhotoImage(Image.open(Image_path + Button_1_values[i] + '.jpg').resize(Normal_button_size))
        Button_1_images_initialize += Image_initialize_1,
        
        Image_initialize_3 = ImageTk.PhotoImage(Image.open(Image_path + Button_3_values[i] + '.jpg').resize(Normal_button_size))
        Button_3_images_initialize += Image_initialize_3,
        
        Image_initialize_6 = ImageTk.PhotoImage(Image.open(Image_path + Button_6_values[i] + '.jpg').resize(Normal_button_size))
        Button_6_images_initialize += Image_initialize_6,
        
        Image_initialize_Minus = ImageTk.PhotoImage(Image.open(Image_path + Button_minus_values[i] +'.jpg').resize(Normal_button_size))
        Button_Minus_images_initialize += Image_initialize_Minus,

        
        Image_initialize_Clear_all = ImageTk.PhotoImage(Image.open(Image_path + Button_Clear_all_values[i] + '.jpg').resize(Clear_button_size))
        Button_Clear_images_initialize += Image_initialize_Clear_all,
        
        Image_initialize_Square = ImageTk.PhotoImage(Image.open(Image_path + Button_square_values[i] + '.jpg').resize(Normal_button_size))
        Button_Square_images_initialize += Image_initialize_Square,

        Image_initialize_Decimal = ImageTk.PhotoImage(Image.open(Image_path + Button_Decimal_values[i] + '.jpg').resize(Normal_button_size))
        Button_Decimal_images_initialize += Image_initialize_Decimal,
        
    except:
        pass

# All Functions Defined Here

Pick_Button_Image_times = 0

def Pick_Button_Image():
    global All_Comboboxes , Pick_Button_Image_times
    Choose_Button_image_window = tk.Toplevel(Calc_window)
    Starting_label = tk.Label(Choose_Button_image_window,text = 'Choose the Image for Different Buttons', font = ('Arial Black',25) , padx = 325 , bd = 8 , relief = tk.SUNKEN , pady = 10)
    Starting_label.grid(row = 0 , columnspan = 3)
    
    Button_names_one_third = ('Choose For Button 9', 'Choose For Button 8', 'Choose For Button 7', 'Choose For Button 6', 'Choose For Button 5', 'Choose For Button 4')
    
    Button_names_two_third = ('Choose For Button 3', 'Choose for Button 2' , 'Choose for Button 1','Choose For Button 0' , 'Choose for Button Plus','Choose for Button Minus')
    
    Button_names_remaining = ('Choose for Button Multiply' , 'Choose for Button Decimal','Choose for Button Divide','Choose for Button Square','Choose for Button Underoot','Choose for Button Equal to')
    
    Button_one_third_label_row_list = tuple((i for i in range(14) if i%2!=0))
    Button_one_third_Combobox_row_list = tuple((i for i in range(1,14) if i%2==0))
    
    Length_Button_names = 6
    
    
    for i in range(Length_Button_names):
        Button_label_one_third = tk.Label(Choose_Button_image_window,text = Button_names_one_third[i],font = ('Times New Roman',20))
        Button_label_one_third.grid(row = Button_one_third_label_row_list[i]  , column = 0 , pady = 10)
        Images_Combobox_one_third = Combobox(Choose_Button_image_window , values = One_third_button_values[i])
        Images_Combobox_one_third.grid(row = Button_one_third_Combobox_row_list[i]  , column = 0)
        if Pick_Button_Image_times == 0:
            Images_Combobox_one_third.set(One_third_button_values[i][0])
        else:
            Images_Combobox_one_third.set(get_values[i])

        All_Comboboxes+=(Images_Combobox_one_third,)

        
    for i in range(Length_Button_names):    
        Button_label_two_third = tk.Label(Choose_Button_image_window,text = Button_names_two_third[i],font = ('Times New Roman',20))
        Button_label_two_third.grid(row = Button_one_third_label_row_list[i]  , column = 1 , pady = 10)
        Images_Combobox_two_third = Combobox(Choose_Button_image_window , values = two_third_button_values[i])
        Images_Combobox_two_third.grid(row = Button_one_third_Combobox_row_list[i]  , column = 1)
        if Pick_Button_Image_times == 0:
            Images_Combobox_two_third.set(two_third_button_values[i][0])
        else:
            Images_Combobox_two_third.set(get_values[i+6])
        All_Comboboxes+=Images_Combobox_two_third,
        
        
    for i in range(Length_Button_names):    
        Button_label_names_remaining = tk.Label(Choose_Button_image_window,text = Button_names_remaining[i],font = ('Times New Roman',20))
        Button_label_names_remaining.grid(row = Button_one_third_label_row_list[i]  , column = 2 , pady = 10)
        Images_Combobox_names_remaining = Combobox(Choose_Button_image_window , values = remaining_Buttons_values[i])
        Images_Combobox_names_remaining.grid(row = Button_one_third_Combobox_row_list[i]  , column = 2)
        Images_Combobox_names_remaining.set(remaining_Buttons_values[i][0])
        if Pick_Button_Image_times == 0:
            Images_Combobox_names_remaining.set(remaining_Buttons_values[i][0])
        else:
            Images_Combobox_names_remaining.set(get_values[i+12])
        All_Comboboxes+=Images_Combobox_names_remaining,

    Button_Clear_all_values = ()
    for i in range(1,8):
        Button_Clear_all_values+=(f'Clear All Image {i}',)
        
    Button_label_clear_all= tk.Label(Choose_Button_image_window,text = 'Choose For Clear All',font = ('Times New Roman',20))
    Button_label_clear_all.grid(row = 14  , column = 1,pady = 15 )
    Images_Combobox_clear_all = Combobox(Choose_Button_image_window,values = Button_Clear_all_values)
    Images_Combobox_clear_all.grid(row = 15 , column = 1)
    if Pick_Button_Image_times == 0:
        Images_Combobox_clear_all.set('Clear All Image 1')
    else:
        Images_Combobox_clear_all.set(get_values[-1])
        
    All_Comboboxes += Images_Combobox_clear_all,
    Pick_Button_Image_times+=1
    
    def Ok_Image():
        global get_values
        get_values = ()
        Button_Images_All_Values = (Button_9_images_initialize,Button_8_images_initialize,Button_7_images_initialize, Button_6_images_initialize ,Button_5_images_initialize ,Button_4_images_initialize ,Button_3_images_initialize ,Button_2_images_initialize ,Button_1_images_initialize ,Button_0_images_initialize, Button_Plus_images_initialize ,Button_Minus_images_initialize ,  Button_Multiply_images_initialize , Button_Decimal_images_initialize , Button_Divide_images_initialize ,  Button_Square_images_initialize ,Button_Underoot_images_initialize ,  Button_Equal_to_images_initialize,Button_Clear_images_initialize)
        for i in All_Comboboxes:
            try:
                get_values+=(i.get(),)
            except:
                pass
        for i in range(len(get_values)):
            Image_place = int(get_values[i][-1])
            Buttons_list[i].config(image = Button_Images_All_Values[i][Image_place-1])
        Choose_Button_image_window.destroy()
        
    
    
        
    Cancel_Button = tk.Button(Choose_Button_image_window , text = 'Cancel',font = ('Arial Black',15),bd = 6)
    Cancel_Button.grid(row = 15 , column = 0)
    
    Ok_Button_Image = tk.Button(Choose_Button_image_window , text = 'OK',font = ('Arial Black',15),bd = 6 , command = Ok_Image)
    Ok_Button_Image.grid(row = 15 , column = 2)
    
    

def Pick_color_background():
    global default_bg_color
    color = cc.askcolor(title = 'Choose Background Color')
    selected = color[1]
    Digits_frame.configure(background = selected)
    default_bg_color = selected
    
    


def Pick_color_Digits():
    global default_bg_digits_color
    color = cc.askcolor(title = 'Choose Background Color')
    for i in Buttons_list:
        i.configure(bg = color[1])
 
def Pick_default_font_style():
    global Font_combobox ,Font_Window
    Font_Window = tk.Toplevel(Calc_window)
    Font_Window.title('Choose Font Style')
    Choose_label = tk.Label(Font_Window,text = 'Choose Font Style',font = ('Times New Roman',30),relief = tk.SUNKEN , bd = 6)
    Choose_label.pack()
    font_families = tuple(font.families())
    Font_combobox = Combobox(Font_Window , values = font_families)
    get_font = Entry_box.cget('font')[0:-3]
    if get_font[0]=='{':
        Font_combobox.set(get_font[1:][:len(get_font)-2])
    else:
        Font_combobox.set(get_font)
    Font_combobox.pack()
    
    def Pick_Font_ok():
        Font_value = Font_combobox.get()
        Entry_box.configure(font = (Font_value,18))
        Font_Window.destroy()
    
    Ok_button = tk.Button(Font_Window ,text = 'OK',command = Pick_Font_ok,bd = 3,font = ('Times New Roman',15))
    Ok_button.pack()
    

def Enter_digit(num):
    if Entry_box.get()=='ERROR!!':
        Entry_box.delete(0,tk.END)
    length = len(Entry_box.get())
    Entry_box.insert(length,num)
    
def clear_all():
    Entry_box.delete(0,tk.END)

def equal_to():
    try:
        evaluated = eval(Entry_box.get())
    except ZeroDivisionError:
        Entry_box.delete(0,tk.END)
        Entry_box.insert(0,'ERROR!!')
    except SyntaxError:
        Entry_box.delete(0,tk.END)
        Entry_box.insert(0,'ERROR!!')
    else:
        Entry_box.delete(0,tk.END)
        Entry_box.insert(0,evaluated)
        

# Creating Menus
main_menu = tk.Menu(Calc_window)
Calc_window.config(menu = main_menu)

file_menu = tk.Menu(main_menu , tearoff = False)
main_menu.add_cascade(label = "File" , menu = file_menu)

Edit_menu = tk.Menu(main_menu , tearoff = False)
main_menu.add_cascade(label = 'Edit' , menu = Edit_menu)
Edit_menu.add_command(label = 'Change Background Colour',command = Pick_color_background)
Edit_menu.add_command(label = 'Change Digits Border Colour',command = Pick_color_Digits)
Edit_menu.add_command(label = 'Change Font Style',command = Pick_default_font_style)
Edit_menu.add_command(label = 'Change Button Image',command = Pick_Button_Image)

# Images for Numbers
Image_names = ('Plus Image 1.jpg','Minus Image 1.jpg','Multiply Image 1.jpg','Decimal Image 1.jpg','Divide Image 1.jpg','Square Image 1.jpg','Underoot Image 1.jpg','Zero Image 1.jpg','One Image 1.jpg','Two Image 1.jpg','Three Image 1.jpg','Four Image 1.jpg','Five Image 1.jpg','Six Image 1.jpg','Seven Image 1.jpg','Eight Image 1.jpg','Nine Image 1.jpg')
All_images_Paths = ()
for i in Image_names:
    All_images_Paths+=(Image_path+f'{i}'),
Final_images = ()
for i in range(len(All_images_Paths)):
    Open_image = Image.open(All_images_Paths[i])
    Open_image = Open_image.resize(Normal_button_size)
    Final_images+=(ImageTk.PhotoImage(Open_image),)
    


# Entry Box Config
Entry_box = tk.Entry(Calc_window ,font = (default_font_style,18) , bd = 8 , relief = tk.SUNKEN)
Entry_box.grid(row = 0, columnspan = 3 , ipady = 5)

# Digits Config 
Digits_frame = tk.Frame(Calc_window,bg = default_bg_color)
Digits_frame.grid(row = 1 , column = 0)
Buttons_list = ()

row_places = (4,3,3,3,2,2,2,1,1,1)
column_places = (0,2,1,0,2,1,0,2,1,0)

remaining_Buttons = ('+','-','*','.','/','**2','**0.5')
remaining_Buttons_row_places = (4,4,5,5,5,6,6)
remaining_Buttons_column_places = (1,2,0,1,2,0,1)

for i in range(9,-1,-1):
    exec(f'Button_digit_{i} = tk.Button(Digits_frame,text = str({i}) ,bd = 4 , image = Final_images[{i}+7] ,bg  = default_bg_digits_color,command = lambda : Enter_digit({i}))')
    exec(f'Buttons_list+=(Button_digit_{i},)')
    exec(f'Button_digit_{i}.grid(row = row_places[{i}] , column = column_places[{i}] , padx = 9, pady = 3 ,ipadx = 3,ipady = 3)')

Remaining_Button_Final_images = Final_images[0:7]

for i in range(len(remaining_Buttons)):
    exec(f'Button_digit_{i+10} = tk.Button(Digits_frame,text = remaining_Buttons[{i}] , font = (default_font_style,25,"bold"),bd = 4 , image = Remaining_Button_Final_images[{i}],bg = default_bg_digits_color,command = lambda : Enter_digit(remaining_Buttons[{i}]))')
    exec(f'Buttons_list+=(Button_digit_{i+10},)')
    exec(f'Button_digit_{i+10}.grid(row = remaining_Buttons_row_places[{i}] , column = remaining_Buttons_column_places[{i}] , padx = 9, pady = 3 ,ipadx = 3,ipady = 3)')

# Equal To Button 

Equal_to_button_image = Button_Equal_to_images_initialize[0]
Equal_to_button = tk.Button(Digits_frame,image = Equal_to_button_image , bd = 4 ,bg = default_bg_digits_color,command = equal_to)
Buttons_list+=(Equal_to_button,)
Equal_to_button.grid(row = 6 , column = 2 , pady = 7,ipadx = 3,ipady = 3,padx = 9)

# Clear All Button
Clear_button_image = Button_Clear_images_initialize[0]
Clear_button = tk.Button(Digits_frame,image = Clear_button_image, bd = 4,bg = default_bg_digits_color,command = clear_all)
Buttons_list+=(Clear_button,)
Clear_button.grid(row = 7 , columnspan = 3 ,padx = 9)
Calc_window.mainloop()

