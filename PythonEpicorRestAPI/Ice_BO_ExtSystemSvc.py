import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.ExtSystemSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ExtSystems(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtSystems items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtSystems
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtSystemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/ExtSystems",headers=creds) as resp:
           return await resp.json()

async def post_ExtSystems(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtSystems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ExtSystemRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ExtSystemRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/ExtSystems", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtSystems_ExtSystemID_TransferMethod(ExtSystemID, TransferMethod, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtSystem item
   Description: Calls GetByID to retrieve the ExtSystem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtSystem
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param TransferMethod: Desc: TransferMethod   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtSystemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/ExtSystems(" + ExtSystemID + "," + TransferMethod + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtSystems_ExtSystemID_TransferMethod(ExtSystemID, TransferMethod, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtSystem for the service
   Description: Calls UpdateExt to update ExtSystem. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtSystem
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param TransferMethod: Desc: TransferMethod   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ExtSystemRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/ExtSystems(" + ExtSystemID + "," + TransferMethod + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtSystems_ExtSystemID_TransferMethod(ExtSystemID, TransferMethod, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtSystem item
   Description: Call UpdateExt to delete ExtSystem item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtSystem
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param TransferMethod: Desc: TransferMethod   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/ExtSystems(" + ExtSystemID + "," + TransferMethod + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtSystems_ExtSystemID_TransferMethod_ExtCompanies(ExtSystemID, TransferMethod, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ExtCompanies items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtCompanies1
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param TransferMethod: Desc: TransferMethod   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/ExtSystems(" + ExtSystemID + "," + TransferMethod + ")/ExtCompanies",headers=creds) as resp:
           return await resp.json()

async def get_ExtSystems_ExtSystemID_TransferMethod_ExtCompanies_Company_ExtSystemID_ExtCompanyID(ExtSystemID, TransferMethod, Company, ExtCompanyID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtCompany item
   Description: Calls GetByID to retrieve the ExtCompany item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompany1
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param TransferMethod: Desc: TransferMethod   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/ExtSystems(" + ExtSystemID + "," + TransferMethod + ")/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanies(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtCompanies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtCompanies
      :param select: Desc: Odata select comma delimited list of fields
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/ExtCompanies",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/ExtCompanies", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanies_Company_ExtSystemID_ExtCompanyID(Company, ExtSystemID, ExtCompanyID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtCompany item
   Description: Calls GetByID to retrieve the ExtCompany item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompany
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtSystemListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseExtSystem, whereClauseExtCompany, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseExtSystem=" + whereClauseExtSystem
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(extSystemID, transferMethod, epicorHeaders = None):
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
   params += "transferMethod=" + transferMethod

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_TestSBConnect(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TestSBConnect
   Description: Test Connectivity to Service Bus with connection information supplied for ExtSystemID
   OperationID: TestSBConnect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestSBConnect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestSBConnect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtSystem(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtSystem
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtSystem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtSystem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtSystem_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtSystemSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtCompanyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ExtCompanyRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtSystemListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ExtSystemListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtSystemRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ExtSystemRow] = obj["value"]
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

class Ice_Tablesets_ExtSystemListRow:
   def __init__(self, obj):
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.ExtSystemName:str = obj["ExtSystemName"]
      """  Full Name of external package  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.FinancialInt:bool = obj["FinancialInt"]
      """  Financial Integration flag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReceiveChgLog:bool = obj["ReceiveChgLog"]
      """  Indicates whether to Receive ChgLog records  """  
      self.EnableServiceBus:bool = obj["EnableServiceBus"]
      """  Indicates whether the Sonic password should be enabled/disabled  """  
      self.ReceiveFin:bool = obj["ReceiveFin"]
      """  Indicates whether to Receive Financial records  """  
      self.ReceiveOrd:bool = obj["ReceiveOrd"]
      """  Indicates whether to Receive Order records  """  
      self.ReceiveProd:bool = obj["ReceiveProd"]
      """  Indicates whether to Receive Production records  """  
      self.ReceiveHelp:bool = obj["ReceiveHelp"]
      """  Indicates whether to Receive Help Desk records  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtSystemRow:
   def __init__(self, obj):
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.ExtSystemName:str = obj["ExtSystemName"]
      """  Full Name of external package  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.FinancialInt:bool = obj["FinancialInt"]
      """  Financial Integration flag  """  
      self.ServiceBusServerFQDN:str = obj["ServiceBusServerFQDN"]
      """  ServiceBusServerFQDN  """  
      self.ServiceBusHTTPPort:int = obj["ServiceBusHTTPPort"]
      """  ServiceBusHTTPPort  """  
      self.ServiceBusTCPPort:int = obj["ServiceBusTCPPort"]
      """  ServiceBusTCPPort  """  
      self.ServiceBusNamespace:str = obj["ServiceBusNamespace"]
      """  ServiceBusNamespace  """  
      self.ServiceBusSecretIssuerName:str = obj["ServiceBusSecretIssuerName"]
      """  ServiceBusSecretIssuerName  """  
      self.ServiceBusSecretIssuerSecret:str = obj["ServiceBusSecretIssuerSecret"]
      """  ServiceBusSecretIssuerSecret  """  
      self.EnvironmentID:str = obj["EnvironmentID"]
      """  EnvironmentID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SBDomain:str = obj["SBDomain"]
      """  SBDomain  """  
      self.SBUser:str = obj["SBUser"]
      """  SBUser  """  
      self.SBPassword:str = obj["SBPassword"]
      """  SBPassword  """  
      self.SBTokenProvider:str = obj["SBTokenProvider"]
      """  SBTokenProvider  """  
      self.SBConnectionString:str = obj["SBConnectionString"]
      """  SBConnectionString  """  
      self.Settings:str = obj["Settings"]
      """  Settings  """  
      self.EnableServiceBus:bool = obj["EnableServiceBus"]
      """  Indicates whether the Sonic password should be enabled/disabled  """  
      self.ReceiveChgLog:bool = obj["ReceiveChgLog"]
      """  Indicates whether to Receive ChgLog records  """  
      self.ReceiveFin:bool = obj["ReceiveFin"]
      """  Indicates whether to Receive Financial records  """  
      self.ReceiveHelp:bool = obj["ReceiveHelp"]
      """  Indicates whether to Receive Help Desk records  """  
      self.ReceiveOrd:bool = obj["ReceiveOrd"]
      """  Indicates whether to Receive Order records  """  
      self.ReceiveProd:bool = obj["ReceiveProd"]
      """  Indicates whether to Receive Production records  """  
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
   transferMethod
   """  
   def __init__(self, obj):
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   extSystemID
   transferMethod
   """  
   def __init__(self, obj):
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ExtSystemTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ExtSystemTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ExtSystemTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ExtSystemListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewExtCompany_input:
   """ Required : 
   ds
   company
   extSystemID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ExtSystemTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      pass

class GetNewExtCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ExtSystemTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtSystem_input:
   """ Required : 
   ds
   extSystemID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ExtSystemTableset] = obj["ds"]
      self.extSystemID:str = obj["extSystemID"]
      pass

class GetNewExtSystem_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ExtSystemTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseExtSystem
   whereClauseExtCompany
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseExtSystem:str = obj["whereClauseExtSystem"]
      self.whereClauseExtCompany:str = obj["whereClauseExtCompany"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ExtSystemTableset] = obj["returnObj"]
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

class Ice_Tablesets_ExtSystemListRow:
   def __init__(self, obj):
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.ExtSystemName:str = obj["ExtSystemName"]
      """  Full Name of external package  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.FinancialInt:bool = obj["FinancialInt"]
      """  Financial Integration flag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReceiveChgLog:bool = obj["ReceiveChgLog"]
      """  Indicates whether to Receive ChgLog records  """  
      self.EnableServiceBus:bool = obj["EnableServiceBus"]
      """  Indicates whether the Sonic password should be enabled/disabled  """  
      self.ReceiveFin:bool = obj["ReceiveFin"]
      """  Indicates whether to Receive Financial records  """  
      self.ReceiveOrd:bool = obj["ReceiveOrd"]
      """  Indicates whether to Receive Order records  """  
      self.ReceiveProd:bool = obj["ReceiveProd"]
      """  Indicates whether to Receive Production records  """  
      self.ReceiveHelp:bool = obj["ReceiveHelp"]
      """  Indicates whether to Receive Help Desk records  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtSystemListTableset:
   def __init__(self, obj):
      self.ExtSystemList:list[Ice_Tablesets_ExtSystemListRow] = obj["ExtSystemList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ExtSystemRow:
   def __init__(self, obj):
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.ExtSystemName:str = obj["ExtSystemName"]
      """  Full Name of external package  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.FinancialInt:bool = obj["FinancialInt"]
      """  Financial Integration flag  """  
      self.ServiceBusServerFQDN:str = obj["ServiceBusServerFQDN"]
      """  ServiceBusServerFQDN  """  
      self.ServiceBusHTTPPort:int = obj["ServiceBusHTTPPort"]
      """  ServiceBusHTTPPort  """  
      self.ServiceBusTCPPort:int = obj["ServiceBusTCPPort"]
      """  ServiceBusTCPPort  """  
      self.ServiceBusNamespace:str = obj["ServiceBusNamespace"]
      """  ServiceBusNamespace  """  
      self.ServiceBusSecretIssuerName:str = obj["ServiceBusSecretIssuerName"]
      """  ServiceBusSecretIssuerName  """  
      self.ServiceBusSecretIssuerSecret:str = obj["ServiceBusSecretIssuerSecret"]
      """  ServiceBusSecretIssuerSecret  """  
      self.EnvironmentID:str = obj["EnvironmentID"]
      """  EnvironmentID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SBDomain:str = obj["SBDomain"]
      """  SBDomain  """  
      self.SBUser:str = obj["SBUser"]
      """  SBUser  """  
      self.SBPassword:str = obj["SBPassword"]
      """  SBPassword  """  
      self.SBTokenProvider:str = obj["SBTokenProvider"]
      """  SBTokenProvider  """  
      self.SBConnectionString:str = obj["SBConnectionString"]
      """  SBConnectionString  """  
      self.Settings:str = obj["Settings"]
      """  Settings  """  
      self.EnableServiceBus:bool = obj["EnableServiceBus"]
      """  Indicates whether the Sonic password should be enabled/disabled  """  
      self.ReceiveChgLog:bool = obj["ReceiveChgLog"]
      """  Indicates whether to Receive ChgLog records  """  
      self.ReceiveFin:bool = obj["ReceiveFin"]
      """  Indicates whether to Receive Financial records  """  
      self.ReceiveHelp:bool = obj["ReceiveHelp"]
      """  Indicates whether to Receive Help Desk records  """  
      self.ReceiveOrd:bool = obj["ReceiveOrd"]
      """  Indicates whether to Receive Order records  """  
      self.ReceiveProd:bool = obj["ReceiveProd"]
      """  Indicates whether to Receive Production records  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtSystemTableset:
   def __init__(self, obj):
      self.ExtSystem:list[Ice_Tablesets_ExtSystemRow] = obj["ExtSystem"]
      self.ExtCompany:list[Ice_Tablesets_ExtCompanyRow] = obj["ExtCompany"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtExtSystemTableset:
   def __init__(self, obj):
      self.ExtSystem:list[Ice_Tablesets_ExtSystemRow] = obj["ExtSystem"]
      self.ExtCompany:list[Ice_Tablesets_ExtCompanyRow] = obj["ExtCompany"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class TestSBConnect_input:
   """ Required : 
   ExtSystemID
   """  
   def __init__(self, obj):
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ID of external system  """  
      pass

class TestSBConnect_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.diagText:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtExtSystemTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtExtSystemTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ExtSystemTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ExtSystemTableset] = obj["ds"]
      pass

      """  output parameters  """  

