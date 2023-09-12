import csv
header = ['username','First Name', 'Last Name','Address','City','State','pincode','email','Phone Number','Phone Device Type','Job Title','Company','From','To','Location','Description','University','Degree','Field','GPA','language','Facebook','LinkedIn','Authorized to Work?','Require sponsorship?','Open to relocation?','Current location','non-compete or non- solicitation agreement?','Salary expectations','Willing to travel?','Gender','race','Are you veteran?','Do you have Disability?','url']
with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    f.close()