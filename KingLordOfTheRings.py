#-------------------------------------------------------------------------------
# Name:        KingLordOfTheRings
# Purpose:
#
# Author:      Huawei WANG
#
# Created:     03/06/2021
# Copyright:   (c) Administrator 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Personnage:
    "Fonctions de base du jeu King Lord of the Rings"

    # Builder
    def __init__(self, nom, vie, force, endurance, rapidité, intelligence, race):
        self.Nom = nom
        self.Vie = int(vie)

        self.Force = int(force)
        self.Endurance = int(endurance)
        self.Rapidité = int(rapidité)
        # vaiable dure pour instant
        self.Intelligence = intelligence
        self.Race = race

    # Méthode estMort()
    def estMort(self):
        return False if self.Vie > 0 else True

    # Méthode pour afficher l'état du personnage
    def afficheEtat(self):
        if self.Vie == 1:
            return "Il reste 1 point de vie à {}.".format(self.Nom)
        elif self.Vie > 1:
            return "Il reste {0} points de vie à {1}.".format(self.Vie, self.Nom)
        else:
            return "{} est mort!".format(self.Nom)

    # Méthode afficheCaractéristique()
    def afficheCaractéristique(self):
        return "{0} a une force de {1}, une endurance de {2},une rapidité de {3}, une intelligence de {4}.".format(self.Nom, self.Force, self.Endurance, self.Rapidité, self.Intelligence,)

    # Méthode perdVie(nbPoints DeViePerdus)
    def perdVie(self, nbPointsDeViePerdus):
        if nbPointsDeViePerdus >= self.Vie:
            return "{} a subi une attaque mortelle!!!".format(self.Nom)
        elif nbPointsDeViePerdus == 1:
            return "{} subit une attaque, il perd 1 point de vie.".format(self.Nom)
        else:
            return "{0} subit une attaque, il perd {1} point de vie.".format(self.Nom, nbPointsDeViePerdus)
        self.Vie -=nbPointsDeViePerdus

    # Méthode gagneVie(nbPoint VieGagne) Si le personnage n'est pas mort
    def gagneVie(self, nbPointVieGagne):
        if self.Vie > 0:
            self.Vie += nbPointVieGagne
            return "{0} a été soigné. Ses points de vie valent maintenant {1}".format(self.Nom, self.Vie)

    # Création de la méthode attaque(autrePersonnage) modification avec 5.0 et esquiveAttaque()
    def attaque(self, autrePersonnage):
        if self.Vie < 0:
            return "{} ne peut attaquer personne : Il est mort!".format(self.Nom)
        elif (round(self.Rapidité*1.2) <= autrePersonnage.Force) and (self.Vie > 0) and (autrePersonnage.Vie > 0):
            self.pointsDeDegats = round(autrePersonnage.Force*0.6)
            self.Vie -= self.pointsDeDegats

    # 4.9 Création de la méthode soigne (autre Personnage, pointsDeSoin)
    def Soigne(self, autrePersonnage, pointsDeSoin):
        if (self.Vie) > 0 and (autrePersonnage.Vie > 0):
            autrePersonnage.Vie += pointsDeSoin
            return "{per} soigne {autrePer}. {autrePer} restaure à {point} point(s) de vie".format(per=self.Nom, autrePer=autrePersonnage.Nom, point=pointsDeSoin)
            #???????????????????? point(s)
        elif autrePersonnage.Vie < 0:
            return "{per} ne peut pas soigner {autrePer}. {autrePer} est mort!!!".format(per=self.Nom, autrePer=autrePersonnage.Nom)
        else:
            return "{autrePer} ne peut pas être soigné par {per}. {per} est mort!!!".format(per=self.Nom, autrePer=autrePersonnage.Nom)

    # 5.0 Création de la méthode esquiveAttaque(autrePersonnage)
    def esquiveAttaque(self, autrePersonnage):
        if (round(self.Rapidité*1.2) > autrePersonnage.Force) and (self.Vie > 0) and (autrePersonnage.Vie > 0):
            return "{per} esquive l'attaque de {autrePer}.\n Esquive: calcul de rapidité de {per}: \n {perRap} contre {autrePerForce} pour la force de {autrePer}".format(per=self.Nom,
                                                                                                                                                                        autrePer=autrePersonnage.Nom,
                                                                                                                                                                        perRap=self.Rapidité,
                                                                                                                                                                        autrePerForce=autrePersonnage.Force)
        elif self.Vie < 0:
            return "{per} ne peut esquiver l'attaque de {autrePer}: {per} est mort!".format(per=self.Nom, autrePer=autrePersonnage.Nom)
        else:
            return "{per} ne peut esquiver l'attaque de {autrePer}: {autrePer} est mort!".format(per=self.Nom, autrePer=autrePersonnage.Nom)

    # 5.1 Création de la méthode seDeplace(pointsDeDeplacement) :
    def seDeplace(self, pointsDeDeplacement):
        pass


# ????????? TypeError: __init__() missing 7 required positional arguments: 'nom', 'vie', 'force', 'endurance', 'rapidité', 'intelligence', and 'race'


##class Magicien(Personnage):
##    def __init__(self):
##        Personnage.__init__(self)
##        magie = round(self.Force*0.6)
##
##    def faireMagie(self, autrePersonne):
##        autrePersonne.Vie += self.pointsDeMagie


def main():

    bilbo = Personnage("Biblo", 100, 10, 10, 10, 10, -2)
    gollum = Personnage("Gollum", 200, 20, 20, 20, 20, -4)
    gandalf = Personnage("Gollum", 500, 20, 20, 20, 20, 6)

    etat_biblo =bilbo.afficheEtat()
    print(etat_biblo)

    est_mort = bilbo.estMort()
    print(est_mort)

    carac = bilbo.afficheCaractéristique()
    print(carac)

    perd_vie = bilbo.perdVie(37)
    print(perd_vie)

    gagne_vie = bilbo.gagneVie(27)
    print(gagne_vie)

    bilbo.attaque(gollum)
    gollum.attaque(bilbo)
    print(bilbo.Vie, gollum.Vie)

    soin = bilbo.Soigne(gandalf, 1000)
    print(soin)

    esqui = bilbo.esquiveAttaque(gollum)
    print(esqui)

    bilbo.seDeplace(15)

    gollum.attaque(bilbo)
    gandalf.attaque(bilbo)

##    gollum = Magicien()
##    magie_gollom = gollum.faireMagie(bilbo)
##    print(bilbo.Vie)
##    magie_gandalf = gandalf.faireMagie(bilbo)
##    print(bilbo.Vie)


if __name__ == '__main__':
    main()
