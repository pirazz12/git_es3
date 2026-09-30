class Scuola:

  def __init__(self):
    self.studenti = []

  # Aggiunta studente
  def aggiungi_studente(self, studente):
    if len(self.studenti) < 1000:
      self.studenti.append(studente)
    else:
      print("Limite massimo di 1000 studenti raggiunto.")

  # Ricerca per cognome
  def cerca_per_cognome(self, cognome):
    trovati = []
    for s in self.studenti:
      if s.cognome.lower() == cognome.lower():
        trovati.append(s)
    return trovati

  # Ricerca per età
  def cerca_per_eta(self, eta):
    trovati = []
    for s in self.studenti:
      if s.eta == eta:
        trovati.append(s)
    return trovati

  # Conteggio studenti
  def conteggio_studenti(self):
    return len(self.studenti)