# Use Ruby base image
FROM ruby:3.3.0

# Set working directory
WORKDIR /app

# Copy project file to the working directory
COPY . /app

# Install dependencies
RUN bundle install

# Expose port 4567 to the outside world
EXPOSE 4567

# Command to run the application
# CMD ["bundle", "exec", "rackup", "--host", "0.0.0.0", "-p", "4567"]
CMD ["ruby", "servicio_marce.rb"]
