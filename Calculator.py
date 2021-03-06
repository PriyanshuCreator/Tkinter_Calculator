import tkinter as tk 
from PIL import ImageTk,Image
from tkinter import colorchooser as cc
from tkinter import font
from tkinter.ttk import Combobox
from os import startfile as sf
from tkinter.messagebox import showerror as se
from tkinter.messagebox import askyesno as ayn
from tkinter import simpledialog as sd
from configparser import ConfigParser as Cp
 
# Configuring File settings
config = Cp()
def Config_file(file, section, system, value):
    config.read(file)
    cfgfile = open(file, 'w')
    config.set(section, system, value)
    config.write(cfgfile)
    cfgfile.close()
config.read('Settings.ini')

# Basic Variables

String_int_values = ('0','1','2','3','4','5','6','7','8','9')
default_bg_color = config.get('Settings','default_bg_color')
default_bg_digits_color = config.get('Settings','default_bg_digits_color')
default_font_style = config.get('Settings','default_font_style')
Normal_button_size = (53,53)
Clear_button_size = (180,100)
Image_path = 'C:\\Users\\Priyanshu\\Desktop\\Button Images\\' 


# Basic Config for Calculator Window
Calc_window = tk.Tk()
Calc_window.title('Normal Calculator')
Calc_window.geometry('263x630')
Calc_window.resizable(width = 0 ,height = 0)
Calc_window.configure(background = 'sky blue')

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
        Images_Combobox_one_third = Combobox(Choose_Button_image_window , values = One_third_button_values[i] , state = 'readonly')
        Images_Combobox_one_third.grid(row = Button_one_third_Combobox_row_list[i]  , column = 0)
        Images_Combobox_one_third.set(config.get('Settings',f'button_{i}'))

        All_Comboboxes+=(Images_Combobox_one_third,)

        
    for i in range(Length_Button_names):    
        Button_label_two_third = tk.Label(Choose_Button_image_window,text = Button_names_two_third[i],font = ('Times New Roman',20))
        Button_label_two_third.grid(row = Button_one_third_label_row_list[i]  , column = 1 , pady = 10)
        Images_Combobox_two_third = Combobox(Choose_Button_image_window , values = two_third_button_values[i] , state = 'readonly')
        Images_Combobox_two_third.grid(row = Button_one_third_Combobox_row_list[i]  , column = 1)
        Images_Combobox_two_third.set(config.get('Settings',f'button_{i+6}'))
        All_Comboboxes+=Images_Combobox_two_third,
        
        
    for i in range(Length_Button_names):    
        Button_label_names_remaining = tk.Label(Choose_Button_image_window,text = Button_names_remaining[i],font = ('Times New Roman',20))
        Button_label_names_remaining.grid(row = Button_one_third_label_row_list[i]  , column = 2 , pady = 10)
        Images_Combobox_names_remaining = Combobox(Choose_Button_image_window , values = remaining_Buttons_values[i],state = 'readonly')
        Images_Combobox_names_remaining.grid(row = Button_one_third_Combobox_row_list[i]  , column = 2)
        Images_Combobox_names_remaining.set(remaining_Buttons_values[i][0])
        Images_Combobox_names_remaining.set(config.get('Settings',f'button_{i+12}'))
        All_Comboboxes+=Images_Combobox_names_remaining,

    Button_Clear_all_values = ()
    for i in range(1,8):
        Button_Clear_all_values+=(f'Clear All Image {i}',)
        
    Button_label_clear_all= tk.Label(Choose_Button_image_window,text = 'Choose For Clear All',font = ('Times New Roman',20))
    Button_label_clear_all.grid(row = 14  , column = 1,pady = 15 )
    Images_Combobox_clear_all = Combobox(Choose_Button_image_window,values = Button_Clear_all_values , state = 'readonly')
    Images_Combobox_clear_all.grid(row = 15 , column = 1)
    Images_Combobox_clear_all.set(config.get('Settings',f'button_18'))
        
    All_Comboboxes += Images_Combobox_clear_all,
    
    def Ok_Image():
        global get_values , Pick_Button_Image_times
        get_values = ()
        Button_Images_All_Values = (Button_9_images_initialize,Button_8_images_initialize,Button_7_images_initialize, Button_6_images_initialize ,Button_5_images_initialize ,Button_4_images_initialize ,Button_3_images_initialize ,Button_2_images_initialize ,Button_1_images_initialize ,Button_0_images_initialize, Button_Plus_images_initialize ,Button_Minus_images_initialize ,  Button_Multiply_images_initialize , Button_Decimal_images_initialize , Button_Divide_images_initialize ,  Button_Square_images_initialize ,Button_Underoot_images_initialize ,  Button_Equal_to_images_initialize,Button_Clear_images_initialize)
        for i in All_Comboboxes:
            try:
                get_values+=(i.get(),)
            except:
                pass
        for i in range(len(get_values)):
            Image_place = int(get_values [i][-1]) if get_values[i][-2] not in String_int_values else int(str(get_values [i][-2]) + str(get_values [i][-1]))
            Buttons_list[i].config(image = Button_Images_All_Values[i][Image_place-1])
            Config_file('Settings.ini','Settings',f'button_{i}',get_values[i])

        Pick_Button_Image_times+=1
        Choose_Button_image_window.destroy()
        
    
    Ok_Button = tk.Button(Choose_Button_image_window , text = 'OK',font = ('Arial Black',15),bd = 6 , command = Ok_Image)
    Ok_Button.grid(row = 15 , column = 2)
    
    

