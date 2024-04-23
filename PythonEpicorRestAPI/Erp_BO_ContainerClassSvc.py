import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ContainerClassSvc
# Description: Master file maintenance business logic for ContainerClass
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ContainerClasses(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ContainerClasses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerClasses
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerClassRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContainerClasses",headers=creds) as resp:
           return await resp.json()

async def post_ContainerClasses(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerClasses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerClassRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ContainerClassRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContainerClasses", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ContainerClasses_Company_ClassCode(Company, ClassCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContainerClass item
   Description: Calls GetByID to retrieve the ContainerClass item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerClass
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ClassCode: Desc: ClassCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerClassRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContainerClasses(" + Company + "," + ClassCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ContainerClasses_Company_ClassCode(Company, ClassCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ContainerClass for the service
   Description: Calls UpdateExt to update ContainerClass. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerClass
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ClassCode: Desc: ClassCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerClassRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContainerClasses(" + Company + "," + ClassCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ContainerClasses_Company_ClassCode(Company, ClassCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ContainerClass item
   Description: Call UpdateExt to delete ContainerClass item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerClass
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ClassCode: Desc: ClassCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContainerClasses(" + Company + "," + ClassCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContainerClasses_Company_ClassCode_ContClassMiscs(Company, ClassCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ContClassMiscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContClassMiscs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ClassCode: Desc: ClassCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContClassMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContainerClasses(" + Company + "," + ClassCode + ")/ContClassMiscs",headers=creds) as resp:
           return await resp.json()

async def get_ContainerClasses_Company_ClassCode_ContClassMiscs_Company_ClassCode_MiscCode(Company, ClassCode, MiscCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContClassMisc item
   Description: Calls GetByID to retrieve the ContClassMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContClassMisc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ClassCode: Desc: ClassCode   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContClassMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContainerClasses(" + Company + "," + ClassCode + ")/ContClassMiscs(" + Company + "," + ClassCode + "," + MiscCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContClassMiscs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ContClassMiscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContClassMiscs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContClassMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContClassMiscs",headers=creds) as resp:
           return await resp.json()

async def post_ContClassMiscs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContClassMiscs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContClassMiscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ContClassMiscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContClassMiscs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ContClassMiscs_Company_ClassCode_MiscCode(Company, ClassCode, MiscCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContClassMisc item
   Description: Calls GetByID to retrieve the ContClassMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContClassMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ClassCode: Desc: ClassCode   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContClassMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContClassMiscs(" + Company + "," + ClassCode + "," + MiscCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ContClassMiscs_Company_ClassCode_MiscCode(Company, ClassCode, MiscCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ContClassMisc for the service
   Description: Calls UpdateExt to update ContClassMisc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContClassMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ClassCode: Desc: ClassCode   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContClassMiscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContClassMiscs(" + Company + "," + ClassCode + "," + MiscCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ContClassMiscs_Company_ClassCode_MiscCode(Company, ClassCode, MiscCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ContClassMisc item
   Description: Call UpdateExt to delete ContClassMisc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContClassMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ClassCode: Desc: ClassCode   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContClassMiscs(" + Company + "," + ClassCode + "," + MiscCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerClassListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseContainerClass, whereClauseContClassMisc, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseContainerClass=" + whereClauseContainerClass
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseContClassMisc=" + whereClauseContClassMisc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(classCode, epicorHeaders = None):
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
   params += "classCode=" + classCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DefaultContainerCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultContainerCost
   Description: Calculates container cost when CostPerVolume or Volume change.
   OperationID: DefaultContainerCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultContainerCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultContainerCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultCostPerVolume(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultCostPerVolume
   Description: Calculates the CostPerVolume.
   OperationID: DefaultCostPerVolume
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultCostPerVolume_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultCostPerVolume_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnContactChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnContactChange
   Description: Verifies if proposed Vendor Contact number is valid. If so, loads Vendor Contact Information.
   OperationID: OnContactChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnContactChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnContactChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnIndirectCostChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnIndirectCostChange
   Description: Verifies if proposed Landed Cost Indirect Cost Code is valid. If so, loads Indirect Cost Amount and Currency code.
   OperationID: OnIndirectCostChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnIndirectCostChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnIndirectCostChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnSupplierChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnSupplierChange
   Description: Verifies if proposed Supplier ID is valid. If so, loads Supplier's name.
   OperationID: OnSupplierChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnSupplierChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnSupplierChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewContainerClass(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewContainerClass
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContainerClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewContClassMisc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewContClassMisc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContClassMisc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContClassMisc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContClassMisc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContClassMiscRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ContClassMiscRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerClassListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ContainerClassListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerClassRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ContainerClassRow] = obj["value"]
      pass

class Erp_Tablesets_ContClassMiscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  Container Shipment Class ID  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Descriptive code assigned by user which uniquely identifies a Purchasing Misc charge/credit master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerClassListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  Container Class Code ID  """  
      self.Description:str = obj["Description"]
      """  Descriptive text identifying the Container Class  """  
      self.ContainerCost:int = obj["ContainerCost"]
      """  Total cost to ship this container  """  
      self.ShippingDays:int = obj["ShippingDays"]
      """  Lead time it takes for this container to reach its destination.  This is a buffer amount used to offset the shipping date to identify when a shipment is due to arrive.  For example if the shipping days is 30 and the ship date of the container is January 1, the expected arrival date of the container is January 31.  """  
      self.Volume:int = obj["Volume"]
      """  Container volume, frequently specified in cubic sq feet.  """  
      self.CostPerVolume:int = obj["CostPerVolume"]
      """  Volume cost of the container.  This is calculated by dividing the container cost by the Volume.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """   Unit of measure used to qualify the Volume.
If entered, must be valid in the standard "Volume" UOMs  (UOMClass.ClassType = "Volume")  """  
      self.LoadPortID:str = obj["LoadPortID"]
      """  Valid Loading Port ID where goods are loaded on the vessel.  """  
      self.DechargePortID:str = obj["DechargePortID"]
      """  Valid port location where goods are unloaded.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  """  
      self.FOB:str = obj["FOB"]
      """  Descriptive code assigned by user which uniquely identifies the fob record.  """  
      self.ContainerCount:int = obj["ContainerCount"]
      """  Number of Containers in this shipment.  """  
      self.PackageCount:int = obj["PackageCount"]
      """  Number of Packages in this shipment.  """  
      self.Weight:int = obj["Weight"]
      """  Total Weight of the shipment.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.ConNum:int = obj["ConNum"]
      """  Carrier (Supplier) Contact number.  Unique identifier for the contact record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  """  
      self.GlobalContainerClass:bool = obj["GlobalContainerClass"]
      """  Marks this ContainerClass as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ConNumName:str = obj["ConNumName"]
      """  Contact name.  """  
      self.ConNumEmailAddress:str = obj["ConNumEmailAddress"]
      """  Contact email address.  """  
      self.ConNumPhoneNum:str = obj["ConNumPhoneNum"]
      """  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  """  
      self.ConNumFaxNum:str = obj["ConNumFaxNum"]
      """  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  """  
      self.DechargePortIDDescription:str = obj["DechargePortIDDescription"]
      """  Country Port Description.  This must be a unique port description within the Company.  """  
      self.DechargePortIDPortID:str = obj["DechargePortIDPortID"]
      """  A unique PortID within the Company and must always be associated with a Country.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      """  Full description of the FOB Code.  """  
      self.LoadPortIDDescription:str = obj["LoadPortIDDescription"]
      """  Country Port Description.  This must be a unique port description within the Company.  """  
      self.LoadPortIDPortID:str = obj["LoadPortIDPortID"]
      """  A unique PortID within the Company and must always be associated with a Country.  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerClassRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  Container Class Code ID  """  
      self.Description:str = obj["Description"]
      """  Descriptive text identifying the Container Class  """  
      self.ContainerCost:int = obj["ContainerCost"]
      """  Total cost to ship this container  """  
      self.ShippingDays:int = obj["ShippingDays"]
      """  Lead time it takes for this container to reach its destination.  This is a buffer amount used to offset the shipping date to identify when a shipment is due to arrive.  For example if the shipping days is 30 and the ship date of the container is January 1, the expected arrival date of the container is January 31.  """  
      self.Volume:int = obj["Volume"]
      """  Container volume, frequently specified in cubic sq feet.  """  
      self.CostPerVolume:int = obj["CostPerVolume"]
      """  Volume cost of the container.  This is calculated by dividing the container cost by the Volume.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """   Unit of measure used to qualify the Volume.
If entered, must be valid in the standard "Volume" UOMs  (UOMClass.ClassType = "Volume")  """  
      self.LoadPortID:str = obj["LoadPortID"]
      """  Valid Loading Port ID where goods are loaded on the vessel.  """  
      self.DechargePortID:str = obj["DechargePortID"]
      """  Valid port location where goods are unloaded.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  """  
      self.FOB:str = obj["FOB"]
      """  Descriptive code assigned by user which uniquely identifies the fob record.  """  
      self.ContainerCount:int = obj["ContainerCount"]
      """  Number of Containers in this shipment.  """  
      self.PackageCount:int = obj["PackageCount"]
      """  Number of Packages in this shipment.  """  
      self.Weight:int = obj["Weight"]
      """  Total Weight of the shipment.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.ConNum:int = obj["ConNum"]
      """  Carrier (Supplier) Contact number.  Unique identifier for the contact record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  """  
      self.GlobalContainerClass:bool = obj["GlobalContainerClass"]
      """  Marks this ContainerClass as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ConNumName:str = obj["ConNumName"]
      self.ConNumFaxNum:str = obj["ConNumFaxNum"]
      self.ConNumPhoneNum:str = obj["ConNumPhoneNum"]
      self.ConNumEmailAddress:str = obj["ConNumEmailAddress"]
      self.DechargePortIDDescription:str = obj["DechargePortIDDescription"]
      self.DechargePortIDPortID:str = obj["DechargePortIDPortID"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.LoadPortIDDescription:str = obj["LoadPortIDDescription"]
      self.LoadPortIDPortID:str = obj["LoadPortIDPortID"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DefaultContainerCost_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerClassTableset] = obj["ds"]
      pass

class DefaultContainerCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultCostPerVolume_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerClassTableset] = obj["ds"]
      pass

class DefaultCostPerVolume_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   classCode
   """  
   def __init__(self, obj):
      self.classCode:str = obj["classCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ContClassMiscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  Container Shipment Class ID  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Descriptive code assigned by user which uniquely identifies a Purchasing Misc charge/credit master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerClassListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  Container Class Code ID  """  
      self.Description:str = obj["Description"]
      """  Descriptive text identifying the Container Class  """  
      self.ContainerCost:int = obj["ContainerCost"]
      """  Total cost to ship this container  """  
      self.ShippingDays:int = obj["ShippingDays"]
      """  Lead time it takes for this container to reach its destination.  This is a buffer amount used to offset the shipping date to identify when a shipment is due to arrive.  For example if the shipping days is 30 and the ship date of the container is January 1, the expected arrival date of the container is January 31.  """  
      self.Volume:int = obj["Volume"]
      """  Container volume, frequently specified in cubic sq feet.  """  
      self.CostPerVolume:int = obj["CostPerVolume"]
      """  Volume cost of the container.  This is calculated by dividing the container cost by the Volume.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """   Unit of measure used to qualify the Volume.
If entered, must be valid in the standard "Volume" UOMs  (UOMClass.ClassType = "Volume")  """  
      self.LoadPortID:str = obj["LoadPortID"]
      """  Valid Loading Port ID where goods are loaded on the vessel.  """  
      self.DechargePortID:str = obj["DechargePortID"]
      """  Valid port location where goods are unloaded.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  """  
      self.FOB:str = obj["FOB"]
      """  Descriptive code assigned by user which uniquely identifies the fob record.  """  
      self.ContainerCount:int = obj["ContainerCount"]
      """  Number of Containers in this shipment.  """  
      self.PackageCount:int = obj["PackageCount"]
      """  Number of Packages in this shipment.  """  
      self.Weight:int = obj["Weight"]
      """  Total Weight of the shipment.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.ConNum:int = obj["ConNum"]
      """  Carrier (Supplier) Contact number.  Unique identifier for the contact record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  """  
      self.GlobalContainerClass:bool = obj["GlobalContainerClass"]
      """  Marks this ContainerClass as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ConNumName:str = obj["ConNumName"]
      """  Contact name.  """  
      self.ConNumEmailAddress:str = obj["ConNumEmailAddress"]
      """  Contact email address.  """  
      self.ConNumPhoneNum:str = obj["ConNumPhoneNum"]
      """  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  """  
      self.ConNumFaxNum:str = obj["ConNumFaxNum"]
      """  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  """  
      self.DechargePortIDDescription:str = obj["DechargePortIDDescription"]
      """  Country Port Description.  This must be a unique port description within the Company.  """  
      self.DechargePortIDPortID:str = obj["DechargePortIDPortID"]
      """  A unique PortID within the Company and must always be associated with a Country.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      """  Full description of the FOB Code.  """  
      self.LoadPortIDDescription:str = obj["LoadPortIDDescription"]
      """  Country Port Description.  This must be a unique port description within the Company.  """  
      self.LoadPortIDPortID:str = obj["LoadPortIDPortID"]
      """  A unique PortID within the Company and must always be associated with a Country.  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerClassListTableset:
   def __init__(self, obj):
      self.ContainerClassList:list[Erp_Tablesets_ContainerClassListRow] = obj["ContainerClassList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ContainerClassRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  Container Class Code ID  """  
      self.Description:str = obj["Description"]
      """  Descriptive text identifying the Container Class  """  
      self.ContainerCost:int = obj["ContainerCost"]
      """  Total cost to ship this container  """  
      self.ShippingDays:int = obj["ShippingDays"]
      """  Lead time it takes for this container to reach its destination.  This is a buffer amount used to offset the shipping date to identify when a shipment is due to arrive.  For example if the shipping days is 30 and the ship date of the container is January 1, the expected arrival date of the container is January 31.  """  
      self.Volume:int = obj["Volume"]
      """  Container volume, frequently specified in cubic sq feet.  """  
      self.CostPerVolume:int = obj["CostPerVolume"]
      """  Volume cost of the container.  This is calculated by dividing the container cost by the Volume.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """   Unit of measure used to qualify the Volume.
If entered, must be valid in the standard "Volume" UOMs  (UOMClass.ClassType = "Volume")  """  
      self.LoadPortID:str = obj["LoadPortID"]
      """  Valid Loading Port ID where goods are loaded on the vessel.  """  
      self.DechargePortID:str = obj["DechargePortID"]
      """  Valid port location where goods are unloaded.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  """  
      self.FOB:str = obj["FOB"]
      """  Descriptive code assigned by user which uniquely identifies the fob record.  """  
      self.ContainerCount:int = obj["ContainerCount"]
      """  Number of Containers in this shipment.  """  
      self.PackageCount:int = obj["PackageCount"]
      """  Number of Packages in this shipment.  """  
      self.Weight:int = obj["Weight"]
      """  Total Weight of the shipment.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.ConNum:int = obj["ConNum"]
      """  Carrier (Supplier) Contact number.  Unique identifier for the contact record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  """  
      self.GlobalContainerClass:bool = obj["GlobalContainerClass"]
      """  Marks this ContainerClass as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ConNumName:str = obj["ConNumName"]
      self.ConNumFaxNum:str = obj["ConNumFaxNum"]
      self.ConNumPhoneNum:str = obj["ConNumPhoneNum"]
      self.ConNumEmailAddress:str = obj["ConNumEmailAddress"]
      self.DechargePortIDDescription:str = obj["DechargePortIDDescription"]
      self.DechargePortIDPortID:str = obj["DechargePortIDPortID"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.LoadPortIDDescription:str = obj["LoadPortIDDescription"]
      self.LoadPortIDPortID:str = obj["LoadPortIDPortID"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerClassTableset:
   def __init__(self, obj):
      self.ContainerClass:list[Erp_Tablesets_ContainerClassRow] = obj["ContainerClass"]
      self.ContClassMisc:list[Erp_Tablesets_ContClassMiscRow] = obj["ContClassMisc"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtContainerClassTableset:
   def __init__(self, obj):
      self.ContainerClass:list[Erp_Tablesets_ContainerClassRow] = obj["ContainerClass"]
      self.ContClassMisc:list[Erp_Tablesets_ContClassMiscRow] = obj["ContClassMisc"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   classCode
   """  
   def __init__(self, obj):
      self.classCode:str = obj["classCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ContainerClassTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ContainerClassTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ContainerClassTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ContainerClassListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewContClassMisc_input:
   """ Required : 
   ds
   classCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerClassTableset] = obj["ds"]
      self.classCode:str = obj["classCode"]
      pass

class GetNewContClassMisc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewContainerClass_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerClassTableset] = obj["ds"]
      pass

class GetNewContainerClass_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseContainerClass
   whereClauseContClassMisc
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseContainerClass:str = obj["whereClauseContainerClass"]
      self.whereClauseContClassMisc:str = obj["whereClauseContClassMisc"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ContainerClassTableset] = obj["returnObj"]
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

class OnContactChange_input:
   """ Required : 
   ipContactNum
   ds
   """  
   def __init__(self, obj):
      self.ipContactNum:int = obj["ipContactNum"]
      """  The Contact Number  """  
      self.ds:list[Erp_Tablesets_ContainerClassTableset] = obj["ds"]
      pass

class OnContactChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnIndirectCostChange_input:
   """ Required : 
   ipMiscCode
   ds
   """  
   def __init__(self, obj):
      self.ipMiscCode:str = obj["ipMiscCode"]
      """  The Supplier ID  """  
      self.ds:list[Erp_Tablesets_ContainerClassTableset] = obj["ds"]
      pass

class OnIndirectCostChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnSupplierChange_input:
   """ Required : 
   ipSupplierID
   ds
   """  
   def __init__(self, obj):
      self.ipSupplierID:str = obj["ipSupplierID"]
      """  The Supplier ID  """  
      self.ds:list[Erp_Tablesets_ContainerClassTableset] = obj["ds"]
      pass

class OnSupplierChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtContainerClassTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtContainerClassTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerClassTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

