import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.ExtCompanySvc
# Description: ExtCompany object
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanies(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtCompanies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtCompanies
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtCompanyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/ExtCompanies",headers=creds) as resp:
           return await resp.json()

async def post_ExtCompanies(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtCompanies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ExtCompanyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ExtCompanyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/ExtCompanies", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanies_Company_ExtSystemID_ExtCompanyID(Company, ExtSystemID, ExtCompanyID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtCompany item
   Description: Calls GetByID to retrieve the ExtCompany item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompany
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtCompanyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtCompanies_Company_ExtSystemID_ExtCompanyID(Company, ExtSystemID, ExtCompanyID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtCompany for the service
   Description: Calls UpdateExt to update ExtCompany. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtCompany
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ExtCompanyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtCompanies_Company_ExtSystemID_ExtCompanyID(Company, ExtSystemID, ExtCompanyID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtCompany item
   Description: Call UpdateExt to delete ExtCompany item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtCompany
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanies_Company_ExtSystemID_ExtCompanyID_IntTransIns(Company, ExtSystemID, ExtCompanyID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get IntTransIns items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_IntTransIns1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IntTransInRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")/IntTransIns",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanies_Company_ExtSystemID_ExtCompanyID_IntTransIns_Company_ExtSystemID_ExtCompanyID_DBSchemaName_DBTableName_DBFieldName_InboundValue_DBFieldValue(Company, ExtSystemID, ExtCompanyID, DBSchemaName, DBTableName, DBFieldName, InboundValue, DBFieldValue, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IntTransIn item
   Description: Calls GetByID to retrieve the IntTransIn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IntTransIn1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param DBSchemaName: Desc: DBSchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param DBFieldName: Desc: DBFieldName   Required: True   Allow empty value : True
      :param InboundValue: Desc: InboundValue   Required: True   Allow empty value : True
      :param DBFieldValue: Desc: DBFieldValue   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.IntTransInRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")/IntTransIns(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + DBSchemaName + "," + DBTableName + "," + DBFieldName + "," + InboundValue + "," + DBFieldValue + ")",headers=creds) as resp:
           return await resp.json()

async def get_IntTransIns(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get IntTransIns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IntTransIns
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IntTransInRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/IntTransIns",headers=creds) as resp:
           return await resp.json()

async def post_IntTransIns(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IntTransIns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.IntTransInRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.IntTransInRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/IntTransIns", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_IntTransIns_Company_ExtSystemID_ExtCompanyID_DBSchemaName_DBTableName_DBFieldName_InboundValue_DBFieldValue(Company, ExtSystemID, ExtCompanyID, DBSchemaName, DBTableName, DBFieldName, InboundValue, DBFieldValue, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IntTransIn item
   Description: Calls GetByID to retrieve the IntTransIn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IntTransIn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param DBSchemaName: Desc: DBSchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param DBFieldName: Desc: DBFieldName   Required: True   Allow empty value : True
      :param InboundValue: Desc: InboundValue   Required: True   Allow empty value : True
      :param DBFieldValue: Desc: DBFieldValue   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.IntTransInRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/IntTransIns(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + DBSchemaName + "," + DBTableName + "," + DBFieldName + "," + InboundValue + "," + DBFieldValue + ")",headers=creds) as resp:
           return await resp.json()

async def patch_IntTransIns_Company_ExtSystemID_ExtCompanyID_DBSchemaName_DBTableName_DBFieldName_InboundValue_DBFieldValue(Company, ExtSystemID, ExtCompanyID, DBSchemaName, DBTableName, DBFieldName, InboundValue, DBFieldValue, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update IntTransIn for the service
   Description: Calls UpdateExt to update IntTransIn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_IntTransIn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param DBSchemaName: Desc: DBSchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param DBFieldName: Desc: DBFieldName   Required: True   Allow empty value : True
      :param InboundValue: Desc: InboundValue   Required: True   Allow empty value : True
      :param DBFieldValue: Desc: DBFieldValue   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.IntTransInRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/IntTransIns(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + DBSchemaName + "," + DBTableName + "," + DBFieldName + "," + InboundValue + "," + DBFieldValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_IntTransIns_Company_ExtSystemID_ExtCompanyID_DBSchemaName_DBTableName_DBFieldName_InboundValue_DBFieldValue(Company, ExtSystemID, ExtCompanyID, DBSchemaName, DBTableName, DBFieldName, InboundValue, DBFieldValue, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete IntTransIn item
   Description: Call UpdateExt to delete IntTransIn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_IntTransIn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param DBSchemaName: Desc: DBSchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param DBFieldName: Desc: DBFieldName   Required: True   Allow empty value : True
      :param InboundValue: Desc: InboundValue   Required: True   Allow empty value : True
      :param DBFieldValue: Desc: DBFieldValue   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/IntTransIns(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + DBSchemaName + "," + DBTableName + "," + DBFieldName + "," + InboundValue + "," + DBFieldValue + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtCompanyListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseExtCompany, whereClauseIntTransIn, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseExtCompany=" + whereClauseExtCompany
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseIntTransIn=" + whereClauseIntTransIn
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(extSystemID, extCompanyID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "extSystemID=" + extSystemID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "extCompanyID=" + extCompanyID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtCompany
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewIntTransIn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewIntTransIn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewIntTransIn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIntTransIn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIntTransIn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtCompanyListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ExtCompanyListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtCompanyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ExtCompanyRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IntTransInRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_IntTransInRow] = obj["value"]
      pass

class Ice_Tablesets_ExtCompanyListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.ListDelimiter:str = obj["ListDelimiter"]
      """  The character to use as a List Delimiter for interfacing with an external system.  """  
      self.ExtCompanyName:str = obj["ExtCompanyName"]
      """  Name or description of the external company.  """  
      self.AppServerURL:str = obj["AppServerURL"]
      """  Application Server URL  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtCompanyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.ListDelimiter:str = obj["ListDelimiter"]
      """  The character to use as a List Delimiter for interfacing with an external system.  """  
      self.ExtCompanyName:str = obj["ExtCompanyName"]
      """  Name or description of the external company.  """  
      self.AppServerURL:str = obj["AppServerURL"]
      """  Application Server URL  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IntTransInRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  DBSchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  Database table name  """  
      self.DBFieldName:str = obj["DBFieldName"]
      """  Database field name  """  
      self.DBFieldValue:str = obj["DBFieldValue"]
      """  Value to which the Inbound value will be translated on an Inbound transaction from an External Integration.  """  
      self.InboundValue:str = obj["InboundValue"]
      """  Inbound value from an External Integration.  This value will be translated to the Database field value.  """  
      self.DefaultValue:bool = obj["DefaultValue"]
      """  Default Value.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   extSystemID
   extCompanyID
   """  
   def __init__(self, obj):
      self.extSystemID:str = obj["extSystemID"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   extSystemID
   extCompanyID
   """  
   def __init__(self, obj):
      self.extSystemID:str = obj["extSystemID"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ExtCompanyTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ExtCompanyTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ExtCompanyTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ExtCompanyListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewExtCompany_input:
   """ Required : 
   ds
   extSystemID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ExtCompanyTableset] = obj["ds"]
      self.extSystemID:str = obj["extSystemID"]
      pass

class GetNewExtCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewIntTransIn_input:
   """ Required : 
   ds
   extSystemID
   extCompanyID
   dbSchemaName
   dbTableName
   dbFieldName
   inboundValue
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ExtCompanyTableset] = obj["ds"]
      self.extSystemID:str = obj["extSystemID"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.dbSchemaName:str = obj["dbSchemaName"]
      self.dbTableName:str = obj["dbTableName"]
      self.dbFieldName:str = obj["dbFieldName"]
      self.inboundValue:str = obj["inboundValue"]
      pass

class GetNewIntTransIn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseExtCompany
   whereClauseIntTransIn
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseExtCompany:str = obj["whereClauseExtCompany"]
      self.whereClauseIntTransIn:str = obj["whereClauseIntTransIn"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ExtCompanyTableset] = obj["returnObj"]
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

class Ice_Tablesets_ExtCompanyListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.ListDelimiter:str = obj["ListDelimiter"]
      """  The character to use as a List Delimiter for interfacing with an external system.  """  
      self.ExtCompanyName:str = obj["ExtCompanyName"]
      """  Name or description of the external company.  """  
      self.AppServerURL:str = obj["AppServerURL"]
      """  Application Server URL  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtCompanyListTableset:
   def __init__(self, obj):
      self.ExtCompanyList:list[Ice_Tablesets_ExtCompanyListRow] = obj["ExtCompanyList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ExtCompanyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.ListDelimiter:str = obj["ListDelimiter"]
      """  The character to use as a List Delimiter for interfacing with an external system.  """  
      self.ExtCompanyName:str = obj["ExtCompanyName"]
      """  Name or description of the external company.  """  
      self.AppServerURL:str = obj["AppServerURL"]
      """  Application Server URL  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtCompanyTableset:
   def __init__(self, obj):
      self.ExtCompany:list[Ice_Tablesets_ExtCompanyRow] = obj["ExtCompany"]
      self.IntTransIn:list[Ice_Tablesets_IntTransInRow] = obj["IntTransIn"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_IntTransInRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  DBSchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  Database table name  """  
      self.DBFieldName:str = obj["DBFieldName"]
      """  Database field name  """  
      self.DBFieldValue:str = obj["DBFieldValue"]
      """  Value to which the Inbound value will be translated on an Inbound transaction from an External Integration.  """  
      self.InboundValue:str = obj["InboundValue"]
      """  Inbound value from an External Integration.  This value will be translated to the Database field value.  """  
      self.DefaultValue:bool = obj["DefaultValue"]
      """  Default Value.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UpdExtExtCompanyTableset:
   def __init__(self, obj):
      self.ExtCompany:list[Ice_Tablesets_ExtCompanyRow] = obj["ExtCompany"]
      self.IntTransIn:list[Ice_Tablesets_IntTransInRow] = obj["IntTransIn"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtExtCompanyTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtExtCompanyTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

