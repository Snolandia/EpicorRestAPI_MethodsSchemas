import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ECOOprSearchSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOOprSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOprSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/ECOOprSearches",headers=creds) as resp:
           return await resp.json()

async def post_ECOOprSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOprSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/ECOOprSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOOprSearches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOprSearch item
   Description: Calls GetByID to retrieve the ECOOprSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/ECOOprSearches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOOprSearches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOOprSearch for the service
   Description: Calls UpdateExt to update ECOOprSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOprSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/ECOOprSearches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOOprSearches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOOprSearch item
   Description: Call UpdateExt to delete ECOOprSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOprSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/ECOOprSearches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseECOOpr, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseECOOpr=" + whereClauseECOOpr
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, partNum, revisionNum, altMethod, processMfgID, oprSeq, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "groupID=" + groupID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "revisionNum=" + revisionNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "altMethod=" + altMethod
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "processMfgID=" + processMfgID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "oprSeq=" + oprSeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOOpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOOpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOOprListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOOprRow] = obj["value"]
      pass

class Erp_Tablesets_ECOOprListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Master Code - Links the JobOper  record with a OpMaster record. Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  """  
      self.EstSetHours:int = obj["EstSetHours"]
      """  The estimated set up hours. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours.  """  
      self.EstProdHours:int = obj["EstProdHours"]
      """   The estimated Production run hours for internal operations (Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (RunQty / Std).
If StdFormat = "PM" then (RunQty / Std ) / 60.
If StdFormat = "OH" then (RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (RunQty/Basis) X Std.
If StdFormat = "MP" then ((RunQty/Basis) X Std) / 60.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Production Quantity per one of the Parent Item.  """  
      self.Machines:int = obj["Machines"]
      """  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  Inventory UOM  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  """  
      self.DaysOut:int = obj["DaysOut"]
      """  Hours required is calculated as days * 8.  """  
      self.SubPartNum:str = obj["SubPartNum"]
      """  The PartNum to be shipped to the subcontract. Defaults as the Part number of the method to which it belongs (ECOOpr.PartNum).  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job operation comments.  """  
      self.SchedRelation:str = obj["SchedRelation"]
      """   Indicates the scheduling relationship between this and the preceding operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  """  
      self.RunQty:int = obj["RunQty"]
      """  The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0. This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  """  
      self.AddlSetupHours:int = obj["AddlSetupHours"]
      """  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calculations are rounded up to the next whole number before multiplying by the AddlSetUpHours.  """  
      self.AddlSetUpQty:int = obj["AddlSetUpQty"]
      """  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  """  
      self.APSPrepOp:int = obj["APSPrepOp"]
      """  Indicates the operation that must precede this operation.  Mainly used to model one to many routing structures.  """  
      self.APSNextOp:int = obj["APSNextOp"]
      """  This is the next operation in the routing.  -1 makes this operation the last one in the routing so far; -2 makes it the first one in the routing so far; 0 means no successor.  """  
      self.APSAltOp:int = obj["APSAltOp"]
      """  Specifies the operation for which this is an alternate.  """  
      self.APSSpecificResource:str = obj["APSSpecificResource"]
      """  Used to assign an operation to a specific resource so that APS does not schedule it elsewhere.  Overrides APSCapability.  """  
      self.APSCycleTime:int = obj["APSCycleTime"]
      """   Cycles per minute.
SQL:  IIF(CINT(JobOper.RunQty) = 0 OR JobOper.SubContract = TRUE, "0", JobOper.EstProdHours * 60 /  JobOper.RunQty)  """  
      self.APSConstantTime:int = obj["APSConstantTime"]
      """   Fixed time, in decimal minutes, to be added to the operation.  Can be used to represent cleanup time or model outsource time.
SQL: IFF(JobOper.SubContract = TRUE, (JobOper.DaysOut * 1440), "0")  """  
      self.APSSetupGroup:int = obj["APSSetupGroup"]
      """  Used to group operations to save on setups.  """  
      self.APSMakeFactor:int = obj["APSMakeFactor"]
      """  Quantity of Part per cycle.  """  
      self.APSContainerSize:int = obj["APSContainerSize"]
      """  Quantity that must be completed before the next operation can start (for overlap); quantity per batch (for batch resources); Auxiliary resource quantity.  """  
      self.APSSchedulerName:str = obj["APSSchedulerName"]
      """  Name of the APS Scheduler Module in which to schedule this operation.  """  
      self.APSMaxLength:int = obj["APSMaxLength"]
      """  If the scheduled time exceeds this value then the operation is split into operations which do not exceed this length.  """  
      self.APSTransferTime:int = obj["APSTransferTime"]
      """  Time between the end of this operation and the start time of the successor operation.  """  
      self.APSEffectiveness:int = obj["APSEffectiveness"]
      """  Cycle time and constant times are divided by this value to get schedule times.  Zeros disable this feature.  """  
      self.APSOperationClass:str = obj["APSOperationClass"]
      """  Type of Operation: P for Prep, D for Processing (Dispatchable in APS terminology).  """  
      self.APSAuxResource:str = obj["APSAuxResource"]
      """  Auxiliary resource requirements.   This is a comma and tilde delimited list of APSAuxResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  """  
      self.APSAddResource:str = obj["APSAddResource"]
      """  Additional resource requirements.   This is a comma and tilde delimited list of APSAddResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  For Additional Resources the Duration = 5 (entire Operation).  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  """  
      self.FAQty:int = obj["FAQty"]
      """  The quantity requested for first article inspection.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this part operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this part subcontract operation.  Can be zero if RFQ(s) are not required.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.OrigOprSeq:int = obj["OrigOprSeq"]
      """  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  """  
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operation to save on setups.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PrimarySetupOpDtl:int = obj["PrimarySetupOpDtl"]
      """   Identifies the primary ECOOpDtl to be used for setup.  The setup time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = S or B.  """  
      self.PrimaryProdOpDtl:int = obj["PrimaryProdOpDtl"]
      """   Identifies the primary ECOOpDtl to be used for production.  The production run time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = P or B.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description.  """  
      self.StageNumber:str = obj["StageNumber"]
      """  The stage number of the operations.  Entered only when the related PartRev.UseStaging flag is true.  """  
      self.BaseMethodOverridden:bool = obj["BaseMethodOverridden"]
      """  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  Parent Alternate Routing method of this part operation.  """  
      self.ParentOprSeq:int = obj["ParentOprSeq"]
      """  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  """  
      self.BrkQty01:int = obj["BrkQty01"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty02:int = obj["BrkQty02"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty03:int = obj["BrkQty03"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty04:int = obj["BrkQty04"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty05:int = obj["BrkQty05"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty06:int = obj["BrkQty06"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty07:int = obj["BrkQty07"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty08:int = obj["BrkQty08"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty09:int = obj["BrkQty09"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty10:int = obj["BrkQty10"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.PBrkCost01:int = obj["PBrkCost01"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost02:int = obj["PBrkCost02"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost03:int = obj["PBrkCost03"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost04:int = obj["PBrkCost04"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost05:int = obj["PBrkCost05"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost06:int = obj["PBrkCost06"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost07:int = obj["PBrkCost07"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost08:int = obj["PBrkCost08"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost09:int = obj["PBrkCost09"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost10:int = obj["PBrkCost10"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkStdRate01:int = obj["PBrkStdRate01"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate02:int = obj["PBrkStdRate02"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate03:int = obj["PBrkStdRate03"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate04:int = obj["PBrkStdRate04"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate05:int = obj["PBrkStdRate05"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate06:int = obj["PBrkStdRate06"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate07:int = obj["PBrkStdRate07"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate08:int = obj["PBrkStdRate08"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate09:int = obj["PBrkStdRate09"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate10:int = obj["PBrkStdRate10"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.SNRequiredOpr:bool = obj["SNRequiredOpr"]
      """  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  """  
      self.SNRequiredSubConShip:bool = obj["SNRequiredSubConShip"]
      """  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  """  
      self.Weight:int = obj["Weight"]
      """  Operation Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Operation Weight UOM defaulted from Part Master.  """  
      self.SendAheadType:str = obj["SendAheadType"]
      """   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  """  
      self.SendAheadOffset:int = obj["SendAheadOffset"]
      """   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  """  
      self.PrjRoleList:str = obj["PrjRoleList"]
      """  Delimited list of PrjRoleCd codes that are allowed for this operation.  """  
      self.UseAllRoles:bool = obj["UseAllRoles"]
      """  Allow use all Roles  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.PctReg:int = obj["PctReg"]
      """  PctReg  """  
      self.SetupMaterial:int = obj["SetupMaterial"]
      """  SetupMaterial  """  
      self.MaterialColorRating:int = obj["MaterialColorRating"]
      """  MaterialColorRating  """  
      self.MiscInfo1:str = obj["MiscInfo1"]
      """  MiscInfo1  """  
      self.MiscInfo2:str = obj["MiscInfo2"]
      """  MiscInfo2  """  
      self.SetupURL:str = obj["SetupURL"]
      """  SetupURL  """  
      self.ExpPctUp:int = obj["ExpPctUp"]
      """  ExpPctUp  """  
      self.ExpCycTm:int = obj["ExpCycTm"]
      """  ExpCycTm  """  
      self.ExpGood:int = obj["ExpGood"]
      """  ExpGood  """  
      self.NonProdLimit:int = obj["NonProdLimit"]
      """  NonProdLimit  """  
      self.AutoSpcEnable:bool = obj["AutoSpcEnable"]
      """  AutoSpcEnable  """  
      self.AutoSpcPeriod:int = obj["AutoSpcPeriod"]
      """  AutoSpcPeriod  """  
      self.PartQualEnable:bool = obj["PartQualEnable"]
      """  PartQualEnable  """  
      self.AutoSpcSubgroup:int = obj["AutoSpcSubgroup"]
      """  AutoSpcSubgroup  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PulsesPerCycle:int = obj["PulsesPerCycle"]
      """  PulsesPerCycle  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.TemplateID:str = obj["TemplateID"]
      """  TemplateID  """  
      self.SubRevisionNum:str = obj["SubRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Master Code - Links the JobOper  record with a OpMaster record. Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  """  
      self.EstSetHours:int = obj["EstSetHours"]
      """  The estimated set up hours. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours.  """  
      self.EstProdHours:int = obj["EstProdHours"]
      """   The estimated Production run hours for internal operations (Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (RunQty / Std).
If StdFormat = "PM" then (RunQty / Std ) / 60.
If StdFormat = "OH" then (RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (RunQty/Basis) X Std.
If StdFormat = "MP" then ((RunQty/Basis) X Std) / 60.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Production Quantity per one of the Parent Item.  """  
      self.Machines:int = obj["Machines"]
      """  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  Inventory UOM  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  """  
      self.DaysOut:int = obj["DaysOut"]
      """  Hours required is calculated as days * 8.  """  
      self.SubPartNum:str = obj["SubPartNum"]
      """  The PartNum to be shipped to the subcontract. Defaults as the Part number of the method to which it belongs (ECOOpr.PartNum).  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job operation comments.  """  
      self.SchedRelation:str = obj["SchedRelation"]
      """   Indicates the scheduling relationship between this and the preceding operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  """  
      self.RunQty:int = obj["RunQty"]
      """  The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0. This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  """  
      self.AddlSetupHours:int = obj["AddlSetupHours"]
      """  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calculations are rounded up to the next whole number before multiplying by the AddlSetUpHours.  """  
      self.AddlSetUpQty:int = obj["AddlSetUpQty"]
      """  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  """  
      self.APSPrepOp:int = obj["APSPrepOp"]
      """  Indicates the operation that must precede this operation.  Mainly used to model one to many routing structures.  """  
      self.APSNextOp:int = obj["APSNextOp"]
      """  This is the next operation in the routing.  -1 makes this operation the last one in the routing so far; -2 makes it the first one in the routing so far; 0 means no successor.  """  
      self.APSAltOp:int = obj["APSAltOp"]
      """  Specifies the operation for which this is an alternate.  """  
      self.APSSpecificResource:str = obj["APSSpecificResource"]
      """  Used to assign an operation to a specific resource so that APS does not schedule it elsewhere.  Overrides APSCapability.  """  
      self.APSCycleTime:int = obj["APSCycleTime"]
      """   Cycles per minute.
SQL:  IIF(CINT(JobOper.RunQty) = 0 OR JobOper.SubContract = TRUE, "0", JobOper.EstProdHours * 60 /  JobOper.RunQty)  """  
      self.APSConstantTime:int = obj["APSConstantTime"]
      """   Fixed time, in decimal minutes, to be added to the operation.  Can be used to represent cleanup time or model outsource time.
SQL: IFF(JobOper.SubContract = TRUE, (JobOper.DaysOut * 1440), "0")  """  
      self.APSSetupGroup:int = obj["APSSetupGroup"]
      """  Used to group operations to save on setups.  """  
      self.APSMakeFactor:int = obj["APSMakeFactor"]
      """  Quantity of Part per cycle.  """  
      self.APSContainerSize:int = obj["APSContainerSize"]
      """  Quantity that must be completed before the next operation can start (for overlap); quantity per batch (for batch resources); Auxiliary resource quantity.  """  
      self.APSSchedulerName:str = obj["APSSchedulerName"]
      """  Name of the APS Scheduler Module in which to schedule this operation.  """  
      self.APSMaxLength:int = obj["APSMaxLength"]
      """  If the scheduled time exceeds this value then the operation is split into operations which do not exceed this length.  """  
      self.APSTransferTime:int = obj["APSTransferTime"]
      """  Time between the end of this operation and the start time of the successor operation.  """  
      self.APSEffectiveness:int = obj["APSEffectiveness"]
      """  Cycle time and constant times are divided by this value to get schedule times.  Zeros disable this feature.  """  
      self.APSOperationClass:str = obj["APSOperationClass"]
      """  Type of Operation: P for Prep, D for Processing (Dispatchable in APS terminology).  """  
      self.APSAuxResource:str = obj["APSAuxResource"]
      """  Auxiliary resource requirements.   This is a comma and tilde delimited list of APSAuxResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  """  
      self.APSAddResource:str = obj["APSAddResource"]
      """  Additional resource requirements.   This is a comma and tilde delimited list of APSAddResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  For Additional Resources the Duration = 5 (entire Operation).  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  """  
      self.FAQty:int = obj["FAQty"]
      """  The quantity requested for first article inspection.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this part operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this part subcontract operation.  Can be zero if RFQ(s) are not required.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.OrigOprSeq:int = obj["OrigOprSeq"]
      """  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  """  
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operation to save on setups.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PrimarySetupOpDtl:int = obj["PrimarySetupOpDtl"]
      """   Identifies the primary ECOOpDtl to be used for setup.  The setup time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = S or B.  """  
      self.PrimaryProdOpDtl:int = obj["PrimaryProdOpDtl"]
      """   Identifies the primary ECOOpDtl to be used for production.  The production run time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = P or B.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description.  """  
      self.StageNumber:str = obj["StageNumber"]
      """  The stage number of the operations.  Entered only when the related PartRev.UseStaging flag is true.  """  
      self.BaseMethodOverridden:bool = obj["BaseMethodOverridden"]
      """  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  Parent Alternate Routing method of this part operation.  """  
      self.ParentOprSeq:int = obj["ParentOprSeq"]
      """  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  """  
      self.BrkQty01:int = obj["BrkQty01"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty02:int = obj["BrkQty02"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty03:int = obj["BrkQty03"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty04:int = obj["BrkQty04"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty05:int = obj["BrkQty05"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty06:int = obj["BrkQty06"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty07:int = obj["BrkQty07"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty08:int = obj["BrkQty08"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty09:int = obj["BrkQty09"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty10:int = obj["BrkQty10"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.PBrkCost01:int = obj["PBrkCost01"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost02:int = obj["PBrkCost02"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost03:int = obj["PBrkCost03"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost04:int = obj["PBrkCost04"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost05:int = obj["PBrkCost05"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost06:int = obj["PBrkCost06"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost07:int = obj["PBrkCost07"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost08:int = obj["PBrkCost08"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost09:int = obj["PBrkCost09"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost10:int = obj["PBrkCost10"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkStdRate01:int = obj["PBrkStdRate01"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate02:int = obj["PBrkStdRate02"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate03:int = obj["PBrkStdRate03"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate04:int = obj["PBrkStdRate04"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate05:int = obj["PBrkStdRate05"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate06:int = obj["PBrkStdRate06"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate07:int = obj["PBrkStdRate07"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate08:int = obj["PBrkStdRate08"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate09:int = obj["PBrkStdRate09"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate10:int = obj["PBrkStdRate10"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.SNRequiredOpr:bool = obj["SNRequiredOpr"]
      """  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  """  
      self.SNRequiredSubConShip:bool = obj["SNRequiredSubConShip"]
      """  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  """  
      self.Weight:int = obj["Weight"]
      """  Operation Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Operation Weight UOM defaulted from Part Master.  """  
      self.SendAheadType:str = obj["SendAheadType"]
      """   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  """  
      self.SendAheadOffset:int = obj["SendAheadOffset"]
      """   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  """  
      self.PrjRoleList:str = obj["PrjRoleList"]
      """  Delimited list of PrjRoleCd codes that are allowed for this operation.  """  
      self.UseAllRoles:bool = obj["UseAllRoles"]
      """  Allow use all Roles  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.PctReg:int = obj["PctReg"]
      """  PctReg  """  
      self.SetupMaterial:int = obj["SetupMaterial"]
      """  SetupMaterial  """  
      self.MaterialColorRating:int = obj["MaterialColorRating"]
      """  MaterialColorRating  """  
      self.MiscInfo1:str = obj["MiscInfo1"]
      """  MiscInfo1  """  
      self.MiscInfo2:str = obj["MiscInfo2"]
      """  MiscInfo2  """  
      self.SetupURL:str = obj["SetupURL"]
      """  SetupURL  """  
      self.ExpPctUp:int = obj["ExpPctUp"]
      """  ExpPctUp  """  
      self.ExpCycTm:int = obj["ExpCycTm"]
      """  ExpCycTm  """  
      self.ExpGood:int = obj["ExpGood"]
      """  ExpGood  """  
      self.NonProdLimit:int = obj["NonProdLimit"]
      """  NonProdLimit  """  
      self.AutoSpcEnable:bool = obj["AutoSpcEnable"]
      """  AutoSpcEnable  """  
      self.AutoSpcPeriod:int = obj["AutoSpcPeriod"]
      """  AutoSpcPeriod  """  
      self.PartQualEnable:bool = obj["PartQualEnable"]
      """  PartQualEnable  """  
      self.AutoSpcSubgroup:int = obj["AutoSpcSubgroup"]
      """  AutoSpcSubgroup  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PulsesPerCycle:int = obj["PulsesPerCycle"]
      """  PulsesPerCycle  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.TemplateID:str = obj["TemplateID"]
      """  TemplateID  """  
      self.SubRevisionNum:str = obj["SubRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.DspBillAddr:str = obj["DspBillAddr"]
      """  The vendor's name and bill to address  """  
      self.EnableSNReqSubConShip:bool = obj["EnableSNReqSubConShip"]
      """  Field used to control the flag on SNRequiredSubConShip field on UI screens.  """  
      self.EnableSNRequiredOpr:bool = obj["EnableSNRequiredOpr"]
      """  Used as a flag to enable controls on UI screens  """  
      self.FinalOpr:bool = obj["FinalOpr"]
      """  The final operation field  """  
      self.HasPriceBreaks:bool = obj["HasPriceBreaks"]
      """  Flag to let you know if you have price breaks.  """  
      self.IsPartOpr:bool = obj["IsPartOpr"]
      """  Is this a PartOpr?  Used when building the tree to show PartOpr as ECOOpr.  """  
      self.OldOprSeq:int = obj["OldOprSeq"]
      """  The original or old OprSeq.  Used when changing the OprSeq.  """  
      self.OpStdDescription:str = obj["OpStdDescription"]
      self.PLMChar03:str = obj["PLMChar03"]
      """  PML ID  """  
      self.PrimaryResourceGrpDesc:str = obj["PrimaryResourceGrpDesc"]
      """  Primary Resource Group description  """  
      self.PrimaryResourceGrpID:str = obj["PrimaryResourceGrpID"]
      """  The Resource Group ID of the primary production operation detail.  """  
      self.RefreshResources:bool = obj["RefreshResources"]
      """  Indicates if the scheduling resources should be refreshed when the op code changes.  """  
      self.SetHoursPerMach:int = obj["SetHoursPerMach"]
      """  The setup hours per machines.  """  
      self.StdFrmtDesc:str = obj["StdFrmtDesc"]
      """  The standard format description.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  The value of the ecorev.usestaging field for UI purposes  """  
      self.AutoReceive:bool = obj["AutoReceive"]
      """  The auto receive field  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.PrimaryProdOpDtlDesc:str = obj["PrimaryProdOpDtlDesc"]
      self.PrimarySetupOpDtlDesc:str = obj["PrimarySetupOpDtlDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.APSSchedulerNameAPSSchedulerName:str = obj["APSSchedulerNameAPSSchedulerName"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PrimaryProdOpDtlOpDtlDesc:str = obj["PrimaryProdOpDtlOpDtlDesc"]
      self.PrimarySetupOpDtlOpDtlDesc:str = obj["PrimarySetupOpDtlOpDtlDesc"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      self.SetupGroupDescription:str = obj["SetupGroupDescription"]
      self.StageNoDescription:str = obj["StageNoDescription"]
      self.SubPartNumTrackInventoryAttributes:bool = obj["SubPartNumTrackInventoryAttributes"]
      self.SubPartNumPricePerCode:str = obj["SubPartNumPricePerCode"]
      self.SubPartNumTrackDimension:bool = obj["SubPartNumTrackDimension"]
      self.SubPartNumTrackSerialNum:bool = obj["SubPartNumTrackSerialNum"]
      self.SubPartNumSellingFactor:int = obj["SubPartNumSellingFactor"]
      self.SubPartNumTrackLots:bool = obj["SubPartNumTrackLots"]
      self.SubPartNumSalesUM:str = obj["SubPartNumSalesUM"]
      self.SubPartNumPartDescription:str = obj["SubPartNumPartDescription"]
      self.SubPartNumIUM:str = obj["SubPartNumIUM"]
      self.SubPartNumAttrClassID:str = obj["SubPartNumAttrClassID"]
      self.SubPartNumTrackInventoryByRevision:bool = obj["SubPartNumTrackInventoryByRevision"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   oprSeq
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      self.oprSeq:int = obj["oprSeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ECOOprListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Master Code - Links the JobOper  record with a OpMaster record. Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  """  
      self.EstSetHours:int = obj["EstSetHours"]
      """  The estimated set up hours. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours.  """  
      self.EstProdHours:int = obj["EstProdHours"]
      """   The estimated Production run hours for internal operations (Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (RunQty / Std).
If StdFormat = "PM" then (RunQty / Std ) / 60.
If StdFormat = "OH" then (RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (RunQty/Basis) X Std.
If StdFormat = "MP" then ((RunQty/Basis) X Std) / 60.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Production Quantity per one of the Parent Item.  """  
      self.Machines:int = obj["Machines"]
      """  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  Inventory UOM  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  """  
      self.DaysOut:int = obj["DaysOut"]
      """  Hours required is calculated as days * 8.  """  
      self.SubPartNum:str = obj["SubPartNum"]
      """  The PartNum to be shipped to the subcontract. Defaults as the Part number of the method to which it belongs (ECOOpr.PartNum).  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job operation comments.  """  
      self.SchedRelation:str = obj["SchedRelation"]
      """   Indicates the scheduling relationship between this and the preceding operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  """  
      self.RunQty:int = obj["RunQty"]
      """  The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0. This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  """  
      self.AddlSetupHours:int = obj["AddlSetupHours"]
      """  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calculations are rounded up to the next whole number before multiplying by the AddlSetUpHours.  """  
      self.AddlSetUpQty:int = obj["AddlSetUpQty"]
      """  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  """  
      self.APSPrepOp:int = obj["APSPrepOp"]
      """  Indicates the operation that must precede this operation.  Mainly used to model one to many routing structures.  """  
      self.APSNextOp:int = obj["APSNextOp"]
      """  This is the next operation in the routing.  -1 makes this operation the last one in the routing so far; -2 makes it the first one in the routing so far; 0 means no successor.  """  
      self.APSAltOp:int = obj["APSAltOp"]
      """  Specifies the operation for which this is an alternate.  """  
      self.APSSpecificResource:str = obj["APSSpecificResource"]
      """  Used to assign an operation to a specific resource so that APS does not schedule it elsewhere.  Overrides APSCapability.  """  
      self.APSCycleTime:int = obj["APSCycleTime"]
      """   Cycles per minute.
SQL:  IIF(CINT(JobOper.RunQty) = 0 OR JobOper.SubContract = TRUE, "0", JobOper.EstProdHours * 60 /  JobOper.RunQty)  """  
      self.APSConstantTime:int = obj["APSConstantTime"]
      """   Fixed time, in decimal minutes, to be added to the operation.  Can be used to represent cleanup time or model outsource time.
SQL: IFF(JobOper.SubContract = TRUE, (JobOper.DaysOut * 1440), "0")  """  
      self.APSSetupGroup:int = obj["APSSetupGroup"]
      """  Used to group operations to save on setups.  """  
      self.APSMakeFactor:int = obj["APSMakeFactor"]
      """  Quantity of Part per cycle.  """  
      self.APSContainerSize:int = obj["APSContainerSize"]
      """  Quantity that must be completed before the next operation can start (for overlap); quantity per batch (for batch resources); Auxiliary resource quantity.  """  
      self.APSSchedulerName:str = obj["APSSchedulerName"]
      """  Name of the APS Scheduler Module in which to schedule this operation.  """  
      self.APSMaxLength:int = obj["APSMaxLength"]
      """  If the scheduled time exceeds this value then the operation is split into operations which do not exceed this length.  """  
      self.APSTransferTime:int = obj["APSTransferTime"]
      """  Time between the end of this operation and the start time of the successor operation.  """  
      self.APSEffectiveness:int = obj["APSEffectiveness"]
      """  Cycle time and constant times are divided by this value to get schedule times.  Zeros disable this feature.  """  
      self.APSOperationClass:str = obj["APSOperationClass"]
      """  Type of Operation: P for Prep, D for Processing (Dispatchable in APS terminology).  """  
      self.APSAuxResource:str = obj["APSAuxResource"]
      """  Auxiliary resource requirements.   This is a comma and tilde delimited list of APSAuxResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  """  
      self.APSAddResource:str = obj["APSAddResource"]
      """  Additional resource requirements.   This is a comma and tilde delimited list of APSAddResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  For Additional Resources the Duration = 5 (entire Operation).  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  """  
      self.FAQty:int = obj["FAQty"]
      """  The quantity requested for first article inspection.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this part operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this part subcontract operation.  Can be zero if RFQ(s) are not required.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.OrigOprSeq:int = obj["OrigOprSeq"]
      """  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  """  
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operation to save on setups.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PrimarySetupOpDtl:int = obj["PrimarySetupOpDtl"]
      """   Identifies the primary ECOOpDtl to be used for setup.  The setup time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = S or B.  """  
      self.PrimaryProdOpDtl:int = obj["PrimaryProdOpDtl"]
      """   Identifies the primary ECOOpDtl to be used for production.  The production run time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = P or B.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description.  """  
      self.StageNumber:str = obj["StageNumber"]
      """  The stage number of the operations.  Entered only when the related PartRev.UseStaging flag is true.  """  
      self.BaseMethodOverridden:bool = obj["BaseMethodOverridden"]
      """  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  Parent Alternate Routing method of this part operation.  """  
      self.ParentOprSeq:int = obj["ParentOprSeq"]
      """  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  """  
      self.BrkQty01:int = obj["BrkQty01"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty02:int = obj["BrkQty02"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty03:int = obj["BrkQty03"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty04:int = obj["BrkQty04"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty05:int = obj["BrkQty05"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty06:int = obj["BrkQty06"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty07:int = obj["BrkQty07"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty08:int = obj["BrkQty08"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty09:int = obj["BrkQty09"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty10:int = obj["BrkQty10"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.PBrkCost01:int = obj["PBrkCost01"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost02:int = obj["PBrkCost02"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost03:int = obj["PBrkCost03"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost04:int = obj["PBrkCost04"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost05:int = obj["PBrkCost05"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost06:int = obj["PBrkCost06"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost07:int = obj["PBrkCost07"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost08:int = obj["PBrkCost08"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost09:int = obj["PBrkCost09"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost10:int = obj["PBrkCost10"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkStdRate01:int = obj["PBrkStdRate01"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate02:int = obj["PBrkStdRate02"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate03:int = obj["PBrkStdRate03"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate04:int = obj["PBrkStdRate04"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate05:int = obj["PBrkStdRate05"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate06:int = obj["PBrkStdRate06"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate07:int = obj["PBrkStdRate07"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate08:int = obj["PBrkStdRate08"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate09:int = obj["PBrkStdRate09"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate10:int = obj["PBrkStdRate10"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.SNRequiredOpr:bool = obj["SNRequiredOpr"]
      """  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  """  
      self.SNRequiredSubConShip:bool = obj["SNRequiredSubConShip"]
      """  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  """  
      self.Weight:int = obj["Weight"]
      """  Operation Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Operation Weight UOM defaulted from Part Master.  """  
      self.SendAheadType:str = obj["SendAheadType"]
      """   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  """  
      self.SendAheadOffset:int = obj["SendAheadOffset"]
      """   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  """  
      self.PrjRoleList:str = obj["PrjRoleList"]
      """  Delimited list of PrjRoleCd codes that are allowed for this operation.  """  
      self.UseAllRoles:bool = obj["UseAllRoles"]
      """  Allow use all Roles  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.PctReg:int = obj["PctReg"]
      """  PctReg  """  
      self.SetupMaterial:int = obj["SetupMaterial"]
      """  SetupMaterial  """  
      self.MaterialColorRating:int = obj["MaterialColorRating"]
      """  MaterialColorRating  """  
      self.MiscInfo1:str = obj["MiscInfo1"]
      """  MiscInfo1  """  
      self.MiscInfo2:str = obj["MiscInfo2"]
      """  MiscInfo2  """  
      self.SetupURL:str = obj["SetupURL"]
      """  SetupURL  """  
      self.ExpPctUp:int = obj["ExpPctUp"]
      """  ExpPctUp  """  
      self.ExpCycTm:int = obj["ExpCycTm"]
      """  ExpCycTm  """  
      self.ExpGood:int = obj["ExpGood"]
      """  ExpGood  """  
      self.NonProdLimit:int = obj["NonProdLimit"]
      """  NonProdLimit  """  
      self.AutoSpcEnable:bool = obj["AutoSpcEnable"]
      """  AutoSpcEnable  """  
      self.AutoSpcPeriod:int = obj["AutoSpcPeriod"]
      """  AutoSpcPeriod  """  
      self.PartQualEnable:bool = obj["PartQualEnable"]
      """  PartQualEnable  """  
      self.AutoSpcSubgroup:int = obj["AutoSpcSubgroup"]
      """  AutoSpcSubgroup  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PulsesPerCycle:int = obj["PulsesPerCycle"]
      """  PulsesPerCycle  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.TemplateID:str = obj["TemplateID"]
      """  TemplateID  """  
      self.SubRevisionNum:str = obj["SubRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOprListTableset:
   def __init__(self, obj):
      self.ECOOprList:list[Erp_Tablesets_ECOOprListRow] = obj["ECOOprList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ECOOprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Master Code - Links the JobOper  record with a OpMaster record. Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  """  
      self.EstSetHours:int = obj["EstSetHours"]
      """  The estimated set up hours. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours.  """  
      self.EstProdHours:int = obj["EstProdHours"]
      """   The estimated Production run hours for internal operations (Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (RunQty / Std).
If StdFormat = "PM" then (RunQty / Std ) / 60.
If StdFormat = "OH" then (RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (RunQty/Basis) X Std.
If StdFormat = "MP" then ((RunQty/Basis) X Std) / 60.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Production Quantity per one of the Parent Item.  """  
      self.Machines:int = obj["Machines"]
      """  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  Inventory UOM  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  """  
      self.DaysOut:int = obj["DaysOut"]
      """  Hours required is calculated as days * 8.  """  
      self.SubPartNum:str = obj["SubPartNum"]
      """  The PartNum to be shipped to the subcontract. Defaults as the Part number of the method to which it belongs (ECOOpr.PartNum).  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job operation comments.  """  
      self.SchedRelation:str = obj["SchedRelation"]
      """   Indicates the scheduling relationship between this and the preceding operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  """  
      self.RunQty:int = obj["RunQty"]
      """  The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0. This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  """  
      self.AddlSetupHours:int = obj["AddlSetupHours"]
      """  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calculations are rounded up to the next whole number before multiplying by the AddlSetUpHours.  """  
      self.AddlSetUpQty:int = obj["AddlSetUpQty"]
      """  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  """  
      self.APSPrepOp:int = obj["APSPrepOp"]
      """  Indicates the operation that must precede this operation.  Mainly used to model one to many routing structures.  """  
      self.APSNextOp:int = obj["APSNextOp"]
      """  This is the next operation in the routing.  -1 makes this operation the last one in the routing so far; -2 makes it the first one in the routing so far; 0 means no successor.  """  
      self.APSAltOp:int = obj["APSAltOp"]
      """  Specifies the operation for which this is an alternate.  """  
      self.APSSpecificResource:str = obj["APSSpecificResource"]
      """  Used to assign an operation to a specific resource so that APS does not schedule it elsewhere.  Overrides APSCapability.  """  
      self.APSCycleTime:int = obj["APSCycleTime"]
      """   Cycles per minute.
SQL:  IIF(CINT(JobOper.RunQty) = 0 OR JobOper.SubContract = TRUE, "0", JobOper.EstProdHours * 60 /  JobOper.RunQty)  """  
      self.APSConstantTime:int = obj["APSConstantTime"]
      """   Fixed time, in decimal minutes, to be added to the operation.  Can be used to represent cleanup time or model outsource time.
SQL: IFF(JobOper.SubContract = TRUE, (JobOper.DaysOut * 1440), "0")  """  
      self.APSSetupGroup:int = obj["APSSetupGroup"]
      """  Used to group operations to save on setups.  """  
      self.APSMakeFactor:int = obj["APSMakeFactor"]
      """  Quantity of Part per cycle.  """  
      self.APSContainerSize:int = obj["APSContainerSize"]
      """  Quantity that must be completed before the next operation can start (for overlap); quantity per batch (for batch resources); Auxiliary resource quantity.  """  
      self.APSSchedulerName:str = obj["APSSchedulerName"]
      """  Name of the APS Scheduler Module in which to schedule this operation.  """  
      self.APSMaxLength:int = obj["APSMaxLength"]
      """  If the scheduled time exceeds this value then the operation is split into operations which do not exceed this length.  """  
      self.APSTransferTime:int = obj["APSTransferTime"]
      """  Time between the end of this operation and the start time of the successor operation.  """  
      self.APSEffectiveness:int = obj["APSEffectiveness"]
      """  Cycle time and constant times are divided by this value to get schedule times.  Zeros disable this feature.  """  
      self.APSOperationClass:str = obj["APSOperationClass"]
      """  Type of Operation: P for Prep, D for Processing (Dispatchable in APS terminology).  """  
      self.APSAuxResource:str = obj["APSAuxResource"]
      """  Auxiliary resource requirements.   This is a comma and tilde delimited list of APSAuxResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  """  
      self.APSAddResource:str = obj["APSAddResource"]
      """  Additional resource requirements.   This is a comma and tilde delimited list of APSAddResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  For Additional Resources the Duration = 5 (entire Operation).  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  """  
      self.FAQty:int = obj["FAQty"]
      """  The quantity requested for first article inspection.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this part operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this part subcontract operation.  Can be zero if RFQ(s) are not required.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.OrigOprSeq:int = obj["OrigOprSeq"]
      """  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  """  
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operation to save on setups.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PrimarySetupOpDtl:int = obj["PrimarySetupOpDtl"]
      """   Identifies the primary ECOOpDtl to be used for setup.  The setup time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = S or B.  """  
      self.PrimaryProdOpDtl:int = obj["PrimaryProdOpDtl"]
      """   Identifies the primary ECOOpDtl to be used for production.  The production run time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = P or B.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description.  """  
      self.StageNumber:str = obj["StageNumber"]
      """  The stage number of the operations.  Entered only when the related PartRev.UseStaging flag is true.  """  
      self.BaseMethodOverridden:bool = obj["BaseMethodOverridden"]
      """  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  Parent Alternate Routing method of this part operation.  """  
      self.ParentOprSeq:int = obj["ParentOprSeq"]
      """  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  """  
      self.BrkQty01:int = obj["BrkQty01"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty02:int = obj["BrkQty02"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty03:int = obj["BrkQty03"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty04:int = obj["BrkQty04"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty05:int = obj["BrkQty05"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty06:int = obj["BrkQty06"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty07:int = obj["BrkQty07"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty08:int = obj["BrkQty08"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty09:int = obj["BrkQty09"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty10:int = obj["BrkQty10"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.PBrkCost01:int = obj["PBrkCost01"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost02:int = obj["PBrkCost02"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost03:int = obj["PBrkCost03"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost04:int = obj["PBrkCost04"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost05:int = obj["PBrkCost05"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost06:int = obj["PBrkCost06"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost07:int = obj["PBrkCost07"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost08:int = obj["PBrkCost08"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost09:int = obj["PBrkCost09"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost10:int = obj["PBrkCost10"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkStdRate01:int = obj["PBrkStdRate01"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate02:int = obj["PBrkStdRate02"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate03:int = obj["PBrkStdRate03"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate04:int = obj["PBrkStdRate04"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate05:int = obj["PBrkStdRate05"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate06:int = obj["PBrkStdRate06"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate07:int = obj["PBrkStdRate07"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate08:int = obj["PBrkStdRate08"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate09:int = obj["PBrkStdRate09"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate10:int = obj["PBrkStdRate10"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.SNRequiredOpr:bool = obj["SNRequiredOpr"]
      """  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  """  
      self.SNRequiredSubConShip:bool = obj["SNRequiredSubConShip"]
      """  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  """  
      self.Weight:int = obj["Weight"]
      """  Operation Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Operation Weight UOM defaulted from Part Master.  """  
      self.SendAheadType:str = obj["SendAheadType"]
      """   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  """  
      self.SendAheadOffset:int = obj["SendAheadOffset"]
      """   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  """  
      self.PrjRoleList:str = obj["PrjRoleList"]
      """  Delimited list of PrjRoleCd codes that are allowed for this operation.  """  
      self.UseAllRoles:bool = obj["UseAllRoles"]
      """  Allow use all Roles  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.PctReg:int = obj["PctReg"]
      """  PctReg  """  
      self.SetupMaterial:int = obj["SetupMaterial"]
      """  SetupMaterial  """  
      self.MaterialColorRating:int = obj["MaterialColorRating"]
      """  MaterialColorRating  """  
      self.MiscInfo1:str = obj["MiscInfo1"]
      """  MiscInfo1  """  
      self.MiscInfo2:str = obj["MiscInfo2"]
      """  MiscInfo2  """  
      self.SetupURL:str = obj["SetupURL"]
      """  SetupURL  """  
      self.ExpPctUp:int = obj["ExpPctUp"]
      """  ExpPctUp  """  
      self.ExpCycTm:int = obj["ExpCycTm"]
      """  ExpCycTm  """  
      self.ExpGood:int = obj["ExpGood"]
      """  ExpGood  """  
      self.NonProdLimit:int = obj["NonProdLimit"]
      """  NonProdLimit  """  
      self.AutoSpcEnable:bool = obj["AutoSpcEnable"]
      """  AutoSpcEnable  """  
      self.AutoSpcPeriod:int = obj["AutoSpcPeriod"]
      """  AutoSpcPeriod  """  
      self.PartQualEnable:bool = obj["PartQualEnable"]
      """  PartQualEnable  """  
      self.AutoSpcSubgroup:int = obj["AutoSpcSubgroup"]
      """  AutoSpcSubgroup  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PulsesPerCycle:int = obj["PulsesPerCycle"]
      """  PulsesPerCycle  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.TemplateID:str = obj["TemplateID"]
      """  TemplateID  """  
      self.SubRevisionNum:str = obj["SubRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.DspBillAddr:str = obj["DspBillAddr"]
      """  The vendor's name and bill to address  """  
      self.EnableSNReqSubConShip:bool = obj["EnableSNReqSubConShip"]
      """  Field used to control the flag on SNRequiredSubConShip field on UI screens.  """  
      self.EnableSNRequiredOpr:bool = obj["EnableSNRequiredOpr"]
      """  Used as a flag to enable controls on UI screens  """  
      self.FinalOpr:bool = obj["FinalOpr"]
      """  The final operation field  """  
      self.HasPriceBreaks:bool = obj["HasPriceBreaks"]
      """  Flag to let you know if you have price breaks.  """  
      self.IsPartOpr:bool = obj["IsPartOpr"]
      """  Is this a PartOpr?  Used when building the tree to show PartOpr as ECOOpr.  """  
      self.OldOprSeq:int = obj["OldOprSeq"]
      """  The original or old OprSeq.  Used when changing the OprSeq.  """  
      self.OpStdDescription:str = obj["OpStdDescription"]
      self.PLMChar03:str = obj["PLMChar03"]
      """  PML ID  """  
      self.PrimaryResourceGrpDesc:str = obj["PrimaryResourceGrpDesc"]
      """  Primary Resource Group description  """  
      self.PrimaryResourceGrpID:str = obj["PrimaryResourceGrpID"]
      """  The Resource Group ID of the primary production operation detail.  """  
      self.RefreshResources:bool = obj["RefreshResources"]
      """  Indicates if the scheduling resources should be refreshed when the op code changes.  """  
      self.SetHoursPerMach:int = obj["SetHoursPerMach"]
      """  The setup hours per machines.  """  
      self.StdFrmtDesc:str = obj["StdFrmtDesc"]
      """  The standard format description.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  The value of the ecorev.usestaging field for UI purposes  """  
      self.AutoReceive:bool = obj["AutoReceive"]
      """  The auto receive field  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.PrimaryProdOpDtlDesc:str = obj["PrimaryProdOpDtlDesc"]
      self.PrimarySetupOpDtlDesc:str = obj["PrimarySetupOpDtlDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.APSSchedulerNameAPSSchedulerName:str = obj["APSSchedulerNameAPSSchedulerName"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PrimaryProdOpDtlOpDtlDesc:str = obj["PrimaryProdOpDtlOpDtlDesc"]
      self.PrimarySetupOpDtlOpDtlDesc:str = obj["PrimarySetupOpDtlOpDtlDesc"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      self.SetupGroupDescription:str = obj["SetupGroupDescription"]
      self.StageNoDescription:str = obj["StageNoDescription"]
      self.SubPartNumTrackInventoryAttributes:bool = obj["SubPartNumTrackInventoryAttributes"]
      self.SubPartNumPricePerCode:str = obj["SubPartNumPricePerCode"]
      self.SubPartNumTrackDimension:bool = obj["SubPartNumTrackDimension"]
      self.SubPartNumTrackSerialNum:bool = obj["SubPartNumTrackSerialNum"]
      self.SubPartNumSellingFactor:int = obj["SubPartNumSellingFactor"]
      self.SubPartNumTrackLots:bool = obj["SubPartNumTrackLots"]
      self.SubPartNumSalesUM:str = obj["SubPartNumSalesUM"]
      self.SubPartNumPartDescription:str = obj["SubPartNumPartDescription"]
      self.SubPartNumIUM:str = obj["SubPartNumIUM"]
      self.SubPartNumAttrClassID:str = obj["SubPartNumAttrClassID"]
      self.SubPartNumTrackInventoryByRevision:bool = obj["SubPartNumTrackInventoryByRevision"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOprSearchTableset:
   def __init__(self, obj):
      self.ECOOpr:list[Erp_Tablesets_ECOOprRow] = obj["ECOOpr"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtECOOprSearchTableset:
   def __init__(self, obj):
      self.ECOOpr:list[Erp_Tablesets_ECOOprRow] = obj["ECOOpr"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   oprSeq
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      self.oprSeq:int = obj["oprSeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ECOOprSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ECOOprSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ECOOprSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ECOOprListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewECOOpr_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ECOOprSearchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      pass

class GetNewECOOpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ECOOprSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseECOOpr
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseECOOpr:str = obj["whereClauseECOOpr"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ECOOprSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtECOOprSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtECOOprSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ECOOprSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ECOOprSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

