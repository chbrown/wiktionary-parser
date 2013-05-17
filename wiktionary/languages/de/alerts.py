from wiktionary.alerts import Alert, FixableAlert

class SubstantivTabelleAlert(Alert):
    description = 'Substantiv Tabelle seems incorrect'

class FixableSubstantivTabelleAlert(FixableAlert):
    description = 'Substantiv Tabelle seems incorrect'

class UnreadableAlert(Alert):
    description = 'Substantiv Tabelle was not readable.'
