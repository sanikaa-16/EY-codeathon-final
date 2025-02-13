class Config:
    # Change this line:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  # This will create app.db in your project root
    
    # Rest of the config remains the same
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'poornavfblr@gmail.com'
    MAIL_PASSWORD = 'ppyetvyvqjitsixl' 
    MAIL_DEFAULT_SENDER = 'poornavfblr@gmail.com'