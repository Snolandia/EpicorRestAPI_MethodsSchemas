import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PayMethodSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PayMethods(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PayMethods items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PayMethods
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PayMethodRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethods",headers=creds) as resp:
           return await resp.json()

async def post_PayMethods(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PayMethods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PayMethodRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PayMethodRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethods", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PayMethods_Company_PMUID(Company, PMUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PayMethod item
   Description: Calls GetByID to retrieve the PayMethod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PayMethod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PMUID: Desc: PMUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PayMethodRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethods(" + Company + "," + PMUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PayMethods_Company_PMUID(Company, PMUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PayMethod for the service
   Description: Calls UpdateExt to update PayMethod. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PayMethod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PMUID: Desc: PMUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PayMethodRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethods(" + Company + "," + PMUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PayMethods_Company_PMUID(Company, PMUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PayMethod item
   Description: Call UpdateExt to delete PayMethod item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PayMethod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PMUID: Desc: PMUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethods(" + Company + "," + PMUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PayMethods_Company_PMUID_PayMethodProps(Company, PMUID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PayMethodProps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PayMethodProps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PMUID: Desc: PMUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PayMethodPropRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethods(" + Company + "," + PMUID + ")/PayMethodProps",headers=creds) as resp:
           return await resp.json()

async def get_PayMethods_Company_PMUID_PayMethodProps_Company_PMUID_EFTHeadUID_EFTPropUID(Company, PMUID, EFTHeadUID, EFTPropUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PayMethodProp item
   Description: Calls GetByID to retrieve the PayMethodProp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PayMethodProp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PMUID: Desc: PMUID   Required: True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param EFTPropUID: Desc: EFTPropUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PayMethodPropRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethods(" + Company + "," + PMUID + ")/PayMethodProps(" + Company + "," + PMUID + "," + EFTHeadUID + "," + EFTPropUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PayMethodProps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PayMethodProps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PayMethodProps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PayMethodPropRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethodProps",headers=creds) as resp:
           return await resp.json()

async def post_PayMethodProps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PayMethodProps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PayMethodPropRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PayMethodPropRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethodProps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PayMethodProps_Company_PMUID_EFTHeadUID_EFTPropUID(Company, PMUID, EFTHeadUID, EFTPropUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PayMethodProp item
   Description: Calls GetByID to retrieve the PayMethodProp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PayMethodProp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PMUID: Desc: PMUID   Required: True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param EFTPropUID: Desc: EFTPropUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PayMethodPropRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethodProps(" + Company + "," + PMUID + "," + EFTHeadUID + "," + EFTPropUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PayMethodProps_Company_PMUID_EFTHeadUID_EFTPropUID(Company, PMUID, EFTHeadUID, EFTPropUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PayMethodProp for the service
   Description: Calls UpdateExt to update PayMethodProp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PayMethodProp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PMUID: Desc: PMUID   Required: True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param EFTPropUID: Desc: EFTPropUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PayMethodPropRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethodProps(" + Company + "," + PMUID + "," + EFTHeadUID + "," + EFTPropUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PayMethodProps_Company_PMUID_EFTHeadUID_EFTPropUID(Company, PMUID, EFTHeadUID, EFTPropUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PayMethodProp item
   Description: Call UpdateExt to delete PayMethodProp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PayMethodProp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PMUID: Desc: PMUID   Required: True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param EFTPropUID: Desc: EFTPropUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethodProps(" + Company + "," + PMUID + "," + EFTHeadUID + "," + EFTPropUID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PayMethodListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePayMethod, whereClausePayMethodProp, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePayMethod=" + whereClausePayMethod
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePayMethodProp=" + whereClausePayMethodProp
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(pmUID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "pmUID=" + pmUID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetPayMethods(epicorHeaders = None):
   """  
   Summary: Invoke method GetPayMethods
   Description: Get the PayMethod List Tableset
   OperationID: GetPayMethods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPayMethods_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ChangePayMethodEFTHeadUID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePayMethodEFTHeadUID
   Description: Method to call when changing the paymethod electronic interface.
   OperationID: ChangePayMethodEFTHeadUID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePayMethodEFTHeadUID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePayMethodEFTHeadUID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePayMethodPMSource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePayMethodPMSource
   Description: Method to call when changing the paymethod source.
   OperationID: ChangePayMethodPMSource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePayMethodPMSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePayMethodPMSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePayMethodType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePayMethodType
   Description: Method to call when changing the paymethod source.
   OperationID: ChangePayMethodType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePayMethodType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePayMethodType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMXSATCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMXSATCode
   Description: Performs required logic when PayMethod.MXSATCode is modified.
   OperationID: ChangeMXSATCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMXSATCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMXSATCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCOPayMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCOPayMethod
   Description: Performs required logic when PayMethod.COPayMethod is modified.
   OperationID: ChangeCOPayMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCOPayMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCOPayMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteOldPayMethodProps(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteOldPayMethodProps
   Description: This method should be called when the Scope or Electronic Interface is changed
   OperationID: DeleteOldPayMethodProps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteOldPayMethodProps_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteOldPayMethodProps_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetIdByName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetIdByName
   Description: Method for retrieving ID, PMUID using Payment Method Name.
   OperationID: GetIdByName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIdByName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIdByName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_NameChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method NameChanged
   Description: get by name only
   OperationID: NameChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NameChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NameChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetAPInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetAPInfo
   Description: Enable APInfo Tab.
   OperationID: SetAPInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetAPInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetAPInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDepositSlipsCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDepositSlipsCodeDescList
   Description: Gets list of codes/descriptions for Deposit Slips combo-box
   OperationID: GetDepositSlipsCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDepositSlipsCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDepositSlipsCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListDepositSlips(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListDepositSlips
   Description: Returns a List Dataset for DepositSlips
   OperationID: GetListDepositSlips
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListDepositSlips_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListDepositSlips_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByNamePMSource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByNamePMSource
   Description: get by id alternate
   OperationID: GetByNamePMSource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByNamePMSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByNamePMSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_KChangePayMethodPMSource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method KChangePayMethodPMSource
   Description: Row changed event for PMSourceModule
   OperationID: KChangePayMethodPMSource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KChangePayMethodPMSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KChangePayMethodPMSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_KChangePayMethodEFTHeadUID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method KChangePayMethodEFTHeadUID
   Description: Row changed event for PMSourceModule
   OperationID: KChangePayMethodEFTHeadUID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KChangePayMethodEFTHeadUID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KChangePayMethodEFTHeadUID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_KChangePayMethodType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method KChangePayMethodType
   Description: Row changed event for Type
   OperationID: KChangePayMethodType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KChangePayMethodType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KChangePayMethodType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_KChangedType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method KChangedType
   Description: Row changed event for Type
   OperationID: KChangedType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KChangedType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KChangedType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_KChangedPMSource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method KChangedPMSource
   Description: Row changed event for PMSource
   OperationID: KChangedPMSource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KChangedPMSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KChangedPMSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfPayMethodType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfPayMethodType
   OperationID: OnChangeOfPayMethodType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfPayMethodType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfPayMethodType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPayMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPayMethod
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPayMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPayMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPayMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPayMethodProp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPayMethodProp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPayMethodProp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPayMethodProp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPayMethodProp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PayMethodListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodPropRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PayMethodPropRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PayMethodRow] = obj["value"]
      pass

class Erp_Tablesets_PayMethodListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.Name:str = obj["Name"]
      """  Name of the payment method  """  
      self.Type:int = obj["Type"]
      """   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Indicates the electronic interface that shall be used for the payment method  """  
      self.PIType:str = obj["PIType"]
      """  Payment Instrument Type  """  
      self.PIApprove:bool = obj["PIApprove"]
      """  Payment Instrument Approve flag  """  
      self.SysRowID:str = obj["SysRowID"]
      """  System Row ID - GUID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PayMethodPropRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Indicates the electronic interface that shall be used for the payment method  """  
      self.EFTPropUID:int = obj["EFTPropUID"]
      """  Unique identifier of the electronic interface property  """  
      self.PropValue:str = obj["PropValue"]
      """  Property Value, always defined as string value  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  System row ID - GUID  """  
      self.StringCol:str = obj["StringCol"]
      """  String Column  """  
      self.ListCol:str = obj["ListCol"]
      """  List Column  """  
      self.LogicalCol:bool = obj["LogicalCol"]
      """  Logical Column  """  
      self.DecimalCol:int = obj["DecimalCol"]
      """  Decimal Col  """  
      self.DateCol:str = obj["DateCol"]
      """  Date Column  """  
      self.Type:str = obj["Type"]
      """  Pay Method Type - string, list, logical, decimal, date  """  
      self.Name:str = obj["Name"]
      """  Pay Method Property Name  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PayMethodRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.Name:str = obj["Name"]
      """  Name of the payment method  """  
      self.Type:int = obj["Type"]
      """   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Indicates the electronic interface that shall be used for the payment method  """  
      self.OutputFile:str = obj["OutputFile"]
      """  This will be the default filename for the output file created by the electronic interface  """  
      self.OnlyBankCurr:bool = obj["OnlyBankCurr"]
      """  Indicates if this interface will only support payments in the currency of the bank. This will affect selection of invoices in the AP payment function.  """  
      self.PMSource:int = obj["PMSource"]
      """   Indicated the source of payment method
0 = AP payment method
1 = AR payment method  """  
      self.SummarizePerCustomer:bool = obj["SummarizePerCustomer"]
      """   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  """  
      self.DefPayCode:str = obj["DefPayCode"]
      """  Default Payment Code  """  
      self.AutoBankRec:bool = obj["AutoBankRec"]
      """  Auto Bank Reconciliation  """  
      self.SenderRef:str = obj["SenderRef"]
      """  Sender Reference  """  
      self.RegNum:str = obj["RegNum"]
      """  Registration Number  """  
      self.Test:bool = obj["Test"]
      """  Checkbox to indicate test transmissions  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  Reimbursable  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive flag  """  
      self.OverPayPct:int = obj["OverPayPct"]
      """  Contains the overpayment threshold allowed for ar invoices in bank file import.  """  
      self.UnderPayPct:int = obj["UnderPayPct"]
      """  Contains the underpayment threshold allowed for ar invoices in bank file import.  """  
      self.PIType:str = obj["PIType"]
      """  Payment Instrument Type  """  
      self.PIGenMethod:int = obj["PIGenMethod"]
      """  Payment Instrument Generation Method  """  
      self.PIApprove:bool = obj["PIApprove"]
      """  Payment Instrument Approve flag  """  
      self.GlobalPayMethod:bool = obj["GlobalPayMethod"]
      """  Marks this PayMethod as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  System Row ID - GUID  """  
      self.DepositSlips:int = obj["DepositSlips"]
      """  DepositSlips  """  
      self.IsPositiveBalance:bool = obj["IsPositiveBalance"]
      """  IsPositiveBalance  """  
      self.APGrouping:int = obj["APGrouping"]
      """  Specifies how the payments are processed in a bank - individually or in a batch  """  
      self.APIDGeneration:bool = obj["APIDGeneration"]
      """  When this check box is selected, the application uses identifiers generated via an EI program during processing  """  
      self.ARGrouping:int = obj["ARGrouping"]
      """  Allows the user to specify how the receipts are processed in a bank - individually or in a batch  """  
      self.ARIDGeneration:bool = obj["ARIDGeneration"]
      """  When this check box is selected, the application uses identifiers generated via an EI program during processing  """  
      self.ARIDTiming:int = obj["ARIDTiming"]
      """  Specify at what moment the application groups AR receipts in batches  """  
      self.EFTDebitMemoHandlingCode:str = obj["EFTDebitMemoHandlingCode"]
      """  EFTDebitMemoHandlingCode  """  
      self.EFTDebitMemoDueDate:str = obj["EFTDebitMemoDueDate"]
      """  EFTDebitMemoDueDate  """  
      self.EFTProductNumDate:str = obj["EFTProductNumDate"]
      """  EFTProductNumDate  """  
      self.EFTProductNumber:int = obj["EFTProductNumber"]
      """  EFTProductNumber  """  
      self.SEPO3Payment:bool = obj["SEPO3Payment"]
      """  SEPO3Payment  """  
      self.SECrossBrdPayMethod:str = obj["SECrossBrdPayMethod"]
      """  SECrossBrdPayMethod  """  
      self.SECurrPocket:str = obj["SECurrPocket"]
      """  SECurrPocket  """  
      self.SEErrorHandling:str = obj["SEErrorHandling"]
      """  SEErrorHandling  """  
      self.SEUseIBAN:str = obj["SEUseIBAN"]
      """  SEUseIBAN  """  
      self.SEPath:str = obj["SEPath"]
      """  SEPath  """  
      self.SECreateErrorLog:bool = obj["SECreateErrorLog"]
      """  SECreateErrorLog  """  
      self.SEFileForEachPayCurr:bool = obj["SEFileForEachPayCurr"]
      """  SEFileForEachPayCurr  """  
      self.NOPaymentList:bool = obj["NOPaymentList"]
      """  NOPaymentList  """  
      self.NOTelepayPayment:bool = obj["NOTelepayPayment"]
      """  NOTelepayPayment  """  
      self.NOTelepayReply:bool = obj["NOTelepayReply"]
      """  NOTelepayReply  """  
      self.DEFeeRule:str = obj["DEFeeRule"]
      """  DEFeeRule  """  
      self.DESerialNum:int = obj["DESerialNum"]
      """  DESerialNum  """  
      self.DEStateNum:str = obj["DEStateNum"]
      """  DEStateNum  """  
      self.DELastUseDate:str = obj["DELastUseDate"]
      """  DELastUseDate  """  
      self.MXPaidAs:str = obj["MXPaidAs"]
      """  MXPaidAs  """  
      self.MXPaymentNum:int = obj["MXPaymentNum"]
      """  MXPaymentNum  """  
      self.MXTotalPayments:int = obj["MXTotalPayments"]
      """  MXTotalPayments  """  
      self.MXPaymentType:int = obj["MXPaymentType"]
      """  The field specifies the mexican type of the payment: 2 – Check, 3 – Transfer, 0 – Other  """  
      self.MXSATCode:str = obj["MXSATCode"]
      """  MXSATCode  """  
      self.MXSATDesc:str = obj["MXSATDesc"]
      """  MXSATDesc  """  
      self.PymtProposal:bool = obj["PymtProposal"]
      """  PymtProposal  """  
      self.AutoCheckNum:bool = obj["AutoCheckNum"]
      """  AutoCheckNum  """  
      self.EnterPymtTotal:bool = obj["EnterPymtTotal"]
      """  EnterPymtTotal  """  
      self.CheckNumSeq:int = obj["CheckNumSeq"]
      """  CheckNumSeq  """  
      self.US1099KTranType:str = obj["US1099KTranType"]
      """  Form 1099-K Transaction Type  """  
      self.US1099KAmtThreshold:int = obj["US1099KAmtThreshold"]
      """  Form 1099-K Third Party Network Amount Threshold  """  
      self.US1099KTranThreshold:int = obj["US1099KTranThreshold"]
      """  Form 1099-K Third Party Network Transaction Threshold  """  
      self.COPayForm:str = obj["COPayForm"]
      """  COPayForm  """  
      self.COPayMethod:str = obj["COPayMethod"]
      """  COPayMethod  """  
      self.TypeCode:str = obj["TypeCode"]
      """  UNCL4461  """  
      self.EnableThresholds:bool = obj["EnableThresholds"]
      """  Indicates if the threshold fields are enabled  """  
      self.IsCZLocalization:bool = obj["IsCZLocalization"]
      self.PMSourceModule:str = obj["PMSourceModule"]
      """  Shows a char representation of a PMSource: 0 = AP, 1 = AR.  """  
      self.EnableAPInfo:bool = obj["EnableAPInfo"]
      """  EnableAPInfo  """  
      self.COPayMethodDesc:str = obj["COPayMethodDesc"]
      self.TypeDescription:str = obj["TypeDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.EFTHeadName:str = obj["EFTHeadName"]
      self.EFTHeadType:int = obj["EFTHeadType"]
      self.PITypeDescription:str = obj["PITypeDescription"]
      self.XbSystELIEinvoice:bool = obj["XbSystELIEinvoice"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeCOPayMethod_input:
   """ Required : 
   coPayFormCode
   ds
   """  
   def __init__(self, obj):
      self.coPayFormCode:str = obj["coPayFormCode"]
      """  Proposed input value  """  
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

class ChangeCOPayMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMXSATCode_input:
   """ Required : 
   ipMXSATCode
   ds
   """  
   def __init__(self, obj):
      self.ipMXSATCode:str = obj["ipMXSATCode"]
      """  Proposed input value of SAT Code / "Form of Payment"  """  
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

class ChangeMXSATCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePayMethodEFTHeadUID_input:
   """ Required : 
   ProposedEFTHeadUID
   ds
   """  
   def __init__(self, obj):
      self.ProposedEFTHeadUID:int = obj["ProposedEFTHeadUID"]
      """  The proposed paymethod electronic interface  """  
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

class ChangePayMethodEFTHeadUID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePayMethodPMSource_input:
   """ Required : 
   ProposedPMSourceModule
   ds
   """  
   def __init__(self, obj):
      self.ProposedPMSourceModule:str = obj["ProposedPMSourceModule"]
      """  The proposed paymethod source  """  
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

class ChangePayMethodPMSource_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePayMethodType_input:
   """ Required : 
   ProposedType
   ds
   """  
   def __init__(self, obj):
      self.ProposedType:int = obj["ProposedType"]
      """  The proposed paymethod type  """  
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

class ChangePayMethodType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   pmUID
   """  
   def __init__(self, obj):
      self.pmUID:int = obj["pmUID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteOldPayMethodProps_input:
   """ Required : 
   fieldChanged
   ds
   """  
   def __init__(self, obj):
      self.fieldChanged:str = obj["fieldChanged"]
      """  Indicates which field was changed that caused the method to be called.  """  
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

class DeleteOldPayMethodProps_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.returnMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_PayMethodListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.Name:str = obj["Name"]
      """  Name of the payment method  """  
      self.Type:int = obj["Type"]
      """   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Indicates the electronic interface that shall be used for the payment method  """  
      self.PIType:str = obj["PIType"]
      """  Payment Instrument Type  """  
      self.PIApprove:bool = obj["PIApprove"]
      """  Payment Instrument Approve flag  """  
      self.SysRowID:str = obj["SysRowID"]
      """  System Row ID - GUID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PayMethodListTableset:
   def __init__(self, obj):
      self.PayMethodList:list[Erp_Tablesets_PayMethodListRow] = obj["PayMethodList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PayMethodPropRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Indicates the electronic interface that shall be used for the payment method  """  
      self.EFTPropUID:int = obj["EFTPropUID"]
      """  Unique identifier of the electronic interface property  """  
      self.PropValue:str = obj["PropValue"]
      """  Property Value, always defined as string value  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  System row ID - GUID  """  
      self.StringCol:str = obj["StringCol"]
      """  String Column  """  
      self.ListCol:str = obj["ListCol"]
      """  List Column  """  
      self.LogicalCol:bool = obj["LogicalCol"]
      """  Logical Column  """  
      self.DecimalCol:int = obj["DecimalCol"]
      """  Decimal Col  """  
      self.DateCol:str = obj["DateCol"]
      """  Date Column  """  
      self.Type:str = obj["Type"]
      """  Pay Method Type - string, list, logical, decimal, date  """  
      self.Name:str = obj["Name"]
      """  Pay Method Property Name  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PayMethodRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.Name:str = obj["Name"]
      """  Name of the payment method  """  
      self.Type:int = obj["Type"]
      """   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Indicates the electronic interface that shall be used for the payment method  """  
      self.OutputFile:str = obj["OutputFile"]
      """  This will be the default filename for the output file created by the electronic interface  """  
      self.OnlyBankCurr:bool = obj["OnlyBankCurr"]
      """  Indicates if this interface will only support payments in the currency of the bank. This will affect selection of invoices in the AP payment function.  """  
      self.PMSource:int = obj["PMSource"]
      """   Indicated the source of payment method
0 = AP payment method
1 = AR payment method  """  
      self.SummarizePerCustomer:bool = obj["SummarizePerCustomer"]
      """   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  """  
      self.DefPayCode:str = obj["DefPayCode"]
      """  Default Payment Code  """  
      self.AutoBankRec:bool = obj["AutoBankRec"]
      """  Auto Bank Reconciliation  """  
      self.SenderRef:str = obj["SenderRef"]
      """  Sender Reference  """  
      self.RegNum:str = obj["RegNum"]
      """  Registration Number  """  
      self.Test:bool = obj["Test"]
      """  Checkbox to indicate test transmissions  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  Reimbursable  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive flag  """  
      self.OverPayPct:int = obj["OverPayPct"]
      """  Contains the overpayment threshold allowed for ar invoices in bank file import.  """  
      self.UnderPayPct:int = obj["UnderPayPct"]
      """  Contains the underpayment threshold allowed for ar invoices in bank file import.  """  
      self.PIType:str = obj["PIType"]
      """  Payment Instrument Type  """  
      self.PIGenMethod:int = obj["PIGenMethod"]
      """  Payment Instrument Generation Method  """  
      self.PIApprove:bool = obj["PIApprove"]
      """  Payment Instrument Approve flag  """  
      self.GlobalPayMethod:bool = obj["GlobalPayMethod"]
      """  Marks this PayMethod as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  System Row ID - GUID  """  
      self.DepositSlips:int = obj["DepositSlips"]
      """  DepositSlips  """  
      self.IsPositiveBalance:bool = obj["IsPositiveBalance"]
      """  IsPositiveBalance  """  
      self.APGrouping:int = obj["APGrouping"]
      """  Specifies how the payments are processed in a bank - individually or in a batch  """  
      self.APIDGeneration:bool = obj["APIDGeneration"]
      """  When this check box is selected, the application uses identifiers generated via an EI program during processing  """  
      self.ARGrouping:int = obj["ARGrouping"]
      """  Allows the user to specify how the receipts are processed in a bank - individually or in a batch  """  
      self.ARIDGeneration:bool = obj["ARIDGeneration"]
      """  When this check box is selected, the application uses identifiers generated via an EI program during processing  """  
      self.ARIDTiming:int = obj["ARIDTiming"]
      """  Specify at what moment the application groups AR receipts in batches  """  
      self.EFTDebitMemoHandlingCode:str = obj["EFTDebitMemoHandlingCode"]
      """  EFTDebitMemoHandlingCode  """  
      self.EFTDebitMemoDueDate:str = obj["EFTDebitMemoDueDate"]
      """  EFTDebitMemoDueDate  """  
      self.EFTProductNumDate:str = obj["EFTProductNumDate"]
      """  EFTProductNumDate  """  
      self.EFTProductNumber:int = obj["EFTProductNumber"]
      """  EFTProductNumber  """  
      self.SEPO3Payment:bool = obj["SEPO3Payment"]
      """  SEPO3Payment  """  
      self.SECrossBrdPayMethod:str = obj["SECrossBrdPayMethod"]
      """  SECrossBrdPayMethod  """  
      self.SECurrPocket:str = obj["SECurrPocket"]
      """  SECurrPocket  """  
      self.SEErrorHandling:str = obj["SEErrorHandling"]
      """  SEErrorHandling  """  
      self.SEUseIBAN:str = obj["SEUseIBAN"]
      """  SEUseIBAN  """  
      self.SEPath:str = obj["SEPath"]
      """  SEPath  """  
      self.SECreateErrorLog:bool = obj["SECreateErrorLog"]
      """  SECreateErrorLog  """  
      self.SEFileForEachPayCurr:bool = obj["SEFileForEachPayCurr"]
      """  SEFileForEachPayCurr  """  
      self.NOPaymentList:bool = obj["NOPaymentList"]
      """  NOPaymentList  """  
      self.NOTelepayPayment:bool = obj["NOTelepayPayment"]
      """  NOTelepayPayment  """  
      self.NOTelepayReply:bool = obj["NOTelepayReply"]
      """  NOTelepayReply  """  
      self.DEFeeRule:str = obj["DEFeeRule"]
      """  DEFeeRule  """  
      self.DESerialNum:int = obj["DESerialNum"]
      """  DESerialNum  """  
      self.DEStateNum:str = obj["DEStateNum"]
      """  DEStateNum  """  
      self.DELastUseDate:str = obj["DELastUseDate"]
      """  DELastUseDate  """  
      self.MXPaidAs:str = obj["MXPaidAs"]
      """  MXPaidAs  """  
      self.MXPaymentNum:int = obj["MXPaymentNum"]
      """  MXPaymentNum  """  
      self.MXTotalPayments:int = obj["MXTotalPayments"]
      """  MXTotalPayments  """  
      self.MXPaymentType:int = obj["MXPaymentType"]
      """  The field specifies the mexican type of the payment: 2 – Check, 3 – Transfer, 0 – Other  """  
      self.MXSATCode:str = obj["MXSATCode"]
      """  MXSATCode  """  
      self.MXSATDesc:str = obj["MXSATDesc"]
      """  MXSATDesc  """  
      self.PymtProposal:bool = obj["PymtProposal"]
      """  PymtProposal  """  
      self.AutoCheckNum:bool = obj["AutoCheckNum"]
      """  AutoCheckNum  """  
      self.EnterPymtTotal:bool = obj["EnterPymtTotal"]
      """  EnterPymtTotal  """  
      self.CheckNumSeq:int = obj["CheckNumSeq"]
      """  CheckNumSeq  """  
      self.US1099KTranType:str = obj["US1099KTranType"]
      """  Form 1099-K Transaction Type  """  
      self.US1099KAmtThreshold:int = obj["US1099KAmtThreshold"]
      """  Form 1099-K Third Party Network Amount Threshold  """  
      self.US1099KTranThreshold:int = obj["US1099KTranThreshold"]
      """  Form 1099-K Third Party Network Transaction Threshold  """  
      self.COPayForm:str = obj["COPayForm"]
      """  COPayForm  """  
      self.COPayMethod:str = obj["COPayMethod"]
      """  COPayMethod  """  
      self.TypeCode:str = obj["TypeCode"]
      """  UNCL4461  """  
      self.EnableThresholds:bool = obj["EnableThresholds"]
      """  Indicates if the threshold fields are enabled  """  
      self.IsCZLocalization:bool = obj["IsCZLocalization"]
      self.PMSourceModule:str = obj["PMSourceModule"]
      """  Shows a char representation of a PMSource: 0 = AP, 1 = AR.  """  
      self.EnableAPInfo:bool = obj["EnableAPInfo"]
      """  EnableAPInfo  """  
      self.COPayMethodDesc:str = obj["COPayMethodDesc"]
      self.TypeDescription:str = obj["TypeDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.EFTHeadName:str = obj["EFTHeadName"]
      self.EFTHeadType:int = obj["EFTHeadType"]
      self.PITypeDescription:str = obj["PITypeDescription"]
      self.XbSystELIEinvoice:bool = obj["XbSystELIEinvoice"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PayMethodTableset:
   def __init__(self, obj):
      self.PayMethod:list[Erp_Tablesets_PayMethodRow] = obj["PayMethod"]
      self.PayMethodProp:list[Erp_Tablesets_PayMethodPropRow] = obj["PayMethodProp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPayMethodTableset:
   def __init__(self, obj):
      self.PayMethod:list[Erp_Tablesets_PayMethodRow] = obj["PayMethod"]
      self.PayMethodProp:list[Erp_Tablesets_PayMethodPropRow] = obj["PayMethodProp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   pmUID
   """  
   def __init__(self, obj):
      self.pmUID:int = obj["pmUID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PayMethodTableset] = obj["returnObj"]
      pass

class GetByNamePMSource_input:
   """ Required : 
   name
   pmSource
   """  
   def __init__(self, obj):
      self.name:str = obj["name"]
      self.pmSource:int = obj["pmSource"]
      pass

class GetByNamePMSource_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PayMethodTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PayMethodTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PayMethodTableset] = obj["returnObj"]
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

class GetDepositSlipsCodeDescList_input:
   """ Required : 
   sARIDTiming
   """  
   def __init__(self, obj):
      self.sARIDTiming:str = obj["sARIDTiming"]
      pass

class GetDepositSlipsCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  List of Deposit Slips  codes/descriptions  """  
      pass

class GetIdByName_input:
   """ Required : 
   cName
   """  
   def __init__(self, obj):
      self.cName:str = obj["cName"]
      """  Name  """  
      pass

class GetIdByName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.iPMUID:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetListDepositSlips_input:
   """ Required : 
   whereClause
   bankAcctID
   pmName
   pmUIDs
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  whereClause  """  
      self.bankAcctID:str = obj["bankAcctID"]
      self.pmName:str = obj["pmName"]
      """  payment method name  """  
      self.pmUIDs:str = obj["pmUIDs"]
      """  list of payment UIDs  """  
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetListDepositSlips_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PayMethodListTableset] = obj["returnObj"]
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
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PayMethodListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPayMethodProp_input:
   """ Required : 
   ds
   pmUID
   efTHeadUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      self.pmUID:int = obj["pmUID"]
      self.efTHeadUID:int = obj["efTHeadUID"]
      pass

class GetNewPayMethodProp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPayMethod_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

class GetNewPayMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPayMethods_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PayMethodListTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClausePayMethod
   whereClausePayMethodProp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePayMethod:str = obj["whereClausePayMethod"]
      self.whereClausePayMethodProp:str = obj["whereClausePayMethodProp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PayMethodTableset] = obj["returnObj"]
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

class KChangePayMethodEFTHeadUID_input:
   """ Required : 
   ProposedEFTHeadUID
   ds
   """  
   def __init__(self, obj):
      self.ProposedEFTHeadUID:int = obj["ProposedEFTHeadUID"]
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

class KChangePayMethodEFTHeadUID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class KChangePayMethodPMSource_input:
   """ Required : 
   ProposedPMSourceModule
   ds
   """  
   def __init__(self, obj):
      self.ProposedPMSourceModule:str = obj["ProposedPMSourceModule"]
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

class KChangePayMethodPMSource_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class KChangePayMethodType_input:
   """ Required : 
   ProposedType
   ds
   """  
   def __init__(self, obj):
      self.ProposedType:int = obj["ProposedType"]
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

class KChangePayMethodType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class KChangedPMSource_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

class KChangedPMSource_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class KChangedType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

class KChangedType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class NameChanged_input:
   """ Required : 
   name
   ds
   """  
   def __init__(self, obj):
      self.name:str = obj["name"]
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

class NameChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfPayMethodType_input:
   """ Required : 
   PMUID
   ds
   """  
   def __init__(self, obj):
      self.PMUID:int = obj["PMUID"]
      """  Paymenth Method ID  """  
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

class OnChangeOfPayMethodType_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetAPInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

class SetAPInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPayMethodTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPayMethodTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

