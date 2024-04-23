import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ShopWrnSvc
# Description: Labor warning for a specific labor detail or header record -
           used with shop Tracker and data collection, labor entry, labor edit list
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ShopWrns(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShopWrns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShopWrns
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShopWrnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/ShopWrns",headers=creds) as resp:
           return await resp.json()

async def post_ShopWrns(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShopWrns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShopWrnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShopWrnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/ShopWrns", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShopWrns_Company_WarnType_LaborHedSeq_LaborDtlSeq_LabWarnNum(Company, WarnType, LaborHedSeq, LaborDtlSeq, LabWarnNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShopWrn item
   Description: Calls GetByID to retrieve the ShopWrn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShopWrn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarnType: Desc: WarnType   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param LabWarnNum: Desc: LabWarnNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShopWrnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/ShopWrns(" + Company + "," + WarnType + "," + LaborHedSeq + "," + LaborDtlSeq + "," + LabWarnNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShopWrns_Company_WarnType_LaborHedSeq_LaborDtlSeq_LabWarnNum(Company, WarnType, LaborHedSeq, LaborDtlSeq, LabWarnNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShopWrn for the service
   Description: Calls UpdateExt to update ShopWrn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShopWrn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarnType: Desc: WarnType   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param LabWarnNum: Desc: LabWarnNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShopWrnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/ShopWrns(" + Company + "," + WarnType + "," + LaborHedSeq + "," + LaborDtlSeq + "," + LabWarnNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShopWrns_Company_WarnType_LaborHedSeq_LaborDtlSeq_LabWarnNum(Company, WarnType, LaborHedSeq, LaborDtlSeq, LabWarnNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShopWrn item
   Description: Call UpdateExt to delete ShopWrn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShopWrn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarnType: Desc: WarnType   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param LabWarnNum: Desc: LabWarnNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/ShopWrns(" + Company + "," + WarnType + "," + LaborHedSeq + "," + LaborDtlSeq + "," + LabWarnNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShopWrnListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseShopWrn, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseShopWrn=" + whereClauseShopWrn
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(warnType, laborHedSeq, laborDtlSeq, labWarnNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True
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
   params += "warnType=" + warnType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "laborHedSeq=" + laborHedSeq
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "laborDtlSeq=" + laborDtlSeq
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "labWarnNum=" + labWarnNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_MoveToHistory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveToHistory
   Description: Set MoveToHistory flag
   OperationID: MoveToHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveToHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveToHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveAllToHistory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveAllToHistory
   Description: Set MoveAllToHistory flag
This is just for Kinetic UI
   OperationID: MoveAllToHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveAllToHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveAllToHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveAllToHistoryTrackerNoDataSet(epicorHeaders = None):
   """  
   Summary: Invoke method MoveAllToHistoryTrackerNoDataSet
   Description: Set CurrWarn flag to false for all records in Shop Tracker
without passing a dataset
This is just for Kinetic UI
   OperationID: MoveAllToHistoryTrackerNoDataSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveAllToHistoryTrackerNoDataSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewShopWrn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShopWrn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShopWrn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShopWrn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShopWrn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShopWrnListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShopWrnListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShopWrnRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShopWrnRow] = obj["value"]
      pass

class Erp_Tablesets_ShopWrnListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  An integer assigned by the system to uniquely identify the LaborHed record. This integer is created by using the database sequence "LaborHedSeq".  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.LabWarnNum:int = obj["LabWarnNum"]
      """  Identifies a Labor warning  """  
      self.CurrWarn:bool = obj["CurrWarn"]
      """  Shop Tracker viewed warnings are initially set to True for easy review; all others are set to False.  """  
      self.EventDate:str = obj["EventDate"]
      """  The Date the event that created the warning occurred  """  
      self.EventTime:int = obj["EventTime"]
      """  The Time the event was created in seconds since midnight.  """  
      self.MsgText:str = obj["MsgText"]
      """  Message warning text(e.g. with scrap/rework reason etc.)  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  """  
      self.OprSeq:int = obj["OprSeq"]
      """   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group master.
For production labor (LaborType = "S" or "P") the default is from the JobOper.WcCode.
For indirect labor (LaborType = I) there is no default.  """  
      self.VariancePct:int = obj["VariancePct"]
      """   The percentage that this operation varied. Greater than the limit
from the Warning table.  """  
      self.WarnType:str = obj["WarnType"]
      """  Indicates if this is a labor or Material warning  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EmployeeNumName:str = obj["EmployeeNumName"]
      """  Employee's full name  """  
      self.EmployeeNumSupervisorName:str = obj["EmployeeNumSupervisorName"]
      """  Employee Supervisor name  """  
      self.DspEventTime:str = obj["DspEventTime"]
      """  The EventTime converted to HH:MM:SS  """  
      self.TransMsgText:str = obj["TransMsgText"]
      """  Translated message text  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShopWrnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  An integer assigned by the system to uniquely identify the LaborHed record. This integer is created by using the database sequence "LaborHedSeq".  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.LabWarnNum:int = obj["LabWarnNum"]
      """  Identifies a Labor warning  """  
      self.CurrWarn:bool = obj["CurrWarn"]
      """  Shop Tracker viewed warnings are initially set to True for easy review; all others are set to False.  """  
      self.EventDate:str = obj["EventDate"]
      """  The Date the event that created the warning occurred  """  
      self.EventTime:int = obj["EventTime"]
      """  The Time the event was created in seconds since midnight.  """  
      self.MsgText:str = obj["MsgText"]
      """  Message warning text(e.g. with scrap/rework reason etc.)  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  """  
      self.OprSeq:int = obj["OprSeq"]
      """   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group master.
For production labor (LaborType = "S" or "P") the default is from the JobOper.WcCode.
For indirect labor (LaborType = I) there is no default.  """  
      self.VariancePct:int = obj["VariancePct"]
      """   The percentage that this operation varied. Greater than the limit
from the Warning table.  """  
      self.WarnType:str = obj["WarnType"]
      """  Indicates if this is a labor or Material warning  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EmployeeNumName:str = obj["EmployeeNumName"]
      """  Employee's full name  """  
      self.EmployeeNumSupervisorName:str = obj["EmployeeNumSupervisorName"]
      """  Employee Supervisor name  """  
      self.DspEventTime:str = obj["DspEventTime"]
      """  The EventTime converted to HH:MM:SS  """  
      self.TransMsgText:str = obj["TransMsgText"]
      """  Translated message text  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.EmpBasicNameSupervisorID:str = obj["EmpBasicNameSupervisorID"]
      self.EmpBasicNameName:str = obj["EmpBasicNameName"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.WarningRptShpTracker:bool = obj["WarningRptShpTracker"]
      self.WarningRptDataCollect:bool = obj["WarningRptDataCollect"]
      self.WarningRptLbrEnt:bool = obj["WarningRptLbrEnt"]
      self.WarningRptLbrEdit:bool = obj["WarningRptLbrEdit"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   warnType
   laborHedSeq
   laborDtlSeq
   labWarnNum
   """  
   def __init__(self, obj):
      self.warnType:str = obj["warnType"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      self.labWarnNum:int = obj["labWarnNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ShopWrnListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  An integer assigned by the system to uniquely identify the LaborHed record. This integer is created by using the database sequence "LaborHedSeq".  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.LabWarnNum:int = obj["LabWarnNum"]
      """  Identifies a Labor warning  """  
      self.CurrWarn:bool = obj["CurrWarn"]
      """  Shop Tracker viewed warnings are initially set to True for easy review; all others are set to False.  """  
      self.EventDate:str = obj["EventDate"]
      """  The Date the event that created the warning occurred  """  
      self.EventTime:int = obj["EventTime"]
      """  The Time the event was created in seconds since midnight.  """  
      self.MsgText:str = obj["MsgText"]
      """  Message warning text(e.g. with scrap/rework reason etc.)  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  """  
      self.OprSeq:int = obj["OprSeq"]
      """   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group master.
For production labor (LaborType = "S" or "P") the default is from the JobOper.WcCode.
For indirect labor (LaborType = I) there is no default.  """  
      self.VariancePct:int = obj["VariancePct"]
      """   The percentage that this operation varied. Greater than the limit
from the Warning table.  """  
      self.WarnType:str = obj["WarnType"]
      """  Indicates if this is a labor or Material warning  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EmployeeNumName:str = obj["EmployeeNumName"]
      """  Employee's full name  """  
      self.EmployeeNumSupervisorName:str = obj["EmployeeNumSupervisorName"]
      """  Employee Supervisor name  """  
      self.DspEventTime:str = obj["DspEventTime"]
      """  The EventTime converted to HH:MM:SS  """  
      self.TransMsgText:str = obj["TransMsgText"]
      """  Translated message text  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShopWrnListTableset:
   def __init__(self, obj):
      self.ShopWrnList:list[Erp_Tablesets_ShopWrnListRow] = obj["ShopWrnList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ShopWrnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  An integer assigned by the system to uniquely identify the LaborHed record. This integer is created by using the database sequence "LaborHedSeq".  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.LabWarnNum:int = obj["LabWarnNum"]
      """  Identifies a Labor warning  """  
      self.CurrWarn:bool = obj["CurrWarn"]
      """  Shop Tracker viewed warnings are initially set to True for easy review; all others are set to False.  """  
      self.EventDate:str = obj["EventDate"]
      """  The Date the event that created the warning occurred  """  
      self.EventTime:int = obj["EventTime"]
      """  The Time the event was created in seconds since midnight.  """  
      self.MsgText:str = obj["MsgText"]
      """  Message warning text(e.g. with scrap/rework reason etc.)  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  """  
      self.OprSeq:int = obj["OprSeq"]
      """   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group master.
For production labor (LaborType = "S" or "P") the default is from the JobOper.WcCode.
For indirect labor (LaborType = I) there is no default.  """  
      self.VariancePct:int = obj["VariancePct"]
      """   The percentage that this operation varied. Greater than the limit
from the Warning table.  """  
      self.WarnType:str = obj["WarnType"]
      """  Indicates if this is a labor or Material warning  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EmployeeNumName:str = obj["EmployeeNumName"]
      """  Employee's full name  """  
      self.EmployeeNumSupervisorName:str = obj["EmployeeNumSupervisorName"]
      """  Employee Supervisor name  """  
      self.DspEventTime:str = obj["DspEventTime"]
      """  The EventTime converted to HH:MM:SS  """  
      self.TransMsgText:str = obj["TransMsgText"]
      """  Translated message text  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.EmpBasicNameSupervisorID:str = obj["EmpBasicNameSupervisorID"]
      self.EmpBasicNameName:str = obj["EmpBasicNameName"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.WarningRptShpTracker:bool = obj["WarningRptShpTracker"]
      self.WarningRptDataCollect:bool = obj["WarningRptDataCollect"]
      self.WarningRptLbrEnt:bool = obj["WarningRptLbrEnt"]
      self.WarningRptLbrEdit:bool = obj["WarningRptLbrEdit"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShopWrnTableset:
   def __init__(self, obj):
      self.ShopWrn:list[Erp_Tablesets_ShopWrnRow] = obj["ShopWrn"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtShopWrnTableset:
   def __init__(self, obj):
      self.ShopWrn:list[Erp_Tablesets_ShopWrnRow] = obj["ShopWrn"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   warnType
   laborHedSeq
   laborDtlSeq
   labWarnNum
   """  
   def __init__(self, obj):
      self.warnType:str = obj["warnType"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      self.labWarnNum:int = obj["labWarnNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ShopWrnTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ShopWrnTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ShopWrnTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ShopWrnListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewShopWrn_input:
   """ Required : 
   ds
   warnType
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ShopWrnTableset] = obj["ds"]
      self.warnType:str = obj["warnType"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      pass

class GetNewShopWrn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ShopWrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseShopWrn
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseShopWrn:str = obj["whereClauseShopWrn"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ShopWrnTableset] = obj["returnObj"]
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

class MoveAllToHistoryTrackerNoDataSet_output:
   def __init__(self, obj):
      pass

class MoveAllToHistory_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ShopWrnTableset] = obj["ds"]
      pass

class MoveAllToHistory_output:
   def __init__(self, obj):
      pass

class MoveToHistory_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ShopWrnTableset] = obj["ds"]
      pass

class MoveToHistory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ShopWrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtShopWrnTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtShopWrnTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ShopWrnTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ShopWrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