def Pick_color_background():
    global default_bg_color
    color = cc.askcolor(title = 'Choose Background Color')
    selected = color[1]
    Digits_frame.configure(background = selected)
    if selected:
        Config_file('Settings.ini','Settings','default_bg_color',selected)

def Pick_color_Digits():
    global default_bg_digits_color
    color = cc.askcolor(title = 'Choose Background Color')
    selected = color[1]
    for i in Buttons_list:
        i.configure(bg = selected)
    if selected:
        Config_file('Settings.ini','Settings','default_bg_digits_color',selected)
 
def Pick_default_font_style():
    global Font_combobox ,Font_Window
    Font_Window = tk.Toplevel(Calc_window)
    Font_Window.title('Choose Font Style')
    Choose_label = tk.Label(Font_Window,text = 'Choose Font Style',font = ('Times New Roman',30),relief = tk.SUNKEN , bd = 6)
    Choose_label.pack()
    font_families = tuple(font.families())
    Font_combobox = Combobox(Font_Window , values = font_families , state = 'readonly')
    Font_combobox.set(config.get('Settings','default_font_style'))
    Font_combobox.pack()
    
    def Pick_Font_ok():
        Font_value = Font_combobox.get()
        Entry_box.configure(font = (Font_value,18))
        Config_file('Settings.ini','Settings','default_font_style',f'{Font_value}')
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
    except NameError:
        Entry_box.delete(0,tk.END)
        Entry_box.insert(0,'ERROR!!')
    else:
        with open('History.txt','a') as f:
            f.write(f'{Entry_box.get()} = {evaluated}\n')
            
        Entry_box.delete(0,tk.END)
        Entry_box.insert(0,evaluated)
        
def Show_History():
    with open('History.txt' , 'r') as f:
        if len(f.readlines())==0:
            se('Error' , 'No History Present')
        else:
            sf('History.txt')

def Clear_History():
    with open('History.txt','r') as f:
        if len(f.readlines())==0:
            se('Error','History is Already Empty')
        else:
            get_answer = ayn('Calculator','Are you sure you want to clear the History ? ')
            if get_answer:
                with open('History.txt' , 'w') as f:
                    pass

