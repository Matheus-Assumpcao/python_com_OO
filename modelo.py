class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    @property
    def like(self):
        return self._like

    def dar_like(self):
        self._like += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Likes: {self._like}"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Duração {self.duracao} min - Likes: {self._like}"

class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - {self.temporada} temporadas - Likes: {self._like}"

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

vingadores = Filme("vingadores - utimato", 2019, 180)
the_boys = Serie("the boys", 2021, 2)
ldj = Filme("liga da justiça", 2020, 200)
twd = Serie("The Walking Dead", 2012, 9)

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
ldj.dar_like()
ldj.dar_like()
twd.dar_like()
twd.dar_like()
twd.dar_like()
twd.dar_like()
the_boys.dar_like()
the_boys.dar_like()
the_boys.dar_like()

filmes_e_serie = [vingadores, the_boys, ldj, twd]
playlist_fim_de_semana = Playlist("fim de semana", filmes_e_serie)

print(f"Tamanho da playlist: {len(playlist_fim_de_semana)}")

for programa in playlist_fim_de_semana:
    print(programa)

print(f"Ta ou não ta? {vingadores in playlist_fim_de_semana}")
print(playlist_fim_de_semana[1])
