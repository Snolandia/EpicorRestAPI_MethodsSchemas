import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.BOReaderSvc
# Description: Business Object Data Reader.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(serviceNamespace, whereClause, columnList, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Call GetRows method
   OperationID: Get_GetRows
      :param serviceNamespace: Desc: The fully resolved Service name   Required: True   Allow empty value : True
      :param whereClause: Desc: WhereClause   Required: True   Allow empty value : True
      :param columnList: Desc: List of Columns to return   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "serviceNamespace=" + serviceNamespace
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "columnList=" + columnList

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(serviceNamespace, whereClause, columnList, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Call GetList method
   OperationID: Get_GetList
      :param serviceNamespace: Desc: The fully resolved Service name   Required: True   Allow empty value : True
      :param whereClause: Desc: WhereClause   Required: True   Allow empty value : True
      :param columnList: Desc: List of Columns to return   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "serviceNamespace=" + serviceNamespace
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "columnList=" + columnList

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetCodeDescList(tableName, columnName, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Gets a list of code and description pairs for a column.  First tries to find the list
using the ICE system code and then if not found will try the ERP system code.
   OperationID: Get_GetCodeDescList
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tableName=" + tableName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "columnName=" + columnName

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetCodeDescriptionList(systemCode, tableName, columnName, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescriptionList
   Description: Get a list of code and description pairs for a column.
   OperationID: Get_GetCodeDescriptionList
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescriptionList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "systemCode=" + systemCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tableName=" + tableName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "columnName=" + columnName

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetListWithPaging(serviceNamespace, whereClause, pageSize, columnList, epicorHeaders = None):
   """  
   Summary: Invoke method GetListWithPaging
   Description: Call GetList method
   OperationID: Get_GetListWithPaging
      :param serviceNamespace: Desc: The fully resolved Service name   Required: True   Allow empty value : True
      :param whereClause: Desc: WhereClause   Required: True   Allow empty value : True
   Required: True
      :param columnList: Desc: List of Columns to return   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListWithPaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "serviceNamespace=" + serviceNamespace
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "columnList=" + columnList

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetRowsWithPaging(serviceNamespace, whereClause, pageSize, columnList, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsWithPaging
   Description: Call GetRows method
   OperationID: Get_GetRowsWithPaging
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWithPaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "serviceNamespace=" + serviceNamespace
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "columnList=" + columnList

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetRowsFirstTable(serviceNamespace, whereClause, columnList, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsFirstTable
   Description: Method returns dataset with first data table only
   OperationID: Get_GetRowsFirstTable
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFirstTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "serviceNamespace=" + serviceNamespace
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "columnList=" + columnList

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetRowsFirstTableWithPaging(serviceNamespace, whereClause, pageSize, columnList, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsFirstTableWithPaging
   Description: Method returns dataset with first data table only with paging
   OperationID: Get_GetRowsFirstTableWithPaging
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFirstTableWithPaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "serviceNamespace=" + serviceNamespace
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "columnList=" + columnList

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_InvokeAlternateSearchMethod(serviceNamespace, searchMethod, whereClause, columnList, epicorHeaders = None):
   """  
   Summary: Invoke method InvokeAlternateSearchMethod
   Description: Invoke the Alternate Search Method by method name
   OperationID: Get_InvokeAlternateSearchMethod
      :param serviceNamespace: Desc: The fully resolved Service name   Required: True   Allow empty value : True
      :param searchMethod: Desc: The name of the Alternate Search method   Required: True   Allow empty value : True
      :param whereClause: Desc: WhereClause   Required: True   Allow empty value : True
      :param columnList: Desc: List of Columns to return   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvokeAlternateSearchMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "serviceNamespace=" + serviceNamespace
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "searchMethod=" + searchMethod
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "columnList=" + columnList

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_InvokeAlternateSearchMethodWithPaging(serviceNamespace, searchMethod, whereClause, columnList, pageSize, epicorHeaders = None):
   """  
   Summary: Invoke method InvokeAlternateSearchMethodWithPaging
   Description: Invoke the Alternate Search Method by method name
   OperationID: Get_InvokeAlternateSearchMethodWithPaging
      :param serviceNamespace: Desc: The fully resolved Service name   Required: True   Allow empty value : True
      :param searchMethod: Desc: The name of the Alternate Search method   Required: True   Allow empty value : True
      :param whereClause: Desc: WhereClause   Required: True   Allow empty value : True
      :param columnList: Desc: List of Columns to return   Required: True   Allow empty value : True
      :param pageSize: Desc: Number of records   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvokeAlternateSearchMethodWithPaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "serviceNamespace=" + serviceNamespace
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "searchMethod=" + searchMethod
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "columnList=" + columnList
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_InvokeAlternateSearchMethodWithParams(serviceNamespace, searchMethod, executionParamsJson, columnList, epicorHeaders = None):
   """  
   Summary: Invoke method InvokeAlternateSearchMethodWithParams
   Description: Invoke the Alternate Search Method by method name
   OperationID: Get_InvokeAlternateSearchMethodWithParams
      :param serviceNamespace: Desc: The fully resolved Service name   Required: True   Allow empty value : True
      :param searchMethod: Desc: The name of the Alternate Search method   Required: True   Allow empty value : True
      :param executionParamsJson: Desc: Parameters of alternative search method as json string   Required: True   Allow empty value : True
      :param columnList: Desc: List of Columns to return   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvokeAlternateSearchMethodWithParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "serviceNamespace=" + serviceNamespace
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "searchMethod=" + searchMethod
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "executionParamsJson=" + executionParamsJson
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "columnList=" + columnList

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_InvokeAlternateSearchMethodWithParamsWithPaging(serviceNamespace, searchMethod, executionParamsJson, columnList, pageSize, epicorHeaders = None):
   """  
   Summary: Invoke method InvokeAlternateSearchMethodWithParamsWithPaging
   Description: Invoke the Alternate Search Method by method name
   OperationID: Get_InvokeAlternateSearchMethodWithParamsWithPaging
      :param serviceNamespace: Desc: The fully resolved Service name   Required: True   Allow empty value : True
      :param searchMethod: Desc: The name of the Alternate Search method   Required: True   Allow empty value : True
      :param executionParamsJson: Desc: Parameters of alternative search method as json string   Required: True   Allow empty value : True
      :param columnList: Desc: List of Columns to return   Required: True   Allow empty value : True
      :param pageSize: Desc: Number of records   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvokeAlternateSearchMethodWithParamsWithPaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "serviceNamespace=" + serviceNamespace
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "searchMethod=" + searchMethod
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "executionParamsJson=" + executionParamsJson
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "columnList=" + columnList
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class GetCodeDescList_input:
   """ Required : 
   tableName
   columnName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.columnName:str = obj["columnName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCodeDescriptionList_input:
   """ Required : 
   systemCode
   tableName
   columnName
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.tableName:str = obj["tableName"]
      self.columnName:str = obj["columnName"]
      pass

class GetCodeDescriptionList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetListWithPaging_input:
   """ Required : 
   serviceNamespace
   whereClause
   pageSize
   columnList
   """  
   def __init__(self, obj):
      self.serviceNamespace:str = obj["serviceNamespace"]
      """  The fully resolved Service name  """  
      self.whereClause:str = obj["whereClause"]
      """  WhereClause  """  
      self.pageSize:int = obj["pageSize"]
      self.columnList:str = obj["columnList"]
      """  List of Columns to return  """  
      pass

class GetListWithPaging_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetList_input:
   """ Required : 
   serviceNamespace
   whereClause
   columnList
   """  
   def __init__(self, obj):
      self.serviceNamespace:str = obj["serviceNamespace"]
      """  The fully resolved Service name  """  
      self.whereClause:str = obj["whereClause"]
      """  WhereClause  """  
      self.columnList:str = obj["columnList"]
      """  List of Columns to return  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetRowsFirstTableWithPaging_input:
   """ Required : 
   serviceNamespace
   whereClause
   pageSize
   columnList
   """  
   def __init__(self, obj):
      self.serviceNamespace:str = obj["serviceNamespace"]
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.columnList:str = obj["columnList"]
      pass

class GetRowsFirstTableWithPaging_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetRowsFirstTable_input:
   """ Required : 
   serviceNamespace
   whereClause
   columnList
   """  
   def __init__(self, obj):
      self.serviceNamespace:str = obj["serviceNamespace"]
      self.whereClause:str = obj["whereClause"]
      self.columnList:str = obj["columnList"]
      pass

class GetRowsFirstTable_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetRowsWithPaging_input:
   """ Required : 
   serviceNamespace
   whereClause
   pageSize
   columnList
   """  
   def __init__(self, obj):
      self.serviceNamespace:str = obj["serviceNamespace"]
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.columnList:str = obj["columnList"]
      pass

class GetRowsWithPaging_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetRows_input:
   """ Required : 
   serviceNamespace
   whereClause
   columnList
   """  
   def __init__(self, obj):
      self.serviceNamespace:str = obj["serviceNamespace"]
      """  The fully resolved Service name  """  
      self.whereClause:str = obj["whereClause"]
      """  WhereClause  """  
      self.columnList:str = obj["columnList"]
      """  List of Columns to return  """  
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class InvokeAlternateSearchMethodWithPaging_input:
   """ Required : 
   serviceNamespace
   searchMethod
   whereClause
   columnList
   pageSize
   """  
   def __init__(self, obj):
      self.serviceNamespace:str = obj["serviceNamespace"]
      """  The fully resolved Service name  """  
      self.searchMethod:str = obj["searchMethod"]
      """  The name of the Alternate Search method  """  
      self.whereClause:str = obj["whereClause"]
      """  WhereClause  """  
      self.columnList:str = obj["columnList"]
      """  List of Columns to return  """  
      self.pageSize:int = obj["pageSize"]
      """  Number of records  """  
      pass

class InvokeAlternateSearchMethodWithPaging_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  The results of the Alternate Search method  """  
      pass

class InvokeAlternateSearchMethodWithParamsWithPaging_input:
   """ Required : 
   serviceNamespace
   searchMethod
   executionParamsJson
   columnList
   pageSize
   """  
   def __init__(self, obj):
      self.serviceNamespace:str = obj["serviceNamespace"]
      """  The fully resolved Service name  """  
      self.searchMethod:str = obj["searchMethod"]
      """  The name of the Alternate Search method  """  
      self.executionParamsJson:str = obj["executionParamsJson"]
      """  Parameters of alternative search method as json string  """  
      self.columnList:str = obj["columnList"]
      """  List of Columns to return  """  
      self.pageSize:int = obj["pageSize"]
      """  Number of records  """  
      pass

class InvokeAlternateSearchMethodWithParamsWithPaging_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  The results of the Alternate Search method  """  
      pass

class InvokeAlternateSearchMethodWithParams_input:
   """ Required : 
   serviceNamespace
   searchMethod
   executionParamsJson
   columnList
   """  
   def __init__(self, obj):
      self.serviceNamespace:str = obj["serviceNamespace"]
      """  The fully resolved Service name  """  
      self.searchMethod:str = obj["searchMethod"]
      """  The name of the Alternate Search method  """  
      self.executionParamsJson:str = obj["executionParamsJson"]
      """  Parameters of alternative search method as json string  """  
      self.columnList:str = obj["columnList"]
      """  List of Columns to return  """  
      pass

class InvokeAlternateSearchMethodWithParams_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  The results of the Alternate Search method  """  
      pass

class InvokeAlternateSearchMethod_input:
   """ Required : 
   serviceNamespace
   searchMethod
   whereClause
   columnList
   """  
   def __init__(self, obj):
      self.serviceNamespace:str = obj["serviceNamespace"]
      """  The fully resolved Service name  """  
      self.searchMethod:str = obj["searchMethod"]
      """  The name of the Alternate Search method  """  
      self.whereClause:str = obj["whereClause"]
      """  WhereClause  """  
      self.columnList:str = obj["columnList"]
      """  List of Columns to return  """  
      pass

class InvokeAlternateSearchMethod_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  The results of the Alternate Search method  """  
      pass

