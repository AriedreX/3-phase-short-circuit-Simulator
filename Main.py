################################################################################
#       _____ _                 _           _                  _               #
#      / ____(_)               | |         | |                | |              #
#     | (___  _ _ __ ___  _   _| | __ _  __| | ___  _ __    __| | ___          #
#      \___ \| | '_ ` _ \| | | | |/ _` |/ _` |/ _ \| '__|  / _` |/ _ \         #
#      ____) | | | | | | | |_| | | (_| | (_| | (_) | |    | (_| |  __/         #
#     |_____/|_|_| |_| |_|\__,_|_|\__,_|\__,_|\___/|_|     \__,_|\___|         #
#       _____           _          _______   _  __  __      _                  #
#      / ____|         | |        |__   __| (_)/ _|/_/     (_)                 #
#     | |    _   _ _ __| |_ ___      | |_ __ _| |_ __ _ ___ _  ___ ___         #
#     | |   | | | | '__| __/ _ \     | | '__| |  _/ _` / __| |/ __/ _ \        #
#     | |___| |_| | |  | || (_) |    | | |  | | || (_| \__ \ | (_| (_) |       #
#      \_____\__,_|_|   \__\___/     |_|_|  |_|_| \__,_|___/_|\___\___/        #
#                                                                              #
################################################################################
#Versão 1.0                                                                    #
#Data:24/06/2019                                                               #
#Autores: Ricardo Macedo e Antonio Galiza                                      #
#Contatos: angacego(at)gmail(dot)com                                           #
################################################################################
#          Script da interface gráfica e da composição dos gráficos            #
################################################################################
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import matplotlib.pyplot as plt
from kivy.uix.button import  Button
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock
from kivy.uix.togglebutton import ToggleButton
from time import asctime
from transformacoes import *

