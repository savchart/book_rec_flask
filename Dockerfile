# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the local files to the container
COPY . .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the shell script to download the data
RUN chmod +x download_data.sh && \
    ./download_data.sh

# Check if the data files are present in the data folder
RUN ls data | grep -E "BX-Book-Ratings.csv|BX-Books.csv"

# Run the create_dataframe script
RUN python create_db.py

# Check if the df file is present in the data folder
RUN ls data | grep "df.csv"

# Run the main script
CMD ["python", "app.py"]
