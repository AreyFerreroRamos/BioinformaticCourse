from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

simple_sequence = Seq("ATAGTCTG")
print(simple_sequence)

simple_sequence_record = SeqRecord(simple_sequence)
simple_sequence_record.id = "AC56463"
simple_sequence_record.description = "El gen de la felicidad"
print(simple_sequence_record)