class Transformadas(App):

    def build(self):
        Window.clearcolor = (  1, 1, 1, 1)

        self.plot = False
        self.x = 0
        plt.plot([1, 23, 2, 4])
        plt.ylabel('some numbers')

        self.box = FloatLayout()

        self.rotulo_t = Label(text="Tempo Inicial\n da Simulação", color=(0,0,0,1),pos_hint={'center_x': .07,'center_y': .95})
        self.txt_t = TextInput(hint_text='0', size_hint=(.05,.05),pos_hint={'center_x': .175,'center_y': .95}, multiline=False)

        self.rotulo_passo = Label(text="Passo do Tempo\n da Simulação", color=(0,0,0,1),pos_hint={'center_x': .075,'center_y': .88})
        self.txt_passo = TextInput(hint_text='0.001', size_hint=(.1,.05),pos_hint={'center_x': .2,'center_y': .88}, multiline=False)

        self.rotulo_amp_A = Label(text="Amplitude\n Fase A", color=(0,0,0,1),pos_hint={'center_x': .32,'center_y': .95})
        self.rotulo_amp_B = Label(text="Amplitude\n Fase B", color=(0,0,0,1),pos_hint={'center_x': .48,'center_y': .95})
        self.rotulo_amp_C = Label(text="Amplitude\n Fase C", color=(0,0,0,1),pos_hint={'center_x': .64,'center_y': .95})
        self.txt_amp_A = TextInput(hint_text='1', size_hint=(.05,.05),pos_hint={ 'center_x': .4, 'center_y': .95}, multiline=False)
        self.txt_amp_B = TextInput(hint_text='1', size_hint=(.05,.05),pos_hint={ 'center_x': .56, 'center_y': .95}, multiline=False)
        self.txt_amp_C = TextInput(hint_text='1', size_hint=(.05,.05),pos_hint={'center_x': .72, 'center_y': .95}, multiline=False)

        self.txt_def_A = TextInput(hint_text='0', size_hint=(.05,.05),pos_hint={'center_x': .4, 'center_y': .88}, multiline=False)
        self.txt_def_B = TextInput(hint_text='-120', size_hint=(.05,.05),pos_hint={ 'center_x': .56, 'center_y': .88}, multiline=False)
        self.txt_def_C = TextInput(hint_text='120', size_hint=(.05,.05),pos_hint={'center_x': .72, 'center_y': .88}, multiline=False)
        self.rotulo_def_A = Label(text="Defasagem\n Fase A", color=(0,0,0,1),pos_hint={'center_x': .32,'center_y': .88})
        self.rotulo_def_B = Label(text="Defasagem\n Fase B", color=(0,0,0,1),pos_hint={'center_x': .48,'center_y': .88})
        self.rotulo_def_C = Label(text="Defasagem\n Fase C", color=(0,0,0,1),pos_hint={'center_x': .64,'center_y': .88})

        self.rotulo_theta = Label(text="Teta", color=(0,0,0,1),pos_hint={'center_x': .775,'center_y': .95})
        self.txt_theta = TextInput(hint_text='0', size_hint=(.05,.05),pos_hint={'center_x': .83,'center_y': .95}, multiline=False)

        self.rotulo_fps = Label(text="Freq.", color=(0,0,0,1),pos_hint={'center_x': .775,'center_y': .88})
        self.txt_fps = TextInput(hint_text='60', size_hint=(.05,.05),pos_hint={'center_x': .83,'center_y': .88}, multiline=False)

        self.rotulo_t_i = Label(text="Início\n do Curto", color=(0,0,0,1),pos_hint={'center_x': .9,'center_y': .95})
        self.txt_t_i = TextInput(hint_text='0', size_hint=(.05,.05),pos_hint={'center_x': .97,'center_y': .95}, multiline=False)

        self.rotulo_t_f = Label(text="Fim do\n Curto", color=(0,0,0,1),pos_hint={'center_x': .9,'center_y': .88})
        self.txt_t_f = TextInput(hint_text='0', size_hint=(.05,.05),pos_hint={'center_x': .97,'center_y': .88}, multiline=False)

        self.rotulo_curto_mono = Label(text="Tipo de Curto", color=(0,0,0,1),pos_hint={'center_x': .825,'center_y': .8})

        self.cb_curto_mono = ToggleButton(text='Monofásico', size_hint=(.12,.05),group="curto",pos_hint={'center_x': .825,'center_y': .75},background_normal='', background_color= [.8, .8, .8, 1],color=[0,0,0,1])

        self.cb_curto_bi = ToggleButton(text='Bifásico', size_hint=(.12,.05),group="curto",pos_hint={'center_x': .825,'center_y': .69},background_normal='', background_color= [.8, .8, .8, 1],color=[0,0,0,1])

        self.cb_curto_bi_terra = ToggleButton(text='Bifásico\n com terra', size_hint=(.12,.07),group="curto",pos_hint={'center_x': .825,'center_y': .62},background_normal='', background_color= [.8, .8, .8, 1],color=[0,0,0,1])

        self.cb_curto_tri = ToggleButton(text='Trifásico', size_hint=(.12,.05),group="curto",pos_hint={'center_x': .825,'center_y': .55},background_normal='', background_color= [.8, .8, .8, 1],color=[0,0,0,1])

        self.rotulo_curto_fases = Label(text="Fases", color=(0,0,0,1),pos_hint={'center_x': .95,'center_y': .8})

        self.cb_AAB = ToggleButton(text='A/AB', size_hint=(.08,.05),group="fases",pos_hint={'center_x': .95,'center_y': .75},background_normal='', background_color= [.8, .8, .8, 1],color=[0,0,0,1])

        self.cb_BAC = ToggleButton(text='B/AC', size_hint=(.08,.05),group="fases",pos_hint={'center_x': .95,'center_y': .69},background_normal='', background_color= [.8, .8, .8, 1],color=[0,0,0,1])

        self.cb_CBC = ToggleButton(text='C/BC', size_hint=(.08,.05),group="fases",pos_hint={'center_x': .95,'center_y': .63},background_normal='', background_color= [.8, .8, .8, 1],color=[0,0,0,1])

        self.btn = Button(text='Parar', on_press=self.clearText, size_hint=(.2,.1),pos_hint={'center_x': 0.875, 'center_y': 0.34},background_normal='', background_color= [.8, .8, .8, 1],color=[0,0,0,1])
        self.btn2 = Button(text='Iniciar', on_press=self.Plota, size_hint=(.2,.1),pos_hint={'center_x': 0.875, 'center_y': 0.45},background_normal='', background_color= [.8, .8, .8, 1],color=[0,0,0,1])
        self.save = Button(text='Salvar', on_press=self.Salvar, size_hint=(.2,.1),pos_hint={'center_x': 0.875, 'center_y': 0.23},background_normal='', background_color= [.8, .8, .8, 1],color=[0,0,0,1])

        self.tela = FigureCanvasKivyAgg(plt.gcf(), size_hint=(.75,.75),pos_hint={'center_y': .45})

        self.box.add_widget(self.rotulo_t)
        self.box.add_widget(self.txt_t)
        self.box.add_widget(self.rotulo_passo)
        self.box.add_widget(self.txt_passo)
        self.box.add_widget(self.rotulo_theta)
        self.box.add_widget(self.txt_theta)
        self.box.add_widget(self.rotulo_amp_A)
        self.box.add_widget(self.txt_amp_A)
        self.box.add_widget(self.rotulo_amp_B)
        self.box.add_widget(self.txt_amp_B)
        self.box.add_widget(self.rotulo_amp_C)
        self.box.add_widget(self.txt_amp_C)
        self.box.add_widget(self.rotulo_def_A)
        self.box.add_widget(self.txt_def_A)
        self.box.add_widget(self.rotulo_def_B)
        self.box.add_widget(self.txt_def_B)
        self.box.add_widget(self.rotulo_def_C)
        self.box.add_widget(self.txt_def_C)
        self.box.add_widget(self.rotulo_t_i)
        self.box.add_widget(self.txt_t_i)
        self.box.add_widget(self.rotulo_t_f)
        self.box.add_widget(self.txt_t_f)
        self.box.add_widget(self.rotulo_fps)
        self.box.add_widget(self.txt_fps)

        self.box.add_widget(self.rotulo_curto_mono)
        self.box.add_widget(self.cb_curto_mono)
        self.box.add_widget(self.cb_curto_bi)
        self.box.add_widget(self.cb_curto_bi_terra)
        self.box.add_widget(self.cb_curto_tri)

        self.box.add_widget(self.rotulo_curto_fases)
        self.box.add_widget(self.cb_AAB)
        self.box.add_widget(self.cb_BAC)
        self.box.add_widget(self.cb_CBC)

        self.box.add_widget(self.btn)
        self.box.add_widget(self.btn2)
        self.box.add_widget(self.save)

        self.t = float(self.txt_t.hint_text)
        self.passo = float(self.txt_passo.hint_text)
        self.f = float(self.txt_fps.hint_text)
        self.theta = float(self.txt_theta.hint_text)*pi/180-pi/2
        self.ampA = float(self.txt_amp_A.hint_text)
        self.ampB = float(self.txt_amp_B.hint_text)
        self.ampC = float(self.txt_amp_C.hint_text)
        self.defA= float(self.txt_def_A.hint_text)*pi/180
        self.defB= float(self.txt_def_B.hint_text)*pi/180
        self.defC= float(self.txt_def_C.hint_text)*pi/180
        self.freq = float(self.txt_fps.hint_text)
        self.omega = 2*pi*self.freq
        self.Dic = {"normal":False,"down":True}
        self.temCurto = False
        self.curtoMono = False
        self.curtoBi = False
        self.curtoBiTerra = False
        self.curtoTri = False
        self.faseAAB = False
        self.faseBAC = False
        self.faseCBC = False
        self.t_i = 0.0
        self.t_f = 0.0
        self.programado = False

        xa = self.ampA*sin(self.omega*self.t+self.defA)
        xb = self.ampB*sin(self.omega*self.t+self.defB)
        xc = self.ampC*sin(self.omega*self.t+self.defC)

        self.ListaTempo=[self.t]
        self.FaseA=[xa]
        self.FaseB=[xb]
        self.FaseC=[xc]
        self.FaseA2=[xa]
        self.FaseB2=[xb]
        self.FaseC2=[xc]


        ab0 = abc2alfabeta0(xa,xb,xc)

        self.ListaIAlpha = [ab0[0]]
        self.ListaIBeta = [ab0[1]]
        self.ListaSeq0 = [ab0[2]]

        dq0 = alfabeta02dq0(xa,xb,xc,self.t,self.omega,self.theta)

        self.ListaD = [dq0[0]]
        self.ListaQ = [dq0[1]]
        self.ListaSeq0dq = [dq0[2]]

        plt.clf()
        self.box.remove_widget(self.tela)
        plt.plot([1])
        self.tela = FigureCanvasKivyAgg(plt.gcf(), size_hint=(.75,.75),pos_hint={'center_y': .45})
        self.box.add_widget(self.tela)

        Clock.schedule_interval(self.update, 1/24)

        return self.box

    def clearText(self, instance):
        self.t = 0

        self.txt_t.text = ''
        self.txt_t_i.text = ''
        self.txt_t_f.text = ''
        self.txt_theta.text = ''

        xa = self.ampA*sin(self.omega*self.t+self.defA)
        xb = self.ampB*sin(self.omega*self.t+self.defB)
        xc = self.ampC*sin(self.omega*self.t+self.defC)
        self.ListaTempo=[self.t]

        self.FaseA=[xa]
        self.FaseB=[xb]
        self.FaseC=[xc]

        self.FaseA2=[xa]
        self.FaseB2=[xb]
        self.FaseC2=[xc]

        ab0 = abc2alfabeta0(xa,xb,xc)
        self.ListaIAlpha = [ab0[0]]
        self.ListaIBeta = [ab0[1]]
        self.ListaSeq0 = [ab0[2]]
        dq0 = alfabeta02dq0(ab0[0],ab0[1],ab0[2],self.t,self.omega,self.theta)
        self.ListaD = [dq0[0]]
        self.ListaQ = [dq0[1]]
        self.ListaSeq0dq = [dq0[2]]

        self.txt_t.hint_text="0"
        self.x=0
        self.btn2.text="Iniciar"
        plt.clf()
        self.box.remove_widget(self.tela)
        plt.plot([1])
        self.tela = FigureCanvasKivyAgg(plt.gcf(), size_hint=(.75,.75),pos_hint={'center_y': .45})
        self.box.add_widget(self.tela)
        self.plot = False

        Clock.unschedule(self.update)

    def Plota(self,instance):
        if self.plot:
            self.plot = False
            self.btn2.text="Retomar"
        else:
            self.plot = True

            Clock.unschedule(self.update)
            Clock.schedule_interval(self.update, 1/24)

            try:
                self.t = float(self.txt_t.text)
            except:
                try:
                    self.t = float(self.txt_t.hint_text)
                except:
                    self.t = 0
            try:
                self.passo = float(self.txt_passo.text)
            except:
                try:
                    self.passo = float(self.txt_passo.hint_text)
                except:
                    self.passo = 0.001
            try:
                self.freq = float(self.txt_fps.text)
            except:
                try:
                    self.freq = float(self.txt_fps.hint_text)
                except:
                    self.freq = 60
            try:
                self.defA = float(self.txt_def_A.text)*pi/180
            except:
                try:
                    self.defA = float(self.txt_def_A.hint_text)*pi/180
                except:
                    self.defA = 0
            try:
                self.defB = float(self.txt_def_B.text)*pi/180
            except:
                try:
                    self.defB = float(self.txt_def_B.hint_text)*pi/180
                except:
                    self.defB = -120*pi/180
            try:
                self.defC = float(self.txt_def_C.text)*pi/180
            except:
                try:
                    self.defC = float(self.txt_def_C.hint_text)*pi/180
                except:
                    self.defC = 120*pi/180
            try:
                self.ampA = float(self.txt_amp_A.text)
            except:
                try:
                    self.ampA = float(self.txt_amp_A.hint_text)
                except:
                    self.ampA = 1
            try:
                self.ampB = float(self.txt_amp_B.text)
            except:
                try:
                    self.ampB = float(self.txt_amp_B.hint_text)
                    self.ampB = 1
                except:
                    self.ampB = 1
            try:
                self.ampC = float(self.txt_amp_C.text)
            except:
                try:
                    self.ampC = float(self.txt_amp_C.hint_text)
                    self.ampC = 1
                except:
                    self.ampC = 1
            try:
                self.t_i = float(self.txt_t_i.text)
            except:
                try:
                    self.t_i = float(self.txt_t_i.hint_text)
                except:
                    self.t_i = 0.0
            try:
                self.t_f = float(self.txt_t_f.text)
            except:
                try:
                    self.t_f = float(self.txt_t_f.hint_text)
                except:
                    self.t_f = 0.0
            try:
                self.theta = float(self.txt_theta.text)*pi/180 -pi/2
            except:
                try:
                    self.theta = float(self.txt_theta.hint_text)*pi/180 -pi/2
                except:
                    self.theta = 0.0-pi/2

            self.btn2.text="Pausar"

    def Salvar(self,instance):
        plt.savefig("Figura"+asctime().replace(" ","")+".png")

    def update(self,instance):
        if self.plot:
            self.x+=1
            self.t+=self.passo
            if self.txt_t.text == '':
                self.txt_t.hint_text=str(self.t)
            else:
                self.txt_t.text=str(self.t)

            xa = self.ampA*sin(self.omega*self.t+self.defA)
            xb = self.ampB*sin(self.omega*self.t+self.defB)
            xc = self.ampC*sin(self.omega*self.t+self.defC)

            if self.txt_t_i.text == '' or self.txt_t_f == '' or  self.t_i == self.t_f or self.t>=self.t_f:
                if not self.programado:
                    self.curtoMono = self.Dic[self.cb_curto_mono.state]
                    self.curtoBi = self.Dic[self.cb_curto_bi.state]
                    self.curtoBiTerra = self.Dic[self.cb_curto_bi_terra.state]
                    self.curtoTri = self.Dic[self.cb_curto_tri.state]
                    self.faseAAB = self.Dic[self.cb_AAB.state]
                    self.faseBAC = self.Dic[self.cb_BAC.state]
                    self.faseCBC = self.Dic[self.cb_CBC.state]
                else:
                    self.curtoMono = False
                    self.curtoBi = False
                    self.curtoBiTerra = False
                    self.curtoTri = False
                    self.faseAAB = False
                    self.faseBAC = False
                    self.faseCBC = False
                    self.cb_curto_mono.state = "normal"
                    self.cb_curto_bi.state = "normal"
                    self.cb_curto_bi_terra.state = "normal"
                    self.cb_curto_tri.state = "normal"
                    self.cb_AAB.state = "normal"
                    self.cb_BAC.state = "normal"
                    self.cb_CBC.state = "normal"
                    self.programado = False

                TipoDoCurto = converte(self.curtoMono,self.curtoBi,self.curtoBiTerra,self.curtoTri,self.faseAAB,self.faseBAC,self.faseCBC)
                if TipoDoCurto[0]:
                    xa,xb,xc = curtos(xa,xb,xc,TipoDoCurto[1],TipoDoCurto[2],TipoDoCurto[3])

            else:
                if self.t_i>self.t_f:
                    tint = self.t_f
                    self.t_f = self.t_i
                    self.t_i= tint
                if self.t>self.t_i and self.t<self.t_f:
                    self.programado = True
                    self.curtoMono = self.Dic[self.cb_curto_mono.state]
                    self.curtoBi = self.Dic[self.cb_curto_bi.state]
                    self.curtoBiTerra = self.Dic[self.cb_curto_bi_terra.state]
                    self.curtoTri = self.Dic[self.cb_curto_tri.state]
                    self.faseAAB = self.Dic[self.cb_AAB.state]
                    self.faseBAC = self.Dic[self.cb_BAC.state]
                    self.faseCBC = self.Dic[self.cb_CBC.state]

                    TipoDoCurto = converte(self.curtoMono,self.curtoBi,self.curtoBiTerra,self.curtoTri,self.faseAAB,self.faseBAC,self.faseCBC)
                    if TipoDoCurto[0]:
                        xa,xb,xc = curtos(xa,xb,xc,TipoDoCurto[1],TipoDoCurto[2],TipoDoCurto[3])
                else:
                    pass

            ab0 = abc2alfabeta0(xa,xb,xc)
            dq0 = alfabeta02dq0(ab0[0],ab0[1],ab0[2],self.t,self.omega,self.theta)
            abc = dq02abc(dq0[0],dq0[1],dq0[2],self.t,self.omega,self.theta)

            if len(self.ListaIAlpha)>99:
                plt.clf()
                self.FaseA = self.FaseA[1:]+[xa]
                self.FaseB = self.FaseB[1:]+[xb]
                self.FaseC = self.FaseC[1:]+[xc]
                self.ListaIAlpha = self.ListaIAlpha[1:]+[ab0[0]]
                self.ListaIBeta = self.ListaIBeta[1:]+[ab0[1]]
                self.ListaSeq0 = self.ListaSeq0[1:]+[ab0[2]]
                self.ListaTempo = self.ListaTempo[1:]+[self.t*1000]
                self.ListaD = self.ListaD[1:]+[dq0[0]]
                self.ListaQ = self.ListaQ[1:]+[dq0[1]]
                self.ListaSeq0dq = self.ListaSeq0dq[1:]+[dq0[2]]
                self.FaseA2 = self.FaseA2[1:]+[abc[0]]
                self.FaseB2 = self.FaseB2[1:]+[abc[1]]
                self.FaseC2 = self.FaseC2[1:]+[abc[2]]