def Swap_Buttons_Places():
    global Buttons_list
    Buttons_names_list = ('1','2','3','4','5','6','7','8','9','0','+','-','*','.','/','**2','**0.5','=')
    Buttons_list_Swap = Buttons_list[:10][::-1]
    Button_places = tuple(zip(row_places[::-1] + remaining_Buttons_row_places,column_places[::-1] +remaining_Buttons_column_places)) + ((6,2),)
    
    while True:
        try:
            get_places_both = sd.askstring('Simple Calculator' , 'Enter the Button Names to Change Places (comma Separated): ')
            Button_replace_first , Button_replace_second = get_places_both.split(',')
            Button_replace_first , Button_replace_second = Button_replace_first.strip().lower() , Button_replace_second.strip().lower()
        except:
            if get_places_both:
                se('Error','Please type valid numbers only')
            else:
                break
            
            
            
        else:
            if Button_replace_first == Button_replace_second and Button_replace_first and  Button_replace_second in Buttons_names_list:
                se('Error','Both Buttons are Same!!')
                
                
            elif Button_replace_first == 'clear' or Button_replace_second == 'clear':
                se('Error','Can\'t change place of Button Clear')
                
                
            elif Button_replace_first not in Buttons_names_list or Button_replace_second not in Buttons_names_list:
                se('Error',f'Can\'t Swap the Button {Button_replace_first} with {Button_replace_second}')
                
                
            else:
                try:
                    a,b = int(Button_replace_first) , int(Button_replace_second)
                except:
                    get_Button_place = list(Buttons_names_list).index
                    if Button_replace_first in String_int_values: 
                        a = int(Button_replace_first)
                        first_button_row = Buttons_list[get_Button_place(Button_replace_second)].grid_info()['row']
                        first_button_column = Buttons_list[get_Button_place(Button_replace_second)].grid_info()['column']                        
                        second_button_row = Buttons_list_Swap[a].grid_info()['row']
                        second_button_column = Buttons_list_Swap[a].grid_info()['column']
                        Buttons_list[get_Button_place(Button_replace_second)].grid(row = second_button_row ,column = second_button_column)
                        Buttons_list_Swap[a].grid(row = first_button_row ,column = first_button_column)
                        break
                    
                    elif Button_replace_second in String_int_values:
                        b = int(Button_replace_second)
                        first_button_row = Buttons_list_Swap[b].grid_info()['row']
                        first_button_column = Buttons_list_Swap[b].grid_info()['column']
                        second_button_row = Buttons_list[get_Button_place(Button_replace_first)].grid_info()['row']
                        second_button_column = Buttons_list[get_Button_place(Button_replace_first)].grid_info()['column'] 
                        Buttons_list[get_Button_place(Button_replace_first)].grid(row = first_button_row ,column = first_button_column)
                        Buttons_list_Swap[b].grid(row = second_button_row ,column = second_button_column )
                        break
                    else:
                        first_button_row = Buttons_list[get_Button_place(Button_replace_second)].grid_info()['row']
                        first_button_column = Buttons_list[get_Button_place(Button_replace_second)].grid_info()['column']
                        second_button_row = Buttons_list[get_Button_place(Button_replace_first)].grid_info()['row']
                        second_button_column = Buttons_list[get_Button_place(Button_replace_first)].grid_info()['column'] 
                        Buttons_list[get_Button_place(Button_replace_first)].grid(row = first_button_row ,column = first_button_column)
                        Buttons_list[get_Button_place(Button_replace_second)].grid(row = second_button_row ,column = second_button_column)
                        break
                else:
                    first_button_row = Buttons_list_Swap[b].grid_info()['row']
                    first_button_column = Buttons_list_Swap[b].grid_info()['column']
                    second_button_row = Buttons_list_Swap[a].grid_info()['row']
                    second_button_column = Buttons_list_Swap[a].grid_info()['column']
                    Buttons_list_Swap[a].grid(row = first_button_row ,column = first_button_column)
                    Buttons_list_Swap[b].grid(row = second_button_row ,column = second_button_column )
                    break
          
with open('History.txt' , 'a') as f:
    pass

