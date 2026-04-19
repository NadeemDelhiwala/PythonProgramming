#String immutable 
string="string"
print(string[1]);
# cannot change the original string.
# string[1]="T";
# print(string);
print(string.replace("t","T"));
new_string=string.replace("s","Y");
print(f"Creates a copy of the original string but does not change the original string {new_string}")
print(string);
