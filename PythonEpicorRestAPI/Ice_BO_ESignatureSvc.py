import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.ESignatureSvc
# Description: ESginature Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ESignatures(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ESignatures items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ESignatures
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ESignatureAuditRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/ESignatures",headers=creds) as resp:
           return await resp.json()

async def post_ESignatures(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ESignatures
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ESignatureAuditRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ESignatureAuditRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/ESignatures", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ESignatures_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ESignature item
   Description: Calls GetByID to retrieve the ESignature item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ESignature
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ESignatureAuditRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/ESignatures(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ESignatures_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ESignature for the service
   Description: Calls UpdateExt to update ESignature. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ESignature
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ESignatureAuditRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/ESignatures(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ESignatures_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ESignature item
   Description: Call UpdateExt to delete ESignature item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ESignature
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/ESignatures(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ESignatureAuditListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseESignatureAudit, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseESignatureAudit=" + whereClauseESignatureAudit
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(sysRowID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "sysRowID=" + sysRowID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetByRelatedToSysRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByRelatedToSysRowID
   Description: Return ESignature record base on RelatedToSysRowID
   OperationID: GetByRelatedToSysRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByRelatedToSysRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByRelatedToSysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DoesESignatureAuditExist(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DoesESignatureAuditExist
   Description: Check to see if report exists.
   OperationID: DoesESignatureAuditExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DoesESignatureAuditExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DoesESignatureAuditExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewESignatureAudit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewESignatureAudit
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewESignatureAudit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewESignatureAudit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewESignatureAudit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ESignatureSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ESignatureAuditListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ESignatureAuditListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ESignatureAuditRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ESignatureAuditRow] = obj["value"]
      pass

class Ice_Tablesets_ESignatureAuditListRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  RelatedToTableName  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.DirectiveID:str = obj["DirectiveID"]
      """  DirectiveID  """  
      self.DirectiveSource:str = obj["DirectiveSource"]
      """  DirectiveSource  """  
      self.DirectiveName:str = obj["DirectiveName"]
      """  DirectiveName  """  
      self.DirectiveMethod:str = obj["DirectiveMethod"]
      """  DirectiveMethod  """  
      self.DirectiveType:int = obj["DirectiveType"]
      """  DirectiveType  """  
      self.DirectiveTypeName:str = obj["DirectiveTypeName"]
      """  DirectiveTypeName  """  
      self.SignedToken:str = obj["SignedToken"]
      """  SignedToken  """  
      self.SecGroupCode:str = obj["SecGroupCode"]
      """  SecGroupCode  """  
      self.RequestedBy:str = obj["RequestedBy"]
      """  RequestedBy  """  
      self.RequestedByName:str = obj["RequestedByName"]
      """  RequestedByName  """  
      self.RequestedByEMailAddress:str = obj["RequestedByEMailAddress"]
      """  RequestedByEmailAddress  """  
      self.RequestedByTimeZone:str = obj["RequestedByTimeZone"]
      """  RequestedByTimeZone  """  
      self.SignedBy:str = obj["SignedBy"]
      """  SignedBy  """  
      self.SignedByName:str = obj["SignedByName"]
      """  SignedByName  """  
      self.SignedByEMailAddress:str = obj["SignedByEMailAddress"]
      """  SignedByEmailAddress  """  
      self.SignedByTimeZone:str = obj["SignedByTimeZone"]
      """  SignedByTimeZone  """  
      self.SignedOn:str = obj["SignedOn"]
      """  SignedOn  """  
      self.ICEVersion:str = obj["ICEVersion"]
      """  ICEVersion  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ESignatureAuditRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  RelatedToTableName  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.DirectiveID:str = obj["DirectiveID"]
      """  DirectiveID  """  
      self.DirectiveSource:str = obj["DirectiveSource"]
      """  DirectiveSource  """  
      self.DirectiveName:str = obj["DirectiveName"]
      """  DirectiveName  """  
      self.DirectiveMethod:str = obj["DirectiveMethod"]
      """  DirectiveMethod  """  
      self.DirectiveType:int = obj["DirectiveType"]
      """  DirectiveType  """  
      self.DirectiveTypeName:str = obj["DirectiveTypeName"]
      """  DirectiveTypeName  """  
      self.SignedToken:str = obj["SignedToken"]
      """  SignedToken  """  
      self.SecGroupCode:str = obj["SecGroupCode"]
      """  SecGroupCode  """  
      self.RequestedBy:str = obj["RequestedBy"]
      """  RequestedBy  """  
      self.RequestedByName:str = obj["RequestedByName"]
      """  RequestedByName  """  
      self.RequestedByEMailAddress:str = obj["RequestedByEMailAddress"]
      """  RequestedByEmailAddress  """  
      self.RequestedByTimeZone:str = obj["RequestedByTimeZone"]
      """  RequestedByTimeZone  """  
      self.SignedBy:str = obj["SignedBy"]
      """  SignedBy  """  
      self.SignedByName:str = obj["SignedByName"]
      """  SignedByName  """  
      self.SignedByEMailAddress:str = obj["SignedByEMailAddress"]
      """  SignedByEmailAddress  """  
      self.SignedByTimeZone:str = obj["SignedByTimeZone"]
      """  SignedByTimeZone  """  
      self.SignedOn:str = obj["SignedOn"]
      """  SignedOn  """  
      self.ICEVersion:str = obj["ICEVersion"]
      """  ICEVersion  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.TransactionText:str = obj["TransactionText"]
      """  TransactionText  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   sysRowID
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DoesESignatureAuditExist_input:
   """ Required : 
   relatedToSysRowID
   """  
   def __init__(self, obj):
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      """  RelatedToSysRowID that is referencing from other tables.  """  
      pass

class DoesESignatureAuditExist_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  `true` if the ESignatureAudit exists.  """  
      pass

class GetByID_input:
   """ Required : 
   sysRowID
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ESignatureTableset] = obj["returnObj"]
      pass

class GetByRelatedToSysRowID_input:
   """ Required : 
   relatedToSysRowID
   """  
   def __init__(self, obj):
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      """  RelatedToSysRowID that is referencing from other tables.  """  
      pass

class GetByRelatedToSysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ESignatureTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ESignatureTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ESignatureTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ESignatureAuditListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewESignatureAudit_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ESignatureTableset] = obj["ds"]
      pass

class GetNewESignatureAudit_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ESignatureTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseESignatureAudit
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseESignatureAudit:str = obj["whereClauseESignatureAudit"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ESignatureTableset] = obj["returnObj"]
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

class Ice_Tablesets_ESignatureAuditListRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  RelatedToTableName  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.DirectiveID:str = obj["DirectiveID"]
      """  DirectiveID  """  
      self.DirectiveSource:str = obj["DirectiveSource"]
      """  DirectiveSource  """  
      self.DirectiveName:str = obj["DirectiveName"]
      """  DirectiveName  """  
      self.DirectiveMethod:str = obj["DirectiveMethod"]
      """  DirectiveMethod  """  
      self.DirectiveType:int = obj["DirectiveType"]
      """  DirectiveType  """  
      self.DirectiveTypeName:str = obj["DirectiveTypeName"]
      """  DirectiveTypeName  """  
      self.SignedToken:str = obj["SignedToken"]
      """  SignedToken  """  
      self.SecGroupCode:str = obj["SecGroupCode"]
      """  SecGroupCode  """  
      self.RequestedBy:str = obj["RequestedBy"]
      """  RequestedBy  """  
      self.RequestedByName:str = obj["RequestedByName"]
      """  RequestedByName  """  
      self.RequestedByEMailAddress:str = obj["RequestedByEMailAddress"]
      """  RequestedByEmailAddress  """  
      self.RequestedByTimeZone:str = obj["RequestedByTimeZone"]
      """  RequestedByTimeZone  """  
      self.SignedBy:str = obj["SignedBy"]
      """  SignedBy  """  
      self.SignedByName:str = obj["SignedByName"]
      """  SignedByName  """  
      self.SignedByEMailAddress:str = obj["SignedByEMailAddress"]
      """  SignedByEmailAddress  """  
      self.SignedByTimeZone:str = obj["SignedByTimeZone"]
      """  SignedByTimeZone  """  
      self.SignedOn:str = obj["SignedOn"]
      """  SignedOn  """  
      self.ICEVersion:str = obj["ICEVersion"]
      """  ICEVersion  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ESignatureAuditListTableset:
   def __init__(self, obj):
      self.ESignatureAuditList:list[Ice_Tablesets_ESignatureAuditListRow] = obj["ESignatureAuditList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ESignatureAuditRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  RelatedToTableName  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.DirectiveID:str = obj["DirectiveID"]
      """  DirectiveID  """  
      self.DirectiveSource:str = obj["DirectiveSource"]
      """  DirectiveSource  """  
      self.DirectiveName:str = obj["DirectiveName"]
      """  DirectiveName  """  
      self.DirectiveMethod:str = obj["DirectiveMethod"]
      """  DirectiveMethod  """  
      self.DirectiveType:int = obj["DirectiveType"]
      """  DirectiveType  """  
      self.DirectiveTypeName:str = obj["DirectiveTypeName"]
      """  DirectiveTypeName  """  
      self.SignedToken:str = obj["SignedToken"]
      """  SignedToken  """  
      self.SecGroupCode:str = obj["SecGroupCode"]
      """  SecGroupCode  """  
      self.RequestedBy:str = obj["RequestedBy"]
      """  RequestedBy  """  
      self.RequestedByName:str = obj["RequestedByName"]
      """  RequestedByName  """  
      self.RequestedByEMailAddress:str = obj["RequestedByEMailAddress"]
      """  RequestedByEmailAddress  """  
      self.RequestedByTimeZone:str = obj["RequestedByTimeZone"]
      """  RequestedByTimeZone  """  
      self.SignedBy:str = obj["SignedBy"]
      """  SignedBy  """  
      self.SignedByName:str = obj["SignedByName"]
      """  SignedByName  """  
      self.SignedByEMailAddress:str = obj["SignedByEMailAddress"]
      """  SignedByEmailAddress  """  
      self.SignedByTimeZone:str = obj["SignedByTimeZone"]
      """  SignedByTimeZone  """  
      self.SignedOn:str = obj["SignedOn"]
      """  SignedOn  """  
      self.ICEVersion:str = obj["ICEVersion"]
      """  ICEVersion  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.TransactionText:str = obj["TransactionText"]
      """  TransactionText  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ESignatureTableset:
   def __init__(self, obj):
      self.ESignatureAudit:list[Ice_Tablesets_ESignatureAuditRow] = obj["ESignatureAudit"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtESignatureTableset:
   def __init__(self, obj):
      self.ESignatureAudit:list[Ice_Tablesets_ESignatureAuditRow] = obj["ESignatureAudit"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtESignatureTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtESignatureTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ESignatureTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ESignatureTableset] = obj["ds"]
      pass

      """  output parameters  """  

