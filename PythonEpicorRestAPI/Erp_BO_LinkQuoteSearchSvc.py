import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.LinkQuoteSearchSvc
# Description: This bo will create a temp table of records used to select
"linked quotes" for the Get Details.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LinkQuoteSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LinkQuoteSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseJobProd, whereClauseOrderDtl, whereClauseQuoteDtl, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: This methods will return all of the LinkQuoteSearch records which will be a subset
of the 'for each jobprod, each orderdtl of jobprod, each quotedtl of orderdtl'
records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table (LinkQuoteSearch) we need our own public method.
   OperationID: Get_GetRows
      :param whereClauseJobProd: Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      :param whereClauseOrderDtl: Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      :param whereClauseQuoteDtl: Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      :param pageSize: Desc: The page size, used only for UI adaptor   Required: True
      :param absolutePage: Desc: The absolute page, used only for the UI adaptor   Required: True
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
   params += "whereClauseJobProd=" + whereClauseJobProd
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseOrderDtl=" + whereClauseOrderDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteDtl=" + whereClauseQuoteDtl
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
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LinkQuoteSearchSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_LinkQuoteSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.JobNum:str = obj["JobNum"]
      """  The job number.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The order number.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The order line number.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  The quote number.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The quote line.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  The line description.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  The customer part number.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  The customer revision number.  """  
      self.MfgDetail:bool = obj["MfgDetail"]
      """  Do manufacturing details exist?  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LinkQuoteSearchTableset:
   def __init__(self, obj):
      self.LinkQuoteSearch:list[Erp_Tablesets_LinkQuoteSearchRow] = obj["LinkQuoteSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseJobProd
   whereClauseOrderDtl
   whereClauseQuoteDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseJobProd:str = obj["whereClauseJobProd"]
      """  The where clause to restrict data for  """  
      self.whereClauseOrderDtl:str = obj["whereClauseOrderDtl"]
      """  The where clause to restrict data for  """  
      self.whereClauseQuoteDtl:str = obj["whereClauseQuoteDtl"]
      """  The where clause to restrict data for  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LinkQuoteSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

