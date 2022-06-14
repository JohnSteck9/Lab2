from random import randint
import csv

FIRST_NAME = ["Short Story: The Truth About MOSCOW BURNED DOWN", "Best MOSCOW BURNED DOWN Android/iPhone Apps",
         "Get Better MOSCOW BURNED DOWN Results By Following 3 Simple Steps",
         "Here Is What You Should Do For Your MOSCOW BURNED DOWN",
         "3 Tips About MOSCOW BURNED DOWN You Can't Afford To Miss",
         "Apply These 5 Secret Techniques To Improve MOSCOW BURNED DOWN",
         "3 Easy Ways To Make MOSCOW BURNED DOWN Faster", "3 Easy Ways To Make MOSCOW BURNED DOWN Faster"]



SECOND_NAME = ["Short Story: The Truth About MOSCOW BURNED DOWN", "Best MOSCOW BURNED DOWN Android/iPhone Apps",
         "Get Better MOSCOW BURNED DOWN Results By Following 3 Simple Steps",
         "Here Is What You Should Do For Your MOSCOW BURNED DOWN",
         "3 Tips About MOSCOW BURNED DOWN You Can't Afford To Miss",
         "Apply These 5 Secret Techniques To Improve MOSCOW BURNED DOWN",
         "3 Easy Ways To Make MOSCOW BURNED DOWN Faster", "3 Easy Ways To Make MOSCOW BURNED DOWN Faster"]

EMAIL = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla',
           'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan',
           'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan',
           'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana',
           'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso',
           'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic',
           'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo',
           'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba',
           'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador',
           'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)',
           'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia',
           'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece',
           'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana',
           'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong',
           'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man',
           'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati',
           "Korea, Democratic People's Republic of", "Korea", 'Republic of Kuwait', 'Kyrgyzstan',
           "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
           'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
           'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico',
           'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat',
           'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia',
           'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands',
           'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea',
           'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion',
           'Romania', 'russian pederation', 'Rwanda', 'Saint Barthélemy',
           'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia',
           'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa',
           'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone',
           'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia',
           'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname',
           'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic',
           'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo',
           'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands',
           'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States',
           'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu',
           'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.',
           'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']

# MESSAGE_ID = ["pending", "end", "creating"]



def generate_data():
    with open('sample_data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "first_name", "second_name", "email", "message_id"])
        for i in range(1000):
            request_data = []
            id = i + 1
            request_data.append(id)
            first_name = FIRST_NAME[randint(0, 2)]
            request_data.append(first_name)
            second_name = SECOND_NAME[randint(0, len(SECOND_NAME) - 1)]
            request_data.append(second_name)
            email = EMAIL[randint(0, 7)]
            request_data.append(email)
            message_id = 'none'
            request_data.append(message_id)
            writer.writerow(request_data)


generate_data()