class Studente:

  def __init__(self, nome, cognome, eta, citta_residenza):
    self.nome = nome
    self.cognome = cognome
    self.eta = eta
    self.citta_residenza = citta_residenza

  # Classificazione Biennio / Triennio in base all'età
  def classificazione(self):
    if self.eta <= 15:
      return "Biennio"
    else:
      return "Triennio"

  def __str__(self):
    return f"{self.cognome} {self.nome}, Età: {self.eta} ({self.classificazione()}), Città: {self.citta_residenza}"