import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ECCCustomerSvc
# Description: ECC Customer/Consumer main object
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECCCustomerSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECCCustomerSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ECCCustomerPortal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ECCCustomerPortal
   Description: Main portal for all customer/consumer connect processing
   OperationID: ECCCustomerPortal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ECCCustomerPortal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ECCCustomerPortal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECCCustomerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConfigurationChangePart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConfigurationChangePart
   Description: When a configurator part number becomes a standard part this method will pull in the pricing for that part similar to functionality in Sales Order and Quote
   OperationID: ConfigurationChangePart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfigurationChangePart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfigurationChangePart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECCCustomerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ConfigurationChangePart_input:
   """ Required : 
   guid
   """  
   def __init__(self, obj):
      self.guid:str = obj["guid"]
      pass

class ConfigurationChangePart_output:
   def __init__(self, obj):
      pass

class ECCCustomerPortal_input:
   """ Required : 
   requestMsg
   """  
   def __init__(self, obj):
      self.requestMsg:list[System_Xml_Linq_XElement] = obj["requestMsg"]
      pass

class ECCCustomerPortal_output:
   def __init__(self, obj):
      self.returnObj:list[System_Xml_Linq_XElement] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.requestMsg:list[System_Xml_Linq_XElement] = obj["requestMsg"]
      pass

      """  output parameters  """  

class System_Xml_Linq_XAttribute:
   def __init__(self, obj):
      self.IsNamespaceDeclaration:bool = obj["IsNamespaceDeclaration"]
      self.Name:list[System_Xml_Linq_XName] = obj["Name"]
      self.NextAttribute:list[System_Xml_Linq_XAttribute] = obj["NextAttribute"]
      self.NodeType:int = obj["NodeType"]
      self.PreviousAttribute:list[System_Xml_Linq_XAttribute] = obj["PreviousAttribute"]
      self.Value:str = obj["Value"]
      self.BaseUri:str = obj["BaseUri"]
      self.Document:list[System_Xml_Linq_XDocument] = obj["Document"]
      self.Parent:list[System_Xml_Linq_XElement] = obj["Parent"]
      pass

class System_Xml_Linq_XDeclaration:
   def __init__(self, obj):
      self.Encoding:str = obj["Encoding"]
      self.Standalone:str = obj["Standalone"]
      self.Version:str = obj["Version"]
      pass

class System_Xml_Linq_XDocument:
   def __init__(self, obj):
      self.Declaration:list[System_Xml_Linq_XDeclaration] = obj["Declaration"]
      self.DocumentType:list[System_Xml_Linq_XDocumentType] = obj["DocumentType"]
      self.NodeType:int = obj["NodeType"]
      self.Root:list[System_Xml_Linq_XElement] = obj["Root"]
      self.FirstNode:list[System_Xml_Linq_XNode] = obj["FirstNode"]
      self.LastNode:list[System_Xml_Linq_XNode] = obj["LastNode"]
      self.NextNode:list[System_Xml_Linq_XNode] = obj["NextNode"]
      self.PreviousNode:list[System_Xml_Linq_XNode] = obj["PreviousNode"]
      self.BaseUri:str = obj["BaseUri"]
      self.Document:list[System_Xml_Linq_XDocument] = obj["Document"]
      self.Parent:list[System_Xml_Linq_XElement] = obj["Parent"]
      pass

class System_Xml_Linq_XDocumentType:
   def __init__(self, obj):
      self.InternalSubset:str = obj["InternalSubset"]
      self.Name:str = obj["Name"]
      self.NodeType:int = obj["NodeType"]
      self.PublicId:str = obj["PublicId"]
      self.SystemId:str = obj["SystemId"]
      self.NextNode:list[System_Xml_Linq_XNode] = obj["NextNode"]
      self.PreviousNode:list[System_Xml_Linq_XNode] = obj["PreviousNode"]
      self.BaseUri:str = obj["BaseUri"]
      self.Document:list[System_Xml_Linq_XDocument] = obj["Document"]
      self.Parent:list[System_Xml_Linq_XElement] = obj["Parent"]
      pass

class System_Xml_Linq_XElement:
   def __init__(self, obj):
      self.FirstAttribute:list[System_Xml_Linq_XAttribute] = obj["FirstAttribute"]
      self.HasAttributes:bool = obj["HasAttributes"]
      self.HasElements:bool = obj["HasElements"]
      self.IsEmpty:bool = obj["IsEmpty"]
      self.LastAttribute:list[System_Xml_Linq_XAttribute] = obj["LastAttribute"]
      self.Name:list[System_Xml_Linq_XName] = obj["Name"]
      self.NodeType:int = obj["NodeType"]
      self.Value:str = obj["Value"]
      self.FirstNode:list[System_Xml_Linq_XNode] = obj["FirstNode"]
      self.LastNode:list[System_Xml_Linq_XNode] = obj["LastNode"]
      self.NextNode:list[System_Xml_Linq_XNode] = obj["NextNode"]
      self.PreviousNode:list[System_Xml_Linq_XNode] = obj["PreviousNode"]
      self.BaseUri:str = obj["BaseUri"]
      self.Document:list[System_Xml_Linq_XDocument] = obj["Document"]
      self.Parent:list[System_Xml_Linq_XElement] = obj["Parent"]
      pass

class System_Xml_Linq_XName:
   def __init__(self, obj):
      self.LocalName:str = obj["LocalName"]
      self.Namespace:list[System_Xml_Linq_XNamespace] = obj["Namespace"]
      self.NamespaceName:str = obj["NamespaceName"]
      pass

class System_Xml_Linq_XNamespace:
   def __init__(self, obj):
      self.NamespaceName:str = obj["NamespaceName"]
      pass

class System_Xml_Linq_XNode:
   def __init__(self, obj):
      self.NextNode:list[System_Xml_Linq_XNode] = obj["NextNode"]
      self.PreviousNode:list[System_Xml_Linq_XNode] = obj["PreviousNode"]
      self.BaseUri:str = obj["BaseUri"]
      self.Document:list[System_Xml_Linq_XDocument] = obj["Document"]
      self.NodeType:int = obj["NodeType"]
      self.Parent:list[System_Xml_Linq_XElement] = obj["Parent"]
      pass