#==============================================================================#
                p1 = plt.subplot(4, 1, 1)
                pA = p1.plot(self.ListaTempo,self.FaseA)
                pB = p1.plot(self.ListaTempo,self.FaseB)
                pC = p1.plot(self.ListaTempo,self.FaseC)

                p1.legend((pA[0], pB[0], pC[0]), ('Fase A', 'Fase B', 'Fase C'), loc='upper left')
                plt.title('Componentes de Fase')
                plt.ylabel('Amplitude(kV)')
                plt.xlabel('tempo(ms)')
                plt.grid()
                #plt.ylim((-1.25*max([self.ampA,self.ampB,self.ampC]), 1.25*max([self.ampA,self.ampB,self.ampC])))
#==============================================================================#
                p2 = plt.subplot(4, 1, 2)
                pAlpha = p2.plot(self.ListaTempo,self.ListaIAlpha)
                pBeta = p2.plot(self.ListaTempo,self.ListaIBeta)
                p0AB = p2.plot(self.ListaTempo,self.ListaSeq0,linewidth=0.75)

                p2.legend((pAlpha[0], pBeta[0], p0AB[0]), ('Comp. Alfa', 'Comp. Beta', 'Comp. Homopolar'), loc='upper left')
                plt.title('Transformada de Clarke')
                plt.ylabel('Amplitude(kV)')
                plt.grid()

                #plt.ylim((-1.25*max([self.ampA,self.ampB,self.ampC]), 1.25*max([self.ampA,self.ampB,self.ampC])))
