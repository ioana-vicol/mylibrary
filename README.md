# Bibliothek

Das Programm "mylibrary" ermöglicht das Hinzufügen und Löschen von Büchern, die Suche nach Büchern, die Empfehlung eines zufälligen Buches, das Ausleihen- und die Rückgabe eines Buches.

Book() verwaltet die Eigenschaften wie Autor, Titel und Genre

BookSeries() erbt die Eigenschaften aus der Klasse "Book". Diese beschreibt beispielsweise eine Buchreihe, und erweitert die Eigenschaften der simplen Klasse "Book" um weitere Eigenschaften wie die Gesamtanzahl der Teile und die Teilliste

BookLibrary() ist die Hauptlogik der Bibliothek. Hier wird eine Liste der Bücher erstellt, und das Hinzufügen- und Löschen der Bücher werden anhand von Funktionen verwaltet. 

User() ermöglicht die verwaltung von Benutzer und die Liste der ausgeliehenen Bücher.

main() erstellt das "Hauptmenu" des Programmes, und ermöglicht die Interaktion mit der gesamten Buchbibliothek.
