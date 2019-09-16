
# 문자열 보간(String Interpolation) 
message = "String Interpolation";

print("Message: " + message)
print(f"Message: {message}") # 권장 방식 
print("Message: %s" %(message))

# 오래된 방식
print("Message: {} - {}".format(message, message))
print("Message: {0} - {1}".format(message, message))
