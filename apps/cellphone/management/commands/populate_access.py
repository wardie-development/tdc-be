from django.core.management.base import BaseCommand
from apps.cellphone.models import Cellphone, Brand, CellphoneAccess


class Command(BaseCommand):

    def handle(self, *args, **options):
        entities = """
42,https://tecnicosdecelular.com.br/tabela-plus/,TDC,equipetdc,75981642302,2023-09-06 15:43:04,2025-12-30 12:42:00,1
43,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jaciel,bvf2iv,75982414475,2023-09-06 16:23:49,2024-02-29 13:23:00,1
44,https://tecnicosdecelular.com.br/tabela-plus-teste/,Brunna,cxxww#,64993184709,2023-09-06 18:08:33,2023-09-07 15:06:00,1
45,https://tecnicosdecelular.com.br/tabela-plus/,Wellington Pereira,ibbmac,11944416393,2023-09-06 18:23:37,2023-10-06 15:09:00,1
46,https://tecnicosdecelular.com.br/tabela-plus-teste/,Linconl Martins,26@40g,66999397920,2023-09-06 18:55:14,2023-09-07 15:55:00,1
47,https://tecnicosdecelular.com.br/tabela-plus/,Iana Paula Rocha da Silva,1xaczp,77981299303,2023-09-06 19:15:30,2023-10-06 16:15:00,1
48,https://tecnicosdecelular.com.br/tabela-plus/,Matheus Felipe,7twp2i,33991325871,2023-09-06 19:25:22,2024-03-06 16:25:00,1
49,https://tecnicosdecelular.com.br/tabela-plus/,Matheus Levi Ramos,o486s3,55999532848,2023-09-06 19:47:18,2024-03-06 16:47:00,1
50,https://tecnicosdecelular.com.br/tabela-plus-teste/,Cristiano Gonçalves,gma5vk,11960942295,2023-09-06 22:18:24,2023-09-07 19:18:00,1
51,https://tecnicosdecelular.com.br/tabela-plus-teste/,Flávia Sotana,z8j370,15991766059,2023-09-06 23:00:08,2023-09-07 19:18:00,1
52,https://tecnicosdecelular.com.br/tabela-plus-teste/,Antônia Vasconcelos de Sousa,m1kmft,99984472790,2023-09-07 16:24:34,2023-09-08 13:24:00,1
53,https://tecnicosdecelular.com.br/tabela-plus/,Emily Jeane,bqrrfu,97984232918,2023-09-07 17:24:17,2024-01-06 16:04:00,1
54,https://tecnicosdecelular.com.br/tabela-plus/,Ricardo Miguell Alves Amaral,mb7wha,21989108299,2023-09-07 17:24:50,2024-03-08 13:25:00,1
55,https://tecnicosdecelular.com.br/tabela-plus-teste/,Sávio Gabriel,2os040,11983689696,2023-09-07 17:57:24,2024-03-08 13:25:00,1
56,https://tecnicosdecelular.com.br/tabela-plus/,Kallebe Costa,pg4ve4,62999776045,2023-09-07 18:08:47,2024-02-05 15:10:00,1
57,https://tecnicosdecelular.com.br/tabela-plus/,Walerson Silva,vq3jyg,64974006629,2023-09-07 18:11:45,2024-02-14 15:10:00,1
58,https://tecnicosdecelular.com.br/tabela-plus/,Tancredo Rodrigues,3t#oz4,82982004599,2023-09-07 18:14:05,2024-03-02 15:10:00,1
59,https://tecnicosdecelular.com.br/tabela-plus/,Edivaldo da Costa Veloso,sxxas9,86994785230,2023-09-07 18:18:04,2023-11-18 15:17:00,1
60,https://tecnicosdecelular.com.br/tabela-plus/,Érica Silva,edn6v5,19991197970,2023-09-07 18:19:04,2023-11-22 15:17:00,1
61,https://tecnicosdecelular.com.br/tabela-plus/,José Raimundo,y1a6n0,71988664657,2023-09-07 18:20:31,2024-01-26 15:20:00,1
62,https://tecnicosdecelular.com.br/tabela-plus/,Talles Barros,ajv5qx,19991312121,2023-09-07 18:49:43,2024-02-24 15:49:00,1
63,https://tecnicosdecelular.com.br/tabela-plus-teste/,Israel pereira lima,#8px7c,21975846599,2023-09-07 18:55:58,2023-09-08 15:55:00,1
64,https://tecnicosdecelular.com.br/tabela-plus/,Sidiane Gervasio,vy3svp,62981201258,2023-09-07 19:02:31,2023-12-16 16:01:00,1
65,https://tecnicosdecelular.com.br/tabela-plus/,Cleonice Bento,3ppj5c,88999660300,2023-09-07 20:27:06,2023-12-05 17:26:00,1
66,https://tecnicosdecelular.com.br/tabela-plus-teste/,Allan Santos Azevedo de Assis,yct7mr,21982552937,2023-09-07 21:40:44,2023-10-07 18:40:00,1
67,https://tecnicosdecelular.com.br/tabela-plus-teste/,Antonio Abreu de Souza,jxjtaz,61998164738,2023-09-08 00:58:32,2023-09-10 21:58:00,1
68,https://tecnicosdecelular.com.br/tabela-plus-teste/,Monique Antunes de Carvalho,llkmtx,31985056995,2023-09-08 02:02:31,2023-09-10 23:02:00,1
69,https://tecnicosdecelular.com.br/tabela-plus/,Antonio Abreu de Souza,vq0fqb,61998164738,2023-09-08 11:57:32,2023-10-08 08:57:00,1
70,https://tecnicosdecelular.com.br/tabela-plus-teste/,Leonardo Brito e Silva,lrdgdt,99984945569,2023-09-08 14:34:16,2023-09-10 11:33:00,1
71,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gilson da Silva Ferreira,j@auwo,82999283082,2023-09-08 14:37:40,2023-09-10 11:33:00,1
72,https://tecnicosdecelular.com.br/tabela-plus-teste/,Maria Aparecida Souza Santos,iv2mxl,82993270068,2023-09-08 14:38:41,2023-09-10 11:33:00,1
76,https://tecnicosdecelular.com.br/tabela-plus-teste/,Andre Henrique da Silva,pdy45z,11976335262,2023-09-08 16:35:17,2023-09-10 13:33:00,1
77,https://tecnicosdecelular.com.br/tabela-plus/,Bruna Santana da Silva,8ob3@i,27992597545,2023-09-08 16:41:13,2023-10-14 13:42:00,1
78,https://tecnicosdecelular.com.br/tabela-plus/,Caio Garrido,y@teu8,21980689084,2023-09-08 16:56:59,2024-02-19 13:42:00,1
79,https://tecnicosdecelular.com.br/tabela-plus/,Kênio Raimundo,g5jge@,33999748391,2023-09-08 17:03:40,2024-01-18 14:03:00,1
80,https://tecnicosdecelular.com.br/tabela-plus/,Anderson dos Santos,ahmfns,11976712659,2023-09-08 17:14:02,2024-02-12 14:13:00,1
82,https://tecnicosdecelular.com.br/tabela-plus/,Luis Barreto,rg750c,21975645164,2023-09-08 17:16:04,2024-02-16 14:13:00,1
83,https://tecnicosdecelular.com.br/tabela-plus/,Fernando dos Reis,pg48y8,11989464456,2023-09-08 17:17:06,2024-01-01 14:13:00,1
84,https://tecnicosdecelular.com.br/tabela-plus/,José Ernandes,1@edud,88993279840,2023-09-08 17:19:20,2024-02-07 14:13:00,1
85,https://tecnicosdecelular.com.br/tabela-plus/,Sabrina Fernanda,rmok0t,21979730279,2023-09-08 17:20:53,2023-11-22 14:13:00,1
86,https://tecnicosdecelular.com.br/tabela-plus/,Érick Gouvêa,v6p7ti,43996956700,2023-09-08 17:27:57,2023-12-19 14:13:00,1
87,https://tecnicosdecelular.com.br/tabela-plus/,Patrick Ferreira,nefolr,96984094461,2023-09-08 17:29:15,2023-09-23 14:13:00,1
89,https://tecnicosdecelular.com.br/tabela-plus/,Joersians Maik,#nbpqf,89994158120,2023-09-08 17:32:53,2023-12-17 14:32:00,1
90,https://tecnicosdecelular.com.br/tabela-plus/,Luis Gustavo,pv7#s6,18997057220,2023-09-08 17:34:52,2024-02-07 14:32:00,1
91,https://tecnicosdecelular.com.br/tabela-plus/,Paulo Sérgio Paiva,ia@hv5,32988255582,2023-09-08 17:37:30,2024-01-05 14:32:00,1
92,https://tecnicosdecelular.com.br/tabela-plus/,Henrique Trajano,12078800,22988272264,2023-09-08 17:38:39,2024-01-06 14:32:00,1
93,https://tecnicosdecelular.com.br/tabela-plus/,Conserta Aki,46pdh4,11968646765,2023-09-08 17:52:09,2023-10-21 14:39:00,1
94,https://tecnicosdecelular.com.br/tabela-plus/,Sarita Alves,0e3w8y,47999288800,2023-09-08 17:54:37,2023-12-09 14:39:00,1
95,https://tecnicosdecelular.com.br/tabela-plus/,Celso Bones,hwdc5n,86999545700,2023-09-08 18:00:35,2023-12-27 14:39:00,1
97,https://tecnicosdecelular.com.br/tabela-plus/,Lucas Prada,weea@u,47991458574,2023-09-08 18:05:41,2024-01-04 14:39:00,1
98,https://tecnicosdecelular.com.br/tabela-plus/,Rubinho Mariotti,nuvu9v,46999114813,2023-09-08 18:08:01,2024-02-16 14:39:00,1
99,https://tecnicosdecelular.com.br/tabela-plus/,Milleni Dourado,9vhxmo,62983182223,2023-09-08 18:11:20,2024-01-14 14:39:00,1
100,https://tecnicosdecelular.com.br/tabela-plus/,Maria Letícia,1n66zc,81999598291,2023-09-08 18:12:28,2024-01-31 14:39:00,1
101,https://tecnicosdecelular.com.br/tabela-plus/,Abda Guedes ,fp4buj,48984657323,2023-09-08 18:13:48,2023-12-07 14:39:00,1
102,https://tecnicosdecelular.com.br/tabela-plus/,Cledimar Leite,axuo6h,61996031886,2023-09-08 18:15:27,2023-10-18 14:39:00,1
103,https://tecnicosdecelular.com.br/tabela-plus/,Matheus Alves Costa,9mcw93,31973576875,2023-09-08 18:37:11,2024-02-28 14:39:00,1
104,https://tecnicosdecelular.com.br/tabela-plus/,Binho Cel,#zdj7j,33988862788,2023-09-08 18:38:50,2024-01-01 14:39:00,1
105,https://tecnicosdecelular.com.br/tabela-plus/,Mayra Patrícia ,149we1,87991689182,2023-09-08 18:44:31,2023-10-08 15:45:00,1
107,https://tecnicosdecelular.com.br/tabela-plus/,Caio Cesar,5ifrdv,16991177120,2023-09-08 18:49:14,2023-12-26 15:45:00,1
108,https://tecnicosdecelular.com.br/tabela-plus-teste/,Mirlei de Ávila,ng7js7,11974774672,2023-09-08 18:50:48,2023-09-10 15:45:00,1
109,https://tecnicosdecelular.com.br/tabela-plus/,Alexandre Brandão,snl4sb,31982767414,2023-09-08 18:53:17,2023-12-05 15:45:00,1
110,https://tecnicosdecelular.com.br/tabela-plus/,Rodrigo Michelon,0tmt@n,55999515249,2023-09-08 18:54:20,2023-12-23 15:45:00,1
111,https://tecnicosdecelular.com.br/tabela-plus/,Adolfo Rezitano,ma@0wh,13988815132,2023-09-08 18:58:24,2023-10-08 15:45:00,0
112,https://tecnicosdecelular.com.br/tabela-plus/,Laura  Sachett,#@z0o2,67998396564,2023-09-08 18:59:56,2023-11-21 15:45:00,1
113,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gabriel Moreira,554b9@,43991210443,2023-09-08 19:01:58,2023-09-10 15:45:00,1
114,https://tecnicosdecelular.com.br/tabela-plus/,Vinícius Santos ,baojz#,62996460095,2023-09-08 19:04:41,2023-12-26 15:45:00,1
115,https://tecnicosdecelular.com.br/tabela-plus/,Pablo Alex,1yvl9#,75999941197,2023-09-08 19:06:46,2023-10-28 15:45:00,1
117,https://tecnicosdecelular.com.br/tabela-plus/,Lucas Silveira,z3h7@4,21972793359,2023-09-08 19:09:07,2024-02-18 16:08:00,1
118,https://tecnicosdecelular.com.br/tabela-plus/,Tayane Oliveira Tadeu,38e8pq,11975002488,2023-09-08 19:10:55,2023-09-10 16:08:00,1
119,https://tecnicosdecelular.com.br/tabela-plus/,Fernando Crispim,@wks1a,14998588163,2023-09-08 19:12:35,2024-02-11 16:08:00,1
120,https://tecnicosdecelular.com.br/tabela-plus/,Cleidimar,rb1596,73991083363,2023-09-08 19:15:14,2023-12-22 16:08:00,1
121,https://tecnicosdecelular.com.br/tabela-plus/,Marcos Anderson,j#7e08,62995288949,2023-09-08 19:16:25,2024-01-06 16:08:00,1
122,https://tecnicosdecelular.com.br/tabela-plus/,Marcos Antônio,r7oe9j,34996673450,2023-09-08 19:18:51,2023-12-17 16:18:00,1
123,https://tecnicosdecelular.com.br/tabela-plus/,Edicarlos Hinode,ob8iab,74988538050,2023-09-08 19:21:04,2024-02-19 16:18:00,1
124,https://tecnicosdecelular.com.br/tabela-plus/,Eduardo Farias,#sru@v,11964670307,2023-09-08 19:24:37,2023-11-28 16:18:00,1
125,https://tecnicosdecelular.com.br/tabela-plus/,Thaigo Vinício,52s@w3,21971413487,2023-09-08 19:27:25,2023-12-12 16:18:00,1
126,https://tecnicosdecelular.com.br/tabela-plus/,Diego Pinto,zu9p2b,77988656035,2023-09-08 19:29:25,2023-09-15 16:18:00,1
127,https://tecnicosdecelular.com.br/tabela-plus/,Michael Piter,umb5zp,27999803400,2023-09-08 19:30:49,2024-02-29 16:18:00,1
128,https://tecnicosdecelular.com.br/tabela-plus/,Maikon Santana,rn8pai,75999796518,2023-09-08 21:36:04,2023-12-23 18:30:00,1
129,https://tecnicosdecelular.com.br/tabela-plus/,Gmc do Brasil,ya@jb#,19974141025,2023-09-08 21:38:26,2024-01-03 18:30:00,1
130,https://tecnicosdecelular.com.br/tabela-plus/,Elias Santos,gig24@,71999497871,2023-09-08 21:40:35,2024-02-02 18:30:00,1
131,https://tecnicosdecelular.com.br/tabela-plus/,Guilherme Venturini,itvdr4,17997226431,2023-09-08 21:47:24,2024-01-31 18:30:00,1
132,https://tecnicosdecelular.com.br/tabela-plus/,Luis Henrique,g4c#9i,33988662825,2023-09-08 21:48:41,2024-02-14 18:30:00,1
133,https://tecnicosdecelular.com.br/tabela-plus/,Jucilene,eutsj2,11955550077,2023-09-08 21:51:25,2024-01-13 18:30:00,1
134,https://tecnicosdecelular.com.br/tabela-plus/,Uedson Vieira,t1i8hk,73998389472,2023-09-08 21:53:13,2023-09-14 18:30:00,1
135,https://tecnicosdecelular.com.br/tabela-plus/,Paulo Rossitto,p05@47,14996898322,2023-09-08 21:56:18,2024-02-04 18:30:00,1
136,https://tecnicosdecelular.com.br/tabela-plus/,Gustavo Cardelli,j7l9k5,16997177071,2023-09-08 21:57:36,2024-06-29 10:05:00,1
137,https://tecnicosdecelular.com.br/tabela-plus/,Valdeir Rodrigues,0qhpxt,65999187990,2023-09-08 22:00:29,2024-02-14 18:30:00,1
138,https://tecnicosdecelular.com.br/tabela-plus/,Victor Barcelos,yk9#rw,33999746199,2023-09-08 22:07:55,2024-01-22 18:30:00,1
139,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gabriela Feitosa Santana,hvv8pj,13981873576,2023-09-08 22:17:13,2023-09-10 18:30:00,0
140,https://tecnicosdecelular.com.br/tabela-plus/,Miguel Goulart,9fyg31,48998334966,2023-09-08 22:43:33,2024-02-10 19:40:00,1
141,https://tecnicosdecelular.com.br/tabela-plus/,Moab Matias,76@l@b,88982186455,2023-09-08 22:46:38,2024-01-06 19:44:00,1
142,https://tecnicosdecelular.com.br/tabela-plus/,Idelvan Santana Porto,95909g,73999479042,2023-09-08 22:48:24,2024-03-08 19:50:00,1
143,https://tecnicosdecelular.com.br/tabela-plus/,Leucimaria Maia,j85m7i,11981612049,2023-09-08 22:57:17,2023-12-02 19:50:00,1
144,https://tecnicosdecelular.com.br/tabela-plus/,Jean Matos,4rn@t3,48998046493,2023-09-08 22:58:29,2023-12-30 19:50:00,1
145,https://tecnicosdecelular.com.br/tabela-plus/,Everton Moraes,p03#l7,45999997395,2023-09-08 23:01:33,2024-02-17 19:50:00,1
146,https://tecnicosdecelular.com.br/tabela-plus/,Gabriela Feitosa Santana,x#j78a,13981873576,2023-09-08 23:16:00,2023-10-08 20:15:00,1
148,https://tecnicosdecelular.com.br/tabela-plus/,Everthon Douglas,60ur2n,11998457543,2023-09-08 23:31:51,2023-10-08 20:31:00,1
149,https://tecnicosdecelular.com.br/tabela-plus-teste/,Pollyane Nery Santos,pollyane,38991495122,2023-09-09 14:47:19,2023-09-12 11:46:00,1
150,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jutahy Silva De Santana,Jutahy,71984795174,2023-09-09 14:49:21,2023-09-12 11:46:00,1
151,https://tecnicosdecelular.com.br/tabela-plus-teste/,Eduardo Henrique Gomes Vieira,mjxrq2,31997986035,2023-09-09 15:00:37,2023-09-12 11:46:00,0
152,https://tecnicosdecelular.com.br/tabela-plus-teste/,Luiz Fernando Cazionato de Souza,8oe0v7,14999090543,2023-09-09 15:03:01,2023-09-12 11:46:00,1
153,https://tecnicosdecelular.com.br/tabela-plus/,Eduardo Henrique Gomes Vieira,gp664b,31997986035,2023-09-09 15:50:36,2023-10-09 12:50:00,1
154,https://tecnicosdecelular.com.br/tabela-plus/,Josias de Jesus,3pwcax,79996738365,2023-09-09 15:55:42,2023-10-10 12:50:00,1
155,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gustavo Henrique Pereira Dutra,kshbqa,31971934565,2023-09-09 16:03:32,2023-09-11 12:50:00,1
156,https://tecnicosdecelular.com.br/tabela-plus-teste/,Luciano,k29a1s,66992071950,2023-09-09 16:27:24,2023-09-11 12:50:00,1
157,https://tecnicosdecelular.com.br/tabela-plus-teste/,Fábio Vaz da Silva,n7sgjm,41996101538,2023-09-09 16:28:17,2023-09-11 12:50:00,1
158,https://tecnicosdecelular.com.br/tabela-plus-teste/,Valdir Gomes,wqkae5,85985686399,2023-09-10 01:38:50,2023-09-12 22:32:00,1
159,https://tecnicosdecelular.com.br/tabela-plus-teste/,Piter César de arruda,t5cfl@,11952158052,2023-09-10 01:40:17,2023-09-12 22:32:00,1
160,https://tecnicosdecelular.com.br/tabela-plus/,Ezequiel Ignaszevski,v9nh4i,47988573434,2023-09-10 01:43:25,2024-01-13 22:32:00,1
161,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gabriel Pereira,ngyku0,82999511031,2023-09-10 01:44:50,2023-09-12 22:32:00,1
162,https://tecnicosdecelular.com.br/tabela-plus/,Gabriel Mateus,x7rmi9,15997266951,2023-09-10 01:47:40,2023-09-12 22:32:00,1
163,https://tecnicosdecelular.com.br/tabela-plus/,Carlos Augusto,@w14dk,11957785078,2023-09-10 01:52:10,2024-01-03 22:32:00,1
164,https://tecnicosdecelular.com.br/tabela-plus/,Dennis Augusto Riotinto,1jaffz,11958408186,2023-09-10 02:08:53,2023-10-09 22:32:00,1
165,https://tecnicosdecelular.com.br/tabela-plus/,Samir de Souza,841n6f,51998881796,2023-09-10 12:56:42,2024-01-27 09:56:00,1
166,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jeff Castro,06466v,21969432225,2023-09-10 12:59:31,2023-09-13 09:56:00,1
167,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gustavo Honório,vxx4j2,11942814532,2023-09-10 13:07:23,2023-09-13 09:56:00,1
168,https://tecnicosdecelular.com.br/tabela-plus-teste/,Pablo Henrique,se3xv1,67981061885,2023-09-10 13:09:05,2023-09-13 09:56:00,1
169,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jaqueline Gonçalves dos Santos,n2plpw,71996620686,2023-09-10 13:12:00,2023-09-13 09:56:00,0
170,https://tecnicosdecelular.com.br/tabela-plus-teste/,Erica Menezes dos Santos,hzfsv@,75982810023,2023-09-10 13:13:02,2023-09-13 09:56:00,1
171,https://tecnicosdecelular.com.br/tabela-plus-teste/,João Carlos Lopes,fpylne,38999465748,2023-09-10 13:16:32,2023-09-13 09:56:00,1
172,https://tecnicosdecelular.com.br/tabela-plus/,Jaqueline Gonçalves dos Santos,n2plpw,71996620686,2023-09-10 13:31:34,2023-10-10 10:16:00,1
174,https://tecnicosdecelular.com.br/tabela-plus-teste/,Oseias Borges Soares,nlf0jv,71981708128,2023-09-10 14:19:48,2023-09-13 11:19:00,1
175,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rerisson,mfgpj5,81998732353,2023-09-11 11:16:19,2023-09-14 08:16:00,1
176,https://tecnicosdecelular.com.br/tabela-plus-teste/,Daynor,s@gw89,97984112204,2023-09-11 11:19:42,2023-09-14 08:16:00,1
177,https://tecnicosdecelular.com.br/tabela-plus-teste/,José Felipe,38rb3e,44998569868,2023-09-11 11:26:14,2023-09-14 08:24:00,1
178,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rodrigo,cuxlrk,35988469796,2023-09-11 11:31:26,2023-09-14 08:31:00,1
179,https://tecnicosdecelular.com.br/tabela-plus-teste/,Ângelo Saulo,c4h8im,31983450222,2023-09-11 12:03:02,2023-09-14 08:31:00,1
180,https://tecnicosdecelular.com.br/tabela-plus/,Fernando Kloster,ec2g9f,42999899406,2023-09-11 12:45:26,2024-03-11 09:41:00,1
181,https://tecnicosdecelular.com.br/tabela-plus/,Pedro Guilherme de Camargo,w642@p,42988397957,2023-09-11 13:07:18,2023-10-11 10:08:00,1
183,https://tecnicosdecelular.com.br/tabela-plus-teste/,Paulo Ricardo,k3af4i,11997417745,2023-09-11 13:28:06,2023-09-14 10:27:00,1
186,https://tecnicosdecelular.com.br/tabela-plus-teste/,Felipe Almeida,rgosg1,21982855333,2023-09-11 14:07:46,2023-10-11 11:06:00,1
188,https://tecnicosdecelular.com.br/tabela-plus-teste/,Danylo Viera,nn5qb6,82993645326,2023-09-11 14:17:01,2023-09-14 11:15:00,1
192,https://tecnicosdecelular.com.br/tabela-plus-teste/,Laurianne Ricarda,fae0kl,94992179842,2023-09-11 16:30:58,2023-09-14 13:30:00,1
193,https://tecnicosdecelular.com.br/tabela-plus/,Emerson da Silva,gex41s,71993581204,2023-09-11 16:35:24,2023-10-11 13:34:00,1
194,https://tecnicosdecelular.com.br/tabela-plus-teste/,Márcio,vf6912,18988280626,2023-09-11 16:50:15,2023-09-14 13:49:00,1
196,https://tecnicosdecelular.com.br/tabela-plus/,Thiago de Melo,qoxc3q,15996499688,2023-09-11 17:15:45,2023-10-11 14:14:00,1
197,https://tecnicosdecelular.com.br/tabela-plus-teste/,FC Tech,6bj@2t,31971926669,2023-09-11 17:19:18,2023-09-14 14:19:00,1
198,https://tecnicosdecelular.com.br/tabela-plus-teste/,Cellphone,40dwlv,27995310584,2023-09-11 18:28:30,2023-09-14 15:27:00,1
199,https://tecnicosdecelular.com.br/tabela-plus-teste/,Marco antonio,hmad7h,28998863256,2023-09-11 18:35:29,2023-09-14 15:34:00,1
200,https://tecnicosdecelular.com.br/tabela-plus-teste/,Hamilton Lima,m9@yrc,84994786159,2023-09-11 18:38:06,2023-09-14 15:37:00,1
202,https://tecnicosdecelular.com.br/tabela-plus/,Márcio,290q@8,18988280626,2023-09-11 18:43:41,2024-03-11 15:43:00,1
203,https://tecnicosdecelular.com.br/tabela-plus/,Felipe Henrique Pereira,st@8ku,31971926669,2023-09-11 20:21:15,2023-10-11 17:20:00,1
205,https://tecnicosdecelular.com.br/tabela-plus/,Gabriel Abrantes,2sbr33,21966454760,2023-09-11 22:33:18,2023-10-11 19:32:00,1
206,https://tecnicosdecelular.com.br/tabela-plus-teste/,Edilson Soares,0ha9sb,82999922339,2023-09-11 22:39:30,2023-09-14 19:39:00,1
207,https://tecnicosdecelular.com.br/tabela-plus/,Géssica Lanes,j03smi,22992146588,2023-09-12 12:10:46,2023-10-12 09:08:00,1
208,https://tecnicosdecelular.com.br/tabela-plus-teste/,Emilly Ângelo,24eqng,48988248433,2023-09-12 13:04:28,2023-09-15 10:04:00,1
209,https://tecnicosdecelular.com.br/tabela-plus-teste/,Juan Kinber,kncfj5,19994572292,2023-09-12 13:20:22,2023-09-15 10:20:00,1
210,https://tecnicosdecelular.com.br/tabela-plus-teste/,Guilherme Emerick,cx9p5c,31972147051,2023-09-12 13:37:15,2023-09-15 10:37:00,1
212,https://tecnicosdecelular.com.br/tabela-plus-teste/,Renan Ferreira,d1y2p4,38999424654,2023-09-12 14:27:46,2023-09-15 11:27:00,1
214,https://tecnicosdecelular.com.br/tabela-plus-teste/,Matheus Bernardino,rqdboc,47997526879,2023-09-12 16:24:35,2023-09-15 13:24:00,1
215,https://tecnicosdecelular.com.br/tabela-plus-teste/,Alisson Júnior ,ti2bda,71994165894,2023-09-12 16:28:11,2023-09-15 13:24:00,1
218,https://tecnicosdecelular.com.br/tabela-plus-teste/,Guilherme Santos,5z367g,62984712780,2023-09-12 16:35:03,2023-09-15 13:34:00,1
219,https://tecnicosdecelular.com.br/tabela-plus-teste/,Eduardo Fernando,ywvl@9,11930288078,2023-09-12 17:06:28,2023-09-15 14:06:00,1
220,https://tecnicosdecelular.com.br/tabela-plus-teste/,Cliente Teste,tdc108,84996167565,2023-09-12 18:04:15,2024-01-09 08:12:00,1
221,https://tecnicosdecelular.com.br/tabela-plus-teste/,Andreza de Oliveira,higmxo,31974019521,2023-09-12 18:20:26,2023-09-15 15:20:00,1
222,https://tecnicosdecelular.com.br/tabela-plus-teste/,Marcus Tadeu,j0dmui,62991196121,2023-09-12 18:53:48,2023-09-15 15:53:00,1
223,https://tecnicosdecelular.com.br/tabela-plus-teste/,Everson José,kyqtdf,42999170925,2023-09-12 18:59:51,2023-09-15 15:59:00,1
224,https://tecnicosdecelular.com.br/tabela-plus-teste/,Manoel messias,tdlirx,83987328457,2023-09-12 19:23:54,2023-09-15 16:23:00,1
225,https://tecnicosdecelular.com.br/tabela-plus-teste/,Carlos Lucas,222a@s,21993680236,2023-09-12 19:24:01,2023-09-15 16:23:00,1
226,https://tecnicosdecelular.com.br/tabela-plus-teste/,Deiber Alexis,ad0ts@,17991180882,2023-09-12 22:20:36,2023-09-15 19:20:00,1
227,https://tecnicosdecelular.com.br/tabela-plus/,Valtair Lemes,sozfo3,35999310036,2023-09-12 23:02:51,2024-03-12 20:01:00,1
228,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gustavo Henrique,a@rgi1,31992159701,2023-09-13 00:42:31,2023-09-15 21:42:00,1
231,https://tecnicosdecelular.com.br/tabela-plus-teste/,Andressa Freire,03qbrx,71991840173,2023-09-13 01:12:05,2023-09-15 22:11:00,1
232,https://tecnicosdecelular.com.br/tabela-plus-teste/,Alex Santos,y@08ki,51997279349,2023-09-13 12:33:56,2023-09-16 09:33:00,1
234,https://tecnicosdecelular.com.br/tabela-plus-teste/,Caroline Alves,qxo84o,34991827102,2023-09-13 12:45:55,2023-09-16 09:43:00,1
235,https://tecnicosdecelular.com.br/tabela-plus-teste/,Debora Tayna,65gxul,55997087038,2023-09-13 13:02:09,2023-09-16 10:01:00,1
236,https://tecnicosdecelular.com.br/tabela-plus-teste/,Michelly Americana,25l2y6,34999540578,2023-09-13 13:14:32,2023-09-16 10:14:00,1
237,https://tecnicosdecelular.com.br/tabela-plus/,Luciano de Assis,f31apv,27998381147,2023-09-13 13:54:03,2023-12-05 10:53:00,1
238,https://tecnicosdecelular.com.br/tabela-plus-teste/,MHL CELL,splzq0,11954991831,2023-09-13 14:05:16,2023-09-16 11:05:00,1
240,https://tecnicosdecelular.com.br/tabela-plus-teste/,Ana Paula,7it@ql,66996975767,2023-09-13 14:49:10,2023-09-16 11:48:00,1
243,https://tecnicosdecelular.com.br/tabela-plus-teste/,Arthur Muller,5@@foi,94981165758,2023-09-13 17:00:01,2023-09-16 13:59:00,1
244,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gilberto Rodrigues,3685lm,34999609430,2023-09-13 17:10:48,2023-09-16 14:06:00,1
245,https://tecnicosdecelular.com.br/tabela-plus-teste/,Matheus,261xxz,11949613366,2023-09-13 17:19:42,2023-09-16 14:19:00,1
246,https://tecnicosdecelular.com.br/tabela-plus/,Vandilson Rodrigues,xozf@6,77999274425,2023-09-13 17:34:29,2024-03-13 14:31:00,1
247,https://tecnicosdecelular.com.br/tabela-plus/,Rafael Borges,ic9qka,44999018241,2023-09-13 17:48:49,2023-10-13 14:47:00,1
248,https://tecnicosdecelular.com.br/tabela-plus-teste/,Willian Rafael,48nkhx,19986092023,2023-09-13 18:34:49,2023-09-16 15:34:00,1
249,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jazailza,1@zp4i,47992691132,2023-09-13 18:37:28,2023-09-16 15:34:00,1
250,https://tecnicosdecelular.com.br/tabela-plus-teste/,Larissa Gomes,z6u8jd,12996666756,2023-09-13 18:56:08,2023-09-16 15:55:00,1
251,https://tecnicosdecelular.com.br/tabela-plus/,Guilherme Santos,@x3k6s,62984712780,2023-09-13 19:29:57,2023-10-13 16:25:00,1
252,https://tecnicosdecelular.com.br/tabela-plus/,Enny Pinheiro,kwsojh,71987998127,2023-09-13 23:00:22,2023-10-05 19:59:00,1
253,https://tecnicosdecelular.com.br/tabela-plus-teste/,César de Arruda,ojwns3,11952158052,2023-09-13 23:30:38,2023-09-16 20:30:00,1
254,https://tecnicosdecelular.com.br/tabela-plus-teste/,Neto Visgueira,dt9m97,86981390585,2023-09-13 23:33:21,2023-09-16 20:30:00,1
255,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jessé Cardoso,0p37wy,61998598387,2023-09-13 23:34:57,2023-09-16 20:30:00,1
256,https://tecnicosdecelular.com.br/tabela-plus-teste/,Maria Eduarda,osdrl8,13997044329,2023-09-13 23:36:08,2023-09-16 20:30:00,1
257,https://tecnicosdecelular.com.br/tabela-plus-teste/,Mônica Braga,rak6ra,71988386818,2023-09-13 23:37:34,2023-09-16 20:30:00,1
258,https://tecnicosdecelular.com.br/tabela-plus/,William Santos,388@7n,16992379287,2023-09-14 00:06:12,2024-02-24 19:59:00,1
259,https://tecnicosdecelular.com.br/tabela-plus/,Piter César,z@5x9o,11952158052,2023-09-14 00:06:36,2023-10-13 21:05:00,1
260,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jeferson Antonio ,1z3@4f,87996188901,2023-09-14 12:49:33,2023-09-17 09:49:00,1
261,https://tecnicosdecelular.com.br/tabela-plus-teste/,Eric Sampaio,bcx7sm,19971052100,2023-09-14 13:14:26,2023-09-17 10:14:00,1
262,https://tecnicosdecelular.com.br/tabela-plus/,Matheus Bernardino,hgh82e,47997526879,2023-09-14 13:38:39,2023-10-14 10:37:00,1
263,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jonas Batista,e6tyxu,11940172861,2023-09-14 13:41:40,2023-09-17 10:41:00,1
264,https://tecnicosdecelular.com.br/tabela-plus/,Warley Ferreira,u@gsad,67996641448,2023-09-14 14:01:20,2023-10-14 11:01:00,1
265,https://tecnicosdecelular.com.br/tabela-plus-teste/,Marcos dos Santos,4@p65@,69993536495,2023-09-14 14:19:07,2023-09-17 11:18:00,1
267,https://tecnicosdecelular.com.br/tabela-plus-teste/,João Ricardo,39j7fs,13997573185,2023-09-14 16:47:32,2023-09-17 13:47:00,1
268,https://tecnicosdecelular.com.br/tabela-plus-teste/,Anderson Junqueira,5fgmdk,22981334349,2023-09-14 17:40:07,2023-09-17 14:39:00,1
269,https://tecnicosdecelular.com.br/tabela-plus/,João Ricardo,cm@omr,13997573185,2023-09-14 17:41:43,2023-10-14 14:41:00,1
270,https://tecnicosdecelular.com.br/tabela-plus-teste/,Victor Delfim,3jjljh,19996317825,2023-09-14 18:09:03,2023-09-17 15:08:00,1
271,https://tecnicosdecelular.com.br/tabela-plus-teste/,Carlos magno,62oyqi,31992440772,2023-09-14 18:22:42,2023-09-17 15:21:00,1
272,https://tecnicosdecelular.com.br/tabela-plus/,Carlos Magno,w4nxmx,31992440772,2023-09-14 18:44:42,2023-10-14 15:43:00,1
273,https://tecnicosdecelular.com.br/tabela-plus-teste/,Iva Marcos,siypsa,16988584255,2023-09-14 18:56:38,2023-09-17 15:56:00,1
274,https://tecnicosdecelular.com.br/tabela-plus-teste/,Érika Silva,bvylzm,33999479138,2023-09-14 18:59:54,2023-09-17 15:59:00,1
280,https://tecnicosdecelular.com.br/tabela-plus-teste/,Fernando Brasileiro,q0jn1w,41996698794,2023-09-14 19:16:29,2023-09-17 16:16:00,1
281,https://tecnicosdecelular.com.br/tabela-plus-teste/,Marcos César,54pm7r,62998796770,2023-09-15 00:19:25,2023-09-17 21:19:00,1
283,https://tecnicosdecelular.com.br/tabela-plus-teste/,Luiz Antônio,e90up4,55997121283,2023-09-15 00:23:20,2023-09-17 21:23:00,1
286,https://tecnicosdecelular.com.br/tabela-plus-teste/,William Alves,5ls@xf,35984287323,2023-09-15 00:27:30,2023-09-17 21:26:00,1
287,https://tecnicosdecelular.com.br/tabela-plus-teste/,Léo Victor,@c8t0h,71988421655,2023-09-15 11:57:14,2023-09-18 08:57:00,1
288,https://tecnicosdecelular.com.br/tabela-plus-teste/,Tallys Emanuel,a0ub5d,85992099998,2023-09-15 13:55:56,2023-09-18 10:55:00,1
290,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gielson Araujo,eqr36p,91992709825,2023-09-15 14:26:00,2023-09-18 11:25:00,1
291,https://tecnicosdecelular.com.br/tabela-plus-teste/,Djanielton,9j1fra,84996619789,2023-09-15 14:32:38,2023-09-18 11:32:00,1
292,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jackeline,cnra25,24988027807,2023-09-15 16:52:43,2023-09-18 13:52:00,1
294,https://tecnicosdecelular.com.br/tabela-plus-teste/,Débora de Freitas,qls@xf,31991569757,2023-09-15 16:57:27,2023-09-18 13:57:00,1
295,https://tecnicosdecelular.com.br/tabela-plus-teste/,William Farias,xvnaeg,92992862320,2023-09-15 17:16:09,2023-09-18 13:57:00,1
296,https://tecnicosdecelular.com.br/tabela-plus-teste/,Richard Paizante,kw5env,31996636426,2023-09-15 17:23:56,2023-09-18 14:23:00,1
297,https://tecnicosdecelular.com.br/tabela-plus-teste/,Leticia de Jesus,ymfspk,62985397473,2023-09-15 17:29:43,2023-09-18 14:29:00,1
298,https://tecnicosdecelular.com.br/tabela-plus-teste/,Marcio Fernandes,58vsfy,19997838361,2023-09-15 17:51:57,2023-09-18 14:51:00,1
299,https://tecnicosdecelular.com.br/tabela-plus/,William Alves,l7g4td,35984287323,2023-09-15 18:03:41,2024-03-15 15:02:00,1
300,https://tecnicosdecelular.com.br/tabela-plus/,William Diogenes Brandão,wf4trm,62981452127,2023-09-15 21:32:26,2024-03-15 18:31:00,1
301,https://tecnicosdecelular.com.br/tabela-plus-teste/,Éverton Evangelista,h10ce0,31971323133,2023-09-16 11:57:59,2023-09-19 08:57:00,1
302,https://tecnicosdecelular.com.br/tabela-plus-teste/,Clayton Pompilio,@5sz@0,91985529101,2023-09-16 12:45:02,2023-09-19 09:44:00,1
304,https://tecnicosdecelular.com.br/tabela-plus-teste/,José Uerlei,ss52#0,27998072753,2023-09-16 12:57:48,2023-09-19 09:57:00,1
305,https://tecnicosdecelular.com.br/tabela-plus-teste/,José Urlei,o3k2qj,27998072753,2023-09-16 12:59:31,2023-09-19 09:59:00,1
306,https://tecnicosdecelular.com.br/tabela-plus-teste/,Bianca Rebeca,ina0ca,31972498938,2023-09-16 13:25:50,2023-09-19 10:25:00,1
307,https://tecnicosdecelular.com.br/tabela-plus-teste/,Edinaldo Araújo,@92b40,31994666363,2023-09-16 13:32:47,2023-09-19 10:32:00,1
310,https://tecnicosdecelular.com.br/tabela-plus-teste/,André Luiz,3h5@mz,19971518171,2023-09-16 13:41:40,2023-09-19 10:41:00,1
312,https://tecnicosdecelular.com.br/tabela-plus-teste/,Luan Santana,hbxwa8,73999297510,2023-09-16 14:07:36,2023-09-19 11:07:00,1
313,https://tecnicosdecelular.com.br/tabela-plus/,Lara Mendes,1w5pvh,38988188320,2023-09-16 14:51:02,2024-03-19 11:50:00,1
316,https://tecnicosdecelular.com.br/tabela-plus-teste/,Adriano,xq4thm,16992117212,2023-09-16 21:31:50,2023-09-19 18:31:00,1
317,https://tecnicosdecelular.com.br/tabela-plus-teste/,Elisiane,w9cfwp,21969117559,2023-09-16 21:50:44,2023-09-19 18:31:00,1
318,https://tecnicosdecelular.com.br/tabela-plus-teste/,Caio Andrade,7uzwun,71983464710,2023-09-16 22:02:30,2023-09-19 19:02:00,1
320,https://tecnicosdecelular.com.br/tabela-plus-teste/,Caroline,h4nj0x,54999665289,2023-09-16 23:35:25,2023-09-19 20:35:00,1
321,https://tecnicosdecelular.com.br/tabela-plus-teste/,Katia da Cruz,p7dhcv,87991775023,2023-09-18 11:52:41,2023-09-21 08:52:00,1
322,https://tecnicosdecelular.com.br/tabela-plus-teste/,Raphael Rocha,possxj,32999363470,2023-09-18 12:03:56,2023-09-21 09:03:00,1
323,https://tecnicosdecelular.com.br/tabela-plus-teste/,Celio Camilo,k1a7@m,31996252525,2023-09-18 12:29:13,2023-09-21 09:29:00,1
325,https://tecnicosdecelular.com.br/tabela-plus-teste/,Sergio Lopes,3nxr9n,31971612463,2023-09-18 13:28:40,2023-09-21 10:28:00,1
326,https://tecnicosdecelular.com.br/tabela-plus-teste/,Sandro ,gmn487,69992496333,2023-09-18 13:40:58,2023-09-21 10:28:00,1
327,https://tecnicosdecelular.com.br/tabela-plus-teste/,Natael Melo,mmfjsi,67998209025,2023-09-18 13:52:29,2023-09-21 10:28:00,1
328,https://tecnicosdecelular.com.br/tabela-plus/,Jeff Castro,s1u92e,21969432225,2023-09-18 14:25:51,2023-10-18 11:25:00,1
329,https://tecnicosdecelular.com.br/tabela-plus/,Marcos José,v284f6,62998796770,2023-09-18 15:05:15,2023-10-18 12:05:00,1
330,https://tecnicosdecelular.com.br/tabela-plus-teste/,Vanderleia,d05jza,41995972500,2023-09-18 16:41:42,2023-09-21 13:41:00,1
331,https://tecnicosdecelular.com.br/tabela-plus-teste/,Dênio Luis,0zi8ob,71999407113,2023-09-18 16:50:14,2023-09-21 13:50:00,1
332,https://tecnicosdecelular.com.br/tabela-plus-teste/,Thamara Carvalho,o@g935,31983430198,2023-09-18 16:52:08,2023-09-21 13:50:00,1
333,https://tecnicosdecelular.com.br/tabela-plus-teste/,Aline Sousa,@xpdqp,75998309207,2023-09-18 17:27:29,2023-09-21 13:50:00,1
335,https://tecnicosdecelular.com.br/tabela-plus/,Thales,c117yx,35991084588,2023-09-18 17:40:25,2023-12-17 14:40:00,1
338,https://tecnicosdecelular.com.br/tabela-plus/,Augusto Leonardo,hh@471,74988190651,2023-09-18 18:02:43,2024-01-13 15:22:00,1
339,https://tecnicosdecelular.com.br/tabela-plus-teste/,Osvaldo Maciel,@m2el8,89999404061,2023-09-18 18:27:32,2023-09-21 15:27:00,1
341,https://tecnicosdecelular.com.br/tabela-plus-teste/,Emerson Antônio,jq727@,87981065165,2023-09-18 19:05:21,2023-09-21 16:05:00,1
342,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gustavo Neves,9xu6vw,77999621631,2023-09-18 19:19:44,2023-09-21 16:19:00,1
343,https://tecnicosdecelular.com.br/tabela-plus-teste/,Kaique Santos,pmb7bk,11962346902,2023-09-19 11:39:30,2023-09-22 08:39:00,1
344,https://tecnicosdecelular.com.br/tabela-plus-teste/,Julian César,5k1una,73988674888,2023-09-19 11:41:58,2023-09-22 08:39:00,1
346,https://tecnicosdecelular.com.br/tabela-plus-teste/,Fábio Fernando,j8qtxy,19998300378,2023-09-19 11:51:36,2023-09-22 08:51:00,1
347,https://tecnicosdecelular.com.br/tabela-plus-teste/,Alessandra Ferreira,zl3q0t,22992640823,2023-09-19 11:54:41,2023-09-22 08:54:00,1
348,https://tecnicosdecelular.com.br/tabela-plus/,Kaique Santos,6u1snx,11962346902,2023-09-19 12:04:06,2023-10-19 09:03:00,1
349,https://tecnicosdecelular.com.br/tabela-plus-teste/,Hudson Henrique,2jjjb9,65999564436,2023-09-19 12:17:02,2023-10-19 09:16:00,1
350,https://tecnicosdecelular.com.br/tabela-plus-teste/,Keuwin,a8ydef,85991197581,2023-09-19 12:25:22,2023-09-22 09:25:00,1
351,https://tecnicosdecelular.com.br/tabela-plus-teste/,Diego Silva,fb6hyx,35999886668,2023-09-19 12:27:17,2023-09-22 09:27:00,1
352,https://tecnicosdecelular.com.br/tabela-plus-teste/,Paraíso dos Elétrônicos,l181yy,11965741354,2023-09-19 12:41:10,2023-09-22 09:41:00,1
353,https://tecnicosdecelular.com.br/tabela-plus/,Ana Cláudia,4db7@k,88992983513,2023-09-19 13:00:51,2023-10-19 09:58:00,1
358,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jordan Silva,9lixmz,53991723500,2023-09-19 13:16:16,2023-09-22 10:16:00,1
359,https://tecnicosdecelular.com.br/tabela-plus-teste/,Eduardo,k4wpir,62985520362,2023-09-19 13:25:48,2023-09-22 10:25:00,1
360,https://tecnicosdecelular.com.br/tabela-plus-teste/,Nivaldo Lima,j1kg@w,17997246730,2023-09-19 13:29:24,2023-09-22 10:25:00,1
362,https://tecnicosdecelular.com.br/tabela-plus-teste/,Alexsandro,m9xb4n,45991169148,2023-09-19 14:05:43,2023-09-22 11:05:00,1
365,https://tecnicosdecelular.com.br/tabela-plus-teste/,Natália,e2w5mx,11989150007,2023-09-19 14:09:24,2023-09-22 11:09:00,1
366,https://tecnicosdecelular.com.br/tabela-plus-teste/,jaciel,rljha4,75982414475,2023-09-19 14:09:53,2023-10-18 22:06:00,1
368,https://tecnicosdecelular.com.br/tabela-plus-teste/,Karen de Castro,@z2g89,24998581173,2023-09-19 14:13:03,2023-09-22 11:13:00,1
369,https://tecnicosdecelular.com.br/tabela-plus-teste/,TESTE111,yr65#r,75982414475,2023-09-19 14:21:48,2023-10-18 22:06:00,1
370,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jaciel testes,8p5xe3,75982414475,2023-09-19 14:23:09,2023-10-18 22:06:00,1
371,https://tecnicosdecelular.com.br/tabela-plus-teste/,Maxwell,4zjzb8,19987595307,2023-09-19 16:31:52,2023-09-22 13:31:00,1
372,https://tecnicosdecelular.com.br/tabela-plus-teste/,Juan Souza,ea6mb1,14996655599,2023-09-19 16:34:23,2023-09-22 13:31:00,1
373,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gabriel Almeida,ydpwfi,11976889274,2023-09-19 16:38:38,2023-09-22 13:38:00,1
374,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jairo,@c3n@2,95991103974,2023-09-19 16:42:55,2023-09-22 13:38:00,1
375,https://tecnicosdecelular.com.br/tabela-plus-teste/,William da Silva,y5x8@4,71991567813,2023-09-19 16:45:03,2023-09-22 13:45:00,1
376,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jeferson Douglas,m1vvn9,21968939688,2023-09-19 16:53:51,2023-09-22 13:53:00,1
377,https://tecnicosdecelular.com.br/tabela-plus/,Jairo Reis,fi0q7w,95991103974,2023-09-19 17:00:24,2023-10-19 13:59:00,1
378,https://tecnicosdecelular.com.br/tabela-plus/,Natália Quarello,vtyhjw,11989150007,2023-09-19 17:24:30,2023-10-19 14:22:00,1
379,https://tecnicosdecelular.com.br/tabela-plus/,Henrique de Souza,523joe,14981219321,2023-09-19 17:29:17,2024-03-19 14:26:00,1
380,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jefferson Luís,ucqg3g,85998249483,2023-09-19 17:37:41,2023-09-22 14:37:00,1
381,https://tecnicosdecelular.com.br/tabela-plus-teste/,José Caio,nfz1ij,73999183579,2023-09-19 17:47:26,2023-09-22 14:47:00,1
382,https://tecnicosdecelular.com.br/tabela-plus/,José Caio,vtxd@k,73999183579,2023-09-19 18:03:43,2023-10-19 15:00:00,1
383,https://tecnicosdecelular.com.br/tabela-plus-teste/,Bruno Silveira,@aumd8,51998301667,2023-09-19 18:25:06,2023-09-22 15:25:00,1
384,https://tecnicosdecelular.com.br/tabela-plus/,Anna Rayssa,t0jw1g,62994525406,2023-09-19 23:07:11,2023-10-19 20:04:00,1
386,https://tecnicosdecelular.com.br/tabela-plus/,Jonatas Silva,4xas97,84991689817,2023-09-19 23:39:43,2023-10-19 20:39:00,1
387,https://tecnicosdecelular.com.br/tabela-plus-teste/,Guilherme Falcão,@qn9v@,65993122002,2023-09-19 23:43:47,2023-09-22 20:43:00,1
388,https://tecnicosdecelular.com.br/tabela-plus-teste/,Alione,51zv20,19996327603,2023-09-19 23:46:00,2023-09-22 20:45:00,1
389,https://tecnicosdecelular.com.br/tabela-plus/,Aloísio Pereira,yvdp26,38988343760,2023-09-20 13:14:38,2023-10-20 10:14:00,1
390,https://tecnicosdecelular.com.br/tabela-plus/,Eloisio Pereira,4ilqy@,38988343760,2023-09-20 13:17:58,2023-10-20 10:15:00,1
391,https://tecnicosdecelular.com.br/tabela-plus-teste/,Fredson,mdsimc,69999120012,2023-09-20 13:30:44,2023-09-23 10:30:00,1
392,https://tecnicosdecelular.com.br/tabela-plus-teste/,Râmilo,4e31i@,61999162103,2023-09-20 13:33:44,2023-09-23 10:33:00,1
393,https://tecnicosdecelular.com.br/tabela-plus/,Paulo Henrique,4n27zw,64992560638,2023-09-20 13:41:34,2024-06-01 19:08:00,1
394,https://tecnicosdecelular.com.br/tabela-plus-teste/,Aloisio Jeovane,jtm4tg,31997950703,2023-09-20 13:43:21,2023-09-23 10:43:00,1
395,https://tecnicosdecelular.com.br/tabela-plus-teste/,Anderson Maya,2@d4ke,75999403094,2023-09-20 13:51:33,2023-09-23 10:43:00,1
396,https://tecnicosdecelular.com.br/tabela-plus/,Aloisio Jeovane,0pbkx2,31997950703,2023-09-20 13:59:13,2024-03-18 10:59:00,1
398,https://tecnicosdecelular.com.br/tabela-plus/,Luiz Philipe,cskl1@,34997117779,2023-09-20 14:10:35,2024-03-18 11:10:00,1
399,https://tecnicosdecelular.com.br/tabela-plus-teste/,Débora Camargo,8mgfs4,11984443692,2023-09-20 14:38:06,2023-09-23 11:38:00,1
400,https://tecnicosdecelular.com.br/tabela-plus/,Aloisio Jeovane,mlhv1a,31997950703,2023-09-20 14:51:50,2024-03-18 11:51:00,1
401,https://tecnicosdecelular.com.br/tabela-plus-teste/,Keverson,i0zb9m,27998586702,2023-09-20 16:35:54,2023-09-23 13:35:00,1
402,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gabriel Cezar,lg6t09,31993409144,2023-09-20 16:37:40,2023-09-23 13:35:00,1
403,https://tecnicosdecelular.com.br/tabela-plus/,Alberto Júnior,tqp8c2,82999162328,2023-09-20 18:36:04,2024-03-18 15:36:00,1
404,https://tecnicosdecelular.com.br/tabela-plus-teste/,Wagner Israel,gxybr0,61983663880,2023-09-20 19:29:36,2023-09-23 16:29:00,1
405,https://tecnicosdecelular.com.br/tabela-plus-teste/,Isadora,drc@7n,43999176688,2023-09-20 22:28:25,2023-09-23 19:28:00,1
406,https://tecnicosdecelular.com.br/tabela-plus-teste/,Emerson de Jesus,my9yaz,75998940294,2023-09-20 22:43:39,2023-09-23 19:42:00,1
407,https://tecnicosdecelular.com.br/tabela-plus-teste/,Wesley Brum,lkw74y,51998275836,2023-09-20 22:53:32,2023-09-23 19:53:00,1
408,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gabriel Abreu,8aarz2,33998434994,2023-09-21 00:18:32,2023-09-23 21:18:00,1
409,https://tecnicosdecelular.com.br/tabela-plus-teste/,Heric,sujbev,44988279206,2023-09-21 00:43:57,2023-09-23 21:43:00,1
410,https://tecnicosdecelular.com.br/tabela-plus-teste/,Josiane Rosa,89vyir,55991815027,2023-09-21 12:06:47,2023-09-24 09:06:00,1
411,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rafael Celulares,lim3lc,62994746200,2023-09-21 12:25:29,2023-09-24 09:25:00,1
412,https://tecnicosdecelular.com.br/tabela-plus/,Enéas Luna,c3k6s4,81989821433,2023-09-21 12:52:39,2023-10-21 09:50:00,1
413,https://tecnicosdecelular.com.br/tabela-plus/,Joice Mello,51k@up,16991205650,2023-09-21 13:00:59,2023-12-26 09:54:00,1
414,https://tecnicosdecelular.com.br/tabela-plus-teste/,Farley,xotui5,31975348639,2023-09-21 13:12:31,2023-09-24 10:12:00,1
415,https://tecnicosdecelular.com.br/tabela-plus-teste/,Nicole,vh9t7g,31995113856,2023-09-21 13:18:21,2023-09-24 10:18:00,1
416,https://tecnicosdecelular.com.br/tabela-plus-teste/,Marcos Mendes,75366r,17996641940,2023-09-21 13:54:21,2023-09-24 10:54:00,1
417,https://tecnicosdecelular.com.br/tabela-plus-teste/,Bruna Glier,70qqkp,51995904785,2023-09-21 14:18:50,2023-09-24 11:18:00,1
418,https://tecnicosdecelular.com.br/tabela-plus/,Marcos Antônio,3ect62,17996641940,2023-09-21 14:34:48,2023-10-21 11:32:00,1
419,https://tecnicosdecelular.com.br/tabela-plus/,Renan Ferreira,vno5m@,38999424654,2023-09-21 16:52:23,2023-10-21 13:51:00,1
420,https://tecnicosdecelular.com.br/tabela-plus-teste/,Hugo Bueno,7j7l6t,62999498603,2023-09-21 17:15:23,2023-09-24 14:15:00,1
421,https://tecnicosdecelular.com.br/tabela-plus-teste/,Washington,66daym,73999422334,2023-09-21 17:21:01,2023-09-24 14:20:00,1
422,https://tecnicosdecelular.com.br/tabela-plus-teste/,Maria Luisa,4l2aw@,86994810316,2023-09-21 17:22:50,2023-09-24 14:22:00,1
423,https://tecnicosdecelular.com.br/tabela-plus-teste/,André,rn@@zt,71993510955,2023-09-21 17:26:30,2023-09-24 14:26:00,1
424,https://tecnicosdecelular.com.br/tabela-plus-teste/,Marcos Vinicius,az9uig,91998135494,2023-09-21 18:52:07,2023-09-24 15:52:00,1
425,https://tecnicosdecelular.com.br/tabela-plus-teste/,Edmar Gláucio,5ia50u,51986048752,2023-09-21 19:07:21,2023-09-24 16:07:00,1
426,https://tecnicosdecelular.com.br/tabela-plus-teste/,Itacell,tjvqti,33999366884,2023-09-21 19:20:50,2023-09-24 16:20:00,1
427,https://tecnicosdecelular.com.br/tabela-plus/,Edemar Gláucio,0j4v4m,51986048752,2023-09-21 19:23:46,2023-11-23 11:23:00,1
428,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jeniffer de Souza Santiago,j@gkk5,88992853972,2023-09-21 23:27:12,2023-09-24 20:26:00,1
429,https://tecnicosdecelular.com.br/tabela-plus-teste/,VK Cell,sswkme,85986155460,2023-09-22 01:03:29,2023-09-24 22:03:00,1
430,https://tecnicosdecelular.com.br/tabela-plus-teste/,Genilson dos Santo,h7r35f,71983575246,2023-09-22 01:05:21,2023-09-24 22:03:00,1
431,https://tecnicosdecelular.com.br/tabela-plus-teste/,Thiago José,wr3pe@,84988995707,2023-09-22 01:07:00,2023-09-24 22:06:00,1
432,https://tecnicosdecelular.com.br/tabela-plus-teste/,Josê Antonio,c6sopk,94992210790,2023-09-22 11:46:00,2023-09-25 08:44:00,1
433,https://tecnicosdecelular.com.br/tabela-plus-teste/,José Firmino,fh46pl,31985971372,2023-09-22 11:52:51,2023-09-25 08:44:00,1
434,https://tecnicosdecelular.com.br/tabela-plus/,Adelcio Carvalho,ys1qol,35991556088,2023-09-22 12:56:57,2023-10-22 09:56:00,1
435,https://tecnicosdecelular.com.br/tabela-plus/,Alexsandro Silva,n6dzrq,81992554607,2023-09-22 13:07:37,2023-10-22 10:06:00,1
436,https://tecnicosdecelular.com.br/tabela-plus/,Tiago Dias,ilg4r4,77981038011,2023-09-22 13:16:55,2023-10-22 10:15:00,1
437,https://tecnicosdecelular.com.br/tabela-plus-teste/,Tiago Martins,fym365,21966825086,2023-09-22 14:16:46,2023-09-25 11:16:00,1
438,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gelbia,pem258,27992737086,2023-09-22 14:32:16,2023-09-25 11:32:00,1
439,https://tecnicosdecelular.com.br/tabela-plus/,Tiago Marins,rfh962,21966825086,2023-09-22 14:42:32,2023-10-22 11:42:00,1
440,https://tecnicosdecelular.com.br/tabela-plus-teste/,Lindemberg,htu685,21971107383,2023-09-22 14:59:41,2023-09-25 11:59:00,1
441,https://tecnicosdecelular.com.br/tabela-plus-teste/,Frank Júnior,mnb769,19992344199,2023-09-22 17:26:49,2023-09-25 14:26:00,1
442,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jeane Oliveira,zxt788,81985293249,2023-09-22 17:31:21,2023-09-25 14:31:00,1
443,https://tecnicosdecelular.com.br/tabela-plus-teste/,Bruna Espindola,9tzfq7,48991303788,2023-09-22 17:45:36,2023-09-25 14:45:00,1
444,https://tecnicosdecelular.com.br/tabela-plus-teste/,Ismael,amk938,84999166698,2023-09-22 18:07:45,2023-09-25 15:07:00,1
445,https://tecnicosdecelular.com.br/tabela-plus-teste/,Mariusleide,hyc896,27999927478,2023-09-22 18:37:29,2023-09-25 15:37:00,1
446,https://tecnicosdecelular.com.br/tabela-plus-teste/,Miguel Dantas,1xfuoj,11911504928,2023-09-22 19:07:23,2023-09-25 16:06:00,1
447,https://tecnicosdecelular.com.br/tabela-plus-teste/,CristianoCardoso ,pld2br,11980705813,2023-09-22 19:13:00,2023-09-25 16:12:00,1
448,https://tecnicosdecelular.com.br/tabela-plus-teste/,Alex Machado,kqj571,51998738048,2023-09-22 22:42:10,2023-09-25 19:42:00,1
449,https://tecnicosdecelular.com.br/tabela-plus-teste/,Àvilla,pkz725,62993202782,2023-09-22 22:57:58,2023-09-25 19:57:00,1
450,https://tecnicosdecelular.com.br/tabela-plus-teste/,Zacaria,suj363,41996255725,2023-09-23 00:14:05,2023-09-25 21:14:00,1
451,https://tecnicosdecelular.com.br/tabela-plus-teste/,Aline,bhq244,91983407105,2023-09-23 01:13:46,2023-09-25 22:13:00,1
452,https://tecnicosdecelular.com.br/tabela-plus/,William Raynert,fvu987,47988845702,2023-09-23 11:52:14,2024-02-19 15:46:00,1
453,https://tecnicosdecelular.com.br/tabela-plus-teste/,Priscila Silva,agm674,91984856389,2023-09-23 13:32:23,2023-09-26 10:32:00,1
454,https://tecnicosdecelular.com.br/tabela-plus-teste/,Francisco Evandro,teu988,88981985094,2023-09-23 13:36:29,2023-09-26 10:36:00,1
455,https://tecnicosdecelular.com.br/tabela-plus-teste/,Caio Kock,k3yz3k,73999346233,2023-09-23 14:39:02,2023-09-26 11:38:00,1
456,https://tecnicosdecelular.com.br/tabela-plus/,Marília Eduarda,ysw233,11944434444,2023-09-23 17:21:39,2024-03-21 14:21:00,1
457,https://tecnicosdecelular.com.br/tabela-plus-teste/,Alysson,wex174,47992492829,2023-09-23 17:24:18,2023-09-26 14:24:00,1
458,https://tecnicosdecelular.com.br/tabela-plus-teste/,Raquel,xvq745,13996684543,2023-09-23 17:40:12,2023-09-26 14:40:00,1
459,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jessica Maiara,wwd625,11988092010,2023-09-23 20:05:07,2023-09-26 17:05:00,1
460,https://tecnicosdecelular.com.br/tabela-plus-teste/,Pâmela,vcs823,18998068044,2023-09-23 20:15:18,2023-09-26 17:15:00,1
461,https://tecnicosdecelular.com.br/tabela-plus/,Luiz Henrique de Jesus,yxe177,73988683251,2023-09-23 20:34:17,2024-03-21 17:34:00,1
462,https://tecnicosdecelular.com.br/tabela-plus-teste/,Ênio Lúcio,nty635,69992620175,2023-09-23 20:42:23,2023-09-26 17:41:00,1
463,https://tecnicosdecelular.com.br/tabela-plus/,Ênio Lúcio da Silva,hgv996,69992620175,2023-09-23 21:37:42,2024-03-21 18:37:00,1
464,https://tecnicosdecelular.com.br/tabela-plus-teste/,Vilson Lima,ppeogi,85991418032,2023-09-25 11:49:34,2023-09-28 08:48:00,1
465,https://tecnicosdecelular.com.br/tabela-plus-teste/,Tiago Alves,26usj2,79999814010,2023-09-25 12:08:40,2023-09-28 09:08:00,1
466,https://tecnicosdecelular.com.br/tabela-plus-teste/,Matheus Kaue,fxb486,11997739928,2023-09-25 13:09:04,2023-09-28 10:09:00,1
468,https://tecnicosdecelular.com.br/tabela-plus-teste/,Camile da Rosa,qdc616,41995972037,2023-09-25 13:48:26,2023-09-28 10:48:00,1
469,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rafael Vieira,kfn261,22992837985,2023-09-25 13:54:04,2023-09-28 10:54:00,1
470,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rafael Luiz,r55ng0,31989705665,2023-09-25 14:40:21,2023-09-28 11:39:00,1
471,https://tecnicosdecelular.com.br/tabela-plus/,Agência Mídia Digital,sfq148,19991344122,2023-09-25 14:46:03,2023-12-24 11:45:00,1
472,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rúbens Júnior,xbt883,62982600707,2023-09-25 16:33:04,2023-09-28 13:33:00,1
473,https://tecnicosdecelular.com.br/tabela-plus-teste/,Lourenço Júnior,jjf683,63991024706,2023-09-25 16:42:10,2023-09-28 13:42:00,1
474,https://tecnicosdecelular.com.br/tabela-plus-teste/,Marcus Vinicius,htp255,21968898208,2023-09-25 16:56:59,2023-09-28 13:56:00,1
475,https://tecnicosdecelular.com.br/tabela-plus-teste/,Leonardo Henrique,uab531,27999116117,2023-09-25 17:46:10,2023-09-28 14:46:00,1
476,https://tecnicosdecelular.com.br/tabela-plus-teste/,Walafe,qpn417,27996646842,2023-09-25 19:23:01,2023-09-28 16:22:00,1
477,https://tecnicosdecelular.com.br/tabela-plus/,,mgu517,51984587943,2023-09-25 21:57:45,2023-10-25 18:56:00,1
478,https://tecnicosdecelular.com.br/tabela-plus/,João Henrique Fraga,zsa256,51984587943,2023-09-25 22:02:25,2023-10-25 19:02:00,1
479,https://tecnicosdecelular.com.br/tabela-plus-teste/,João Victor,kbk899,12997610433,2023-09-25 22:24:25,2023-09-28 19:24:00,1
480,https://tecnicosdecelular.com.br/tabela-plus-teste/,Deivid William,rfp812,51999156102,2023-09-25 23:17:25,2023-09-28 20:17:00,1
481,https://tecnicosdecelular.com.br/tabela-plus-teste/,Alexandre Garcia,cbe539,64999052325,2023-09-25 23:44:43,2023-09-28 20:44:00,1
482,https://tecnicosdecelular.com.br/tabela-plus-teste/,Alessandra,nbs186,81989599001,2023-09-26 00:05:58,2023-09-28 21:05:00,1
483,https://tecnicosdecelular.com.br/tabela-plus-teste/,Paulo Roberto,3i7rds,14999075728,2023-09-26 12:25:33,2023-09-29 09:25:00,1
484,https://tecnicosdecelular.com.br/tabela-plus-teste/,Felipe Moraes,urgy2z,48999945852,2023-09-26 12:38:02,2023-09-29 09:37:00,1
486,https://tecnicosdecelular.com.br/tabela-plus-teste/,Douglas Maciel,2ri6v6,34999231435,2023-09-26 12:43:32,2023-09-29 09:43:00,1
487,https://tecnicosdecelular.com.br/tabela-plus/,Douglas Maciel Garcia,sbe338,34999231435,2023-09-26 13:15:27,2023-10-26 10:15:00,1
488,https://tecnicosdecelular.com.br/tabela-plus/,Hudson Henrique,hkh82u,65999564436,2023-09-26 14:26:55,2024-03-26 11:26:00,1
489,https://tecnicosdecelular.com.br/tabela-plus-teste/,Victor Eduardo,vidrj6,69992508590,2023-09-26 14:33:23,2023-09-29 11:33:00,1
490,https://tecnicosdecelular.com.br/tabela-plus-teste/,Fernanda Gonçalves,aq1km0,12996288509,2023-09-26 14:43:23,2023-09-29 11:43:00,1
491,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gedielson,tqs339,41995499264,2023-09-26 16:27:11,2023-09-29 13:27:00,1
492,https://tecnicosdecelular.com.br/tabela-plus/,Alex Rodrigues da Silva,ngm8f2,64993201961,2023-09-26 16:55:45,2024-03-06 13:55:00,1
493,https://tecnicosdecelular.com.br/tabela-plus/,Sandro Rodrigues,fparx3,62992228881,2023-09-26 17:02:28,2024-01-06 15:12:00,1
494,https://tecnicosdecelular.com.br/tabela-plus-teste/,Israel Moreira,a4vn3q,27997666025,2023-09-26 18:20:21,2023-09-29 15:20:00,1
495,https://tecnicosdecelular.com.br/tabela-plus-teste/,Telry Laila,ns9518,41998226847,2023-09-26 18:23:47,2023-09-29 15:23:00,1
496,https://tecnicosdecelular.com.br/tabela-plus/,Raul Lima,yar113,82996633349,2023-09-26 19:07:01,2024-03-02 09:21:00,1
497,https://tecnicosdecelular.com.br/tabela-plus-teste/,Fernando dos Santos,zer664,71985080460,2023-09-26 22:50:53,2023-09-29 19:50:00,1
498,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rafael Lopes,uyt522,62991583952,2023-09-26 23:25:25,2023-09-29 20:25:00,1
499,https://tecnicosdecelular.com.br/tabela-plus-teste/,Welington Castelo,xgt968,11937216751,2023-09-26 23:35:51,2023-09-29 20:35:00,1
500,https://tecnicosdecelular.com.br/tabela-plus-teste/,Vitor Soares,hpm0lv,37998743040,2023-09-27 11:46:18,2023-09-30 08:46:00,1
501,https://tecnicosdecelular.com.br/tabela-plus-teste/,José Ferreira,huxp56,89981439351,2023-09-27 11:54:04,2023-09-30 08:53:00,1
502,https://tecnicosdecelular.com.br/tabela-plus-teste/,Luiz Ricardo,vjx7ih,13978125613,2023-09-27 11:57:20,2023-09-30 08:57:00,1
504,https://tecnicosdecelular.com.br/tabela-plus-teste/,Kelvin Otaviano,5m82nt,88982168790,2023-09-27 12:02:18,2023-09-30 09:02:00,1
505,https://tecnicosdecelular.com.br/tabela-plus-teste/,Roberto Silva,9td7qf,21976813851,2023-09-27 12:10:25,2023-09-30 09:10:00,1
506,https://tecnicosdecelular.com.br/tabela-plus-teste/,Daniel Quadros,9yxnu6,51982070286,2023-09-27 12:28:37,2023-09-30 09:28:00,1
507,https://tecnicosdecelular.com.br/tabela-plus-teste/,Waysen Rauer,6n0v65,84981011517,2023-09-27 12:59:41,2023-09-30 09:59:00,1
508,https://tecnicosdecelular.com.br/tabela-plus-teste/,Flavio Morais ,m7klz7,11994446129,2023-09-27 13:06:23,2023-09-30 10:06:00,1
509,https://tecnicosdecelular.com.br/tabela-plus-teste/,Márcio Santos,nxg539,71982040733,2023-09-27 13:24:06,2023-09-30 10:24:00,1
510,https://tecnicosdecelular.com.br/tabela-plus-teste/,Fabiano Sabino,rfw889,19992130352,2023-09-27 13:25:54,2023-09-30 10:24:00,1
511,https://tecnicosdecelular.com.br/tabela-plus/,Victor Eduardo,jqf359,69992508590,2023-09-27 13:40:50,2023-10-27 10:40:00,1
512,https://tecnicosdecelular.com.br/tabela-plus-teste/,Wellington Amaral,etm898,85997846135,2023-09-27 14:08:21,2023-09-30 11:08:00,1
513,https://tecnicosdecelular.com.br/tabela-plus/,Jeferson da Paixão,cex833,75999855481,2023-09-27 14:13:23,2024-03-27 11:13:00,1
514,https://tecnicosdecelular.com.br/tabela-plus-teste/,Flávia Danila,zfv372,71991676578,2023-09-27 14:22:26,2023-09-30 11:22:00,1
515,https://tecnicosdecelular.com.br/tabela-plus-teste/,Victor Amorim,rgc141,21994194114,2023-09-27 16:24:21,2023-09-30 13:24:00,1
516,https://tecnicosdecelular.com.br/tabela-plus-teste/,Miguel Alexandre,nxp167,21991164025,2023-09-27 16:33:18,2023-09-30 13:33:00,1
517,https://tecnicosdecelular.com.br/tabela-plus-teste/,Igor Gabriel,jnb583,77999311364,2023-09-27 16:36:49,2023-09-30 13:36:00,1
518,https://tecnicosdecelular.com.br/tabela-plus/,José Ferreira,zrz134,89981439351,2023-09-27 16:48:26,2024-03-27 13:48:00,1
519,https://tecnicosdecelular.com.br/tabela-plus-teste/,Ingrid de Melo,1huvhc,21965552260,2023-09-27 17:52:14,2023-09-30 14:52:00,1
520,https://tecnicosdecelular.com.br/tabela-plus-teste/,Adilton Carvalho,ckd4y6,91991375748,2023-09-27 18:07:19,2023-09-30 15:07:00,1
521,https://tecnicosdecelular.com.br/tabela-plus-teste/,Diego da Silva,hzz488,11982732331,2023-09-27 18:19:05,2023-09-30 15:19:00,1
522,https://tecnicosdecelular.com.br/tabela-plus-teste/,Bruna Brito,pmho4z,98988779933,2023-09-27 18:36:04,2023-09-30 15:35:00,1
523,https://tecnicosdecelular.com.br/tabela-plus/,Matheus Kaue,xaq887,11997739928,2023-09-27 19:27:48,2023-10-27 16:27:00,1
524,https://tecnicosdecelular.com.br/tabela-plus/,Vitor Soares,wtk987,37998743040,2023-09-28 01:23:08,2023-10-27 22:22:00,1
525,https://tecnicosdecelular.com.br/tabela-plus-teste/,Larissa Veloso,yhk382,64999513268,2023-09-28 01:24:56,2023-09-30 22:24:00,1
526,https://tecnicosdecelular.com.br/tabela-plus-teste/,João Victor,dua393,17988199129,2023-09-28 11:56:07,2023-10-01 08:56:00,1
527,https://tecnicosdecelular.com.br/tabela-plus-teste/,Cristian Alexander,qfx258,67996262090,2023-09-28 11:57:34,2023-10-01 08:56:00,1
528,https://tecnicosdecelular.com.br/tabela-plus-teste/,José Claudevane,sqq459,63999421240,2023-09-28 12:00:02,2023-10-01 08:59:00,1
529,https://tecnicosdecelular.com.br/tabela-plus-teste/,Taiane,arw669,65999372101,2023-09-28 12:21:39,2023-10-01 09:21:00,1
530,https://tecnicosdecelular.com.br/tabela-plus/,Israel Moreira,cxw757,27997666025,2023-09-28 12:24:04,2023-10-28 09:23:00,1
531,https://tecnicosdecelular.com.br/tabela-plus/,José Santiago,bqh459,83991506001,2023-09-28 12:36:16,2024-06-16 10:49:00,1
532,https://tecnicosdecelular.com.br/tabela-plus-teste/,Letícia Ramos,zkm162,19999178738,2023-09-28 12:45:00,2023-10-01 09:44:00,1
533,https://tecnicosdecelular.com.br/tabela-plus-teste/,Julia Andrade,xhu637,21967782452,2023-09-28 12:47:11,2023-10-01 09:47:00,1
534,https://tecnicosdecelular.com.br/tabela-plus-teste/,William Velozo,mwt244,51994494775,2023-09-28 12:58:13,2023-10-01 09:58:00,1
535,https://tecnicosdecelular.com.br/tabela-plus-teste/,Eliaquim,wyh792,64992084730,2023-09-28 13:12:16,2023-10-01 10:12:00,1
536,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gervásio Dias,ufc881,75991451313,2023-09-28 14:28:17,2023-10-01 11:28:00,1
537,https://tecnicosdecelular.com.br/tabela-plus-teste/,Vinícius Paiva,ckw996,48988616681,2023-09-28 14:48:33,2023-10-01 11:48:00,1
538,https://tecnicosdecelular.com.br/tabela-plus-teste/,Robert Augusto,rnq665,65996972171,2023-09-28 17:41:29,2023-10-01 14:41:00,1
539,https://tecnicosdecelular.com.br/tabela-plus-teste/,Daiana Silva,epg698,21977343859,2023-09-28 18:00:15,2023-10-01 15:00:00,1
540,https://tecnicosdecelular.com.br/tabela-plus-teste/,Luiz Eduardo,fbu559,91992826317,2023-09-28 18:03:41,2023-10-01 15:00:00,1
541,https://tecnicosdecelular.com.br/tabela-plus-teste/,Francis,sym136,31984217646,2023-09-28 18:24:32,2023-10-01 15:24:00,1
542,https://tecnicosdecelular.com.br/tabela-plus-teste/,Hudson,vpx112,21980471470,2023-09-28 19:26:45,2023-10-01 16:26:00,1
543,https://tecnicosdecelular.com.br/tabela-plus-teste/,Clayton dos Santos,mwz949,11996961313,2023-09-28 22:43:26,2023-10-01 19:43:00,1
545,https://tecnicosdecelular.com.br/tabela-plus-teste/,Maicon Moraes,sed798,54981399436,2023-09-28 22:52:49,2023-10-01 19:52:00,1
546,https://tecnicosdecelular.com.br/tabela-plus-teste/,teste,evn200,75982414475,2023-09-29 12:52:15,2023-10-28 20:00:00,1
547,https://tecnicosdecelular.com.br/tabela-plus-teste/,Eleandra,gzv546,16988181719,2023-09-29 12:59:01,2023-10-02 09:58:00,1
548,https://tecnicosdecelular.com.br/tabela-plus-teste/,José Lucas,xsw344,35984782070,2023-09-29 13:01:49,2023-10-02 10:01:00,1
549,https://tecnicosdecelular.com.br/tabela-plus-teste/,Luiz Fernando,qnb255,33984221111,2023-09-29 13:04:12,2023-10-02 10:04:00,1
550,https://tecnicosdecelular.com.br/tabela-plus-teste/,Fabrícia Kelly,zmz626,83996944442,2023-09-29 13:06:36,2023-10-02 10:06:00,1
551,https://tecnicosdecelular.com.br/tabela-plus-teste/,Alice Piccole,wpn137,14991045307,2023-09-29 13:09:45,2023-10-02 10:09:00,1
552,https://tecnicosdecelular.com.br/tabela-plus-teste/,Ederson Luiz,hxw994,54981298190,2023-09-29 14:00:08,2023-10-02 11:00:00,1
553,https://tecnicosdecelular.com.br/tabela-plus-teste/,Ruama,aab262,21992707997,2023-09-29 14:10:29,2023-10-02 11:10:00,1
554,https://tecnicosdecelular.com.br/tabela-plus-teste/,Caíque Borges,ffd373,64996096117,2023-09-29 14:17:58,2023-10-02 11:17:00,1
555,https://tecnicosdecelular.com.br/tabela-plus-teste/,Valter Santos,jwv548,71991392826,2023-09-29 14:20:24,2023-10-02 11:20:00,1
556,https://tecnicosdecelular.com.br/tabela-plus-teste/,Celson Almeida,duf644,32988942686,2023-09-29 14:46:26,2023-10-02 11:45:00,1
557,https://tecnicosdecelular.com.br/tabela-plus/,Ederson Luiz,bfu297,54981298190,2023-09-29 16:23:45,2023-10-29 13:23:00,1
558,https://tecnicosdecelular.com.br/tabela-plus-teste/,Wagner Cardoso,gcw151,98984575553,2023-09-29 17:23:28,2023-10-02 14:23:00,1
559,https://tecnicosdecelular.com.br/tabela-plus/,Robert Augusto,etn491,65996972171,2023-09-29 17:31:45,2023-10-29 14:30:00,1
560,https://tecnicosdecelular.com.br/tabela-plus-teste/,Bruno Barth,yqe483,55981191497,2023-09-29 17:42:25,2023-10-02 14:42:00,1
561,https://tecnicosdecelular.com.br/tabela-plus-teste/,Thiarles,fmc733,66984539289,2023-09-29 17:46:04,2023-10-02 14:45:00,1
562,https://tecnicosdecelular.com.br/tabela-plus-teste/,Claudiney,yay342,11941384979,2023-09-29 17:53:18,2023-10-02 14:53:00,1
563,https://tecnicosdecelular.com.br/tabela-plus-teste/,Tarlandio,bvg681,21972468666,2023-09-29 18:05:37,2023-10-29 15:04:00,1
564,https://tecnicosdecelular.com.br/tabela-plus-teste/,Leonardo Moraes,bzd323,47997588571,2023-09-29 18:44:32,2023-10-02 15:44:00,1
565,https://tecnicosdecelular.com.br/tabela-plus/,Tainara Nunes,fnr869,17996561336,2023-09-29 20:07:04,2023-09-30 17:00:00,1
566,https://tecnicosdecelular.com.br/tabela-plus/,Gabriel José,xsj659,19997646940,2023-09-30 00:20:53,2023-11-02 21:16:00,1
567,https://tecnicosdecelular.com.br/tabela-plus/,Cristian Alexsander,bet659,67996262090,2023-09-30 00:25:29,2024-03-29 21:25:00,1
568,https://tecnicosdecelular.com.br/tabela-plus-teste/,Denisson,qyv617,79988123869,2023-09-30 00:33:27,2023-10-02 21:33:00,1
569,https://tecnicosdecelular.com.br/tabela-plus-teste/,Kaun Souza,vnc196,92986008412,2023-09-30 00:52:35,2023-10-02 21:52:00,1
570,https://tecnicosdecelular.com.br/tabela-plus-teste/,Érica Ferreira Pinho,cxc327,64992006663,2023-09-30 02:00:46,2023-10-02 23:00:00,1
571,https://tecnicosdecelular.com.br/tabela-plus-teste/,Marcelo Damasceno,vug449,37998402030,2023-09-30 13:12:20,2023-10-03 10:12:00,1
572,https://tecnicosdecelular.com.br/tabela-plus-teste/,Everton Carlos,xek227,54996300189,2023-09-30 13:14:45,2023-10-03 10:14:00,1
573,https://tecnicosdecelular.com.br/tabela-plus-teste/,Flávio Augusto,dqp769,62982581070,2023-09-30 13:23:29,2023-10-03 10:23:00,1
574,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gabriel Henrique,kue682,19998487949,2023-09-30 13:32:59,2023-10-03 10:32:00,1
575,https://tecnicosdecelular.com.br/tabela-plus-teste/,Carlos Alexandre,gfy417,48999684037,2023-09-30 14:02:31,2023-10-03 11:02:00,1
576,https://tecnicosdecelular.com.br/tabela-plus-teste/,Luiz Sirqueira,vpa127,21978749531,2023-09-30 22:00:58,2023-10-03 19:00:00,1
577,https://tecnicosdecelular.com.br/tabela-plus-teste/,Letícia Ferreira,jdk655,11949087999,2023-09-30 22:03:19,2023-10-03 19:03:00,1
578,https://tecnicosdecelular.com.br/tabela-plus-teste/,Paulo Victor,nyf511,64993327200,2023-09-30 22:05:00,2023-10-03 19:04:00,1
579,https://tecnicosdecelular.com.br/tabela-plus-teste/,Juniarley,stz752,38998069971,2023-09-30 22:39:09,2023-10-03 19:38:00,1
580,https://tecnicosdecelular.com.br/tabela-plus-teste/,Natanael Gomes,aqq542,85996160667,2023-10-02 11:47:11,2023-10-05 08:46:00,1
581,https://tecnicosdecelular.com.br/tabela-plus-teste/,Ramon Rodrigues,ebw345,11969689115,2023-10-02 11:50:03,2023-10-05 08:46:00,1
582,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jhonatan de Sousa,cmt624,63992999899,2023-10-02 11:53:57,2023-10-05 08:46:00,1
586,https://tecnicosdecelular.com.br/tabela-plus/,Jessilane Santos,zug737,89988163873,2023-10-02 12:12:25,2023-11-02 09:11:00,1
587,https://tecnicosdecelular.com.br/tabela-plus/,Fabiane Franklin,unc663,44991264999,2023-10-02 14:23:33,2023-11-02 11:23:00,1
588,https://tecnicosdecelular.com.br/tabela-plus-teste/,Vitor Gabriel,jjk655,62994981677,2023-10-02 14:47:37,2023-10-05 11:46:00,1
590,https://tecnicosdecelular.com.br/tabela-plus-teste/,Carlos André,vch486,64992461418,2023-10-02 14:53:21,2023-10-05 11:53:00,1
591,https://tecnicosdecelular.com.br/tabela-plus-teste/,Giovanna,ych976,11988586232,2023-10-02 14:54:56,2023-10-05 11:54:00,1
592,https://tecnicosdecelular.com.br/tabela-plus-teste/,Lucas Alge,dnu914,41998143606,2023-10-02 14:55:24,2023-10-05 11:53:00,1
593,https://tecnicosdecelular.com.br/tabela-plus-teste/,Reydson Souza,dmq366,91982787235,2023-10-02 14:57:07,2023-10-05 11:53:00,1
594,https://tecnicosdecelular.com.br/tabela-plus-teste/,Caique Lopes,mea813,77999859685,2023-10-02 14:58:53,2023-10-05 11:53:00,1
596,https://tecnicosdecelular.com.br/tabela-plus-teste/,Paulo Flavio,gda647,61998087150,2023-10-02 15:01:16,2023-10-05 12:01:00,1
597,https://tecnicosdecelular.com.br/tabela-plus-teste/,Guilherme Abão,etg899,43933678263,2023-10-02 15:05:54,2023-10-05 12:05:00,1
598,https://tecnicosdecelular.com.br/tabela-plus-teste/,Joana Soares,qmw724,32998545628,2023-10-02 16:24:15,2023-10-05 13:23:00,1
599,https://tecnicosdecelular.com.br/tabela-plus/,Caique Rodrigues,dcd368,77999859685,2023-10-02 16:47:03,2023-11-02 13:46:00,1
600,https://tecnicosdecelular.com.br/tabela-plus/,Ekles Ludierry,yhx528,43996438348,2023-10-02 17:36:12,2023-11-02 14:36:00,1
601,https://tecnicosdecelular.com.br/tabela-plus-teste/,Aparecido Santos,fjc863,82981682722,2023-10-02 17:41:52,2023-10-05 14:41:00,1
602,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rodrigo Reis,ban316,21965406002,2023-10-02 17:43:56,2023-10-05 14:43:00,1
603,https://tecnicosdecelular.com.br/tabela-plus-teste/,Dário Dias,hdz289,61991655015,2023-10-02 17:46:18,2023-10-05 14:46:00,1
604,https://tecnicosdecelular.com.br/tabela-plus-teste/,Willys,meh955,86988485774,2023-10-02 17:48:19,2023-10-05 14:48:00,1
605,https://tecnicosdecelular.com.br/tabela-plus-teste/,Cláudio José,ndd828,11981692028,2023-10-02 18:05:26,2023-10-05 15:05:00,1
606,https://tecnicosdecelular.com.br/tabela-plus-teste/,João Luiz ,eze418,35992372997,2023-10-02 19:08:44,2023-10-05 16:08:00,1
607,https://tecnicosdecelular.com.br/tabela-plus-teste/,Mabelle,cqb523,32991957458,2023-10-02 19:27:38,2023-10-05 16:27:00,1
608,https://tecnicosdecelular.com.br/tabela-plus-teste/,Paulo Trindade,qks142,19921333289,2023-10-02 23:57:06,2023-10-05 20:57:00,1
609,https://tecnicosdecelular.com.br/tabela-plus-teste/,Lorena Rodrigues,suf982,64992736739,2023-10-03 00:15:53,2023-10-05 21:15:00,1
610,https://tecnicosdecelular.com.br/tabela-plus-teste/,Sandriele,rtb374,65996192796,2023-10-03 00:17:29,2023-10-05 21:17:00,1
611,https://tecnicosdecelular.com.br/tabela-plus-teste/,Wesley da Silva,nsv295,75982856744,2023-10-03 00:18:56,2023-10-05 21:18:00,1
612,https://tecnicosdecelular.com.br/tabela-plus-teste/,Igor Diniz,nrn763,45998243589,2023-10-03 00:21:11,2023-10-05 21:21:00,1
613,https://tecnicosdecelular.com.br/tabela-plus/,Eleandra Daniela,deq943,16988181719,2023-10-03 00:26:42,2023-11-02 21:25:00,1
614,https://tecnicosdecelular.com.br/tabela-plus-teste/,Augusto José,hyv435,24981439722,2023-10-03 00:33:11,2023-10-05 21:33:00,1
615,https://tecnicosdecelular.com.br/tabela-plus-teste/,Matheus Luiz,ymw374,21971495189,2023-10-03 00:34:49,2023-10-05 21:34:00,1
616,https://tecnicosdecelular.com.br/tabela-plus/,Matheus Luiz,psv397,21971495189,2023-10-03 00:50:13,2023-11-01 21:50:00,1
617,https://tecnicosdecelular.com.br/tabela-plus/,Taiane Pereira,jnn233,65999372101,2023-10-03 11:28:44,2023-11-02 08:28:00,1
618,https://tecnicosdecelular.com.br/tabela-plus-teste/,Ângelo,sez311,71996951757,2023-10-03 12:32:43,2023-10-06 09:32:00,1
619,https://tecnicosdecelular.com.br/tabela-plus-teste/,Isabella Bonatti,fps321,11932724033,2023-10-03 12:38:16,2023-10-06 09:38:00,1
620,https://tecnicosdecelular.com.br/tabela-plus-teste/,Caroline Maia,zpp529,51991692121,2023-10-03 13:03:07,2023-10-06 10:02:00,1
621,https://tecnicosdecelular.com.br/tabela-plus-teste/,Weverson ,nyb957,98991948468,2023-10-03 13:05:37,2023-10-06 10:05:00,1
622,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rayser,tqk963,24981093457,2023-10-03 13:24:57,2023-10-06 10:24:00,1
623,https://tecnicosdecelular.com.br/tabela-plus-teste/,Geovane Pereira,bhe227,34998233476,2023-10-03 13:32:13,2023-10-06 10:32:00,1
624,https://tecnicosdecelular.com.br/tabela-plus-teste/,Felipe Silva,nan486,11939486695,2023-10-03 13:35:47,2023-10-06 10:35:00,1
625,https://tecnicosdecelular.com.br/tabela-plus/,Isabelle Bonatti,vct187,11932724033,2023-10-03 13:37:01,2023-11-03 10:36:00,1
626,https://tecnicosdecelular.com.br/tabela-plus-teste/,Douglas Felipe,uxz674,42999116028,2023-10-03 14:04:09,2023-10-06 11:03:00,1
627,https://tecnicosdecelular.com.br/tabela-plus/,Geovane Pereira,ufq269,34998233476,2023-10-03 14:21:29,2024-04-03 11:21:00,1
628,https://tecnicosdecelular.com.br/tabela-plus/,Paulo Roberto,vkt838,21970303646,2023-10-03 14:31:07,2023-11-03 11:29:00,1
629,https://tecnicosdecelular.com.br/tabela-plus/,Lorena Rodrigues,fgx135,64992736739,2023-10-03 14:36:01,2023-11-03 11:35:00,1
630,https://tecnicosdecelular.com.br/tabela-plus/,Victor Erik,bjg944,37998284569,2023-10-03 14:41:10,2023-11-03 11:40:00,1
631,https://tecnicosdecelular.com.br/tabela-plus-teste/,Nielton Mendes,qfx742,74999777589,2023-10-03 14:52:37,2023-10-06 11:52:00,1
632,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jackeline Rodrigues,tkd159,65999082012,2023-10-03 14:52:55,2023-10-06 11:52:00,1
633,https://tecnicosdecelular.com.br/tabela-plus/,Douglas Felipe,fur762,42999116028,2023-10-03 16:15:32,2024-04-03 13:15:00,1
634,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jonata Oliveira,qkb483,61995542791,2023-10-03 16:24:56,2023-10-06 13:24:00,1
635,https://tecnicosdecelular.com.br/tabela-plus-teste/,José Edvanildo,gfg366,35998407882,2023-10-03 16:28:27,2023-10-06 13:28:00,1
636,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gustavo,ufb493,16992896174,2023-10-03 16:34:06,2023-10-06 13:33:00,1
638,https://tecnicosdecelular.com.br/tabela-plus-teste/,Keila,fpx595,61981578163,2023-10-03 16:49:56,2023-10-06 13:49:00,1
639,https://tecnicosdecelular.com.br/tabela-plus-teste/,João Correia,mjj117,79991591179,2023-10-03 16:51:45,2023-10-06 13:51:00,1
640,https://tecnicosdecelular.com.br/tabela-plus-teste/,Caio Tadeu,yhz396,19992575789,2023-10-03 16:53:53,2023-10-06 13:53:00,1
641,https://tecnicosdecelular.com.br/tabela-plus-teste/,Fernando Santiago,tfr161,47997334999,2023-10-03 18:26:47,2023-10-06 15:26:00,1
642,https://tecnicosdecelular.com.br/tabela-plus-teste/,Patrick,xag198,69981558063,2023-10-03 19:02:36,2023-10-06 16:02:00,1
643,https://tecnicosdecelular.com.br/tabela-plus-teste/,Raphaela,csp716,69992268655,2023-10-03 19:19:46,2023-10-06 16:19:00,1
644,https://tecnicosdecelular.com.br/tabela-plus-teste/,João Henrique,wax698,15996633120,2023-10-03 22:35:22,2023-10-06 19:35:00,1
645,https://tecnicosdecelular.com.br/tabela-plus-teste/,João Márcio,mjw422,88999211158,2023-10-03 22:46:53,2023-10-06 19:46:00,1
646,https://tecnicosdecelular.com.br/tabela-plus-teste/,Elton José,fkj599,74988626471,2023-10-03 22:52:05,2023-10-06 19:51:00,1
647,https://tecnicosdecelular.com.br/tabela-plus-teste/,Edielson,ncf292,62993478349,2023-10-03 23:02:17,2023-10-06 20:02:00,1
649,https://tecnicosdecelular.com.br/tabela-plus-teste/,Fernando da Silva,svb525,84981714522,2023-10-03 23:11:20,2023-10-06 20:11:00,1
650,https://tecnicosdecelular.com.br/tabela-plus-teste/,Wagner Braga,rsf193,21965282600,2023-10-03 23:24:36,2023-10-06 20:24:00,1
651,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rafael Ricarte,yfc846,85994370926,2023-10-03 23:27:47,2023-10-06 20:27:00,1
652,https://tecnicosdecelular.com.br/tabela-plus-teste/,Bruno Alessandro,fvz422,19987464600,2023-10-03 23:33:34,2023-10-06 20:33:00,1
653,https://tecnicosdecelular.com.br/tabela-plus-teste/,Alex Rodrigues,rwx872,11996670051,2023-10-03 23:44:26,2023-10-06 20:44:00,1
655,https://tecnicosdecelular.com.br/tabela-plus-teste/,Amilca Souza,gbd235,11974546980,2023-10-04 00:51:59,2024-04-03 21:51:00,1
656,https://tecnicosdecelular.com.br/tabela-plus/,Amilca Souza,bbp496,11974546980,2023-10-04 00:55:12,2024-04-03 21:54:00,1
657,https://tecnicosdecelular.com.br/tabela-plus/,Thalyson Santos,mzn249,79996799040,2023-10-04 01:21:07,2023-11-03 22:20:00,1
660,https://tecnicosdecelular.com.br/tabela-plus-teste/,Osvaldo Pinto,rpf145,35932125631,2023-10-04 12:26:30,2023-10-07 09:26:00,1
661,https://tecnicosdecelular.com.br/tabela-plus-teste/,Marcus Vinicius,zhv846,71981994121,2023-10-04 13:33:21,2023-10-07 10:33:00,1
662,https://tecnicosdecelular.com.br/tabela-plus-teste/,Yasmi Neirian,wep813,71999081978,2023-10-04 13:47:18,2023-10-07 10:47:00,1
663,https://tecnicosdecelular.com.br/tabela-plus-teste/,Felipe Souza,abs773,75998640017,2023-10-04 14:09:57,2023-10-07 11:09:00,1
664,https://tecnicosdecelular.com.br/tabela-plus-teste/,Wallace,qsr399,22999916026,2023-10-04 14:35:13,2023-10-07 11:35:00,1
665,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rafael Pereira,qee923,93991921966,2023-10-04 14:44:44,2023-10-07 11:44:00,1
666,https://tecnicosdecelular.com.br/tabela-plus-teste/,Edno,vmh561,84991539621,2023-10-04 14:48:08,2023-10-07 11:47:00,1
667,https://tecnicosdecelular.com.br/tabela-plus-teste/,Daniela da Silva,sth959,32998811257,2023-10-04 14:51:49,2023-10-07 11:51:00,1
668,https://tecnicosdecelular.com.br/tabela-plus/,Osvaldo Pint,scj411,35932125631,2023-10-04 15:09:03,2023-11-03 12:08:00,1
669,https://tecnicosdecelular.com.br/tabela-plus/,Osvaldo Pinto Correia,ybm552,35932125631,2023-10-04 16:02:25,2023-11-03 13:02:00,1
670,https://tecnicosdecelular.com.br/tabela-plus-teste/,Wesley Silva,mcr993,73981507394,2023-10-04 17:41:23,2023-10-07 14:40:00,1
671,https://tecnicosdecelular.com.br/tabela-plus-teste/,Luiz Fernando,qsq842,66999434377,2023-10-04 17:43:32,2023-10-07 14:43:00,1
672,https://tecnicosdecelular.com.br/tabela-plus-teste/,Fábio Santos,wqw988,11990274287,2023-10-04 17:46:12,2023-10-07 14:46:00,1
673,https://tecnicosdecelular.com.br/tabela-plus-teste/,Paula Soulto,pfj759,41995690460,2023-10-04 17:59:31,2023-10-07 14:59:00,1
674,https://tecnicosdecelular.com.br/tabela-plus-teste/,Kaio Ramos,mey298,22997123099,2023-10-04 18:01:15,2023-10-07 15:00:00,1
675,https://tecnicosdecelular.com.br/tabela-plus-teste/,Pamela Souto,krr754,41998308202,2023-10-04 18:04:29,2023-10-07 15:04:00,1
676,https://tecnicosdecelular.com.br/tabela-plus-teste/,Juliano Ferrari,cmt323,48999108500,2023-10-04 18:26:54,2023-10-07 15:26:00,1
677,https://tecnicosdecelular.com.br/tabela-plus/,Pamela Souto,mna956,41998308202,2023-10-04 18:47:06,2024-04-04 15:46:00,1
678,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gabriel Carvalho,bgb696,21974767768,2023-10-04 23:37:37,2023-10-07 20:37:00,1
679,https://tecnicosdecelular.com.br/tabela-plus-teste/,Leonardo Marttiolli,hcf723,11947982422,2023-10-04 23:39:57,2023-10-07 20:39:00,1
680,https://tecnicosdecelular.com.br/tabela-plus-teste/,Luan Rafael,dsn191,42999440322,2023-10-05 11:35:44,2023-10-08 08:35:00,1
681,https://tecnicosdecelular.com.br/tabela-plus-teste/,Maria Carolina,krf192,98985093757,2023-10-05 11:55:53,2023-10-08 08:55:00,1
682,https://tecnicosdecelular.com.br/tabela-plus-teste/,Wanderson Santos,bsj784,85999318499,2023-10-05 13:06:13,2023-10-08 10:05:00,1
683,https://tecnicosdecelular.com.br/tabela-plus-teste/,Welligton Ximenes,azx979,67998285118,2023-10-05 13:39:25,2023-10-08 10:39:00,1
685,https://tecnicosdecelular.com.br/tabela-plus/,Eliaquim Santos,shz588,64992084730,2023-10-05 14:12:50,2023-11-05 11:12:00,1
686,https://tecnicosdecelular.com.br/tabela-plus-teste/,Lúcia Inácia,kyz479,31993223149,2023-10-05 14:37:39,2023-10-08 11:37:00,1
687,https://tecnicosdecelular.com.br/tabela-plus-teste/,Miguel Pereira,hud494,11974259319,2023-10-05 16:51:56,2023-10-08 13:51:00,1
688,https://tecnicosdecelular.com.br/tabela-plus-teste/,José Ribamar,qec274,99844614469,2023-10-05 16:57:22,2023-10-08 13:57:00,1
689,https://tecnicosdecelular.com.br/tabela-plus-teste/,Easysjronline,zyt547,98992688487,2023-10-05 17:10:03,2023-10-08 14:09:00,1
690,https://tecnicosdecelular.com.br/tabela-plus-teste/,Mariane Cardoso,uyj743,43991376860,2023-10-05 17:18:25,2023-10-08 14:18:00,1
691,https://tecnicosdecelular.com.br/tabela-plus-teste/,Thiago Alves,zwg261,17992289369,2023-10-05 18:07:32,2023-10-08 15:07:00,1
692,https://tecnicosdecelular.com.br/tabela-plus-teste/,Weslley Batista,tcm324,85998363020,2023-10-05 18:12:32,2023-10-08 15:12:00,1
693,https://tecnicosdecelular.com.br/tabela-plus-teste/,André da Rocha,gtk274,45999376437,2023-10-05 18:34:35,2023-10-08 15:34:00,1
694,https://tecnicosdecelular.com.br/tabela-plus-teste/,Weslley Henrique,ttq117,85998363020,2023-10-05 18:41:57,2023-10-08 15:41:00,1
695,https://tecnicosdecelular.com.br/tabela-plus/,Weslley Henrique,sua428,85998363020,2023-10-05 18:45:21,2023-11-05 15:44:00,1
696,https://tecnicosdecelular.com.br/tabela-plus-teste/,David Jurchaks,pff969,41996204926,2023-10-05 18:47:54,2023-10-08 15:47:00,1
697,https://tecnicosdecelular.com.br/tabela-plus/,André da Rocha,xcu666,45999376437,2023-10-05 18:59:00,2024-04-05 15:58:00,1
698,https://tecnicosdecelular.com.br/tabela-plus/,Thiago Alves,cdz488,17992289369,2023-10-05 19:02:41,2024-04-05 16:02:00,1
699,https://tecnicosdecelular.com.br/tabela-plus/,Aragon Acessórios,dha443,45999101872,2023-10-05 19:03:10,2023-11-28 15:12:00,1
700,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jader Eduardo,uat452,69981182346,2023-10-05 19:07:41,2023-10-08 16:07:00,1
701,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rozino Amorim,mev761,98984464205,2023-10-05 19:10:38,2023-10-08 16:10:00,1
702,https://tecnicosdecelular.com.br/tabela-plus-teste/,Raimundo Sales ,vzh212,85999364713,2023-10-05 19:15:14,2023-10-08 16:14:00,1
703,https://tecnicosdecelular.com.br/tabela-plus-teste/,Keylla Hamylles,zms418,27992429950,2023-10-05 19:19:25,2023-10-08 16:18:00,1
704,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gabriel Alves,dgc324,69992911356,2023-10-06 01:13:52,2023-10-08 22:13:00,1
705,https://tecnicosdecelular.com.br/tabela-plus-teste/,Andrei Rodrigues,uyx261,11985532651,2023-10-06 01:15:36,2023-10-08 22:15:00,1
706,https://tecnicosdecelular.com.br/tabela-plus-teste/,Auziel,cyw948,96991711164,2023-10-06 01:17:19,2023-10-08 22:17:00,1
707,https://tecnicosdecelular.com.br/tabela-plus-teste/,Ivo Cell,hbg949,79981024958,2023-10-06 11:23:37,2023-10-09 08:23:00,1
708,https://tecnicosdecelular.com.br/tabela-plus-teste/,Diego Nunes,jmt295,31995719501,2023-10-06 12:12:16,2023-10-09 09:12:00,1
709,https://tecnicosdecelular.com.br/tabela-plus-teste/,Cezar de Farias,ubu171,41987315195,2023-10-06 12:15:11,2023-10-09 09:14:00,1
710,https://tecnicosdecelular.com.br/tabela-plus-teste/,Sérgio Alberto,mze477,13996992994,2023-10-06 12:27:35,2023-10-09 09:27:00,1
711,https://tecnicosdecelular.com.br/tabela-plus-teste/,Brunna,qyf191,51989925310,2023-10-06 12:31:33,2023-10-09 09:31:00,1
712,https://tecnicosdecelular.com.br/tabela-plus-teste/,Marcus Fernando,rjx679,99992277099,2023-10-06 13:14:22,2023-10-09 10:13:00,1
713,https://tecnicosdecelular.com.br/tabela-plus-teste/,Flávia Menezes,jhm255,21993748369,2023-10-06 13:24:36,2023-10-09 10:24:00,1
714,https://tecnicosdecelular.com.br/tabela-plus-teste/,Edson Oliveira,hxw759,47997660712,2023-10-06 16:59:03,2023-10-09 13:58:00,1
715,https://tecnicosdecelular.com.br/tabela-plus-teste/,Christyan Lucena,wxp546,99984790499,2023-10-06 17:05:37,2023-10-09 14:05:00,1
716,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gedeon,mnt483,61992884717,2023-10-06 17:16:49,2023-10-09 14:16:00,1
717,https://tecnicosdecelular.com.br/tabela-plus-teste/,Túlio Lucas,qjd545,81991899301,2023-10-06 17:40:01,2023-10-09 14:39:00,1
718,https://tecnicosdecelular.com.br/tabela-plus-teste/,Iuri Paixão,kcq649,35988331441,2023-10-06 17:50:57,2023-10-09 14:50:00,1
719,https://tecnicosdecelular.com.br/tabela-plus-teste/,Daniel Ferreira,sgq817,65992896780,2023-10-06 18:27:18,2023-10-09 15:27:00,1
720,https://tecnicosdecelular.com.br/tabela-plus/,Nilson Lee,nev747,86392888666,2023-10-06 18:37:23,2023-11-05 15:36:00,1
721,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jesuino Francisco,meu741,11971079535,2023-10-06 22:02:49,2023-10-09 19:02:00,1
723,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jonas da Silva,wfn244,11995407562,2023-10-07 00:57:55,2023-10-09 21:57:00,1
724,https://tecnicosdecelular.com.br/tabela-plus-teste/,Júlio Borges,dmw538,74999724604,2023-10-07 11:43:36,2023-10-10 08:43:00,1
725,https://tecnicosdecelular.com.br/tabela-plus-teste/,João Pedro,mpy954,83981305897,2023-10-07 11:47:34,2023-10-10 08:47:00,1
726,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gabriel Silva,wwd437,87988672886,2023-10-07 11:50:08,2023-10-10 08:49:00,1
727,https://tecnicosdecelular.com.br/tabela-plus-teste/,Estevison,zmg572,92993820196,2023-10-07 11:57:48,2023-10-10 08:57:00,1
728,https://tecnicosdecelular.com.br/tabela-plus-teste/,Moisés Messias,tar741,91989568032,2023-10-07 12:41:29,2023-10-10 09:41:00,1
729,https://tecnicosdecelular.com.br/tabela-plus/,Moisés Messias,gux824,91989568032,2023-10-07 12:57:13,2023-11-07 09:56:00,1
730,https://tecnicosdecelular.com.br/tabela-plus-teste/,Diego Oliveira,wrx812,64993428173,2023-10-07 13:09:51,2023-10-10 10:09:00,1
731,https://tecnicosdecelular.com.br/tabela-plus/,Diego Oliveira,xnr148,64993428173,2023-10-07 13:29:27,2023-11-07 10:29:00,1
732,https://tecnicosdecelular.com.br/tabela-plus-teste/,Marcus Vinicius,vum634,12996763088,2023-10-07 13:53:05,2023-10-10 10:52:00,1
733,https://tecnicosdecelular.com.br/tabela-plus-teste/,David Yuri,mta111,35997806520,2023-10-07 14:42:55,2023-10-10 11:42:00,1
735,https://tecnicosdecelular.com.br/tabela-plus-teste/,Aline Barros,fsd827,85996013685,2023-10-07 21:42:55,2023-10-10 18:42:00,1
736,https://tecnicosdecelular.com.br/tabela-plus-teste/,Dinho,yac732,81982316930,2023-10-07 23:58:53,2023-10-10 20:58:00,1
737,https://tecnicosdecelular.com.br/tabela-plus-teste/,Matheus Andrei,ath811,48991381729,2023-10-08 00:00:34,2023-10-10 21:00:00,1
738,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jackson de Jesus,yrv729,69993028692,2023-10-08 00:01:50,2023-10-10 21:01:00,1
739,https://tecnicosdecelular.com.br/tabela-plus/,Dinho,jts274,81982316930,2023-10-08 00:10:30,2023-11-07 21:09:00,1
740,https://tecnicosdecelular.com.br/tabela-plus-teste/,Carlos Danyel,nhh888,88992502897,2023-10-08 00:17:09,2023-10-10 21:16:00,1
741,https://tecnicosdecelular.com.br/tabela-plus-teste/,Luana Coelho,vwn637,62995519460,2023-10-09 11:27:21,2023-10-12 08:25:00,1
742,https://tecnicosdecelular.com.br/tabela-plus-teste/,Eduardo Salvari,kvg495,11983907022,2023-10-09 11:56:24,2023-10-12 08:56:00,1
743,https://tecnicosdecelular.com.br/tabela-plus-teste/,Emerson Diniz,zgk735,61993056550,2023-10-09 12:00:05,2023-10-12 08:59:00,1
744,https://tecnicosdecelular.com.br/tabela-plus-teste/,Welligton Miranda,dnh236,77998099348,2023-10-09 12:29:23,2023-10-12 09:29:00,1
746,https://tecnicosdecelular.com.br/tabela-plus-teste/,Emerson Diniz,zhm859,61993056550,2023-10-09 12:44:38,2024-04-09 09:44:00,1
747,https://tecnicosdecelular.com.br/tabela-plus/,Emerson Diniz,dvn973,61993056550,2023-10-09 12:45:08,2024-04-09 09:44:00,1
748,https://tecnicosdecelular.com.br/tabela-plus-teste/,Tiago Tofoli,zyq486,41995057184,2023-10-09 12:56:44,2023-10-12 09:56:00,1
749,https://tecnicosdecelular.com.br/tabela-plus-teste/,Suzilane,tdx189,82988661818,2023-10-09 14:10:04,2023-10-12 11:09:00,1
750,https://tecnicosdecelular.com.br/tabela-plus-teste/,Tiago Tofoli,gey759,41995057184,2023-10-09 14:15:14,2023-10-12 11:14:00,1
751,https://tecnicosdecelular.com.br/tabela-plus/,Suzylaine,haq441,82988661818,2023-10-09 14:27:59,2023-11-09 11:27:00,1
752,https://tecnicosdecelular.com.br/tabela-plus-teste/,Lilian Souza,cha794,55992042820,2023-10-09 14:55:26,2023-10-12 11:54:00,1
753,https://tecnicosdecelular.com.br/tabela-plus-teste/,Ester Bruna,qgf894,31984610665,2023-10-09 15:03:36,2023-10-12 12:03:00,1
754,https://tecnicosdecelular.com.br/tabela-plus-teste/,Paula Rossi,dwj733,17997420692,2023-10-09 15:06:19,2023-10-12 12:05:00,1
755,https://tecnicosdecelular.com.br/tabela-plus-teste/,William Alves,nqu197,31994635813,2023-10-09 18:36:06,2023-10-12 15:35:00,1
756,https://tecnicosdecelular.com.br/tabela-plus-teste/,Júnior Bueno,xsm596,47997729217,2023-10-09 18:39:57,2023-10-12 15:39:00,1
757,https://tecnicosdecelular.com.br/tabela-plus-teste/,Diones Paz,wut783,51999834767,2023-10-09 18:46:09,2023-10-12 15:45:00,1
758,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rafael Alves,txe927,61992049012,2023-10-09 18:48:48,2023-10-12 15:48:00,1
759,https://tecnicosdecelular.com.br/tabela-plus-teste/,Roberto Júnior,bba569,71991376888,2023-10-09 18:54:58,2023-10-12 15:54:00,1
760,https://tecnicosdecelular.com.br/tabela-plus-teste/,Railane da Silva,typ448,94991966855,2023-10-09 19:15:10,2023-10-12 16:14:00,1
761,https://tecnicosdecelular.com.br/tabela-plus-teste/,Lucas da Rosa,vjg571,51996978559,2023-10-09 19:45:12,2023-10-12 16:44:00,1
762,https://tecnicosdecelular.com.br/tabela-plus/,Lucas da Rosa,bzt689,51996978559,2023-10-09 19:51:30,2023-11-09 16:51:00,1
763,https://tecnicosdecelular.com.br/tabela-plus-teste/,Davidson,xju655,95984192419,2023-10-09 20:06:57,2023-10-12 17:06:00,1
764,https://tecnicosdecelular.com.br/tabela-plus-teste/,Adilson Cândio,khe489,21969117559,2023-10-09 23:13:02,2023-10-12 20:12:00,1
765,https://tecnicosdecelular.com.br/tabela-plus-teste/,Edmarley,hpw331,31993150179,2023-10-09 23:14:25,2023-10-12 20:14:00,1
766,https://tecnicosdecelular.com.br/tabela-plus-teste/,Mateus Melo,mgn311,24981527261,2023-10-10 00:16:34,2023-10-12 21:16:00,1
767,https://tecnicosdecelular.com.br/tabela-plus-teste/,Hudson de Jesus,nqa784,31995713407,2023-10-10 00:35:23,2023-10-12 21:35:00,1
768,https://tecnicosdecelular.com.br/tabela-plus/,José Gláucio Carvalho,wyp844,81992763523,2023-10-10 01:02:15,2023-11-09 22:01:00,1
769,https://tecnicosdecelular.com.br/tabela-plus-teste/,Regis da Silva,rqz859,61998668950,2023-10-10 11:45:33,2023-10-13 08:45:00,1
770,https://tecnicosdecelular.com.br/tabela-plus-teste/,Daiana Silva,fcy746,21984540548,2023-10-10 12:34:47,2023-10-13 09:34:00,1
771,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jorge Freitas,pmb579,92993076822,2023-10-10 12:39:07,2023-10-13 09:38:00,1
772,https://tecnicosdecelular.com.br/tabela-plus-teste/,Keisson,kkn634,99996446560,2023-10-10 12:41:43,2023-10-13 09:41:00,1
773,https://tecnicosdecelular.com.br/tabela-plus-teste/,Housseyn,cha974,48991835401,2023-10-10 13:12:35,2023-10-13 10:12:00,1
774,https://tecnicosdecelular.com.br/tabela-plus-teste/,Celir José,yvz577,11964882329,2023-10-10 13:18:16,2023-10-13 10:17:00,1
775,https://tecnicosdecelular.com.br/tabela-plus-teste/,Josyane,bcr141,64740058439,2023-10-10 13:24:42,2023-10-13 10:24:00,1
776,https://tecnicosdecelular.com.br/tabela-plus-teste/,Carlos Henrique,kzd149,13997591366,2023-10-10 13:29:39,2023-10-13 10:29:00,1
777,https://tecnicosdecelular.com.br/tabela-plus-teste/,Canuto,zuc261,88999430733,2023-10-10 14:14:39,2023-10-13 11:13:00,1
778,https://tecnicosdecelular.com.br/tabela-plus-teste/,Milena Reis,wjq479,11953741088,2023-10-10 16:39:47,2023-10-13 13:39:00,1
779,https://tecnicosdecelular.com.br/tabela-plus-teste/,Miriã da Silva,ctg546,11933550529,2023-10-10 16:47:02,2023-10-13 13:46:00,1
780,https://tecnicosdecelular.com.br/tabela-plus-teste/,Lídia Motta,cdj518,19983268829,2023-10-10 16:56:30,2023-10-13 13:56:00,1
781,https://tecnicosdecelular.com.br/tabela-plus-teste/,Thata Cell,mkf224,11993640626,2023-10-10 17:09:40,2023-10-13 14:09:00,1
782,https://tecnicosdecelular.com.br/tabela-plus/,Canuto Diógenes ,jvu258,88999430733,2023-10-10 17:21:49,2023-11-10 14:21:00,1
783,https://tecnicosdecelular.com.br/tabela-plus-teste/,Diorgenes Mendes,kkb285,98981697875,2023-10-10 17:40:33,2023-10-13 14:40:00,1
784,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jordan Rodrigues,bpa126,21992580407,2023-10-10 17:42:29,2023-10-13 14:42:00,1
785,https://tecnicosdecelular.com.br/tabela-plus-teste/,Luiz Guilherme,dnj645,11956051038,2023-10-10 22:19:40,2023-10-13 19:19:00,1
786,https://tecnicosdecelular.com.br/tabela-plus-teste/,Vitor Hugo,xtp678,43988570617,2023-10-10 22:39:29,2023-10-13 19:39:00,1
787,https://tecnicosdecelular.com.br/tabela-plus-teste/,Vinicius Soares,pej756,22997616191,2023-10-10 23:38:25,2023-10-13 20:38:00,1
788,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jhonatha Assunção,dcv444,86995121912,2023-10-11 11:19:50,2023-10-14 08:19:00,1
789,https://tecnicosdecelular.com.br/tabela-plus-teste/,Íris Marques,nyd127,82994162325,2023-10-11 11:31:11,2023-10-14 08:30:00,1
790,https://tecnicosdecelular.com.br/tabela-plus-teste/,Daniel Augusto,yke411,11986538322,2023-10-11 12:31:26,2023-10-14 09:31:00,1
791,https://tecnicosdecelular.com.br/tabela-plus-teste/,Click Fone,pau321,38998861485,2023-10-11 12:33:44,2023-10-14 09:33:00,1
792,https://tecnicosdecelular.com.br/tabela-plus-teste/,João Paulo,vcx671,84991461181,2023-10-11 12:51:35,2023-10-14 09:51:00,1
793,https://tecnicosdecelular.com.br/tabela-plus-teste/,Daniela Vitória,esp418,82994144687,2023-10-11 13:09:43,2023-10-14 10:09:00,1
794,https://tecnicosdecelular.com.br/tabela-plus-teste/,Marileide,esw314,89994139244,2023-10-11 14:40:43,2023-10-14 11:40:00,1
795,https://tecnicosdecelular.com.br/tabela-plus-teste/,Cleiton Cell,vbf388,62995549090,2023-10-11 18:09:45,2023-10-14 15:09:00,1
796,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jenifer Cristina,wxq563,71981886192,2023-10-11 18:13:01,2023-10-14 15:12:00,1
797,https://tecnicosdecelular.com.br/tabela-plus-teste/,Thiago Silva,ydk949,51992860483,2023-10-11 18:18:02,2023-10-14 15:17:00,1
798,https://tecnicosdecelular.com.br/tabela-plus-teste/,Cíntia Raquel,kyg478,41996267227,2023-10-11 18:20:15,2023-10-14 15:20:00,1
799,https://tecnicosdecelular.com.br/tabela-plus-teste/,Osvaldo Maciel,pdm124,89999404061,2023-10-11 19:12:57,2023-10-14 16:12:00,1
800,https://tecnicosdecelular.com.br/tabela-plus/,Cíntia Raquel,qke761,41996267227,2023-10-11 19:22:51,2024-04-11 16:22:00,1
801,https://tecnicosdecelular.com.br/tabela-plus-teste/,Samuel Macedo,atd743,62994909535,2023-10-11 23:13:10,2023-10-14 20:12:00,1
802,https://tecnicosdecelular.com.br/tabela-plus-teste/,Natália dos Santos,fmc552,93988013910,2023-10-12 00:03:14,2023-10-14 21:03:00,1
803,https://tecnicosdecelular.com.br/tabela-plus-teste/,Thiago Ferreira,hnn279,21995062266,2023-10-12 12:04:11,2023-10-15 09:04:00,1
804,https://tecnicosdecelular.com.br/tabela-plus/,Cleiton Cell,cch899,62995549090,2023-10-12 12:32:49,2024-04-12 09:32:00,1
805,https://tecnicosdecelular.com.br/tabela-plus-teste/,Thales Leão,xht341,13981787017,2023-10-12 12:35:31,2023-10-15 09:35:00,1
806,https://tecnicosdecelular.com.br/tabela-plus-teste/,Roberta Oliveira,eux196,21997715809,2023-10-12 12:45:54,2023-10-15 09:45:00,1
807,https://tecnicosdecelular.com.br/tabela-plus/,Thales Leão,ejk742,13981787017,2023-10-12 13:44:47,2024-04-12 10:44:00,1
808,https://tecnicosdecelular.com.br/tabela-plus-teste/,José Evandro,utw561,19983199692,2023-10-12 13:47:33,2023-10-15 10:47:00,1
809,https://tecnicosdecelular.com.br/tabela-plus-teste/,José Erlande,mbm916,88997924947,2023-10-12 16:27:03,2023-10-15 13:26:00,1
810,https://tecnicosdecelular.com.br/tabela-plus-teste/,Genivado Xavier,wzd825,15997018956,2023-10-12 18:05:53,2023-10-15 15:05:00,1
811,https://tecnicosdecelular.com.br/tabela-plus-teste/,Renato,dkj861,22988178206,2023-10-12 20:40:12,2023-10-15 17:40:00,1
812,https://tecnicosdecelular.com.br/tabela-plus-teste/,Milena Ingrid,jre919,84987545516,2023-10-13 11:50:21,2023-10-16 08:50:00,1
813,https://tecnicosdecelular.com.br/tabela-plus-teste/,Paulo Roberto,ccq563,75982325778,2023-10-13 12:05:43,2023-10-16 09:05:00,1
814,https://tecnicosdecelular.com.br/tabela-plus-teste/,Douglas Souza,jcb719,75991771204,2023-10-13 12:43:09,2023-10-16 09:43:00,1
815,https://tecnicosdecelular.com.br/tabela-plus-teste/,Michele Vitório,yfw381,11985176053,2023-10-13 12:57:19,2023-10-16 09:57:00,1
816,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jessica Silva,nxt728,15997273086,2023-10-13 13:22:17,2023-10-16 10:22:00,1
817,https://tecnicosdecelular.com.br/tabela-plus-teste/,Alessander Aparecido,jca369,62981939137,2023-10-13 13:38:45,2023-10-16 10:38:00,1
818,https://tecnicosdecelular.com.br/tabela-plus-teste/,Richard,wdh788,15996570743,2023-10-13 14:12:53,2023-10-16 11:12:00,1
819,https://tecnicosdecelular.com.br/tabela-plus-teste/,Vinícius Ferreira,arj141,21999598324,2023-10-13 14:34:56,2023-10-16 11:34:00,1
820,https://tecnicosdecelular.com.br/tabela-plus-teste/,Fernando Grandini,svb672,19974026860,2023-10-13 14:45:35,2023-10-16 11:45:00,1
821,https://tecnicosdecelular.com.br/tabela-plus-teste/,Cássio Jefferson,muv385,11961228218,2023-10-13 18:14:19,2023-10-16 15:14:00,1
822,https://tecnicosdecelular.com.br/tabela-plus-teste/,Néia Ribeiro,gjt329,48984588376,2023-10-13 19:02:46,2023-10-16 16:02:00,1
823,https://tecnicosdecelular.com.br/tabela-plus/,Alessandro Aparecido,xkz944,62981939137,2023-10-13 21:56:10,2023-11-13 18:55:00,1
824,https://tecnicosdecelular.com.br/tabela-plus-teste/,Luan Souza,hap162,54981162148,2023-10-13 22:24:48,2023-10-16 19:24:00,1
825,https://tecnicosdecelular.com.br/tabela-plus-teste/,Helediomar,xpm574,48999166602,2023-10-13 22:26:30,2023-10-16 19:26:00,1
826,https://tecnicosdecelular.com.br/tabela-plus/,Helediomar de Medeiros,uzc979,48999166602,2023-10-13 22:36:07,2023-11-13 19:35:00,1
827,https://tecnicosdecelular.com.br/tabela-plus-teste/,Alexssandro,yxm573,49841994539,2023-10-13 23:30:05,2023-10-16 20:29:00,1
828,https://tecnicosdecelular.com.br/tabela-plus-teste/,Thiago Silva,tgy848,11995700679,2023-10-13 23:32:30,2023-10-16 20:32:00,1
829,https://tecnicosdecelular.com.br/tabela-plus-teste/,Felipe Cezar,ubb635,92991866634,2023-10-13 23:37:35,2023-10-16 20:37:00,1
832,https://tecnicosdecelular.com.br/tabela-plus-teste/,Gabriela Muller,weq476,47988357987,2023-10-14 11:47:23,2024-04-14 08:47:00,1
833,https://tecnicosdecelular.com.br/tabela-plus/,Gabriela Muller,tnf967,47988357987,2023-10-14 11:49:21,2024-04-14 08:49:00,1
834,https://tecnicosdecelular.com.br/tabela-plus-teste/,Lucas Barbosa,cuy691,11965811433,2023-10-14 12:03:47,2023-10-17 09:03:00,1
835,https://tecnicosdecelular.com.br/tabela-plus-teste/,Juliano Gallegari,chb962,17981472518,2023-10-14 12:16:52,2023-10-17 09:16:00,1
836,https://tecnicosdecelular.com.br/tabela-plus-teste/,Filipe de Carvalho,fzd342,51981238021,2023-10-14 12:19:03,2023-10-17 09:18:00,1
837,https://tecnicosdecelular.com.br/tabela-plus-teste/,Júlio Cezar,vym785,93991259372,2023-10-14 12:21:11,2023-10-17 09:20:00,1
838,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jorge Lucas,yrw954,91980444146,2023-10-14 12:25:13,2023-10-17 09:25:00,1
839,https://tecnicosdecelular.com.br/tabela-plus/,David Vinícius,srd513,41996204926,2023-10-14 13:05:59,2023-11-14 10:05:00,1
840,https://tecnicosdecelular.com.br/tabela-plus/,Jonatha Assunção,wyr179,86995121912,2023-10-14 13:09:01,2023-11-14 10:08:00,1
841,https://tecnicosdecelular.com.br/tabela-plus-teste/,Michael Luiz,abp131,11937797018,2023-10-14 13:11:23,2023-10-17 10:11:00,1
842,https://tecnicosdecelular.com.br/tabela-plus-teste/,Weslley Martins,syq568,82993921824,2023-10-14 13:13:48,2023-10-17 10:13:00,1
843,https://tecnicosdecelular.com.br/tabela-plus-teste/,Paulo Ricardo,tey718,86988175515,2023-10-14 13:34:39,2023-10-17 10:34:00,1
844,https://tecnicosdecelular.com.br/tabela-plus-teste/,Donizeth,rgq279,61986225503,2023-10-14 13:37:58,2023-10-17 10:37:00,1
845,https://tecnicosdecelular.com.br/tabela-plus-teste/,THK,urp781,41999752119,2023-10-14 13:40:30,2023-10-17 10:40:00,1
846,https://tecnicosdecelular.com.br/tabela-plus-teste/,Maycon Notcel,gxh451,62981412986,2023-10-14 13:56:53,2023-10-17 10:56:00,1
847,https://tecnicosdecelular.com.br/tabela-plus/,Lucas Barbosa,grj654,11965811433,2023-10-14 14:06:34,2024-04-14 11:06:00,1
848,https://tecnicosdecelular.com.br/tabela-plus/,Maycon Cruz,byj676,62981412986,2023-10-14 14:17:52,2024-01-14 11:17:00,1
849,https://tecnicosdecelular.com.br/tabela-plus-teste/,Paulo Mansani,hcg739,67999407443,2023-10-14 14:54:40,2023-10-17 11:54:00,1
850,https://tecnicosdecelular.com.br/tabela-plus-teste/,Eriky Ayres,hpm227,22997592620,2023-10-14 21:16:49,2023-10-17 18:16:00,1
851,https://tecnicosdecelular.com.br/tabela-plus-teste/,Caíque Terra,vug934,64992129084,2023-10-14 22:44:05,2023-10-17 19:43:00,1
852,https://tecnicosdecelular.com.br/tabela-plus-teste/,Edivaldo Ribeiro,sxz611,64999348830,2023-10-15 00:17:19,2023-10-17 21:17:00,1
853,https://tecnicosdecelular.com.br/tabela-plus/,Felipe,yjm131,61993960309,2023-10-16 11:42:14,2023-11-16 08:40:00,1
854,https://tecnicosdecelular.com.br/tabela-plus/,Rafael Moreira,emj739,62994746200,2023-10-16 12:19:59,2023-11-15 09:19:00,1
855,https://tecnicosdecelular.com.br/tabela-plus-teste/,Dulce Oliveira,jfw754,77998099717,2023-10-16 13:19:50,2023-10-19 10:19:00,1
856,https://tecnicosdecelular.com.br/tabela-plus-teste/,Ana Karolina,jhg932,28999346327,2023-10-16 13:25:45,2023-10-19 10:25:00,1
857,https://tecnicosdecelular.com.br/tabela-plus-teste/,Geison Vieira,kku275,68992178880,2023-10-16 13:29:27,2023-10-19 10:29:00,1
858,https://tecnicosdecelular.com.br/tabela-plus-teste/,Marcos Antônio,ywb968,87996280731,2023-10-16 13:32:42,2023-10-19 10:32:00,1
859,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rafael Felix,tgj712,11941966618,2023-10-16 13:35:07,2023-10-19 10:34:00,1
860,https://tecnicosdecelular.com.br/tabela-plus-teste/,Wellington Lopes,ugm976,33988479839,2023-10-16 13:39:28,2023-10-19 10:39:00,1
861,https://tecnicosdecelular.com.br/tabela-plus-teste/,Daniela Bruna,kpd452,51993986207,2023-10-16 13:41:30,2023-10-19 10:41:00,1
862,https://tecnicosdecelular.com.br/tabela-plus-teste/,Guilherme Oliveira,skj628,89981060954,2023-10-16 13:44:50,2023-10-19 10:44:00,1
863,https://tecnicosdecelular.com.br/tabela-plus-teste/,Guilherme Ferreira,vtb321,21995331442,2023-10-16 13:50:48,2023-10-19 10:50:00,1
864,https://tecnicosdecelular.com.br/tabela-plus/,Rafael Felix Mota,vdm388,11941966618,2023-10-16 14:05:54,2024-04-16 11:05:00,1
865,https://tecnicosdecelular.com.br/tabela-plus-teste/,Luis Santos,czq428,67984023776,2023-10-16 14:51:54,2023-10-19 11:51:00,1
866,https://tecnicosdecelular.com.br/tabela-plus-teste/,Samuel Neves,xhj451,11983403048,2023-10-16 14:58:27,2023-10-19 11:58:00,1
867,https://tecnicosdecelular.com.br/tabela-plus-teste/,Dellivane,zns429,92994669064,2023-10-16 15:03:20,2023-10-19 12:03:00,1
868,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jailton da Silva,nhq844,75991241044,2023-10-16 16:30:12,2023-10-19 13:30:00,1
869,https://tecnicosdecelular.com.br/tabela-plus-teste/,Alex Barros,guy416,11974491703,2023-10-16 16:47:37,2023-10-19 13:47:00,1
870,https://tecnicosdecelular.com.br/tabela-plus-teste/,Ivanilda da Silva,jnj422,87998077708,2023-10-16 17:04:12,2023-10-19 14:04:00,1
871,https://tecnicosdecelular.com.br/tabela-plus-teste/,Amanda Lima,gtg464,11983194520,2023-10-16 17:41:27,2023-10-19 14:41:00,1
872,https://tecnicosdecelular.com.br/tabela-plus-teste/,Paulo Victor,hkv158,91984332543,2023-10-16 18:24:04,2023-10-19 15:23:00,1
873,https://tecnicosdecelular.com.br/tabela-plus/,ImportsBel,mhr643,91982107726,2023-10-16 18:38:22,2023-12-16 15:37:00,1
874,https://tecnicosdecelular.com.br/tabela-plus/,Caíque Terra,vae115,64992129084,2023-10-16 18:50:01,2024-04-16 15:49:00,1
876,https://tecnicosdecelular.com.br/tabela-plus-teste/,Raphaela,ubz112,32991543182,2023-10-16 18:59:26,2023-10-19 15:59:00,1
877,https://tecnicosdecelular.com.br/tabela-plus-teste/,Mck Atacadista,jbj281,69993541158,2023-10-16 19:18:35,2023-10-19 16:18:00,1
878,https://tecnicosdecelular.com.br/tabela-plus/,Andréia Silva,dky354,11914832576,2023-10-16 22:11:45,2024-01-20 10:46:00,1
879,https://tecnicosdecelular.com.br/tabela-plus-teste/,Fernanda Oliveira,mta426,19999663469,2023-10-16 22:46:07,2023-10-19 19:45:00,1
880,https://tecnicosdecelular.com.br/tabela-plus/,Fernanda Oliveira,rmw687,19999663469,2023-10-16 22:58:11,2023-11-16 19:57:00,1
881,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jucimar Santos,ban935,75998886575,2023-10-16 23:19:47,2023-10-19 20:19:00,1
882,https://tecnicosdecelular.com.br/tabela-plus-teste/,Reinaldo Vitor,jxw588,11946961626,2023-10-16 23:25:00,2023-10-19 20:24:00,1
883,https://tecnicosdecelular.com.br/tabela-plus-teste/,Marciel dos Santos,muf435,79998458866,2023-10-17 12:17:33,2023-10-20 09:17:00,1
884,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rafael Pontana,vhr184,37999635446,2023-10-17 12:34:22,2023-10-20 09:34:00,1
885,https://tecnicosdecelular.com.br/tabela-plus-teste/,Kleber Santos,pyd479,91841281449,2023-10-17 12:39:43,2023-10-20 09:39:00,1
886,https://tecnicosdecelular.com.br/tabela-plus/,Juliana Strunkis,cyu773,55999016550,2023-10-17 13:28:54,2023-12-26 10:20:00,1
887,https://tecnicosdecelular.com.br/tabela-plus-teste/,Maria Josiane,shf264,12974092049,2023-10-17 13:42:49,2023-10-20 10:42:00,1
888,https://tecnicosdecelular.com.br/tabela-plus-teste/,Hiago Barbosa,fzw888,98999011515,2023-10-17 13:47:30,2023-10-20 10:47:00,1
889,https://tecnicosdecelular.com.br/tabela-plus-teste/,Guilherme Pinheiro,dfj977,81996251042,2023-10-17 14:38:16,2023-10-20 11:38:00,1
890,https://tecnicosdecelular.com.br/tabela-plus-teste/,Kaua Felipe,frs796,37998448380,2023-10-17 14:41:43,2023-10-20 11:41:00,1
891,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rafael Pereira,kcf433,11954502619,2023-10-17 14:54:05,2023-10-20 11:53:00,1
893,https://tecnicosdecelular.com.br/tabela-plus/,Adilson Cândido,gay421,21969117559,2023-10-17 16:35:53,2023-11-17 13:35:00,1
894,https://tecnicosdecelular.com.br/tabela-plus-teste/,Roniére,cgr318,55997017498,2023-10-17 16:49:04,2023-10-20 13:48:00,1
895,https://tecnicosdecelular.com.br/tabela-plus-teste/,Samuel Reis,dms216,12996004075,2023-10-17 16:51:41,2023-10-20 13:51:00,1
896,https://tecnicosdecelular.com.br/tabela-plus-teste/,Andressa de Jesus,cfy824,99991078524,2023-10-17 16:54:54,2023-10-20 13:54:00,1
897,https://tecnicosdecelular.com.br/tabela-plus-teste/,Ronaldo Celular,tmw388,21994846389,2023-10-17 17:02:07,2023-10-20 14:01:00,1
898,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jonabson,cmz355,91982373975,2023-10-17 17:11:07,2023-10-20 14:10:00,1
899,https://tecnicosdecelular.com.br/tabela-plus/,Andressa de Jesus,sje772,99991078524,2023-10-17 17:26:49,2023-11-17 14:26:00,1
900,https://tecnicosdecelular.com.br/tabela-plus-teste/,Leonardo Oliveira,wrs124,16991006336,2023-10-17 17:32:27,2023-10-20 14:32:00,1
901,https://tecnicosdecelular.com.br/tabela-plus-teste/,Karine Nunes,jgm143,97984039709,2023-10-17 17:47:54,2023-10-20 14:47:00,1
902,https://tecnicosdecelular.com.br/tabela-plus-teste/,Shirley Nonato,jxf261,81991249739,2023-10-17 19:23:48,2023-10-20 16:23:00,1
903,https://tecnicosdecelular.com.br/tabela-plus-teste/,Igor Dourado,ryh249,77991191392,2023-10-17 22:38:10,2023-10-20 19:37:00,1
904,https://tecnicosdecelular.com.br/tabela-plus-teste/,Aleson Teixeira,yhx444,31983540612,2023-10-17 22:52:55,2023-10-20 19:52:00,1
905,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jucileia Santana,dpc329,75983456516,2023-10-17 22:55:20,2023-10-20 19:55:00,1
906,https://tecnicosdecelular.com.br/tabela-plus-teste/,Henrique da Silva,zez725,66996099350,2023-10-17 23:01:46,2023-10-20 20:01:00,1
907,https://tecnicosdecelular.com.br/tabela-plus-teste/,Evandro da Silva,kyg983,48998496662,2023-10-17 23:07:04,2023-10-20 20:06:00,1
908,https://tecnicosdecelular.com.br/tabela-plus-teste/,Isabelle Regis,hsm333,21996498077,2023-10-17 23:12:58,2023-10-20 20:12:00,1
909,https://tecnicosdecelular.com.br/tabela-plus-teste/,Pedro Gabriel,zau928,74988315292,2023-10-17 23:17:32,2023-10-20 20:17:00,1
910,https://tecnicosdecelular.com.br/tabela-plus-teste/,Daniel Meneses,buc615,12982995113,2023-10-18 11:27:53,2023-10-21 08:27:00,1
911,https://tecnicosdecelular.com.br/tabela-plus-teste/,George José,qse878,81985160639,2023-10-18 11:32:05,2023-10-21 08:31:00,1
912,https://tecnicosdecelular.com.br/tabela-plus-teste/,Aline Pricila,njd844,62993179141,2023-10-18 11:41:17,2023-10-21 08:41:00,1
913,https://tecnicosdecelular.com.br/tabela-plus-teste/,Kelvis Almeida,rxz275,66992309598,2023-10-18 12:54:43,2023-10-21 09:54:00,1
914,https://tecnicosdecelular.com.br/tabela-plus-teste/,Ana Paula,tnu464,38991291618,2023-10-18 13:44:21,2023-10-21 10:43:00,1
915,https://tecnicosdecelular.com.br/tabela-plus-teste/,Cláudia Vieira,jez144,31996520556,2023-10-18 14:12:30,2023-10-21 11:12:00,1
916,https://tecnicosdecelular.com.br/tabela-plus-teste/,Raabe Alves,ktd346,99991561112,2023-10-18 14:33:39,2023-10-21 11:33:00,1
917,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jaqueline Alves,kpm476,43991801657,2023-10-18 14:39:34,2023-10-21 11:39:00,1
918,https://tecnicosdecelular.com.br/tabela-plus-teste/,Maria Karliane,znh964,19984572905,2023-10-18 15:02:47,2023-10-21 12:02:00,1
919,https://tecnicosdecelular.com.br/tabela-plus-teste/,David Ragner,fve267,41988897995,2023-10-18 17:27:02,2023-10-21 14:26:00,1
920,https://tecnicosdecelular.com.br/tabela-plus-teste/,Robert Junio Nunes de Moraes,fsd752,11953137049,2023-10-18 17:28:43,2023-10-21 14:26:00,1
921,https://tecnicosdecelular.com.br/tabela-plus-teste/,Andre Maia de Oliveira,sju688,43991883716,2023-10-18 17:30:02,2023-10-21 14:26:00,1
922,https://tecnicosdecelular.com.br/tabela-plus-teste/,New Tech ,yvr279,62984828875,2023-10-18 17:37:23,2023-10-21 14:37:00,1
924,https://tecnicosdecelular.com.br/tabela-plus-teste/,Claudilene,eub335,83986717379,2023-10-18 18:54:55,2023-10-21 15:54:00,1
925,https://tecnicosdecelular.com.br/tabela-plus/,David Ragner,mqf778,41988897995,2023-10-18 19:13:07,2024-04-18 16:12:00,1
927,https://tecnicosdecelular.com.br/tabela-plus-teste/,Tayuana Bortolini,txg627,49999607848,2023-10-18 19:33:45,2024-04-18 16:33:00,1
928,https://tecnicosdecelular.com.br/tabela-plus/,Tayuana Bortolini,jpe128,49999607848,2023-10-18 19:35:44,2024-04-18 16:35:00,1
929,https://tecnicosdecelular.com.br/tabela-plus-teste/,Alysson Carlos,ybs697,31984193301,2023-10-18 22:42:31,2023-10-21 19:42:00,1
930,https://tecnicosdecelular.com.br/tabela-plus-teste/,José Adson,yvg116,79988367449,2023-10-18 23:09:05,2023-10-21 20:08:00,1
931,https://tecnicosdecelular.com.br/tabela-plus-teste/,Carlos Eduardo,ppq543,79999232839,2023-10-19 12:56:27,2023-10-22 09:56:00,1
932,https://tecnicosdecelular.com.br/tabela-plus/,Fabrício Carlos,ucy342,64996438959,2023-10-19 17:13:58,2024-01-09 08:19:00,1
933,https://tecnicosdecelular.com.br/tabela-plus/,Fernando Henrique,tgv756,11974191587,2023-10-19 17:27:33,2024-04-19 14:27:00,1
934,https://tecnicosdecelular.com.br/tabela-plus/,Alysson Carlos,dmz517,31984193301,2023-10-19 17:55:33,2023-11-19 14:55:00,1
935,https://tecnicosdecelular.com.br/tabela-plus/,Thafiny Gomes,kvn939,94991629827,2023-10-19 18:03:20,2023-11-19 15:02:00,1
936,https://tecnicosdecelular.com.br/tabela-plus/,Alan Danylo,uxk989,81986799607,2023-10-19 18:16:50,2023-11-19 15:16:00,1
937,https://tecnicosdecelular.com.br/tabela-plus/,Karolayne da Silva,fvr645,63984155870,2023-10-19 19:27:09,2023-11-19 16:26:00,1
938,https://tecnicosdecelular.com.br/tabela-plus/,Carlos Eduardo,suy629,79999232839,2023-10-19 19:43:07,2023-11-19 16:43:00,1
939,https://tecnicosdecelular.com.br/tabela-plus/,Márcio Alonso,fwc114,31971432275,2023-10-20 12:21:28,2024-04-20 09:21:00,1
940,https://tecnicosdecelular.com.br/tabela-plus/,Gabriel Pereto,vkq921,66984575279,2023-10-20 12:57:32,2024-01-20 09:57:00,1
941,https://tecnicosdecelular.com.br/tabela-plus/,Lucas Costa,ack358,98970081964,2023-10-20 14:46:32,2023-11-20 11:46:00,1
942,https://tecnicosdecelular.com.br/tabela-plus/,Felipe Ferreira,xyh391,21980937705,2023-10-21 00:20:45,2023-11-20 21:19:00,1
943,https://tecnicosdecelular.com.br/tabela-plus/,Bruno de Sirqueira,rmb658,79988483194,2023-10-21 15:06:45,2024-04-21 12:06:00,1
944,https://tecnicosdecelular.com.br/tabela-plus-teste/,Cristiano Eduardo,zgu333,31984357274,2023-10-23 11:24:25,2023-10-26 08:23:00,1
945,https://tecnicosdecelular.com.br/tabela-plus/,João Paulo,kbe635,98991500540,2023-10-23 12:16:53,2023-11-23 09:18:00,1
946,https://tecnicosdecelular.com.br/tabela-plus/,Cell Shope,mwf437,63991272623,2023-10-23 15:11:29,2024-04-23 12:10:00,1
947,https://tecnicosdecelular.com.br/tabela-plus/,Cloves Henrique,jua254,66984368239,2023-10-23 16:58:04,2024-04-23 13:57:00,1
948,https://tecnicosdecelular.com.br/tabela-plus/,Lindolfo Neto,rcb198,86999219512,2023-10-23 18:15:29,2024-01-23 15:15:00,1
949,https://tecnicosdecelular.com.br/tabela-plus/,Donizeth Martins Soares,vkv582,61986225503,2023-10-23 18:56:28,2024-04-23 16:00:00,1
950,https://tecnicosdecelular.com.br/tabela-plus/,Dhonata,cka912,99984803084,2023-10-24 00:23:19,2023-11-23 21:20:00,1
951,https://tecnicosdecelular.com.br/tabela-plus/,Edvan Fernandes Macedo,pmc245,77981469650,2023-10-24 00:44:17,2023-11-23 21:43:00,1
952,https://tecnicosdecelular.com.br/tabela-plus/,Luiz Fernando,jqs457,13991274756,2023-10-24 16:13:20,2023-11-24 13:09:00,1
953,https://tecnicosdecelular.com.br/tabela-plus/,João Leno,qcy857,92994630493,2023-10-24 16:40:13,2023-11-24 13:38:00,1
954,https://tecnicosdecelular.com.br/tabela-plus/,Vinícius Soares,fmy741,22997616191,2023-10-24 23:08:50,2023-11-24 20:07:00,1
955,https://tecnicosdecelular.com.br/tabela-plus/,Jorge Luis,kdb265,21982264810,2023-10-24 23:43:28,2023-11-24 20:42:00,1
956,https://tecnicosdecelular.com.br/tabela-plus-teste/,testeteste,zsx6922,12123456789,2023-10-25 10:58:47,2023-10-28 07:58:00,1
957,https://tecnicosdecelular.com.br/tabela-plus/,Hyurian Muniz,ewe132,62935483126,2023-10-25 11:38:22,2023-11-25 08:37:00,1
958,https://tecnicosdecelular.com.br/tabela-plus/,Paulo Henrique,rfp456,79998896390,2023-10-25 14:47:57,2023-11-25 11:46:00,1
959,https://tecnicosdecelular.com.br/tabela-plus/,Diego Alex,hpj864,35992720829,2023-10-25 17:40:15,2024-04-25 14:39:00,1
960,https://tecnicosdecelular.com.br/tabela-plus/,Eliseu da Silva,pmf817,21975583622,2023-10-25 19:04:37,2023-11-25 16:04:00,1
961,https://tecnicosdecelular.com.br/tabela-plus/,Maiara da Silva,jme418,18996796951,2023-10-25 22:36:05,2024-01-29 11:55:00,1
962,https://tecnicosdecelular.com.br/tabela-plus/,Renato Gabriel,kjq726,11988092010,2023-10-26 16:27:26,2023-11-26 13:25:00,1
963,https://tecnicosdecelular.com.br/tabela-plus/,Brenno Ícaro,urp814,21976599508,2023-10-26 17:07:22,2023-11-26 14:06:00,1
964,https://tecnicosdecelular.com.br/tabela-plus/,Kayran Kayro,kwm825,91991486401,2023-10-26 18:52:52,2023-11-26 15:51:00,1
965,https://tecnicosdecelular.com.br/tabela-plus/,Ícaro Emanoel,jcb162,88981032074,2023-10-26 18:56:46,2023-11-26 15:56:00,1
966,https://tecnicosdecelular.com.br/tabela-plus/,Alessandro Barbosa,qtn132,91991594582,2023-10-26 19:07:49,2023-11-26 16:07:00,1
967,https://tecnicosdecelular.com.br/tabela-plus-teste/,Douglas Neves,ctp914,11952460720,2023-10-27 11:33:46,2023-10-31 08:33:00,1
968,https://tecnicosdecelular.com.br/tabela-plus/,Ronaldo Lorimier,sxc168,11910076900,2023-10-27 13:48:27,2024-04-27 10:48:00,1
969,https://tecnicosdecelular.com.br/tabela-plus/,Beatriz Vasconcelos,cgb918,22996129451,2023-10-27 16:51:50,2024-05-28 19:26:00,1
970,https://tecnicosdecelular.com.br/tabela-plus/,Felipe Taylor,qkb979,11939486695,2023-10-27 17:27:04,2023-11-27 14:23:00,1
971,https://tecnicosdecelular.com.br/tabela-plus/,Ronaldo Paes,cmq262,12997414505,2023-10-27 19:05:47,2023-11-27 16:05:00,1
972,https://tecnicosdecelular.com.br/tabela-plus/,DL imports,yzx735,82981167797,2023-10-28 11:45:31,2023-11-28 08:44:00,1
973,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jule Marly,cvz741,11949831459,2023-10-28 23:30:38,2023-10-31 20:30:00,1
974,https://tecnicosdecelular.com.br/tabela-plus-teste/,Fátima Grosselli,sbg167,42999655583,2023-10-30 11:41:03,2023-11-02 08:40:00,1
975,https://tecnicosdecelular.com.br/tabela-plus/,Clériston,cmm987,65984522507,2023-10-30 12:23:33,2024-04-30 09:23:00,1
976,https://tecnicosdecelular.com.br/tabela-plus/,Bruno Gerson,yak914,31995934496,2023-10-30 12:44:27,2024-10-30 09:43:00,1
977,https://tecnicosdecelular.com.br/tabela-plus/,Flávio Augusto,srj898,27999869121,2023-10-30 13:04:03,2023-11-30 10:03:00,1
978,https://tecnicosdecelular.com.br/tabela-plus/,Marina Carvalho,dzt877,63991390965,2023-10-30 18:33:59,2023-11-30 15:33:00,1
979,https://tecnicosdecelular.com.br/tabela-plus-teste/,Giomar Klein,dtf493,51991062081,2023-10-31 00:22:16,2023-11-02 21:22:00,1
980,https://tecnicosdecelular.com.br/tabela-plus-teste/,Maykon Jonathan,hrp535,21998621207,2023-10-31 12:22:44,2023-11-03 09:22:00,1
981,https://tecnicosdecelular.com.br/tabela-plus/,Maykon Jonthan,rgg292,21998621207,2023-10-31 13:09:02,2024-01-04 10:06:00,1
982,https://tecnicosdecelular.com.br/tabela-plus/,Arlete Pereira,aft286,38998474776,2023-10-31 14:30:46,2023-11-30 11:29:00,1
983,https://tecnicosdecelular.com.br/tabela-plus-teste/,Júlio Ebraim,udg525,14996567714,2023-11-01 11:25:31,2023-11-04 08:25:00,1
984,https://tecnicosdecelular.com.br/tabela-plus-teste/,Tayane Letícia,fyc436,64992846549,2023-11-02 00:10:10,2023-11-04 21:09:00,1
985,https://tecnicosdecelular.com.br/tabela-plus/,Wellington Costa,xag229,73998280621,2023-11-02 00:33:53,2023-12-01 21:31:00,1
986,https://tecnicosdecelular.com.br/tabela-plus/,Patrick Duarte,zfx626,53999366424,2023-11-02 00:47:22,2023-12-01 21:46:00,1
987,https://tecnicosdecelular.com.br/tabela-plus/,André Assunção,ywq272,93991219331,2023-11-02 18:22:14,2023-12-02 15:21:00,1
988,https://tecnicosdecelular.com.br/tabela-plus-teste/,Alex Pê,cuw347,13991835344,2023-11-03 12:01:55,2023-11-06 09:01:00,1
989,https://tecnicosdecelular.com.br/tabela-plus/,Kayã Victor,sra175,21980776307,2023-11-03 13:52:22,2023-12-03 10:51:00,1
990,https://tecnicosdecelular.com.br/tabela-plus-teste/,teste11,teh411,75981616091,2023-11-03 15:56:15,2023-11-06 12:56:00,1
991,https://tecnicosdecelular.com.br/tabela-plus/,Loja New Art,wkg422,47992514889,2023-11-03 18:34:11,2024-05-03 15:34:00,1
992,https://tecnicosdecelular.com.br/tabela-plus/,Roberta Ribeiro,qth891,11981680584,2023-11-03 18:41:52,2023-12-03 15:36:00,1
993,https://tecnicosdecelular.com.br/tabela-plus/,Cristina Varjão,pwr654,75998557533,2023-11-03 22:38:41,2023-12-03 19:36:00,1
994,https://tecnicosdecelular.com.br/tabela-plus-teste/,Diomar Almeida,mzy634,62994732079,2023-11-04 11:45:05,2023-11-07 08:44:00,1
995,https://tecnicosdecelular.com.br/tabela-plus/,Gabriel Barancelli,krg827,46999077890,2023-11-04 12:57:07,2023-12-04 09:56:00,1
996,https://tecnicosdecelular.com.br/tabela-plus/,Karine Nunes,zea279,97984039709,2023-11-04 13:51:08,2023-12-04 10:49:00,1
997,https://tecnicosdecelular.com.br/tabela-plus/,Vanessa da Silva,muh732,64993429118,2023-11-04 14:03:27,2023-12-04 11:03:00,1
998,https://tecnicosdecelular.com.br/tabela-plus-teste/,Jenifer Ester,gwf446,17996591739,2023-11-04 20:58:00,2023-11-07 17:57:00,1
999,https://tecnicosdecelular.com.br/tabela-plus-teste/,Marlon,jvf544,33988829977,2023-11-06 12:24:43,2023-11-09 09:24:00,1
1000,https://tecnicosdecelular.com.br/tabela-plus/,Cleomar da Rosa,zzx184,51989149055,2023-11-07 11:19:39,2024-05-07 08:19:00,1
1001,https://tecnicosdecelular.com.br/tabela-plus-teste/,Lucas de Souza,unf918,31989011803,2023-11-07 11:44:37,2023-11-10 08:44:00,1
1002,https://tecnicosdecelular.com.br/tabela-plus/,Alex Sandro,myv533,13991835344,2023-11-07 13:29:02,2023-12-07 10:27:00,1
1003,https://tecnicosdecelular.com.br/tabela-plus/,Daniel Carvalho,egf775,15998273283,2023-11-07 16:08:10,2023-12-07 13:07:00,1
1004,https://tecnicosdecelular.com.br/tabela-plus/,Alessandra de Cássia,zgb349,33984006074,2023-11-07 19:30:46,2024-05-07 16:30:00,1
1005,https://tecnicosdecelular.com.br/tabela-plus-teste/,Diego,hcq977,71992292968,2023-11-08 11:17:48,2023-11-11 08:17:00,1
1006,https://tecnicosdecelular.com.br/tabela-plus-teste/,José Edson,whn231,24988460489,2023-11-09 12:29:04,2023-11-12 09:28:00,1
1007,https://tecnicosdecelular.com.br/tabela-plus-teste/,Oseni ,usx821,62985520362,2023-11-09 19:08:57,2023-11-12 16:08:00,1
1008,https://tecnicosdecelular.com.br/tabela-plus-teste/,Aragon ,qdu446,51995404053,2023-11-09 19:31:26,2023-11-12 16:08:00,1
1009,https://tecnicosdecelular.com.br/tabela-plus/,Leandro Nogueira,hzt784,92991287113,2023-11-09 23:50:11,2024-05-09 20:49:00,1
1010,https://tecnicosdecelular.com.br/tabela-plus-teste/,Daniel,kjt125,11988277140,2023-11-10 11:21:42,2023-11-13 08:21:00,1
1011,https://tecnicosdecelular.com.br/tabela-plus/,Maria Luisa,bsk643,86994810316,2023-11-10 11:47:41,2023-12-10 08:46:00,1
1012,https://tecnicosdecelular.com.br/tabela-plus/,Walace,cwb452,28992550642,2023-11-10 12:59:43,2023-12-10 09:57:00,1
1013,https://tecnicosdecelular.com.br/tabela-plus/,Priscila dos Santos,pps874,51995371578,2023-11-10 13:53:48,2023-12-10 10:53:00,1
1014,https://tecnicosdecelular.com.br/tabela-plus/,José Nilton,spd734,79998695727,2023-11-10 13:56:25,2024-05-10 10:55:00,1
1015,https://tecnicosdecelular.com.br/tabela-plus/,Marcelo Pasquali,xmj173,54999019633,2023-11-10 14:17:11,2024-05-10 11:16:00,1
1016,https://tecnicosdecelular.com.br/tabela-plus/,Felipe Coutinho,zyf793,55999089684,2023-11-10 16:52:27,2023-12-10 13:51:00,1
1017,https://tecnicosdecelular.com.br/tabela-plus/,Luiz Fernando,nxs855,69993561367,2023-11-10 17:27:03,2024-01-12 16:43:00,1
1018,https://tecnicosdecelular.com.br/tabela-plus/,Lenara Soares,jam737,85992035922,2023-11-10 18:27:46,2023-12-10 15:26:00,1
1019,https://tecnicosdecelular.com.br/tabela-plus-teste/,Sidivane,nak444,21980595763,2023-11-11 12:57:34,2023-11-14 09:57:00,1
1020,https://tecnicosdecelular.com.br/tabela-plus/,Tiago Henrique,dnr215,16996011695,2023-11-13 11:05:02,2024-02-13 08:01:00,1
1021,https://tecnicosdecelular.com.br/tabela-plus-teste/,Paulo Ferreira,nqv886,61992395870,2023-11-13 13:54:11,2023-11-16 10:54:00,1
1022,https://tecnicosdecelular.com.br/tabela-plus/,Fábio,uud264,11968601757,2023-11-13 14:47:37,2023-12-13 11:45:00,1
1023,https://tecnicosdecelular.com.br/tabela-plus/,Elder,rbv155,62994561380,2023-11-13 23:09:24,2023-12-13 20:09:00,1
1024,https://tecnicosdecelular.com.br/tabela-plus/,Beatriz Vieira,xqx567,17981927817,2023-11-14 00:24:57,2023-12-13 21:24:00,1
1025,https://tecnicosdecelular.com.br/tabela-plus-teste/,Fábio Duarte,ujz922,75991849607,2023-11-14 12:17:12,2023-11-17 09:16:00,1
1026,https://tecnicosdecelular.com.br/tabela-plus/,Arthur Vinícius,kvs846,81998467727,2023-11-14 16:12:54,2023-12-14 13:12:00,1
1027,https://tecnicosdecelular.com.br/tabela-plus/,Lucimara Queiroz,nke856,11997436218,2023-11-14 18:29:42,2024-05-14 15:29:00,1
1028,https://tecnicosdecelular.com.br/tabela-plus/,Wagnei Carneiro,pkx965,62995026379,2023-11-14 19:11:51,2024-02-14 16:11:00,1
1029,https://tecnicosdecelular.com.br/tabela-plus/,Rafael Lacerda,aud726,38992424934,2023-11-14 19:23:47,2024-03-16 10:21:00,1
1030,https://tecnicosdecelular.com.br/tabela-plus-teste/,Diego da Silvana,kcb631,73991803519,2023-11-15 11:37:23,2023-11-18 08:37:00,1
1031,https://tecnicosdecelular.com.br/tabela-plus/,Diego Silva,dfn891,73991803519,2023-11-15 11:49:26,2023-12-15 08:48:00,1
1032,https://tecnicosdecelular.com.br/tabela-plus/,Caio Juarez,dpz638,91980164764,2023-11-15 12:45:55,2023-12-15 09:44:00,1
1033,https://tecnicosdecelular.com.br/tabela-plus-teste/,José Pedro,gju344,61984083900,2023-11-16 11:40:51,2023-11-19 08:40:00,1
1034,https://tecnicosdecelular.com.br/tabela-plus/,Diego Soares,drv372,11913517175,2023-11-16 18:21:18,2023-12-16 15:20:00,1
1035,https://tecnicosdecelular.com.br/tabela-plus/,José Mariano,bcf125,81981933329,2023-11-17 00:47:42,2024-05-16 21:46:00,1
1036,https://tecnicosdecelular.com.br/tabela-plus-teste/,João Lucas,tqf297,22997516608,2023-11-17 12:34:55,2023-11-20 09:34:00,1
1037,https://tecnicosdecelular.com.br/tabela-plus/,Fernandes Neto,pvk667,88999999920,2023-11-17 14:50:44,2024-05-17 11:50:00,1
1038,https://tecnicosdecelular.com.br/tabela-plus/,Click Fone,zdh857,38998861485,2023-11-17 16:32:04,2024-05-17 13:31:00,1
1039,https://tecnicosdecelular.com.br/tabela-plus/,José Leobaldo,dre554,79999997729,2023-11-17 17:04:16,2024-05-17 14:03:00,1
1040,https://tecnicosdecelular.com.br/tabela-plus/,Matheus de Oliveira,yam699,38998574626,2023-11-17 23:33:09,2023-12-17 20:32:00,1
1041,https://tecnicosdecelular.com.br/tabela-plus-teste/,Luan Henrique,wff761,19997982323,2023-11-18 11:52:28,2023-11-21 08:50:00,1
1042,https://tecnicosdecelular.com.br/tabela-plus/,Rayann,pqp281,93999046655,2023-11-18 14:24:00,2023-12-18 11:23:00,1
1043,https://tecnicosdecelular.com.br/tabela-plus/,Emerson Guimarães,twa955,87996155512,2023-11-18 21:03:42,2024-05-16 18:03:00,1
1044,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rhaleney Amorim,gmy663,55819662846,2023-11-20 11:20:40,2023-11-23 08:20:00,1
1045,https://tecnicosdecelular.com.br/tabela-plus/,Ricardo Soares,kke651,15997462812,2023-11-20 12:38:21,2024-06-21 09:00:00,1
1047,https://tecnicosdecelular.com.br/tabela-plus/,Weslen Paulo,nuf883,16993460278,2023-11-20 13:14:54,2024-01-20 14:54:00,1
1048,https://tecnicosdecelular.com.br/tabela-plus/,André Maia,dbv948,43984818845,2023-11-20 13:16:44,2024-01-20 10:58:00,1
1049,https://tecnicosdecelular.com.br/tabela-plus/,Kamilla Rezende,ynr762,22997579668,2023-11-20 14:21:00,2023-12-20 11:20:00,1
1050,https://tecnicosdecelular.com.br/tabela-plus-teste/,Cristiano Silveira,bby863,51997714764,2023-11-21 11:47:06,2023-11-24 08:46:00,1
1051,https://tecnicosdecelular.com.br/tabela-plus/,Bianca Lima,mma765,32991543385,2023-11-21 11:49:40,2023-12-21 08:48:00,1
1052,https://tecnicosdecelular.com.br/tabela-plus/,Cristiano Silveira,ffx677,51997714764,2023-11-21 11:52:24,2024-05-21 08:51:00,1
1053,https://tecnicosdecelular.com.br/tabela-plus/,Marcos Roberto,cmc591,11981241074,2023-11-21 12:13:26,2023-12-21 09:13:00,1
1054,https://tecnicosdecelular.com.br/tabela-plus/,José Carlos,bvg574,64996603565,2023-11-21 12:16:36,2024-02-21 09:16:00,1
1055,https://tecnicosdecelular.com.br/tabela-plus/,Pedro,rpe369,31993834526,2023-11-21 12:51:19,2024-06-21 15:43:00,1
1057,https://tecnicosdecelular.com.br/tabela-plus/,Alfredo Mathis,tgf664,32984922244,2023-11-22 12:12:12,2023-12-22 09:11:00,1
1058,https://tecnicosdecelular.com.br/tabela-plus-teste/,Júnior Alves,shb924,11913603660,2023-11-22 12:48:17,2023-11-25 09:48:00,1
1059,https://tecnicosdecelular.com.br/tabela-plus/,Márcio Vinícius,nuh839,11999301337,2023-11-22 13:16:16,2023-12-22 10:15:00,1
1060,https://tecnicosdecelular.com.br/tabela-plus/,Patrícia Luiz,ted332,66996481151,2023-11-22 14:40:12,2024-05-22 11:40:00,1
1061,https://tecnicosdecelular.com.br/tabela-plus/,Dione Thomazini,zrx166,28999566060,2023-11-22 16:50:36,2024-05-22 13:50:00,1
1062,https://tecnicosdecelular.com.br/tabela-plus/,Letícia Costa,jpd829,64993113397,2023-11-22 17:42:42,2023-12-22 14:42:00,1
1063,https://tecnicosdecelular.com.br/tabela-plus/,Jeferson Martins,rec468,86981685846,2023-11-22 18:24:43,2024-05-22 15:24:00,1
1064,https://tecnicosdecelular.com.br/tabela-plus/,Luana Teste,fkn411,85997210239,2023-11-22 22:12:46,2024-02-29 19:12:00,1
1065,https://tecnicosdecelular.com.br/tabela-plus/,Hugo Vinícius,xmv128,21971830398,2023-11-23 00:00:34,2023-12-22 21:01:00,1
1066,https://tecnicosdecelular.com.br/tabela-plus/,Gustavo Benedito,kzr369,16992896174,2023-11-23 00:08:53,2023-12-22 21:08:00,1
1067,https://tecnicosdecelular.com.br/tabela-plus/,Maria Ingrid,nbk766,21970388111,2023-11-23 11:05:23,2023-12-23 08:04:00,1
1068,https://tecnicosdecelular.com.br/tabela-plus-teste/,Anderson,rqf218,91981341612,2023-11-23 11:33:10,2023-11-26 08:04:00,1
1069,https://tecnicosdecelular.com.br/tabela-plus/,João Santos,wvs515,81984051414,2023-11-23 11:58:16,2023-12-23 08:58:00,1
1070,https://tecnicosdecelular.com.br/tabela-plus/,Leonidas de Jesus,pds543,82987040942,2023-11-23 13:02:22,2023-12-23 10:01:00,1
1071,https://tecnicosdecelular.com.br/tabela-plus/,Leonardo Santos,hfr271,21996402124,2023-11-23 13:11:39,2024-05-23 10:11:00,1
1072,https://tecnicosdecelular.com.br/tabela-plus/,Melquisedeque,kdk588,98986065698,2023-11-23 13:23:29,2023-12-23 10:23:00,1
1073,https://tecnicosdecelular.com.br/tabela-plus/,Antônio Francisco,hzc734,68999377477,2023-11-23 14:03:47,2023-12-23 11:02:00,1
1074,https://tecnicosdecelular.com.br/tabela-plus/,José Carlos,fku139,71987085128,2023-11-23 17:30:50,2023-12-23 14:29:00,1
1075,https://tecnicosdecelular.com.br/tabela-plus/,Mobi Cell,dbe353,48988103366,2023-11-23 19:13:56,2023-12-23 16:12:00,1
1076,https://tecnicosdecelular.com.br/tabela-plus/,Lucas,hgx895,71991037237,2023-11-23 19:22:38,2023-12-23 16:22:00,1
1077,https://tecnicosdecelular.com.br/tabela-plus/,Store Império,fhf712,64992653192,2023-11-23 22:41:38,2023-12-23 19:40:00,1
1079,https://tecnicosdecelular.com.br/tabela-plus/,Rodolfo Flausino,qau342,16993064677,2023-11-24 11:43:11,2023-12-24 08:42:00,1
1080,https://tecnicosdecelular.com.br/tabela-plus/,Douglas Pereira,xjd351,61995682442,2023-11-24 12:06:35,2023-12-24 09:06:00,1
1081,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rafael Lopes,een142,42991088453,2023-11-24 12:28:13,2023-11-27 09:27:00,1
1082,https://tecnicosdecelular.com.br/tabela-plus/,Leonardo Naneti,nsc415,16981352156,2023-11-24 13:36:17,2024-05-24 10:36:00,1
1083,https://tecnicosdecelular.com.br/tabela-plus/,Maik ,tvs241,24992934973,2023-11-24 14:06:18,2023-12-24 11:05:00,1
1084,https://tecnicosdecelular.com.br/tabela-plus-teste/,21 99170-3716,cbd241,21991703716,2023-11-24 17:14:15,2023-11-27 14:14:00,1
1085,https://tecnicosdecelular.com.br/tabela-plus/,Marco Ramon,ref745,18988217192,2023-11-25 00:07:57,2023-12-24 21:07:00,1
1086,https://tecnicosdecelular.com.br/tabela-plus-teste/,Uti Assistência,yhr749,98992165517,2023-11-25 11:23:16,2023-11-28 08:23:00,1
1087,https://tecnicosdecelular.com.br/tabela-plus/,Ismael Lucas,eyx116,71986437310,2023-11-25 20:34:55,2023-12-25 17:33:00,1
1088,https://tecnicosdecelular.com.br/tabela-plus-teste/,Rogerinho,eyv662,31984422259,2023-11-27 11:40:00,2023-11-30 08:39:00,1
1089,https://tecnicosdecelular.com.br/tabela-plus/,Francisco Mardone,afk833,85981578025,2023-11-27 12:49:27,2023-12-27 09:48:00,1
1090,https://tecnicosdecelular.com.br/tabela-plus/,Felipe Ervolino,njy861,18991196369,2023-11-27 13:01:05,2024-01-28 16:25:00,1
1091,https://tecnicosdecelular.com.br/tabela-plus/,Ubiratan Willy,qch326,62991637902,2023-11-27 18:28:03,2024-04-03 19:38:00,1
1093,https://tecnicosdecelular.com.br/tabela-plus/,Jhessey,tyc894,15998196972,2023-11-28 13:47:36,2024-07-03 11:53:00,1
1094,https://tecnicosdecelular.com.br/tabela-plus/,Márcio Vinicius,kzx276,62996218580,2023-11-28 14:10:37,2024-07-03 09:11:00,1
1095,https://tecnicosdecelular.com.br/tabela-plus/,Tiago Carvalho,fft121,55999081311,2023-11-28 14:24:07,2024-05-28 11:23:00,1
1096,https://tecnicosdecelular.com.br/tabela-plus/,Diego Ribeiro,cyx628,21965861983,2023-11-28 14:27:39,2024-05-28 11:27:00,1
1097,https://tecnicosdecelular.com.br/tabela-plus/,Márcio Mauriz,zef245,86999151800,2023-11-28 17:18:35,2024-02-28 14:18:00,1
1098,https://tecnicosdecelular.com.br/tabela-plus/,Nilson Macedo,uur281,66996840384,2023-11-28 18:11:17,2023-12-28 15:11:00,1
1099,https://tecnicosdecelular.com.br/tabela-plus/,Glaydson Ferreira,nbz313,91982323897,2023-11-28 18:14:54,2024-05-28 15:14:00,1
1100,https://tecnicosdecelular.com.br/tabela-plus/,Isaac,wpw648,86994436651,2023-11-28 18:46:19,2023-12-28 15:44:00,1
1101,https://tecnicosdecelular.com.br/tabela-plus-teste/,Débora Fernandes,kjf592,34934152739,2023-11-29 11:49:55,2023-12-02 08:49:00,1
1102,https://tecnicosdecelular.com.br/tabela-plus/,Débora Fernandes,ahg147,34934152739,2023-11-29 12:45:46,2024-06-29 09:45:00,1
1103,https://tecnicosdecelular.com.br/tabela-plus/,Camila Aparecida,wuw248,14981384305,2023-11-29 17:29:12,2024-02-29 14:28:00,1
1104,https://tecnicosdecelular.com.br/tabela-plus/,Iuri Iago,wsf611,16993831359,2023-11-29 23:30:46,2024-05-29 20:30:00,1
1105,https://tecnicosdecelular.com.br/tabela-plus/,Matheus Machado,bxk332,53991371913,2023-11-30 12:07:10,2023-12-30 09:06:00,1
1106,https://tecnicosdecelular.com.br/tabela-plus/,Júnior Bispo,pph955,75981499808,2023-11-30 14:14:42,2024-05-30 11:14:00,1
1107,https://tecnicosdecelular.com.br/tabela-plus/,Brick Cell,khh722,51996353666,2023-11-30 14:40:41,2024-05-30 11:40:00,1
1108,https://tecnicosdecelular.com.br/tabela-plus/,Rodrigo Mendonça,rkx663,22997101764,2023-11-30 18:06:15,2023-12-30 15:05:00,1
1109,https://tecnicosdecelular.com.br/tabela-plus/,Benilo Santos,egj924,27999610610,2023-11-30 18:24:25,2023-12-30 15:24:00,1
1110,https://tecnicosdecelular.com.br/tabela-plus/,Jessica Silva,hjr259,15997273086,2023-11-30 19:41:58,2024-05-30 16:41:00,1
1111,https://tecnicosdecelular.com.br/tabela-plus-teste/,Genildo,xac921,81985718777,2023-12-01 11:25:55,2023-12-04 08:25:00,1
1112,https://tecnicosdecelular.com.br/tabela-plus/,Ednon Andrade,gst734,94984309955,2023-12-01 13:11:18,2024-02-01 10:10:00,1
1113,https://tecnicosdecelular.com.br/tabela-plus/,Monique Antunes,txu264,31985056995,2023-12-01 13:23:59,2024-06-01 10:23:00,1
1114,https://tecnicosdecelular.com.br/tabela-plus/,Rafael Francisco,wsm744,11982807956,2023-12-01 14:01:02,2023-12-31 11:00:00,1
1115,https://tecnicosdecelular.com.br/tabela-plus/,Sidnei,hpv819,65999385379,2023-12-01 16:31:35,2024-06-01 13:31:00,1
1116,https://tecnicosdecelular.com.br/tabela-plus/,Fernando Cavalcante,jvx891,19983620768,2023-12-01 16:56:48,2024-01-01 13:55:00,1
1117,https://tecnicosdecelular.com.br/tabela-plus/,Chaiane Moreira,zwr338,54991142221,2023-12-01 17:15:21,2023-12-31 14:15:00,1
1118,https://tecnicosdecelular.com.br/tabela-plus/,Rai Fernandes,wkn384,62999345508,2023-12-01 17:31:35,2024-02-02 10:13:00,1
1119,https://tecnicosdecelular.com.br/tabela-plus/,Jackeline Rodrigues,qsh722,65998028119,2023-12-01 19:13:56,2024-06-01 16:13:00,1
1120,https://tecnicosdecelular.com.br/tabela-plus/,Matheus Técnico,utn742,11949613366,2023-12-01 22:38:37,2023-12-31 19:37:00,1
1121,https://tecnicosdecelular.com.br/tabela-plus/,Fernando Santana,bew152,88999088060,2023-12-02 01:08:51,2024-01-01 22:07:00,1
1122,https://tecnicosdecelular.com.br/tabela-plus-teste/,Wender Souza,ecc641,11996003419,2023-12-02 12:58:52,2023-12-05 09:58:00,1
1123,https://tecnicosdecelular.com.br/tabela-plus-teste/,Pablo Carvalho,ema513,47996832794,2023-12-02 23:01:20,2023-12-05 20:01:00,1
1124,https://tecnicosdecelular.com.br/tabela-plus-teste/,Lenilson,xnw614,91981075656,2023-12-04 11:50:01,2023-12-07 08:49:00,1
1125,https://tecnicosdecelular.com.br/tabela-plus/,Duda Leite,ekd152,85997113286,2023-12-04 13:11:13,2024-06-04 10:10:00,1
1126,https://tecnicosdecelular.com.br/tabela-plus/,Wellington,csz987,31998036571,2023-12-04 13:13:10,2024-01-04 10:12:00,1
1127,https://tecnicosdecelular.com.br/tabela-plus/,Play Cell,qax182,62981668007,2023-12-04 14:03:11,2024-01-04 11:02:00,1
1128,https://tecnicosdecelular.com.br/tabela-plus/,Alan Lemos,dfz171,99982016630,2023-12-04 16:46:19,2024-01-03 13:45:00,1
1129,https://tecnicosdecelular.com.br/tabela-plus/,Sávio Barbosa,pdy565,33991111048,2023-12-04 16:58:57,2024-06-04 13:58:00,1
1130,https://tecnicosdecelular.com.br/tabela-plus/,Marcos Fernandes,qxs153,99982067163,2023-12-04 17:58:06,2024-07-06 14:56:00,1
1131,https://tecnicosdecelular.com.br/tabela-plus/,Raquel de Almeida,jad797,13991178633,2023-12-04 18:39:28,2024-01-03 15:38:00,1
1132,https://tecnicosdecelular.com.br/tabela-plus/,Guilherme de Oliveira,hnp375,86988628749,2023-12-04 23:19:07,2024-01-04 20:14:00,1
1133,https://tecnicosdecelular.com.br/tabela-plus/,José Adenildo Santos,hvz587,79998769572,2023-12-04 23:20:47,2024-01-04 20:20:00,1
1134,https://tecnicosdecelular.com.br/tabela-plus/,Rafael Fernandes,hbn512,35984631722,2023-12-05 11:30:37,2024-06-05 08:29:00,1
1135,https://tecnicosdecelular.com.br/tabela-plus/,Adilson Silva,hxe744,11977571845,2023-12-05 13:32:45,2024-06-05 10:32:00,1
1136,https://tecnicosdecelular.com.br/tabela-plus/,Rodrigo Neres,zyz374,63984109768,2023-12-05 22:36:06,2024-06-05 19:35:00,1
1137,https://tecnicosdecelular.com.br/tabela-plus/,Ademar Flávio,yeq168,79999524518,2023-12-05 22:57:46,2024-06-05 19:57:00,1
1138,https://tecnicosdecelular.com.br/tabela-plus/,Igor de Jesus,krw265,19998020768,2023-12-05 22:58:32,2024-06-05 19:58:00,1
1139,https://tecnicosdecelular.com.br/tabela-plus/,Iago da Silva Gomes,zdv816,88996910912,2023-12-06 12:16:55,2024-02-06 11:48:00,1
1140,https://tecnicosdecelular.com.br/tabela-plus/,Leonardo Claudino,pkx746,47996635246,2023-12-06 12:22:04,2024-01-06 09:21:00,1
1141,https://tecnicosdecelular.com.br/tabela-plus/,Alex Campestrini,dku842,48991996747,2023-12-06 13:09:23,2024-01-06 10:09:00,1
1142,https://tecnicosdecelular.com.br/tabela-plus/,Romário Neves,jxu518,94992535005,2023-12-06 13:33:30,2024-01-06 10:33:00,1
1143,https://tecnicosdecelular.com.br/tabela-plus/,Eduardo Gomes,etp166,62984851801,2023-12-06 14:06:00,2024-01-06 11:05:00,1
1144,https://tecnicosdecelular.com.br/tabela-plus/,Ederson Je Celulares,jsn664,88999273760,2023-12-06 14:40:49,2024-01-06 11:40:00,1
1145,https://tecnicosdecelular.com.br/tabela-plus/,Luiz Fernando,rnp333,11999221867,2023-12-06 14:53:04,2024-01-06 11:52:00,1
1146,https://tecnicosdecelular.com.br/tabela-plus/,Luiz Fernando,rnp333,11999221867,2023-12-06 14:53:11,2024-01-06 11:52:00,1
1147,https://tecnicosdecelular.com.br/tabela-plus/,Kleber Willian,jwz248,91980123623,2023-12-06 17:51:10,2024-01-06 14:50:00,1
1148,https://tecnicosdecelular.com.br/tabela-plus/,Alexandre Mendes Queiroz,kgu632,11990210023,2023-12-06 19:29:56,2024-01-06 16:29:00,1
1149,https://tecnicosdecelular.com.br/tabela-plus/,Rubens Férinha,ncd898,66984001613,2023-12-06 22:30:44,2024-06-06 19:29:00,1
1150,https://tecnicosdecelular.com.br/tabela-plus/,Nemuel,udc341,94984002641,2023-12-07 00:31:31,2024-01-06 21:30:00,1
1151,https://tecnicosdecelular.com.br/tabela-plus/,Pedro Farias,aar562,81998392996,2023-12-07 12:26:41,2024-01-07 09:26:00,1
1152,https://tecnicosdecelular.com.br/tabela-plus/,Gustavo Machado Leal,knp386,34999245412,2023-12-07 12:29:15,2024-01-07 09:28:00,1
1153,https://tecnicosdecelular.com.br/tabela-plus/,Maria Josiane,wng972,12974092049,2023-12-07 14:26:26,2024-01-07 11:25:00,1
1154,https://tecnicosdecelular.com.br/tabela-plus/,Suellen,sbu832,21975018700,2023-12-07 16:43:42,2024-01-07 13:43:00,1
1155,https://tecnicosdecelular.com.br/tabela-plus/,Thamires Vitória,nhu134,35997193859,2023-12-08 12:10:43,2024-01-08 09:10:00,1
1156,https://tecnicosdecelular.com.br/tabela-plus/,Pedro Henrique Guesso,mbs821,11993229157,2023-12-08 17:24:28,2024-01-08 14:24:00,1
1157,https://tecnicosdecelular.com.br/tabela-plus/,Loja Varitudo,ccw618,73999450845,2023-12-09 14:56:02,2024-01-09 11:55:00,1
1158,https://tecnicosdecelular.com.br/tabela-plus/,Natty Dantas,svk693,11996836716,2023-12-09 21:32:10,2024-01-09 18:31:00,1
1159,https://tecnicosdecelular.com.br/tabela-plus/,Ivã Silva Portigar,yxk629,91984363396,2023-12-10 00:31:16,2024-01-09 21:31:00,1
1160,https://tecnicosdecelular.com.br/tabela-plus/,Alexandre Scapin,mrc665,17997576168,2023-12-11 11:24:18,2024-06-11 08:24:00,1
1161,https://tecnicosdecelular.com.br/tabela-plus/,Oseni Silva,yyw622,62985520362,2023-12-11 13:58:10,2024-06-11 10:57:00,1
1162,https://tecnicosdecelular.com.br/tabela-plus/,Edilson Soares,dnj982,82999922339,2023-12-11 16:25:59,2024-01-11 13:24:00,1
1163,https://tecnicosdecelular.com.br/tabela-plus/,Silviane Pereira,vju194,48988681098,2023-12-11 18:18:25,2024-01-11 15:18:00,1
1164,https://tecnicosdecelular.com.br/tabela-plus/,Bruno Pontes Ferreira,axz786,94991447072,2023-12-12 01:27:11,2024-12-11 22:26:00,1
1165,https://tecnicosdecelular.com.br/tabela-plus/,Júnior IPhones,yfn523,79998131408,2023-12-12 12:19:36,2024-01-12 09:20:00,1
1166,https://tecnicosdecelular.com.br/tabela-plus/,Ivanildo Nery,bek674,71992446173,2023-12-12 12:48:26,2024-01-12 09:48:00,1
1167,https://tecnicosdecelular.com.br/tabela-plus/,Luan Vinícius Santos,wyh656,11978127524,2023-12-12 13:13:55,2024-01-12 10:13:00,1
1168,https://tecnicosdecelular.com.br/tabela-plus/,Dafne Garcia,fnx912,17988423181,2023-12-12 14:06:52,2024-01-12 11:06:00,1
1169,https://tecnicosdecelular.com.br/tabela-plus/,Camila Fortuna,mct787,51999247589,2023-12-12 16:17:01,2024-01-12 13:16:00,1
1170,https://tecnicosdecelular.com.br/tabela-plus/,Amtônio Akimoto,wqm579,73991310000,2023-12-12 17:06:00,2024-01-12 14:05:00,1
1171,https://tecnicosdecelular.com.br/tabela-plus/,Juliano Sanches,xvd782,35991411584,2023-12-12 18:38:26,2024-01-12 15:38:00,1
1172,https://tecnicosdecelular.com.br/tabela-plus-teste/,Teste 2,123tdc,92993940910,2023-12-13 11:02:40,2023-12-16 08:02:00,1
1173,https://tecnicosdecelular.com.br/tabela-plus/,Natã Batista,gax338,62981510325,2023-12-13 13:00:01,2024-01-13 10:00:00,1
1174,https://tecnicosdecelular.com.br/tabela-plus/,Nara Almeida,nbp856,44997165856,2023-12-13 13:52:34,2024-06-13 10:52:00,1
1175,https://tecnicosdecelular.com.br/tabela-plus/,Fabiana Silva,chd645,13982040854,2023-12-13 14:58:50,2024-01-13 11:58:00,1
1176,https://tecnicosdecelular.com.br/tabela-plus/,Jaine Dias Rocha,fgr617,33988375676,2023-12-13 15:01:19,2024-06-13 12:00:00,1
1177,https://tecnicosdecelular.com.br/tabela-plus/,Gilso de Albuquerque,frs599,54999981457,2023-12-13 16:43:37,2024-01-13 13:43:00,1
1178,https://tecnicosdecelular.com.br/tabela-plus/,Douglas Tawan,rnf139,69999449487,2023-12-13 18:06:15,2024-01-13 15:06:00,1
1179,https://tecnicosdecelular.com.br/tabela-plus/,Laysla Karolaine da Silva,kbd137,21994846389,2023-12-13 18:42:48,2024-01-13 15:42:00,1
1180,https://tecnicosdecelular.com.br/tabela-plus/,Vanessa Vitória,fnv888,21959184764,2023-12-13 22:51:09,2024-06-13 19:50:00,1
1181,https://tecnicosdecelular.com.br/tabela-plus/,Daniely Marçal,squ137,62992806244,2023-12-14 12:36:32,2024-01-14 09:35:00,1
1182,https://tecnicosdecelular.com.br/tabela-plus/,Izaque Higinio,eef164,82993565439,2023-12-14 19:31:15,2024-06-14 16:30:00,1
1183,https://tecnicosdecelular.com.br/tabela-plus/,Diego Jeferson,avq733,35984090675,2023-12-15 00:45:25,2024-01-14 21:44:00,1
1184,https://tecnicosdecelular.com.br/tabela-plus/,Matheus Portela Cruz,eqg458,77999881339,2023-12-15 12:07:51,2024-06-15 09:07:00,1
1185,https://tecnicosdecelular.com.br/tabela-plus/,Israel Lopes Dias,czk532,31986023103,2023-12-15 14:13:48,2024-01-15 11:13:00,1
1186,https://tecnicosdecelular.com.br/tabela-plus/,Willian Gustavo da Silva Barbosa,sfb283,12997733172,2023-12-15 17:16:34,2024-06-15 14:16:00,1
1187,https://tecnicosdecelular.com.br/tabela-plus/,João Carlos Lopes,qtr454,38999465748,2023-12-16 00:54:43,2024-06-15 21:54:00,1
1188,https://tecnicosdecelular.com.br/tabela-plus/,Wagner Miranda,mpr217,34988585276,2023-12-16 14:17:13,2024-01-16 11:17:00,1
1189,https://tecnicosdecelular.com.br/tabela-plus/,Mariana Menegrini,sen974,35991645912,2023-12-16 15:04:58,2024-01-16 12:04:00,1
1190,https://tecnicosdecelular.com.br/tabela-plus/,Rodolfo Morais,kaw445,73991691478,2023-12-18 13:57:35,2024-01-18 10:57:00,1
1191,https://tecnicosdecelular.com.br/tabela-plus/,Osman Kergson Vaz de Souza,bsz563,86995929607,2023-12-18 14:44:57,2024-01-18 11:44:00,1
1192,https://tecnicosdecelular.com.br/tabela-plus/,Maria Medeiros,ndr997,11954317358,2023-12-18 16:27:25,2024-01-18 13:27:00,1
1193,https://tecnicosdecelular.com.br/tabela-plus/,Daniel Alves da Silva,jva723,64993028706,2023-12-18 16:53:30,2024-01-18 13:53:00,1
1194,https://tecnicosdecelular.com.br/tabela-plus/,Paulo Henrique Teixeira,gac346,38992623124,2023-12-19 12:22:47,2024-01-19 09:22:00,1
1195,https://tecnicosdecelular.com.br/tabela-plus/,Francis Regis dos Santos,phk179,64999174348,2023-12-19 14:04:45,2024-06-19 11:04:00,1
1196,https://tecnicosdecelular.com.br/tabela-plus/,Igor Expedito Araújo,ayk176,11975257044,2023-12-19 18:11:55,2024-01-19 15:11:00,1
1197,https://tecnicosdecelular.com.br/tabela-plus/,Rafael de Souza,kqj646,85982172956,2023-12-19 22:04:06,2024-01-19 19:03:00,1
1198,https://tecnicosdecelular.com.br/tabela-plus/,Débora Priscila,rqw381,11968128493,2023-12-20 13:01:57,2024-06-20 10:01:00,1
1199,https://tecnicosdecelular.com.br/tabela-plus/,Seriustech Israel,snk227,54991164200,2023-12-20 13:12:19,2024-01-20 10:11:00,1
1200,https://tecnicosdecelular.com.br/tabela-plus/,Denis Rogério,zua233,92994371487,2023-12-20 14:35:37,2024-01-20 11:35:00,1
1201,https://tecnicosdecelular.com.br/tabela-plus/,Techno Gamer,bhh828,94991834549,2023-12-20 16:10:30,2024-06-20 13:10:00,1
1202,https://tecnicosdecelular.com.br/tabela-plus/,Antônio de O. da Silva Neto,jft851,11954850383,2023-12-20 16:12:33,2024-06-20 13:12:00,1
1203,https://tecnicosdecelular.com.br/tabela-plus/,Vitória Vinhais Fernandes,gkk387,34931121552,2023-12-20 17:37:05,2024-01-20 14:36:00,1
1204,https://tecnicosdecelular.com.br/tabela-plus/,Vinícius Gabriel Souza,mja215,37991918141,2023-12-20 18:07:41,2024-01-20 15:06:00,1
1205,https://tecnicosdecelular.com.br/tabela-plus/,Guilherme Santos de Jesus,beu358,13991962134,2023-12-20 19:00:33,2024-01-20 16:00:00,1
1206,https://tecnicosdecelular.com.br/tabela-plus/,Lucas Marchi,jvf992,16993901442,2023-12-21 17:09:53,2024-01-21 14:08:00,1
1207,https://tecnicosdecelular.com.br/tabela-plus/,Ivanilson dos Santos Silva,hgt153,11948420638,2023-12-21 18:10:23,2024-01-21 15:10:00,1
1208,https://tecnicosdecelular.com.br/tabela-plus/,Vinícius Fernando dos Passos,qkp949,79996923693,2023-12-22 00:36:10,2024-01-21 21:35:00,1
1209,https://tecnicosdecelular.com.br/tabela-plus/,Ana Lúcia Cruz,avk845,27988035686,2023-12-22 13:49:31,2024-06-22 10:48:00,1
1210,https://tecnicosdecelular.com.br/tabela-plus/,Igor Frederico de Lima,xry236,31983077904,2023-12-22 17:58:30,2024-01-22 14:59:00,1
1211,https://tecnicosdecelular.com.br/tabela-plus/,Augusto Mendonça,cwf372,67981148307,2023-12-23 12:28:00,2024-06-23 09:27:00,1
1212,https://tecnicosdecelular.com.br/tabela-plus/,Daniel Adrian,pzv132,33999366884,2023-12-23 13:52:01,2024-01-23 10:51:00,1
1213,https://tecnicosdecelular.com.br/tabela-plus/,Marcos Rossato,ujx229,51984758269,2023-12-23 20:28:14,2024-01-23 17:28:00,1
1214,https://tecnicosdecelular.com.br/tabela-plus/,Thiago da Silva Correa ,gew223,21999278152,2023-12-25 18:02:58,2024-06-25 15:02:00,1
1215,https://tecnicosdecelular.com.br/tabela-plus/,Herbert Oliveira,knp498,11947508152,2023-12-25 22:33:08,2024-01-25 19:33:00,1
1216,https://tecnicosdecelular.com.br/tabela-plus/,Rodrigo Mocambite Corico,eqp124,97984299455,2023-12-26 11:57:34,2024-01-26 08:56:00,1
1217,https://tecnicosdecelular.com.br/tabela-plus/,Felipe Thome,fja516,11953939973,2023-12-26 13:11:24,2024-06-26 10:12:00,1
1218,https://tecnicosdecelular.com.br/tabela-plus/,Gilberto Antônio,try942,37999429439,2023-12-26 14:09:45,2024-12-26 11:09:00,1
1219,https://tecnicosdecelular.com.br/tabela-plus/,Luciano Feliciano,pvx735,32984913910,2023-12-26 14:47:44,2024-03-26 11:47:00,1
1220,https://tecnicosdecelular.com.br/tabela-plus/,Fernando Matheus,wwj457,42998123836,2023-12-26 17:00:34,2024-01-26 14:00:00,1
1221,https://tecnicosdecelular.com.br/tabela-plus/,Dávila Store,qtj278,69992049395,2023-12-26 17:56:31,2024-01-26 14:56:00,1
1222,https://tecnicosdecelular.com.br/tabela-plus/,Auziel Luiz,dwd135,96991711164,2023-12-27 16:08:46,2024-06-27 13:08:00,1
1223,https://tecnicosdecelular.com.br/tabela-plus/,Lorena Nascimento Rodrigues,kkg389,65992284683,2023-12-27 18:27:51,2024-06-27 15:27:00,1
1224,https://tecnicosdecelular.com.br/tabela-plus/,Lucas Vinícius Alves Pereira,knp544,66981267262,2023-12-28 13:13:19,2024-06-28 10:13:00,1
1225,https://tecnicosdecelular.com.br/tabela-plus/,João Paulo Ramos,ubj722,33999195951,2023-12-28 13:47:36,2024-01-28 10:47:00,1
1226,https://tecnicosdecelular.com.br/tabela-plus/,Cleyton Anderson,hqw152,11994227772,2023-12-28 14:46:49,2024-01-28 11:46:00,1
1227,https://tecnicosdecelular.com.br/tabela-plus/,Mesaque Silva,cbp936,43998670300,2023-12-28 19:06:21,2024-06-28 16:06:00,1
1228,https://tecnicosdecelular.com.br/tabela-plus/,Jairo Terra,jai123,22999445337,2023-12-29 13:44:24,2024-01-29 10:45:00,1
1229,https://tecnicosdecelular.com.br/tabela-plus/,Rafael Jonatas de Oliveira,zha593,44991671633,2023-12-29 14:12:37,2024-01-29 11:13:00,1
1230,https://tecnicosdecelular.com.br/tabela-plus/,Silmara Messias Carvalho,rbh329,63984941740,2023-12-29 17:21:23,2024-01-29 14:21:00,1
1231,https://tecnicosdecelular.com.br/tabela-plus/,Taynara da Costa Santos,esk374,35992288912,2023-12-29 17:51:42,2024-03-29 14:51:00,1
1232,https://tecnicosdecelular.com.br/tabela-plus/,Gediel,xuj139,41995123935,2023-12-29 19:34:23,2024-06-29 16:34:00,1
1233,https://tecnicosdecelular.com.br/tabela-plus/,Adylla Carneiro,jwu638,62996432546,2023-12-29 23:08:30,2024-06-29 20:08:00,1
1234,https://tecnicosdecelular.com.br/tabela-plus/,Ivan Monteiro de Jesus,fhu644,79996841777,2024-01-02 12:56:05,2024-02-02 09:55:00,1
1235,https://tecnicosdecelular.com.br/tabela-plus/,Victor Guilherme de Costa,wcp563,31982333500,2024-01-02 14:55:47,2024-02-02 11:55:00,1
1236,https://tecnicosdecelular.com.br/tabela-plus/,Fernando Soti,pnt459,41998487466,2024-01-02 17:07:50,2024-02-02 14:07:00,1
1237,https://tecnicosdecelular.com.br/tabela-plus/,Diogo Roberto de Souza,sfx798,19991689290,2024-01-02 17:12:31,2024-02-02 14:12:00,1
1238,https://tecnicosdecelular.com.br/tabela-plus/,Genilson Alves Barbosa,hus151,87999246685,2024-01-02 18:48:49,2024-07-02 15:48:00,1
1239,https://tecnicosdecelular.com.br/tabela-plus/,Silvino Joaquim Barbosa,tje746,81987808885,2024-01-02 19:01:27,2024-02-02 15:59:00,1
1240,https://tecnicosdecelular.com.br/tabela-plus/,Jean Jorge,nqm355,13974105116,2024-01-02 23:29:34,2024-07-02 20:29:00,1
1241,https://tecnicosdecelular.com.br/tabela-plus/,Alfredo Mathis,zbu248,32984922244,2024-01-03 11:40:55,2024-07-03 08:40:00,1
1242,https://tecnicosdecelular.com.br/tabela-plus/,Guilherme Vinal,twm969,62984599917,2024-01-03 11:48:30,2024-02-03 08:47:00,1
1243,https://tecnicosdecelular.com.br/tabela-plus/,Jonas Belchol,bhq177,19982410166,2024-01-03 12:09:48,2024-02-03 09:09:00,1
1244,https://tecnicosdecelular.com.br/tabela-plus/,Evandro Luiz,jgw382,21987006863,2024-01-03 14:58:18,2024-02-03 11:57:00,1
1245,https://tecnicosdecelular.com.br/tabela-plus/,Luciano Fagundes,pvv868,11964849097,2024-01-03 14:59:19,2024-02-03 11:58:00,1
1246,https://tecnicosdecelular.com.br/tabela-plus/,Bruna Naiara,bqz931,19998334023,2024-01-03 18:02:49,2024-02-03 15:02:00,1
1247,https://tecnicosdecelular.com.br/tabela-plus/,Ricardo Dahmer,frh674,47984439480,2024-01-03 18:03:55,2024-07-03 15:03:00,1
1248,https://tecnicosdecelular.com.br/tabela-plus/,Fabiana de Paula,fym783,37933004963,2024-01-03 23:02:24,2025-01-03 20:02:00,1
1249,https://tecnicosdecelular.com.br/tabela-plus/,Francisco José,ecw932,85982213681,2024-01-04 14:29:50,2024-02-04 11:29:00,1
1250,https://tecnicosdecelular.com.br/tabela-plus/,Gleibson Gomes da Costa,hup913,64999236240,2024-01-04 16:27:29,2024-07-04 13:27:00,1
1251,https://tecnicosdecelular.com.br/tabela-plus/,Victor Augusto,fhu512,35997735446,2024-01-04 18:16:23,2024-02-04 15:15:00,1
1252,https://tecnicosdecelular.com.br/tabela-plus/,Leandro Otsuka,dhj695,14991258122,2024-01-04 18:44:18,2024-07-04 15:44:00,1
1253,https://tecnicosdecelular.com.br/tabela-plus/,Daniel Ferreira Araújo,vtz619,62984009517,2024-01-05 12:01:41,2024-07-05 09:01:00,1
1254,https://tecnicosdecelular.com.br/tabela-plus/,Jhonatan Santana,whn826,31992683562,2024-01-05 12:23:09,2024-07-03 09:22:00,1
1255,https://tecnicosdecelular.com.br/tabela-plus/,Mikaiany Deodato ,daq887,85988104773,2024-01-05 12:45:59,2024-02-05 09:45:00,1
1256,https://tecnicosdecelular.com.br/tabela-plus/,Anne Caroline Vidal,qer595,21987140446,2024-01-05 16:15:50,2024-02-05 13:15:00,1
1257,https://tecnicosdecelular.com.br/tabela-plus/,Elton PoitCell,mma825,15991658583,2024-01-05 18:21:02,2024-02-05 15:20:00,1
1258,https://tecnicosdecelular.com.br/tabela-plus/,Leandro Brito,kaj497,81989548831,2024-01-05 18:25:36,2024-07-05 15:25:00,1
1259,https://tecnicosdecelular.com.br/tabela-plus-teste/,Glauciane Guimarães,ewn926,62999487692,2024-01-05 18:54:10,2024-02-04 15:54:00,1
1260,https://tecnicosdecelular.com.br/tabela-plus/,Guthierys Souza,enr241,62998700309,2024-01-05 23:21:54,2024-02-05 20:21:00,1
1261,https://tecnicosdecelular.com.br/tabela-plus/,Alisson Lotar Will,yay315,47999551582,2024-01-05 23:36:06,2024-07-05 20:36:00,1
1262,https://tecnicosdecelular.com.br/tabela-plus/,Samuel Martins Baive,sbb382,67998045818,2024-01-05 23:48:03,2025-01-05 20:47:00,1
1263,https://tecnicosdecelular.com.br/tabela-plus/,Glauciane Guimarães,sub793,62999487692,2024-01-06 11:19:14,2024-02-06 08:20:00,1
1264,https://tecnicosdecelular.com.br/tabela-plus/,Peterson Morães,ptp144,51981144402,2024-01-06 13:34:18,2024-02-06 10:33:00,1
        """
        CellphoneAccess.objects.all().delete()

        for entity in entities.splitlines():
            splited_entity = entity.strip().split(",")
            if len(splited_entity) == 8:
                test_url = "https://tecnicosdecelular.com.br/tabela-plus-teste/"
                _id, url, client, password, whatsapp, created_at, valid_until, active = splited_entity

                if url != test_url:
                    access = CellphoneAccess.objects.create(
                        client=client,
                        whatsapp=whatsapp,
                        password=password,
                        is_active=active == "1"
                    )
                    access.save()
                    access.created_at = created_at
                    access.valid_until = valid_until
                    access.save()
                    print(f"[{access.client}] ({access.whatsapp}) - {access.password}")
