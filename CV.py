import matplotlib.pyplot as plt
import matplotlib.image as image
file = "C:/Users/pedro/OneDrive/Pictures/Screenshots/Captura de pantalla 2024-01-23 215808.png"
logo = image.imread(file)
plt.imshow(logo)
plt.show()


# Text Variables
AboutmeHeader = "SOBRE MÍ"
Aboutme = "Aspirante a Científico de Datos, X es el lugar perfecto para desarrollarme profesionalmente. \nBusco prácticas formativas con posibilidad de permanecer en la empresa.Posibilidad de\nPosibilidad de negociar un TFM para aportar valor a la empresa. "
Name = 'Adrián Lara Velasco'

Contact = 'Almassora, Castellón de la Plana | 722307655 | 28/07/2000 | adrianlaravelasco@gmail.com | linkedin.com/in/adrian-lara-velasco/'

WorkHeader = 'EXPERIENCIA LABORAL'
WorkOneTitle = 'Auxiliar administrativo/contable, Gestoría Hernandez'
WorkOneTime = 'Febrero 2023/Junio 2023'
WorkOneDesc = "- Automatización de procesos contables de la empresa\n- Traspaso de información de clientes entre ERP's\n- Finalización por inicio de estudios de Master"
WorkTwoTitle = 'Ayudante Investigación, Laboratorio Economía Experimental (LEE)'
WorkTwoTime = 'Febrero 2022/Diciembre 2022'
WorkTwoDesc = '- Trabajo realizado durante prácticas fromativas, extendido mediante beca de investigación\n- Encargado de gestionar experimentos de hasta 66 personas simultaneas (+50 experimentos) \n- Experimentalista ayudante en hospital psiquiatrico'

EduHeader = 'EDUCACIÓN'
EduOneTitle = 'Master en Ciencia de Datos, Universitat de Valencia'
EduOneTime = '2023-2024 (En curso)'
EduOneDesc = "- Machine Learning y Deep Learning\n- Procesado de Lenguaje Natural\n- Analisis Exploratorio y Visualización de datos\n- Analisis de señales\n- Programas utilizados: Python, R, Amazon AWS, Azure, MySQL, Tableau"
EduTwoTitle = 'Grado en Economía, Universitat Jaume I'
EduTwoTime = '2018-2022'
EduTwoDesc = "\n- Desarrollo de modelos econométricos utilizando databases en R\n- Ciclo económico y tendencias macroeconómicas\n- Premio a la exelencia académica Ernest Breva curso 2019-2020"

SkillsHeader = 'HERRAMIENTAS DE PROGRAMACIÓN'
SkillsDesc = '- Python: Manejo de Numpy, Pandas, Matplotlib y Scikit-Learn\n- R: Uso de las librerías del paquete tidyverse(dpylr, ggplot y tidyr)\n- SQL: Conocimiento básico, capaz de ejecutar sentencias básicas y subconsultas'

IdioHeader = "IDIOMAS"
Idiomas = "• Valenciano: Nativo\n• Inglés: Competencia Profesional (B2)"

AptHeader = "APTITUDES"
Aptitudes1 = "• Hablar en público\n\n• Resolución de problemas\n\n• Adaptabilidad"
IntHeader = "INTERESES"
Intereses = "• Finanzas cuantitativas\n\n• Procesos Estocásticos\n\n• Teorías de decision"

QRgit = "github.com/adrilave"
text_code = "Este CV ha sido realizado en python, código disponible en Github"
# Setting style for bar graphs

# set font
plt.rcParams['font.family'] = 'arial'

plt.rcParams['font.sans-serif'] = 'STIXGeneral'

#Plotting
fig, ax = plt.subplots(figsize=(8.5, 11))

# Description of everything of the plot

ax.axvline(x=.02, ymin=0, ymax=0.5, color='#007ACC', alpha=0.0, linewidth=50)
plt.axhline(y=.92, xmin=0.15, xmax=0.90, color='black', linewidth=1)
plt.axvline(x=0,ymin = 0,ymax = 0.65, color='#000000', alpha=0.5, linewidth=300)
plt.axhline(y=.88, xmin=0.5, xmax=1, color='#ffffff', linewidth=3)

# set background color
ax.set_facecolor('white')
# remove axes
plt.axis('off')
# add text

#plt.annotate(Header, (.02,.98), weight='regular', fontsize=8, alpha=.75)
plt.annotate(Name, (.50,.96), weight='bold', fontsize=14)
plt.annotate(Contact, (.06,.93), weight='bold', fontsize=8)

#Sobre mi
plt.annotate(AboutmeHeader, (.35,.86), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(Aboutme, (.37,.802), weight='regular', fontsize=9)

# Educación
plt.annotate(EduHeader, (.35,.76), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(EduOneTitle, (.35,.732), weight='bold', fontsize=10)
plt.annotate(EduOneTime, (.35,.717), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduOneDesc, (.37,.625), weight='regular', fontsize=9)
plt.annotate(EduTwoTitle, (.35,.590), weight='bold', fontsize=10)
plt.annotate(EduTwoTime, (.35,.575), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduTwoDesc, (.37,.515), weight='regular', fontsize=9)

# Herramientas de programación
plt.annotate(SkillsHeader, (.35,.48), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(SkillsDesc, (.37,.42), weight='regular', fontsize=9)

# Empleos anteriores
plt.annotate(WorkHeader, (.35,.38), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(WorkOneTitle, (.35,.348), weight='bold', fontsize=10)
plt.annotate(WorkOneTime, (.35,.333), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkOneDesc, (.37,.270), weight='regular', fontsize=9)
plt.annotate(WorkTwoTitle, (.35,.230), weight='bold', fontsize=10)
plt.annotate(WorkTwoTime, (.35,.215), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkTwoDesc, (.37,.150), weight='regular', fontsize=9)

# Idiomas
plt.annotate(IdioHeader, (.35,.110), weight='bold', fontsize=10,color='#58C1B2')
plt.annotate(Idiomas, (.37,.060), weight='regular', fontsize=9)

# Aptitudes
plt.annotate(AptHeader, (.02,.280), weight='bold', fontsize=10,color='#58C1B2')
plt.annotate(Aptitudes1, (.04,.185), weight='regular', fontsize=9,color='#ffffff')
plt.annotate(IntHeader, (.02,.140), weight='bold', fontsize=10,color='#58C1B2')
plt.annotate(Intereses, (.04,.045), weight='regular', fontsize=9,color='#ffffff')

plt.annotate(QRgit, (.05,.330), weight='bold', fontsize=10,color='#ffffff')
plt.annotate(text_code, (.35,.010), weight='regular', fontsize=9)

#add qr code
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)
#The OffsetBox is a simple container artist.
#The child artists are meant to be drawn at a relative position to its #parent.
imagebox = OffsetImage(logo, zoom = 0.2410)
#Annotation box for solar pv logo
#Container for the imagebox referring to a specific position *xy*.
ab = AnnotationBbox(imagebox, (0.1583, 0.737), frameon = False)
ax.add_artist(ab)

arr_code = mpimg.imread('C:/Users/pedro/Downloads/frame.png')
imagebox = OffsetImage(arr_code, zoom=0.3)
ab = AnnotationBbox(imagebox, (0.155, 0.45))
ax.add_artist(ab)

plt.savefig('C:/Users/pedro/Curriculum-Vitae/CV_Adrian_Lara_Velasco.png', dpi=300, bbox_inches='tight')
plt.show()