from vpython import *

# Função que tem como parâmetro o corpo a ser deslocado e faz o cálculo da trajetória
def deslocar(corpo):
    global dt
    queda = True
    p = corpo.traj.point(corpo.traj.npoints-1)['pos']
    corpo.pos += dt*corpo.v + dt**2*corpo.a/2.
    if corpo.v.y < 0 and corpo.pos.y < corpo.radius:
        if p.y != corpo.pos.y:
          f = (p.y - corpo.radius)/(p.y - corpo.pos.y)
          corpo.pos -= (1 - f)*(corpo.pos - p)
          corpo.v += f*dt*corpo.a
          corpo.t += f*dt
        queda = False
    else:
       corpo.t += dt
       corpo.v += dt*corpo.a
    corpo.traj.append(pos=vec(corpo.pos))
    corpo.d += mag(corpo.pos - p)
    return queda

# Função que tem como parâmetro o corpo e retorna os valores de alcance, tempo, distância percorrida e velocidade média
def resultados(corpo):
    p0 = corpo.traj.point(0)['pos']
    alcance = corpo.pos.x - p0.x
    velocidade = corpo.d / corpo.t
    scene.caption += '<b>'+corpo.legenda+'</b>\n'
    scene.caption += 'Tempo de voo         = {:.2f} s\n'.format(corpo.t)
    scene.caption += 'Alcance horizontal   = {:.2f} m\n'.format(alcance)
    scene.caption += 'Distância percorrida = {:.2f} m\n'.format(corpo.d)
    scene.caption += 'Velocidade média     = {:.2f} m/s\n'.format(velocidade)
    return

# Função que tem como parâmetro o corpo, a velocidade e ângulo desse corpo, e uma legenda, e retorna
def projetar(corpo, vel, ang, leg):
    corpo.v = vel*vec(cos(ang*pi/180.), sin(ang*pi/180.), 0)
    corpo.t = corpo.d = 0
    corpo.legenda = leg
    corpo.traj = curve(pos=vec(corpo.pos),color=corpo.color)

# Valores para o usuário entrar
velocidade = float(input("Informe a velocidade que o corpo foi lançado (m/s): "))
angulo = float(input("Informe o ângulo de lançamento do corpo (graus): "))

scene = canvas(title = '<h1>Trabalho de Física I - Prof. Dimitry</h1>'
                       '<h4>Grupo: Italo Vicente Oliveira Uchoa | João Matheus De Lima Alves | Layza Maria Rodrigues Carneiro | Maria Fernanda Cordeiro Crisóstomo | Silvio Gonçalves Xavier Junior</h4>'
                       '<h2>Movimento balístico</h2>', forward=vec(-0.5, -0.2, -1))
scene.caption = '\n\n'

a = 47
dt = 0.01
g = vec(0, -9.8, 0)
q1 = True

corpo = sphere(pos=vec(-7, 0, 1), radius=0.5, texture=textures.earth)
chao = box(pos=vec(0, -0.1, 0), size=vec(20, 0.2, 10), texture=textures.stucco)
parede = box(pos=vec(0, 2.8, -5.05), size=vec(20, 6, 0.1), color=vec(0.7, 0.7, 0.7))
frase = text(pos=vec(0, 2.8, -5), text='404_ERROR', color=color.red, align='center', depth=0.5)

projetar(corpo, velocidade, angulo, 'Resultados do movimento balístico executado pelo corpo')
corpo.a = g

while q1:
    rate(100)
    if q1: q1 = deslocar(corpo)

resultados(corpo)