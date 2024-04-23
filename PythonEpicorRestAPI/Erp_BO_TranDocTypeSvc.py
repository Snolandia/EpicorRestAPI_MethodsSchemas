import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TranDocTypeSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_TranDocTypes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TranDocTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TranDocTypes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TranDocTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypes",headers=creds) as resp:
           return await resp.json()

async def post_TranDocTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TranDocTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TranDocTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TranDocTypes_Company_TranDocTypeID(Company, TranDocTypeID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TranDocType item
   Description: Calls GetByID to retrieve the TranDocType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TranDocType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TranDocTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypes(" + Company + "," + TranDocTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TranDocTypes_Company_TranDocTypeID(Company, TranDocTypeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TranDocType for the service
   Description: Calls UpdateExt to update TranDocType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TranDocType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TranDocTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypes(" + Company + "," + TranDocTypeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TranDocTypes_Company_TranDocTypeID(Company, TranDocTypeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TranDocType item
   Description: Call UpdateExt to delete TranDocType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TranDocType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypes(" + Company + "," + TranDocTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_TranDocTypes_Company_TranDocTypeID_TranDocTypeAuths(Company, TranDocTypeID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TranDocTypeAuths items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TranDocTypeAuths1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TranDocTypeAuthRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypes(" + Company + "," + TranDocTypeID + ")/TranDocTypeAuths",headers=creds) as resp:
           return await resp.json()

async def get_TranDocTypes_Company_TranDocTypeID_TranDocTypeAuths_Company_TranDocTypeID_DcdUserID(Company, TranDocTypeID, DcdUserID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TranDocTypeAuth item
   Description: Calls GetByID to retrieve the TranDocTypeAuth item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TranDocTypeAuth1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TranDocTypeAuthRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypes(" + Company + "," + TranDocTypeID + ")/TranDocTypeAuths(" + Company + "," + TranDocTypeID + "," + DcdUserID + ")",headers=creds) as resp:
           return await resp.json()

async def get_TranDocTypeAuths(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TranDocTypeAuths items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TranDocTypeAuths
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TranDocTypeAuthRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypeAuths",headers=creds) as resp:
           return await resp.json()

async def post_TranDocTypeAuths(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TranDocTypeAuths
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TranDocTypeAuthRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TranDocTypeAuthRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypeAuths", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TranDocTypeAuths_Company_TranDocTypeID_DcdUserID(Company, TranDocTypeID, DcdUserID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TranDocTypeAuth item
   Description: Calls GetByID to retrieve the TranDocTypeAuth item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TranDocTypeAuth
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TranDocTypeAuthRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypeAuths(" + Company + "," + TranDocTypeID + "," + DcdUserID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TranDocTypeAuths_Company_TranDocTypeID_DcdUserID(Company, TranDocTypeID, DcdUserID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TranDocTypeAuth for the service
   Description: Calls UpdateExt to update TranDocTypeAuth. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TranDocTypeAuth
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TranDocTypeAuthRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypeAuths(" + Company + "," + TranDocTypeID + "," + DcdUserID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TranDocTypeAuths_Company_TranDocTypeID_DcdUserID(Company, TranDocTypeID, DcdUserID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TranDocTypeAuth item
   Description: Call UpdateExt to delete TranDocTypeAuth item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TranDocTypeAuth
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypeAuths(" + Company + "," + TranDocTypeID + "," + DcdUserID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TranDocTypeListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseTranDocType, whereClauseTranDocTypeAuth, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseTranDocType=" + whereClauseTranDocType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTranDocTypeAuth=" + whereClauseTranDocTypeAuth
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(tranDocTypeID, epicorHeaders = None):
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
   params += "tranDocTypeID=" + tranDocTypeID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAllUsers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAllUsers
   Description: This method validates All Users flag.
   OperationID: OnChangeAllUsers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAllUsers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAllUsers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAuthUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAuthUser
   Description: This method check if the selected User has alreay default Transaction
Document Type.for this type to update flag Default correctly.
   OperationID: OnChangeAuthUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAuthUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAuthUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeELIDefReportID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeELIDefReportID
   Description: OnChangeELIDefReportID
   OperationID: OnChangeELIDefReportID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeELIDefReportID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeELIDefReportID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TranDocTypeAuthValidate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TranDocTypeAuthValidate
   Description: Check for TranDocTypeAuth is unique
   OperationID: TranDocTypeAuthValidate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TranDocTypeAuthValidate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TranDocTypeAuthValidate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistDefaultTranDocType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistDefaultTranDocType
   OperationID: ExistDefaultTranDocType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistDefaultTranDocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistDefaultTranDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePECode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePECode
   OperationID: OnChangePECode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePECode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePECode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTranDocType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTranDocType
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTranDocType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTranDocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTranDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTranDocTypeAuth(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTranDocTypeAuth
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTranDocTypeAuth
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTranDocTypeAuth_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTranDocTypeAuth_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TranDocTypeAuthRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TranDocTypeAuthRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TranDocTypeListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TranDocTypeListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TranDocTypeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TranDocTypeRow] = obj["value"]
      pass

class Erp_Tablesets_TranDocTypeAuthRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.TranDocTypeAuthLine:int = obj["TranDocTypeAuthLine"]
      """  TranDocTypeAuthLine  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  DcdUserID  """  
      self.SystemTranID:str = obj["SystemTranID"]
      """  SystemTranID  """  
      self.DefaultTranDocType:bool = obj["DefaultTranDocType"]
      """  DefaultTranDocType  """  
      self.FirstForUser:bool = obj["FirstForUser"]
      """  FirstForUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TranDocTypeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SystemTranID:str = obj["SystemTranID"]
      """   The system transaction id assigned to the document type.  Values are:
ARInvoice - AR Invoices
CreditMemo - Credit Memos
PromNote - Promissory Notes
PackSlip - Packing Slips (Customer Shipments)
MiscShip - Miscellaneous Shipments
SCShip - Subcontractor Shipments
TOOrderShip - Transfer Order Shipments
WTaxCert - Withholding Tax Certificates  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive  """  
      self.SystemTranDefault:bool = obj["SystemTranDefault"]
      """  Indicates if the document type is the default for the system transaction.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  Government Uniform Invoice Format Code (Taiwan Localization field)  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  Government Uniform Invoice Deduct Code (Taiwan Localization field)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableSystemTran:bool = obj["EnableSystemTran"]
      """  According to the value of this field SystemTranDefault and Inactive field will be disable or enables.  """  
      self.RowIDSystemTranDefault:str = obj["RowIDSystemTranDefault"]
      """  When SystemTranDefault is marked then looking for the previous SystranDefault, store the ID if is loaded in UI to updated it.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TranDocTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SystemTranID:str = obj["SystemTranID"]
      """   The system transaction id assigned to the document type.  Values are:
ARInvoice - AR Invoices
CreditMemo - Credit Memos
PromNote - Promissory Notes
PackSlip - Packing Slips (Customer Shipments)
MiscShip - Miscellaneous Shipments
SCShip - Subcontractor Shipments
TOOrderShip - Transfer Order Shipments
WTaxCert - Withholding Tax Certificates  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive  """  
      self.SystemTranDefault:bool = obj["SystemTranDefault"]
      """  Indicates if the document type is the default for the system transaction.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  Government Uniform Invoice Format Code (Taiwan Localization field)  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  Government Uniform Invoice Deduct Code (Taiwan Localization field)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAGIPCode:str = obj["AGAGIPCode"]
      """  AGAGIPCode  """  
      self.AGARBACode:str = obj["AGARBACode"]
      """  AGARBACode  """  
      self.AGCOMARBCode:str = obj["AGCOMARBCode"]
      """  AGCOMARBCode  """  
      self.AGDefaultLetter:str = obj["AGDefaultLetter"]
      """  AGDefaultLetter  """  
      self.Returns:bool = obj["Returns"]
      """  Returns  """  
      self.AllUsers:bool = obj["AllUsers"]
      """  AllUsers  """  
      self.PENRInvoices:bool = obj["PENRInvoices"]
      """   Peru Localization Field.      
Non-Resident Invoices  """  
      self.EInvoice:bool = obj["EInvoice"]
      """  EInvoice  """  
      self.PostTaxDeclaration:bool = obj["PostTaxDeclaration"]
      """  PostTaxDeclaration  """  
      self.TWGenerationType:str = obj["TWGenerationType"]
      """  TWGenerationType  """  
      self.INIsExcisable:bool = obj["INIsExcisable"]
      """  Obsolete  """  
      self.INExportType:str = obj["INExportType"]
      """  INExportType  """  
      self.INPurchaseType:str = obj["INPurchaseType"]
      """  Obsolete  """  
      self.INIsServiceType:bool = obj["INIsServiceType"]
      """  Obsolete  """  
      self.PESunatTDT:str = obj["PESunatTDT"]
      """  Peru CSF: SUNAT Table 10  """  
      self.SelfInvoice:bool = obj["SelfInvoice"]
      """  SelfInvoice  """  
      self.PESUNATDetOpType:str = obj["PESUNATDetOpType"]
      """  PESUNATDetOpType  """  
      self.PEInvoiceType:str = obj["PEInvoiceType"]
      """  Peru invoice type  """  
      self.MYOwnUse:bool = obj["MYOwnUse"]
      """  Own Use  """  
      self.ELIEinvoice:bool = obj["ELIEinvoice"]
      """  ELIEinvoice  """  
      self.ELIDefaultEinvoice:bool = obj["ELIDefaultEinvoice"]
      """  ELIDefaultEinvoice  """  
      self.ELIDefReportID:str = obj["ELIDefReportID"]
      """  ELIDefReportID  """  
      self.ELIDefStyleNum:int = obj["ELIDefStyleNum"]
      """  ELIDefStyleNum  """  
      self.ELIDefToMail:str = obj["ELIDefToMail"]
      """  ELIDefToMail  """  
      self.ELIDefCCMail:str = obj["ELIDefCCMail"]
      """  ELIDefCCMail  """  
      self.ELIDefMailTempID:str = obj["ELIDefMailTempID"]
      """  ELIDefMailTempID  """  
      self.ELIDefFromMail:str = obj["ELIDefFromMail"]
      """  ELIDefFromMail  """  
      self.ExternalType:str = obj["ExternalType"]
      """  UNTDID 1001  """  
      self.ELIOperatorCode:str = obj["ELIOperatorCode"]
      """  Operator Code  """  
      self.ELIRcptDefStyleNum:int = obj["ELIRcptDefStyleNum"]
      """  Default E-invoice Report ID  """  
      self.EnableSystemTran:bool = obj["EnableSystemTran"]
      """  According to the value of this field SystemTranDefault and Inactive field will be disable or enables.  """  
      self.PEInvoiceTypeDesc:str = obj["PEInvoiceTypeDesc"]
      self.RedStornoOpt:str = obj["RedStornoOpt"]
      self.RowIDSystemTranDefault:str = obj["RowIDSystemTranDefault"]
      """  When SystemTranDefault is marked then looking for the previous SystranDefault, store the ID if is loaded in UI to updated it.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   tranDocTypeID
   """  
   def __init__(self, obj):
      self.tranDocTypeID:str = obj["tranDocTypeID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_TranDocTypeAuthRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.TranDocTypeAuthLine:int = obj["TranDocTypeAuthLine"]
      """  TranDocTypeAuthLine  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  DcdUserID  """  
      self.SystemTranID:str = obj["SystemTranID"]
      """  SystemTranID  """  
      self.DefaultTranDocType:bool = obj["DefaultTranDocType"]
      """  DefaultTranDocType  """  
      self.FirstForUser:bool = obj["FirstForUser"]
      """  FirstForUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TranDocTypeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SystemTranID:str = obj["SystemTranID"]
      """   The system transaction id assigned to the document type.  Values are:
ARInvoice - AR Invoices
CreditMemo - Credit Memos
PromNote - Promissory Notes
PackSlip - Packing Slips (Customer Shipments)
MiscShip - Miscellaneous Shipments
SCShip - Subcontractor Shipments
TOOrderShip - Transfer Order Shipments
WTaxCert - Withholding Tax Certificates  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive  """  
      self.SystemTranDefault:bool = obj["SystemTranDefault"]
      """  Indicates if the document type is the default for the system transaction.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  Government Uniform Invoice Format Code (Taiwan Localization field)  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  Government Uniform Invoice Deduct Code (Taiwan Localization field)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableSystemTran:bool = obj["EnableSystemTran"]
      """  According to the value of this field SystemTranDefault and Inactive field will be disable or enables.  """  
      self.RowIDSystemTranDefault:str = obj["RowIDSystemTranDefault"]
      """  When SystemTranDefault is marked then looking for the previous SystranDefault, store the ID if is loaded in UI to updated it.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TranDocTypeListTableset:
   def __init__(self, obj):
      self.TranDocTypeList:list[Erp_Tablesets_TranDocTypeListRow] = obj["TranDocTypeList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TranDocTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SystemTranID:str = obj["SystemTranID"]
      """   The system transaction id assigned to the document type.  Values are:
ARInvoice - AR Invoices
CreditMemo - Credit Memos
PromNote - Promissory Notes
PackSlip - Packing Slips (Customer Shipments)
MiscShip - Miscellaneous Shipments
SCShip - Subcontractor Shipments
TOOrderShip - Transfer Order Shipments
WTaxCert - Withholding Tax Certificates  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive  """  
      self.SystemTranDefault:bool = obj["SystemTranDefault"]
      """  Indicates if the document type is the default for the system transaction.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  Government Uniform Invoice Format Code (Taiwan Localization field)  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  Government Uniform Invoice Deduct Code (Taiwan Localization field)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAGIPCode:str = obj["AGAGIPCode"]
      """  AGAGIPCode  """  
      self.AGARBACode:str = obj["AGARBACode"]
      """  AGARBACode  """  
      self.AGCOMARBCode:str = obj["AGCOMARBCode"]
      """  AGCOMARBCode  """  
      self.AGDefaultLetter:str = obj["AGDefaultLetter"]
      """  AGDefaultLetter  """  
      self.Returns:bool = obj["Returns"]
      """  Returns  """  
      self.AllUsers:bool = obj["AllUsers"]
      """  AllUsers  """  
      self.PENRInvoices:bool = obj["PENRInvoices"]
      """   Peru Localization Field.      
Non-Resident Invoices  """  
      self.EInvoice:bool = obj["EInvoice"]
      """  EInvoice  """  
      self.PostTaxDeclaration:bool = obj["PostTaxDeclaration"]
      """  PostTaxDeclaration  """  
      self.TWGenerationType:str = obj["TWGenerationType"]
      """  TWGenerationType  """  
      self.INIsExcisable:bool = obj["INIsExcisable"]
      """  Obsolete  """  
      self.INExportType:str = obj["INExportType"]
      """  INExportType  """  
      self.INPurchaseType:str = obj["INPurchaseType"]
      """  Obsolete  """  
      self.INIsServiceType:bool = obj["INIsServiceType"]
      """  Obsolete  """  
      self.PESunatTDT:str = obj["PESunatTDT"]
      """  Peru CSF: SUNAT Table 10  """  
      self.SelfInvoice:bool = obj["SelfInvoice"]
      """  SelfInvoice  """  
      self.PESUNATDetOpType:str = obj["PESUNATDetOpType"]
      """  PESUNATDetOpType  """  
      self.PEInvoiceType:str = obj["PEInvoiceType"]
      """  Peru invoice type  """  
      self.MYOwnUse:bool = obj["MYOwnUse"]
      """  Own Use  """  
      self.ELIEinvoice:bool = obj["ELIEinvoice"]
      """  ELIEinvoice  """  
      self.ELIDefaultEinvoice:bool = obj["ELIDefaultEinvoice"]
      """  ELIDefaultEinvoice  """  
      self.ELIDefReportID:str = obj["ELIDefReportID"]
      """  ELIDefReportID  """  
      self.ELIDefStyleNum:int = obj["ELIDefStyleNum"]
      """  ELIDefStyleNum  """  
      self.ELIDefToMail:str = obj["ELIDefToMail"]
      """  ELIDefToMail  """  
      self.ELIDefCCMail:str = obj["ELIDefCCMail"]
      """  ELIDefCCMail  """  
      self.ELIDefMailTempID:str = obj["ELIDefMailTempID"]
      """  ELIDefMailTempID  """  
      self.ELIDefFromMail:str = obj["ELIDefFromMail"]
      """  ELIDefFromMail  """  
      self.ExternalType:str = obj["ExternalType"]
      """  UNTDID 1001  """  
      self.ELIOperatorCode:str = obj["ELIOperatorCode"]
      """  Operator Code  """  
      self.ELIRcptDefStyleNum:int = obj["ELIRcptDefStyleNum"]
      """  Default E-invoice Report ID  """  
      self.EnableSystemTran:bool = obj["EnableSystemTran"]
      """  According to the value of this field SystemTranDefault and Inactive field will be disable or enables.  """  
      self.PEInvoiceTypeDesc:str = obj["PEInvoiceTypeDesc"]
      self.RedStornoOpt:str = obj["RedStornoOpt"]
      self.RowIDSystemTranDefault:str = obj["RowIDSystemTranDefault"]
      """  When SystemTranDefault is marked then looking for the previous SystranDefault, store the ID if is loaded in UI to updated it.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TranDocTypeTableset:
   def __init__(self, obj):
      self.TranDocType:list[Erp_Tablesets_TranDocTypeRow] = obj["TranDocType"]
      self.TranDocTypeAuth:list[Erp_Tablesets_TranDocTypeAuthRow] = obj["TranDocTypeAuth"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtTranDocTypeTableset:
   def __init__(self, obj):
      self.TranDocType:list[Erp_Tablesets_TranDocTypeRow] = obj["TranDocType"]
      self.TranDocTypeAuth:list[Erp_Tablesets_TranDocTypeAuthRow] = obj["TranDocTypeAuth"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExistDefaultTranDocType_input:
   """ Required : 
   systemTranID
   userID
   """  
   def __init__(self, obj):
      self.systemTranID:str = obj["systemTranID"]
      self.userID:str = obj["userID"]
      pass

class ExistDefaultTranDocType_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   tranDocTypeID
   """  
   def __init__(self, obj):
      self.tranDocTypeID:str = obj["tranDocTypeID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TranDocTypeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TranDocTypeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TranDocTypeTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TranDocTypeListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewTranDocTypeAuth_input:
   """ Required : 
   ds
   tranDocTypeID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TranDocTypeTableset] = obj["ds"]
      self.tranDocTypeID:str = obj["tranDocTypeID"]
      pass

class GetNewTranDocTypeAuth_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDocTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTranDocType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TranDocTypeTableset] = obj["ds"]
      pass

class GetNewTranDocType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDocTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseTranDocType
   whereClauseTranDocTypeAuth
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTranDocType:str = obj["whereClauseTranDocType"]
      self.whereClauseTranDocTypeAuth:str = obj["whereClauseTranDocTypeAuth"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TranDocTypeTableset] = obj["returnObj"]
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

class OnChangeAllUsers_input:
   """ Required : 
   ds
   pAllUsers
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TranDocTypeTableset] = obj["ds"]
      self.pAllUsers:bool = obj["pAllUsers"]
      """  The proposed All Users value  """  
      pass

class OnChangeAllUsers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDocTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeAuthUser_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TranDocTypeTableset] = obj["ds"]
      pass

class OnChangeAuthUser_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDocTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeELIDefReportID_input:
   """ Required : 
   eliDefReportID
   ds
   """  
   def __init__(self, obj):
      self.eliDefReportID:str = obj["eliDefReportID"]
      self.ds:list[Erp_Tablesets_TranDocTypeTableset] = obj["ds"]
      pass

class OnChangeELIDefReportID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDocTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePECode_input:
   """ Required : 
   codeType
   ds
   """  
   def __init__(self, obj):
      self.codeType:str = obj["codeType"]
      self.ds:list[Erp_Tablesets_TranDocTypeTableset] = obj["ds"]
      pass

class OnChangePECode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDocTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class TranDocTypeAuthValidate_input:
   """ Required : 
   tranDocTypeID
   dcdUserID
   """  
   def __init__(self, obj):
      self.tranDocTypeID:str = obj["tranDocTypeID"]
      """  TranDocTypeID  """  
      self.dcdUserID:str = obj["dcdUserID"]
      """  DcdUserID  """  
      pass

class TranDocTypeAuthValidate_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTranDocTypeTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTranDocTypeTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TranDocTypeTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDocTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

