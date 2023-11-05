import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_alkutilavuus_nollataan_jos_neg(self):
        vara = Varasto(-1)
        self.assertEqual(0, vara.tilavuus)

    def test_alkusaldo_nollataan_jos_neg(self):
        vara = Varasto(1, -1)

        self.assertEqual(0, vara.saldo)

    def test_saldo_suur_kuin_tilavuus(self):
        vara = Varasto(1, 10)
        
        self.assertEqual(1, vara.saldo)

    def test_lisattava_maara_neg(self):
        vara = self.varasto.saldo

        self.varasto.lisaa_varastoon(-1)

        self.assertEqual(vara, self.varasto.saldo)

    def test_lisataan_liikaa_tayttaa(self):
        self.varasto.lisaa_varastoon(100000)

        self.assertEqual(self.varasto.tilavuus, self.varasto.saldo)

    def test_varastosta_ei_voi_ottaa_neg(self):
        vara = self.varasto.saldo

        self.varasto.ota_varastosta(-1)

        self.assertEqual(vara, self.varasto.saldo)

    def test_varastosta_voi_ottaa_kaikki(self):
        varasto = Varasto(10, 10)
        maara = varasto.ota_varastosta(1000)

        self.assertEqual(10, maara)

    def test_str_funktio_palauttaa_oikein(self):
        va = Varasto(10, 10)
        lause = va.__str__()
        oik_lause = "saldo = 10, vielä tilaa 0"

        self.assertEqual(oik_lause, lause)


