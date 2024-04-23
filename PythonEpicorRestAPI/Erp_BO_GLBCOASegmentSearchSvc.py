import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GLBCOASegmentSearchSvc
# Description: shell object for searching the Global segments
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GLBCOASegmentSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLBCOASegmentSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBCOASegmentSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOASegmentSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/GLBCOASegmentSearches",headers=creds) as resp:
           return await resp.json()

async def post_GLBCOASegmentSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBCOASegmentSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBCOASegmentSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBCOASegmentSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/GLBCOASegmentSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLBCOASegmentSearches_Company_ExtCompanyID_COACode_SegmentNbr(Company, ExtCompanyID, COACode, SegmentNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBCOASegmentSearch item
   Description: Calls GetByID to retrieve the GLBCOASegmentSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBCOASegmentSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBCOASegmentSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/GLBCOASegmentSearches(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLBCOASegmentSearches_Company_ExtCompanyID_COACode_SegmentNbr(Company, ExtCompanyID, COACode, SegmentNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLBCOASegmentSearch for the service
   Description: Calls UpdateExt to update GLBCOASegmentSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBCOASegmentSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBCOASegmentSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/GLBCOASegmentSearches(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLBCOASegmentSearches_Company_ExtCompanyID_COACode_SegmentNbr(Company, ExtCompanyID, COACode, SegmentNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLBCOASegmentSearch item
   Description: Call UpdateExt to delete GLBCOASegmentSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBCOASegmentSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/GLBCOASegmentSearches(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOASegmentSearchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGLBCOASegmentSearch, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
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
   params += "whereClauseGLBCOASegmentSearch=" + whereClauseGLBCOASegmentSearch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(extCompanyID, coACode, segmentNbr, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "extCompanyID=" + extCompanyID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "coACode=" + coACode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "segmentNbr=" + segmentNbr

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLBCOASegmentSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLBCOASegmentSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBCOASegmentSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBCOASegmentSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBCOASegmentSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegmentSearchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBCOASegmentSearchListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegmentSearchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBCOASegmentSearchRow] = obj["value"]
      pass

class Erp_Tablesets_GLBCOASegmentSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Company ID of the external company this COA was imported from.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment  """  
      self.Abbreviation:str = obj["Abbreviation"]
      """  Short name of segment.  """  
      self.MaxLength:int = obj["MaxLength"]
      """  Maximum length of the code used for this segment.  Valid values are between 1 and 50.  This value must be at least the value of the minimum length.  The minimum length is the default value.  If a segment is tied to a reference entity the maximum length cannot be less then the length of the reference entity's field.  """  
      self.MinLength:int = obj["MinLength"]
      """  Minimum length of the code to be used for this segment.  Must be a value between 1 and the maximum length.  If the segment is tied to a reference entity the minimum length cannot be greater than the length of the reference entity field.  """  
      self.Dynamic:bool = obj["Dynamic"]
      """  Indicates if accounts with this segment can be created on the fly when posting transactions.  If Yes, the GLAccount table does not have to contain entries with this field populated.  If No, then all valid combinations of segment values (COASegVal) must be defined in the GLAccount table before the account can be used.  """  
      self.UseRefEntity:bool = obj["UseRefEntity"]
      """  Indicates if this segment is related to another business entity.  This is only available if the Dynamic field equals Yes.  """  
      self.RefEntity:str = obj["RefEntity"]
      """  This is the reference entity where the COASegVals are generated from.  Valid values are found in the BusEntities table.  This option is NOT valid for the natural account (segment number 1)  """  
      self.AllowAlpha:bool = obj["AllowAlpha"]
      """  Indicates if alpha characters are allowed in the code.   The default value is yes.  If UseRefEntity equals yes then this field must equal yes.  If no, then only  numeric characters are allowed as segment values.  """  
      self.EntryControl:str = obj["EntryControl"]
      """  Indicates what causes the entry of segment values for this segment.  Valid values are: 0 (zero): Mandatory - the segment is always entered.  1 (one) Natrual account - The option on the natural account determines if this segment is mandatory, optional or not used.  This value is found on the COASegValOpt table.  """  
      self.SegSelfBal:bool = obj["SegSelfBal"]
      """  Indicates if journal entries are automatically balanced.  """  
      self.Level:int = obj["Level"]
      """  The level indicates the order segments will be balanced in case multiple segments are defined as self balancing.  This field can only be updated when SegSelfBal equals yes.  Two self balancing segments cannot have the same level.  Valid values are 1 thorugh the number of segments defined for the COA.  """  
      self.SummaryBal:bool = obj["SummaryBal"]
      """  Indicates if this segment is included in the standard trial balance account.  """  
      self.DetailBal:bool = obj["DetailBal"]
      """  Indicates if balance records are maintained by the system for this segment.  If Yes, this segment is used as part of the GL Account for balance purposes.  """  
      self.KeepOpenBal:bool = obj["KeepOpenBal"]
      """  Indicates if opening balances are kept for expense and revenue accounts.  This is typically used for pjrect accounting where you want to keep the project date balance independent of the financial year.  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  Indicates the order in which this segment is displayed when presenting the GL Account to the user.  Valid values are 1 through 20.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Indicates if this segment is subject to Multi-Company GL Journal processing.  If the COA is marked as MultipCompnay then all controlled segments are flagged as multi-company and this cannot be overwritten by the user.  """  
      self.AutoCreateSegVals:bool = obj["AutoCreateSegVals"]
      """  Indicates if segment values for segments defined as reference entities are to be created each time a newrecord is created.  Only valid if UseRefEntity equals yes and a reference entity is entered.  """  
      self.SelfBalAcct:str = obj["SelfBalAcct"]
      """  Account used  when creating balancing transactions for this segment.  """  
      self.BalSegValue1:str = obj["BalSegValue1"]
      """  Balance Seg Value 1  """  
      self.BalSegValue2:str = obj["BalSegValue2"]
      """  Balance Seg Value 2  """  
      self.BalSegValue3:str = obj["BalSegValue3"]
      """  Balance Seg Value 3  """  
      self.BalSegValue4:str = obj["BalSegValue4"]
      """  Balance Seg Value 4  """  
      self.BalSegValue5:str = obj["BalSegValue5"]
      """  Balance Seg Value 5  """  
      self.BalSegValue6:str = obj["BalSegValue6"]
      """  Balance Seg Value 6  """  
      self.BalSegValue7:str = obj["BalSegValue7"]
      """  Balance Seg Value 7  """  
      self.BalSegValue8:str = obj["BalSegValue8"]
      """  Balance Seg Value 8  """  
      self.BalSegValue9:str = obj["BalSegValue9"]
      """  Balance Seg Value 9  """  
      self.BalSegValue10:str = obj["BalSegValue10"]
      """  Balance Seg Value 10  """  
      self.BalSegValue11:str = obj["BalSegValue11"]
      """  Balance Seg Value 11  """  
      self.BalSegValue12:str = obj["BalSegValue12"]
      """  Balance Seg Value 12  """  
      self.BalSegValue13:str = obj["BalSegValue13"]
      """  Balance Seg Value 13  """  
      self.BalSegValue14:str = obj["BalSegValue14"]
      """  Balance Seg Value 14  """  
      self.BalSegValue15:str = obj["BalSegValue15"]
      """  Balance Seg Value 15  """  
      self.BalSegValue16:str = obj["BalSegValue16"]
      """  Balance Seg Value 16  """  
      self.BalSegValue17:str = obj["BalSegValue17"]
      """  Balance Seg Value 17  """  
      self.BalSegValue18:str = obj["BalSegValue18"]
      """  Balance Seg Value 18  """  
      self.BalSegValue19:str = obj["BalSegValue19"]
      """  Balance Seg Value 19  """  
      self.BalSegValue20:str = obj["BalSegValue20"]
      """  Balance Seg Value 20  """  
      self.SelfOffAcct:str = obj["SelfOffAcct"]
      """  The Self Balance offset account used when balancing this segment.  """  
      self.OffSegValue1:str = obj["OffSegValue1"]
      """  Offset Segment Value 1  """  
      self.OffSegValue2:str = obj["OffSegValue2"]
      """  Offset Segment Value 2  """  
      self.OffSegValue3:str = obj["OffSegValue3"]
      """  Offset Segment Value 3  """  
      self.OffSegValue4:str = obj["OffSegValue4"]
      """  Offset Segment Value 4  """  
      self.OffSegValue5:str = obj["OffSegValue5"]
      """  Offset Segment Value 5  """  
      self.OffSegValue6:str = obj["OffSegValue6"]
      """  Offset Segment Value 6  """  
      self.OffSegValue7:str = obj["OffSegValue7"]
      """  Offset Segment Value 7  """  
      self.OffSegValue8:str = obj["OffSegValue8"]
      """  Offset Segment Value 8  """  
      self.OffSegValue9:str = obj["OffSegValue9"]
      """  Offset Segment Value 9  """  
      self.OffSegValue10:str = obj["OffSegValue10"]
      """  Offset Segment Value 10  """  
      self.OffSegValue11:str = obj["OffSegValue11"]
      """  Offset Segment Value 11  """  
      self.OffSegValue12:str = obj["OffSegValue12"]
      """  Offset Segment Value 12  """  
      self.OffSegValue13:str = obj["OffSegValue13"]
      """  Offset Segment Value 13  """  
      self.OffSegValue14:str = obj["OffSegValue14"]
      """  Offset Segment Value 14  """  
      self.OffSegValue15:str = obj["OffSegValue15"]
      """  Offset Segment Value 15  """  
      self.OffSegValue16:str = obj["OffSegValue16"]
      """  Offset Segment Value 16  """  
      self.OffSegValue17:str = obj["OffSegValue17"]
      """  Offset Segment Value 17  """  
      self.OffSegValue18:str = obj["OffSegValue18"]
      """  Offset Segment Value 18  """  
      self.OffSegValue19:str = obj["OffSegValue19"]
      """  Offset Segment Value 19  """  
      self.OffSegValue20:str = obj["OffSegValue20"]
      """  Offset Segment Value 20  """  
      self.ReverseCategoryID:str = obj["ReverseCategoryID"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBCOASegmentSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Company ID of the external company this COA was imported from.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment  """  
      self.Abbreviation:str = obj["Abbreviation"]
      """  Short name of segment.  """  
      self.MaxLength:int = obj["MaxLength"]
      """  Maximum length of the code used for this segment.  Valid values are between 1 and 50.  This value must be at least the value of the minimum length.  The minimum length is the default value.  If a segment is tied to a reference entity the maximum length cannot be less then the length of the reference entity's field.  """  
      self.MinLength:int = obj["MinLength"]
      """  Minimum length of the code to be used for this segment.  Must be a value between 1 and the maximum length.  If the segment is tied to a reference entity the minimum length cannot be greater than the length of the reference entity field.  """  
      self.Dynamic:bool = obj["Dynamic"]
      """  Indicates if accounts with this segment can be created on the fly when posting transactions.  If Yes, the GLAccount table does not have to contain entries with this field populated.  If No, then all valid combinations of segment values (COASegVal) must be defined in the GLAccount table before the account can be used.  """  
      self.UseRefEntity:bool = obj["UseRefEntity"]
      """  Indicates if this segment is related to another business entity.  This is only available if the Dynamic field equals Yes.  """  
      self.RefEntity:str = obj["RefEntity"]
      """  This is the reference entity where the COASegVals are generated from.  Valid values are found in the BusEntities table.  This option is NOT valid for the natural account (segment number 1)  """  
      self.AllowAlpha:bool = obj["AllowAlpha"]
      """  Indicates if alpha characters are allowed in the code.   The default value is yes.  If UseRefEntity equals yes then this field must equal yes.  If no, then only  numeric characters are allowed as segment values.  """  
      self.EntryControl:str = obj["EntryControl"]
      """  Indicates what causes the entry of segment values for this segment.  Valid values are: 0 (zero): Mandatory - the segment is always entered.  1 (one) Natrual account - The option on the natural account determines if this segment is mandatory, optional or not used.  This value is found on the COASegValOpt table.  """  
      self.SegSelfBal:bool = obj["SegSelfBal"]
      """  Indicates if journal entries are automatically balanced.  """  
      self.Level:int = obj["Level"]
      """  The level indicates the order segments will be balanced in case multiple segments are defined as self balancing.  This field can only be updated when SegSelfBal equals yes.  Two self balancing segments cannot have the same level.  Valid values are 1 thorugh the number of segments defined for the COA.  """  
      self.SummaryBal:bool = obj["SummaryBal"]
      """  Indicates if this segment is included in the standard trial balance account.  """  
      self.DetailBal:bool = obj["DetailBal"]
      """  Indicates if balance records are maintained by the system for this segment.  If Yes, this segment is used as part of the GL Account for balance purposes.  """  
      self.KeepOpenBal:bool = obj["KeepOpenBal"]
      """  Indicates if opening balances are kept for expense and revenue accounts.  This is typically used for pjrect accounting where you want to keep the project date balance independent of the financial year.  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  Indicates the order in which this segment is displayed when presenting the GL Account to the user.  Valid values are 1 through 20.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Indicates if this segment is subject to Multi-Company GL Journal processing.  If the COA is marked as MultipCompnay then all controlled segments are flagged as multi-company and this cannot be overwritten by the user.  """  
      self.AutoCreateSegVals:bool = obj["AutoCreateSegVals"]
      """  Indicates if segment values for segments defined as reference entities are to be created each time a newrecord is created.  Only valid if UseRefEntity equals yes and a reference entity is entered.  """  
      self.SelfBalAcct:str = obj["SelfBalAcct"]
      """  Account used  when creating balancing transactions for this segment.  """  
      self.BalSegValue1:str = obj["BalSegValue1"]
      """  Balance Seg Value 1  """  
      self.BalSegValue2:str = obj["BalSegValue2"]
      """  Balance Seg Value 2  """  
      self.BalSegValue3:str = obj["BalSegValue3"]
      """  Balance Seg Value 3  """  
      self.BalSegValue4:str = obj["BalSegValue4"]
      """  Balance Seg Value 4  """  
      self.BalSegValue5:str = obj["BalSegValue5"]
      """  Balance Seg Value 5  """  
      self.BalSegValue6:str = obj["BalSegValue6"]
      """  Balance Seg Value 6  """  
      self.BalSegValue7:str = obj["BalSegValue7"]
      """  Balance Seg Value 7  """  
      self.BalSegValue8:str = obj["BalSegValue8"]
      """  Balance Seg Value 8  """  
      self.BalSegValue9:str = obj["BalSegValue9"]
      """  Balance Seg Value 9  """  
      self.BalSegValue10:str = obj["BalSegValue10"]
      """  Balance Seg Value 10  """  
      self.BalSegValue11:str = obj["BalSegValue11"]
      """  Balance Seg Value 11  """  
      self.BalSegValue12:str = obj["BalSegValue12"]
      """  Balance Seg Value 12  """  
      self.BalSegValue13:str = obj["BalSegValue13"]
      """  Balance Seg Value 13  """  
      self.BalSegValue14:str = obj["BalSegValue14"]
      """  Balance Seg Value 14  """  
      self.BalSegValue15:str = obj["BalSegValue15"]
      """  Balance Seg Value 15  """  
      self.BalSegValue16:str = obj["BalSegValue16"]
      """  Balance Seg Value 16  """  
      self.BalSegValue17:str = obj["BalSegValue17"]
      """  Balance Seg Value 17  """  
      self.BalSegValue18:str = obj["BalSegValue18"]
      """  Balance Seg Value 18  """  
      self.BalSegValue19:str = obj["BalSegValue19"]
      """  Balance Seg Value 19  """  
      self.BalSegValue20:str = obj["BalSegValue20"]
      """  Balance Seg Value 20  """  
      self.SelfOffAcct:str = obj["SelfOffAcct"]
      """  The Self Balance offset account used when balancing this segment.  """  
      self.OffSegValue1:str = obj["OffSegValue1"]
      """  Offset Segment Value 1  """  
      self.OffSegValue2:str = obj["OffSegValue2"]
      """  Offset Segment Value 2  """  
      self.OffSegValue3:str = obj["OffSegValue3"]
      """  Offset Segment Value 3  """  
      self.OffSegValue4:str = obj["OffSegValue4"]
      """  Offset Segment Value 4  """  
      self.OffSegValue5:str = obj["OffSegValue5"]
      """  Offset Segment Value 5  """  
      self.OffSegValue6:str = obj["OffSegValue6"]
      """  Offset Segment Value 6  """  
      self.OffSegValue7:str = obj["OffSegValue7"]
      """  Offset Segment Value 7  """  
      self.OffSegValue8:str = obj["OffSegValue8"]
      """  Offset Segment Value 8  """  
      self.OffSegValue9:str = obj["OffSegValue9"]
      """  Offset Segment Value 9  """  
      self.OffSegValue10:str = obj["OffSegValue10"]
      """  Offset Segment Value 10  """  
      self.OffSegValue11:str = obj["OffSegValue11"]
      """  Offset Segment Value 11  """  
      self.OffSegValue12:str = obj["OffSegValue12"]
      """  Offset Segment Value 12  """  
      self.OffSegValue13:str = obj["OffSegValue13"]
      """  Offset Segment Value 13  """  
      self.OffSegValue14:str = obj["OffSegValue14"]
      """  Offset Segment Value 14  """  
      self.OffSegValue15:str = obj["OffSegValue15"]
      """  Offset Segment Value 15  """  
      self.OffSegValue16:str = obj["OffSegValue16"]
      """  Offset Segment Value 16  """  
      self.OffSegValue17:str = obj["OffSegValue17"]
      """  Offset Segment Value 17  """  
      self.OffSegValue18:str = obj["OffSegValue18"]
      """  Offset Segment Value 18  """  
      self.OffSegValue19:str = obj["OffSegValue19"]
      """  Offset Segment Value 19  """  
      self.OffSegValue20:str = obj["OffSegValue20"]
      """  Offset Segment Value 20  """  
      self.ReverseCategoryID:str = obj["ReverseCategoryID"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CNIsCFICode:bool = obj["CNIsCFICode"]
      """  CNIsCFICode  """  
      self.SegValueField:str = obj["SegValueField"]
      """  SegValueField  """  
      self.DescFieldName:str = obj["DescFieldName"]
      """  DescFieldName  """  
      self.GlobalCOASegment:bool = obj["GlobalCOASegment"]
      """  GlobalCOASegment  """  
      self.GlobalCOASegmentValues:bool = obj["GlobalCOASegmentValues"]
      """  GlobalCOASegmentValues  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.GlobalValuesLock:bool = obj["GlobalValuesLock"]
      """  GlobalValuesLock  """  
      self.SiteSegment:bool = obj["SiteSegment"]
      """  SiteSegment  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   extCompanyID
   coACode
   segmentNbr
   """  
   def __init__(self, obj):
      self.extCompanyID:str = obj["extCompanyID"]
      self.coACode:str = obj["coACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GLBCOASegmentSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Company ID of the external company this COA was imported from.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment  """  
      self.Abbreviation:str = obj["Abbreviation"]
      """  Short name of segment.  """  
      self.MaxLength:int = obj["MaxLength"]
      """  Maximum length of the code used for this segment.  Valid values are between 1 and 50.  This value must be at least the value of the minimum length.  The minimum length is the default value.  If a segment is tied to a reference entity the maximum length cannot be less then the length of the reference entity's field.  """  
      self.MinLength:int = obj["MinLength"]
      """  Minimum length of the code to be used for this segment.  Must be a value between 1 and the maximum length.  If the segment is tied to a reference entity the minimum length cannot be greater than the length of the reference entity field.  """  
      self.Dynamic:bool = obj["Dynamic"]
      """  Indicates if accounts with this segment can be created on the fly when posting transactions.  If Yes, the GLAccount table does not have to contain entries with this field populated.  If No, then all valid combinations of segment values (COASegVal) must be defined in the GLAccount table before the account can be used.  """  
      self.UseRefEntity:bool = obj["UseRefEntity"]
      """  Indicates if this segment is related to another business entity.  This is only available if the Dynamic field equals Yes.  """  
      self.RefEntity:str = obj["RefEntity"]
      """  This is the reference entity where the COASegVals are generated from.  Valid values are found in the BusEntities table.  This option is NOT valid for the natural account (segment number 1)  """  
      self.AllowAlpha:bool = obj["AllowAlpha"]
      """  Indicates if alpha characters are allowed in the code.   The default value is yes.  If UseRefEntity equals yes then this field must equal yes.  If no, then only  numeric characters are allowed as segment values.  """  
      self.EntryControl:str = obj["EntryControl"]
      """  Indicates what causes the entry of segment values for this segment.  Valid values are: 0 (zero): Mandatory - the segment is always entered.  1 (one) Natrual account - The option on the natural account determines if this segment is mandatory, optional or not used.  This value is found on the COASegValOpt table.  """  
      self.SegSelfBal:bool = obj["SegSelfBal"]
      """  Indicates if journal entries are automatically balanced.  """  
      self.Level:int = obj["Level"]
      """  The level indicates the order segments will be balanced in case multiple segments are defined as self balancing.  This field can only be updated when SegSelfBal equals yes.  Two self balancing segments cannot have the same level.  Valid values are 1 thorugh the number of segments defined for the COA.  """  
      self.SummaryBal:bool = obj["SummaryBal"]
      """  Indicates if this segment is included in the standard trial balance account.  """  
      self.DetailBal:bool = obj["DetailBal"]
      """  Indicates if balance records are maintained by the system for this segment.  If Yes, this segment is used as part of the GL Account for balance purposes.  """  
      self.KeepOpenBal:bool = obj["KeepOpenBal"]
      """  Indicates if opening balances are kept for expense and revenue accounts.  This is typically used for pjrect accounting where you want to keep the project date balance independent of the financial year.  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  Indicates the order in which this segment is displayed when presenting the GL Account to the user.  Valid values are 1 through 20.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Indicates if this segment is subject to Multi-Company GL Journal processing.  If the COA is marked as MultipCompnay then all controlled segments are flagged as multi-company and this cannot be overwritten by the user.  """  
      self.AutoCreateSegVals:bool = obj["AutoCreateSegVals"]
      """  Indicates if segment values for segments defined as reference entities are to be created each time a newrecord is created.  Only valid if UseRefEntity equals yes and a reference entity is entered.  """  
      self.SelfBalAcct:str = obj["SelfBalAcct"]
      """  Account used  when creating balancing transactions for this segment.  """  
      self.BalSegValue1:str = obj["BalSegValue1"]
      """  Balance Seg Value 1  """  
      self.BalSegValue2:str = obj["BalSegValue2"]
      """  Balance Seg Value 2  """  
      self.BalSegValue3:str = obj["BalSegValue3"]
      """  Balance Seg Value 3  """  
      self.BalSegValue4:str = obj["BalSegValue4"]
      """  Balance Seg Value 4  """  
      self.BalSegValue5:str = obj["BalSegValue5"]
      """  Balance Seg Value 5  """  
      self.BalSegValue6:str = obj["BalSegValue6"]
      """  Balance Seg Value 6  """  
      self.BalSegValue7:str = obj["BalSegValue7"]
      """  Balance Seg Value 7  """  
      self.BalSegValue8:str = obj["BalSegValue8"]
      """  Balance Seg Value 8  """  
      self.BalSegValue9:str = obj["BalSegValue9"]
      """  Balance Seg Value 9  """  
      self.BalSegValue10:str = obj["BalSegValue10"]
      """  Balance Seg Value 10  """  
      self.BalSegValue11:str = obj["BalSegValue11"]
      """  Balance Seg Value 11  """  
      self.BalSegValue12:str = obj["BalSegValue12"]
      """  Balance Seg Value 12  """  
      self.BalSegValue13:str = obj["BalSegValue13"]
      """  Balance Seg Value 13  """  
      self.BalSegValue14:str = obj["BalSegValue14"]
      """  Balance Seg Value 14  """  
      self.BalSegValue15:str = obj["BalSegValue15"]
      """  Balance Seg Value 15  """  
      self.BalSegValue16:str = obj["BalSegValue16"]
      """  Balance Seg Value 16  """  
      self.BalSegValue17:str = obj["BalSegValue17"]
      """  Balance Seg Value 17  """  
      self.BalSegValue18:str = obj["BalSegValue18"]
      """  Balance Seg Value 18  """  
      self.BalSegValue19:str = obj["BalSegValue19"]
      """  Balance Seg Value 19  """  
      self.BalSegValue20:str = obj["BalSegValue20"]
      """  Balance Seg Value 20  """  
      self.SelfOffAcct:str = obj["SelfOffAcct"]
      """  The Self Balance offset account used when balancing this segment.  """  
      self.OffSegValue1:str = obj["OffSegValue1"]
      """  Offset Segment Value 1  """  
      self.OffSegValue2:str = obj["OffSegValue2"]
      """  Offset Segment Value 2  """  
      self.OffSegValue3:str = obj["OffSegValue3"]
      """  Offset Segment Value 3  """  
      self.OffSegValue4:str = obj["OffSegValue4"]
      """  Offset Segment Value 4  """  
      self.OffSegValue5:str = obj["OffSegValue5"]
      """  Offset Segment Value 5  """  
      self.OffSegValue6:str = obj["OffSegValue6"]
      """  Offset Segment Value 6  """  
      self.OffSegValue7:str = obj["OffSegValue7"]
      """  Offset Segment Value 7  """  
      self.OffSegValue8:str = obj["OffSegValue8"]
      """  Offset Segment Value 8  """  
      self.OffSegValue9:str = obj["OffSegValue9"]
      """  Offset Segment Value 9  """  
      self.OffSegValue10:str = obj["OffSegValue10"]
      """  Offset Segment Value 10  """  
      self.OffSegValue11:str = obj["OffSegValue11"]
      """  Offset Segment Value 11  """  
      self.OffSegValue12:str = obj["OffSegValue12"]
      """  Offset Segment Value 12  """  
      self.OffSegValue13:str = obj["OffSegValue13"]
      """  Offset Segment Value 13  """  
      self.OffSegValue14:str = obj["OffSegValue14"]
      """  Offset Segment Value 14  """  
      self.OffSegValue15:str = obj["OffSegValue15"]
      """  Offset Segment Value 15  """  
      self.OffSegValue16:str = obj["OffSegValue16"]
      """  Offset Segment Value 16  """  
      self.OffSegValue17:str = obj["OffSegValue17"]
      """  Offset Segment Value 17  """  
      self.OffSegValue18:str = obj["OffSegValue18"]
      """  Offset Segment Value 18  """  
      self.OffSegValue19:str = obj["OffSegValue19"]
      """  Offset Segment Value 19  """  
      self.OffSegValue20:str = obj["OffSegValue20"]
      """  Offset Segment Value 20  """  
      self.ReverseCategoryID:str = obj["ReverseCategoryID"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBCOASegmentSearchListTableset:
   def __init__(self, obj):
      self.GLBCOASegmentSearchList:list[Erp_Tablesets_GLBCOASegmentSearchListRow] = obj["GLBCOASegmentSearchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLBCOASegmentSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Company ID of the external company this COA was imported from.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment  """  
      self.Abbreviation:str = obj["Abbreviation"]
      """  Short name of segment.  """  
      self.MaxLength:int = obj["MaxLength"]
      """  Maximum length of the code used for this segment.  Valid values are between 1 and 50.  This value must be at least the value of the minimum length.  The minimum length is the default value.  If a segment is tied to a reference entity the maximum length cannot be less then the length of the reference entity's field.  """  
      self.MinLength:int = obj["MinLength"]
      """  Minimum length of the code to be used for this segment.  Must be a value between 1 and the maximum length.  If the segment is tied to a reference entity the minimum length cannot be greater than the length of the reference entity field.  """  
      self.Dynamic:bool = obj["Dynamic"]
      """  Indicates if accounts with this segment can be created on the fly when posting transactions.  If Yes, the GLAccount table does not have to contain entries with this field populated.  If No, then all valid combinations of segment values (COASegVal) must be defined in the GLAccount table before the account can be used.  """  
      self.UseRefEntity:bool = obj["UseRefEntity"]
      """  Indicates if this segment is related to another business entity.  This is only available if the Dynamic field equals Yes.  """  
      self.RefEntity:str = obj["RefEntity"]
      """  This is the reference entity where the COASegVals are generated from.  Valid values are found in the BusEntities table.  This option is NOT valid for the natural account (segment number 1)  """  
      self.AllowAlpha:bool = obj["AllowAlpha"]
      """  Indicates if alpha characters are allowed in the code.   The default value is yes.  If UseRefEntity equals yes then this field must equal yes.  If no, then only  numeric characters are allowed as segment values.  """  
      self.EntryControl:str = obj["EntryControl"]
      """  Indicates what causes the entry of segment values for this segment.  Valid values are: 0 (zero): Mandatory - the segment is always entered.  1 (one) Natrual account - The option on the natural account determines if this segment is mandatory, optional or not used.  This value is found on the COASegValOpt table.  """  
      self.SegSelfBal:bool = obj["SegSelfBal"]
      """  Indicates if journal entries are automatically balanced.  """  
      self.Level:int = obj["Level"]
      """  The level indicates the order segments will be balanced in case multiple segments are defined as self balancing.  This field can only be updated when SegSelfBal equals yes.  Two self balancing segments cannot have the same level.  Valid values are 1 thorugh the number of segments defined for the COA.  """  
      self.SummaryBal:bool = obj["SummaryBal"]
      """  Indicates if this segment is included in the standard trial balance account.  """  
      self.DetailBal:bool = obj["DetailBal"]
      """  Indicates if balance records are maintained by the system for this segment.  If Yes, this segment is used as part of the GL Account for balance purposes.  """  
      self.KeepOpenBal:bool = obj["KeepOpenBal"]
      """  Indicates if opening balances are kept for expense and revenue accounts.  This is typically used for pjrect accounting where you want to keep the project date balance independent of the financial year.  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  Indicates the order in which this segment is displayed when presenting the GL Account to the user.  Valid values are 1 through 20.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Indicates if this segment is subject to Multi-Company GL Journal processing.  If the COA is marked as MultipCompnay then all controlled segments are flagged as multi-company and this cannot be overwritten by the user.  """  
      self.AutoCreateSegVals:bool = obj["AutoCreateSegVals"]
      """  Indicates if segment values for segments defined as reference entities are to be created each time a newrecord is created.  Only valid if UseRefEntity equals yes and a reference entity is entered.  """  
      self.SelfBalAcct:str = obj["SelfBalAcct"]
      """  Account used  when creating balancing transactions for this segment.  """  
      self.BalSegValue1:str = obj["BalSegValue1"]
      """  Balance Seg Value 1  """  
      self.BalSegValue2:str = obj["BalSegValue2"]
      """  Balance Seg Value 2  """  
      self.BalSegValue3:str = obj["BalSegValue3"]
      """  Balance Seg Value 3  """  
      self.BalSegValue4:str = obj["BalSegValue4"]
      """  Balance Seg Value 4  """  
      self.BalSegValue5:str = obj["BalSegValue5"]
      """  Balance Seg Value 5  """  
      self.BalSegValue6:str = obj["BalSegValue6"]
      """  Balance Seg Value 6  """  
      self.BalSegValue7:str = obj["BalSegValue7"]
      """  Balance Seg Value 7  """  
      self.BalSegValue8:str = obj["BalSegValue8"]
      """  Balance Seg Value 8  """  
      self.BalSegValue9:str = obj["BalSegValue9"]
      """  Balance Seg Value 9  """  
      self.BalSegValue10:str = obj["BalSegValue10"]
      """  Balance Seg Value 10  """  
      self.BalSegValue11:str = obj["BalSegValue11"]
      """  Balance Seg Value 11  """  
      self.BalSegValue12:str = obj["BalSegValue12"]
      """  Balance Seg Value 12  """  
      self.BalSegValue13:str = obj["BalSegValue13"]
      """  Balance Seg Value 13  """  
      self.BalSegValue14:str = obj["BalSegValue14"]
      """  Balance Seg Value 14  """  
      self.BalSegValue15:str = obj["BalSegValue15"]
      """  Balance Seg Value 15  """  
      self.BalSegValue16:str = obj["BalSegValue16"]
      """  Balance Seg Value 16  """  
      self.BalSegValue17:str = obj["BalSegValue17"]
      """  Balance Seg Value 17  """  
      self.BalSegValue18:str = obj["BalSegValue18"]
      """  Balance Seg Value 18  """  
      self.BalSegValue19:str = obj["BalSegValue19"]
      """  Balance Seg Value 19  """  
      self.BalSegValue20:str = obj["BalSegValue20"]
      """  Balance Seg Value 20  """  
      self.SelfOffAcct:str = obj["SelfOffAcct"]
      """  The Self Balance offset account used when balancing this segment.  """  
      self.OffSegValue1:str = obj["OffSegValue1"]
      """  Offset Segment Value 1  """  
      self.OffSegValue2:str = obj["OffSegValue2"]
      """  Offset Segment Value 2  """  
      self.OffSegValue3:str = obj["OffSegValue3"]
      """  Offset Segment Value 3  """  
      self.OffSegValue4:str = obj["OffSegValue4"]
      """  Offset Segment Value 4  """  
      self.OffSegValue5:str = obj["OffSegValue5"]
      """  Offset Segment Value 5  """  
      self.OffSegValue6:str = obj["OffSegValue6"]
      """  Offset Segment Value 6  """  
      self.OffSegValue7:str = obj["OffSegValue7"]
      """  Offset Segment Value 7  """  
      self.OffSegValue8:str = obj["OffSegValue8"]
      """  Offset Segment Value 8  """  
      self.OffSegValue9:str = obj["OffSegValue9"]
      """  Offset Segment Value 9  """  
      self.OffSegValue10:str = obj["OffSegValue10"]
      """  Offset Segment Value 10  """  
      self.OffSegValue11:str = obj["OffSegValue11"]
      """  Offset Segment Value 11  """  
      self.OffSegValue12:str = obj["OffSegValue12"]
      """  Offset Segment Value 12  """  
      self.OffSegValue13:str = obj["OffSegValue13"]
      """  Offset Segment Value 13  """  
      self.OffSegValue14:str = obj["OffSegValue14"]
      """  Offset Segment Value 14  """  
      self.OffSegValue15:str = obj["OffSegValue15"]
      """  Offset Segment Value 15  """  
      self.OffSegValue16:str = obj["OffSegValue16"]
      """  Offset Segment Value 16  """  
      self.OffSegValue17:str = obj["OffSegValue17"]
      """  Offset Segment Value 17  """  
      self.OffSegValue18:str = obj["OffSegValue18"]
      """  Offset Segment Value 18  """  
      self.OffSegValue19:str = obj["OffSegValue19"]
      """  Offset Segment Value 19  """  
      self.OffSegValue20:str = obj["OffSegValue20"]
      """  Offset Segment Value 20  """  
      self.ReverseCategoryID:str = obj["ReverseCategoryID"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CNIsCFICode:bool = obj["CNIsCFICode"]
      """  CNIsCFICode  """  
      self.SegValueField:str = obj["SegValueField"]
      """  SegValueField  """  
      self.DescFieldName:str = obj["DescFieldName"]
      """  DescFieldName  """  
      self.GlobalCOASegment:bool = obj["GlobalCOASegment"]
      """  GlobalCOASegment  """  
      self.GlobalCOASegmentValues:bool = obj["GlobalCOASegmentValues"]
      """  GlobalCOASegmentValues  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.GlobalValuesLock:bool = obj["GlobalValuesLock"]
      """  GlobalValuesLock  """  
      self.SiteSegment:bool = obj["SiteSegment"]
      """  SiteSegment  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBCOASegmentSearchTableset:
   def __init__(self, obj):
      self.GLBCOASegmentSearch:list[Erp_Tablesets_GLBCOASegmentSearchRow] = obj["GLBCOASegmentSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGLBCOASegmentSearchTableset:
   def __init__(self, obj):
      self.GLBCOASegmentSearch:list[Erp_Tablesets_GLBCOASegmentSearchRow] = obj["GLBCOASegmentSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   extCompanyID
   coACode
   segmentNbr
   """  
   def __init__(self, obj):
      self.extCompanyID:str = obj["extCompanyID"]
      self.coACode:str = obj["coACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLBCOASegmentSearchTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLBCOASegmentSearchTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLBCOASegmentSearchTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLBCOASegmentSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGLBCOASegmentSearch_input:
   """ Required : 
   ds
   extCompanyID
   coACode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBCOASegmentSearchTableset] = obj["ds"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.coACode:str = obj["coACode"]
      pass

class GetNewGLBCOASegmentSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBCOASegmentSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGLBCOASegmentSearch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLBCOASegmentSearch:str = obj["whereClauseGLBCOASegmentSearch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLBCOASegmentSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLBCOASegmentSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLBCOASegmentSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBCOASegmentSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBCOASegmentSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

