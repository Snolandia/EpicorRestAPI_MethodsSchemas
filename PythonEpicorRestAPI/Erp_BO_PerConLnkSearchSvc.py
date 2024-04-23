import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PerConLnkSearchSvc
# Description: The PerConLnkSearch BO combines data from PerCon and PerConLnk.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConLnkSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConLnkSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerConLnkSearchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConLnkSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePerConSearch, whereClausePerConLnkSearch, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: This methods will return all of the PerConLnkSearch records which will be a subset
of the PerCon records that meet the selection criteria. This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table (PerConLnkSearch) we need our own public method.
   OperationID: Get_GetRows
      :param whereClausePerConSearch: Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      :param whereClausePerConLnkSearch: Desc: The where clause to restrict data for   Required: True   Allow empty value : True
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
   params += "whereClausePerConSearch=" + whereClausePerConSearch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePerConLnkSearch=" + whereClausePerConLnkSearch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConLnkSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetListExcludeInactive(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetListExcludeInactive
   Description: This methods will return all of the PerConLnkSearch records which will be a subset
of the PerCon records that meet the selection criteria, excluding inactive Customer Contacts,
Supplier Contacts, Workforces and Buyers. This method will try to mirror the functionality
of the base GetRows method but since we are populating
a temp table (PerConLnkSearch) we need our own public method.
   OperationID: Get_GetListExcludeInactive
      :param whereClause: Desc: The where clause to restrict data for.   Required: True   Allow empty value : True
      :param pageSize: Desc: The page size, used only for UI adaptor   Required: True
      :param absolutePage: Desc: The absolute page, used only for the UI adaptor   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListExcludeInactive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
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
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConLnkSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetRowsExcludeInactive(whereClausePerConSearch, whereClausePerConLnkSearch, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsExcludeInactive
   Description: This methods will return all of the PerConLnkSearch records which will be a subset
of the PerCon records that meet the selection criteria, excluding inactive Customer Contacts,
Supplier Contacts, Workforces and Buyers. This method will try to mirror the
functionality of the base GetRows method but since we are populating
a temp table (PerConLnkSearch) we need our own public method.
   OperationID: Get_GetRowsExcludeInactive
      :param whereClausePerConSearch: Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      :param whereClausePerConLnkSearch: Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      :param pageSize: Desc: The page size, used only for UI adapter   Required: True
      :param absolutePage: Desc: The absolute page, used only for the UI adapter   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsExcludeInactive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePerConSearch=" + whereClausePerConSearch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePerConLnkSearch=" + whereClausePerConLnkSearch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConLnkSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: This methods will return all of the PerConLnkSearch records which will be a subset
of the PerCon records that meet the selection criteria. This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table (PerConLnkSearch) we need our own public method.
   OperationID: Get_GetList
      :param whereClause: Desc: The where clause to restrict data for.   Required: True   Allow empty value : True
      :param pageSize: Desc: The page size, used only for UI adaptor   Required: True
      :param absolutePage: Desc: The absolute page, used only for the UI adaptor   Required: True
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
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConLnkSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustom
   Description: This methods will return all of the PerConLnkSearch records which will be a subset
of the PerCon records that meet the selection criteria. This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table (PerConLnkSearch) we need our own public method.
   OperationID: GetRowsCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConLnkSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetRowsPaging(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsPaging
   Description: Method to return PerConLnk rows.  This method supports server paging.
   OperationID: Get_GetRowsPaging
      :param whereClause: Desc: Where clause for data retrieval   Required: True   Allow empty value : True
      :param pageSize: Desc: Page size   Required: True
      :param absolutePage: Desc: Absolute page   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsPaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
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
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConLnkSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConLnkSearchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PerConLnkSearchListRow] = obj["value"]
      pass

class Erp_Tablesets_PerConLnkSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PerConID:int = obj["PerConID"]
      self.ContextLink:str = obj["ContextLink"]
      self.LinkSysRowID:str = obj["LinkSysRowID"]
      self.Name:str = obj["Name"]
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.Zip:str = obj["Zip"]
      self.Country:str = obj["Country"]
      self.CountryNum:int = obj["CountryNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.BuyerID:str = obj["BuyerID"]
      """  Buyer ID from the PurAgent table.  """  
      self.BuyerName:str = obj["BuyerName"]
      """  Name of the buyer.  """  
      self.CustContactName:str = obj["CustContactName"]
      """  Name of the Customer Contact.  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID from Customer table.  """  
      self.CustName:str = obj["CustName"]
      """  Full name of the customer.  """  
      self.EmpID:str = obj["EmpID"]
      self.EmpName:str = obj["EmpName"]
      self.PurPoint:str = obj["PurPoint"]
      self.PurPointName:str = obj["PurPointName"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.VendorContactName:str = obj["VendorContactName"]
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.PREmpID:str = obj["PREmpID"]
      self.PREmpName:str = obj["PREmpName"]
      self.PrimaryContext:bool = obj["PrimaryContext"]
      self.LinkName:str = obj["LinkName"]
      """  Name in the linked record.  """  
      self.FirstName:str = obj["FirstName"]
      self.MiddleName:str = obj["MiddleName"]
      self.LastName:str = obj["LastName"]
      self.Inactive:bool = obj["Inactive"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_PerConLnkSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PerConID:int = obj["PerConID"]
      self.ContextLink:str = obj["ContextLink"]
      self.LinkSysRowID:str = obj["LinkSysRowID"]
      self.Name:str = obj["Name"]
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.Zip:str = obj["Zip"]
      self.Country:str = obj["Country"]
      self.CountryNum:int = obj["CountryNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.BuyerID:str = obj["BuyerID"]
      """  Buyer ID from the PurAgent table.  """  
      self.BuyerName:str = obj["BuyerName"]
      """  Name of the buyer.  """  
      self.CustContactName:str = obj["CustContactName"]
      """  Name of the Customer Contact.  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID from Customer table.  """  
      self.CustName:str = obj["CustName"]
      """  Full name of the customer.  """  
      self.EmpID:str = obj["EmpID"]
      self.EmpName:str = obj["EmpName"]
      self.PurPoint:str = obj["PurPoint"]
      self.PurPointName:str = obj["PurPointName"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.VendorContactName:str = obj["VendorContactName"]
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.PREmpID:str = obj["PREmpID"]
      self.PREmpName:str = obj["PREmpName"]
      self.PrimaryContext:bool = obj["PrimaryContext"]
      self.LinkName:str = obj["LinkName"]
      """  Name in the linked record.  """  
      self.FirstName:str = obj["FirstName"]
      self.MiddleName:str = obj["MiddleName"]
      self.LastName:str = obj["LastName"]
      self.Inactive:bool = obj["Inactive"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerConLnkSearchListTableset:
   def __init__(self, obj):
      self.PerConLnkSearchList:list[Erp_Tablesets_PerConLnkSearchListRow] = obj["PerConLnkSearchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PerConLnkSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PerConID:int = obj["PerConID"]
      self.ContextLink:str = obj["ContextLink"]
      self.LinkSysRowID:str = obj["LinkSysRowID"]
      self.Name:str = obj["Name"]
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.Zip:str = obj["Zip"]
      self.Country:str = obj["Country"]
      self.CountryNum:int = obj["CountryNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.BuyerID:str = obj["BuyerID"]
      """  Buyer ID from the PurAgent table.  """  
      self.BuyerName:str = obj["BuyerName"]
      """  Name of the buyer.  """  
      self.CustContactName:str = obj["CustContactName"]
      """  Name of the Customer Contact.  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID from Customer table.  """  
      self.CustName:str = obj["CustName"]
      """  Full name of the customer.  """  
      self.EmpID:str = obj["EmpID"]
      self.EmpName:str = obj["EmpName"]
      self.PurPoint:str = obj["PurPoint"]
      self.PurPointName:str = obj["PurPointName"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.VendorContactName:str = obj["VendorContactName"]
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.PREmpID:str = obj["PREmpID"]
      self.PREmpName:str = obj["PREmpName"]
      self.PrimaryContext:bool = obj["PrimaryContext"]
      self.LinkName:str = obj["LinkName"]
      """  Name in the linked record.  """  
      self.FirstName:str = obj["FirstName"]
      self.MiddleName:str = obj["MiddleName"]
      self.LastName:str = obj["LastName"]
      self.Inactive:bool = obj["Inactive"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerConLnkSearchTableset:
   def __init__(self, obj):
      self.PerConLnkSearch:list[Erp_Tablesets_PerConLnkSearchRow] = obj["PerConLnkSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetListExcludeInactive_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The where clause to restrict data for.  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetListExcludeInactive_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PerConLnkSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The where clause to restrict data for.  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PerConLnkSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustom_input:
   """ Required : 
   whereClausePerConSearch
   whereClausePerConLnkSearch
   inactives
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePerConSearch:str = obj["whereClausePerConSearch"]
      """  The where clause to restrict data for  """  
      self.whereClausePerConLnkSearch:str = obj["whereClausePerConLnkSearch"]
      """  The where clause to restrict data for  """  
      self.inactives:bool = obj["inactives"]
      """  Include inactive context links  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetRowsCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PerConLnkSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsExcludeInactive_input:
   """ Required : 
   whereClausePerConSearch
   whereClausePerConLnkSearch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePerConSearch:str = obj["whereClausePerConSearch"]
      """  The where clause to restrict data for  """  
      self.whereClausePerConLnkSearch:str = obj["whereClausePerConLnkSearch"]
      """  The where clause to restrict data for  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adapter  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adapter  """  
      pass

class GetRowsExcludeInactive_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PerConLnkSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsPaging_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where clause for data retrieval  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page  """  
      pass

class GetRowsPaging_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PerConLnkSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePerConSearch
   whereClausePerConLnkSearch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePerConSearch:str = obj["whereClausePerConSearch"]
      """  The where clause to restrict data for  """  
      self.whereClausePerConLnkSearch:str = obj["whereClausePerConLnkSearch"]
      """  The where clause to restrict data for  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PerConLnkSearchTableset] = obj["returnObj"]
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

