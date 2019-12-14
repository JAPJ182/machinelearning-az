# Plantilla para el Pre Procesado de Datos - Datos Categóricos



# Importar el dataset
dataset = read.csv('Data.csv', stringsAsFactors = F)

str(dataset)
# Codificar las variables categóricas
dataset$Country = factor(dataset$Country,
                         levels = c("France", "Spain", "Germany"),
                         labels = c(1, 2, 3))

dataset$Purchased = factor(dataset$Purchased,
                           levels = c("No", "Yes"),
                           labels = c(0,1))
str(dataset)

##Mine
  table(is.na(data))
  
  #1
data$Age <- ifelse(is.na(data$Age),
                   ave(data$Age, FUN = function(x) mean(x, na.rm = T)),
                   data$Age)
#2
data <- ifelse(is.na(data),preProcess(data, method = c("knnImpute")), data )    
data <- tibble(data)
#3
data$Age <- ifelse(is.na(data$Age),
                   ave(data$Age, FUN = function(x) mean(x, na.rm = T)),
                   data$Age)