#==============================================================================#
                p3 = plt.subplot(4, 1, 3)
                pd=p3.plot(self.ListaTempo,self.ListaD)
                pq=p3.plot(self.ListaTempo,self.ListaQ)
                p0park=p3.plot(self.ListaTempo,self.ListaSeq0dq,linewidth=0.75)
                #plt.ylim((-1.25*max([self.ampA,self.ampB,self.ampC]), 1.25*max([self.ampA,self.ampB,self.ampC])))
                p3.legend((pd[0], pq[0], p0park[0]), ('Comp. d', 'Comp. q', 'Comp. Homopolar'), loc='upper left')
                plt.title('Transformada de Park')
                plt.ylabel('Amplitude(kV)')
                plt.grid()
#==============================================================================#
                p4 = plt.subplot(4, 1, 4)
                pA2=p4.plot(self.ListaTempo,self.FaseA2)
                pB2=p4.plot(self.ListaTempo,self.FaseB2)
                pC2=p4.plot(self.ListaTempo,self.FaseC2)
                plt.tight_layout()
                p4.legend((pA2[0], pB2[0], pC2[0]), ('Fase A', 'Fase B', 'Fase C'), loc='upper left')
                plt.title('Componentes de Fase obtidos pela transformação dq0-ABC')
                plt.ylabel('Amplitude(kV)')
                plt.grid()

                #plt.ylim((-1.5*max([self.ampA,self.ampB,self.ampC]), 1.5*max([self.ampA,self.ampB,self.ampC])))
#==============================================================================#
            else:
                self.FaseA += [xa]
                self.FaseB += [xb]
                self.FaseC += [xc]

                self.FaseA2 += [abc[0]]
                self.FaseB2 += [abc[1]]
                self.FaseC2 += [abc[2]]

                self.ListaIAlpha += [ab0[0]]
                self.ListaIBeta += [ab0[1]]
                self.ListaSeq0 += [ab0[2]]
                self.ListaTempo += [self.t*1000]
                self.ListaD += [dq0[0]]
                self.ListaQ += [dq0[1]]
                self.ListaSeq0dq += [dq0[2]]

            self.box.remove_widget(self.tela)
            self.tela = FigureCanvasKivyAgg(plt.gcf(), size_hint=(.75,.75),pos_hint={'center_y': .45})
            self.box.add_widget(self.tela)
        else:
            pass

Transformadas().run()