# Defining Button images variables
button_0 = 'Nine Image 3'
button_1 = 'Eight Image 1'
button_2 = 'Seven Image 1'
button_3 = 'Six Image 1'
button_4 = 'Five Image 1'
button_5 = 'Four Image 1'
button_6 = 'Three Image 1'
button_7 = 'Two Image 1'
button_8 = 'One Image 1'
button_9 = 'Zero Image 1'
button_10 = 'Plus Image 1'
button_11 = 'Minus Image 1'
button_12 = 'Multiply Image 1'
button_13 = 'Decimal Image 1'
button_14 = 'Divide Image 1'
button_15 = 'Square Image 1'
button_16 = 'Underoot Image 1'
button_17 = 'Equal To Image 1'
button_18 = 'Clear All Image 1'

Buttons_images_variables_list = (button_0,button_1 , button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9, button_10,button_11,button_12,button_13,button_14,button_15,button_16,button_17 , button_18)


# Creating Menus
main_menu = tk.Menu(Calc_window)
Calc_window.config(menu = main_menu)

file_menu = tk.Menu(main_menu , tearoff = False)
main_menu.add_cascade(label = "File" , menu = file_menu)
file_menu.add_command(label = 'Show History' , command = Show_History)
file_menu.add_command(label = 'Clear History' , command = Clear_History)


Edit_menu = tk.Menu(main_menu , tearoff = False)
main_menu.add_cascade(label = 'Edit' , menu = Edit_menu)
Edit_menu.add_command(label = 'Change Background Colour',command = Pick_color_background)
Edit_menu.add_command(label = 'Change Digits Border Colour',command = Pick_color_Digits)
Edit_menu.add_command(label = 'Change Font Style',command = Pick_default_font_style)
Edit_menu.add_command(label = 'Change Button Image',command = Pick_Button_Image)
Edit_menu.add_command(label = 'Change Button Themes')
Edit_menu.add_command(label = 'Swap Buttons Places',command = Swap_Buttons_Places)

# Images for Numbers
All_images_Paths = ()
for i in range(17):
    image_name = config.get('Settings',f'button_{i}')
    All_images_Paths+=(Image_path + image_name+'.jpg'),
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
    exec(f'Button_digit_{i} = tk.Button(Digits_frame,text = str({i}) ,bd = 4 , image = Final_images[{9-i}] ,bg  = default_bg_digits_color,command = lambda : Enter_digit({i}))')
    exec(f'Buttons_list+=(Button_digit_{i},)')
    exec(f'Button_digit_{i}.grid(row = row_places[{i}] , column = column_places[{i}] , padx = 9, pady = 3 ,ipadx = 3,ipady = 3)')

Remaining_Button_Final_images = Final_images[0:7]

for i in range(len(remaining_Buttons)):
    exec(f'Button_digit_{i+10} = tk.Button(Digits_frame,text = remaining_Buttons[{i}] , font = (default_font_style,25,"bold"),bd = 4 , image = Final_images[{i+10}],bg = default_bg_digits_color,command = lambda : Enter_digit(remaining_Buttons[{i}]))')
    exec(f'Buttons_list+=(Button_digit_{i+10},)')
    exec(f'Button_digit_{i+10}.grid(row = remaining_Buttons_row_places[{i}] , column = remaining_Buttons_column_places[{i}] , padx = 9, pady = 3 ,ipadx = 3,ipady = 3)')

# Equal To Button 
Equal_to_button_image_number = int(config.get('Settings','button_17')[-1])
Equal_to_button_image = Button_Equal_to_images_initialize[Equal_to_button_image_number-1]
Equal_to_button = tk.Button(Digits_frame,image = Equal_to_button_image , bd = 4 ,bg = default_bg_digits_color,command = equal_to)
Buttons_list+=(Equal_to_button,)
Equal_to_button.grid(row = 6 , column = 2 , pady = 7,ipadx = 3,ipady = 3,padx = 9)

# Clear All Button
Clear_button_image_number = int(config.get('Settings','button_18')[-1])
Clear_button_image = Button_Clear_images_initialize[Clear_button_image_number-1]
Clear_button = tk.Button(Digits_frame,image = Clear_button_image, bd = 4,bg = default_bg_digits_color,command = clear_all)
Buttons_list+=(Clear_button,)
Clear_button.grid(row = 7 , columnspan = 3 ,padx = 9)
Calc_window.mainloop()

