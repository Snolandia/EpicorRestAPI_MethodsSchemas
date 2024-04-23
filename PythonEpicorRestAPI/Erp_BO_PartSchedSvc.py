import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartSchedSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PartScheds(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartScheds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartScheds
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartScheds",headers=creds) as resp:
           return await resp.json()

async def post_PartScheds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartScheds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartSchedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartSchedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartScheds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartScheds_Company_PartNum_Plant(Company, PartNum, Plant, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartSched item
   Description: Calls GetByID to retrieve the PartSched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartSched
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartScheds(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartScheds_Company_PartNum_Plant(Company, PartNum, Plant, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartSched for the service
   Description: Calls UpdateExt to update PartSched. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartSched
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartSchedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartScheds(" + Company + "," + PartNum + "," + Plant + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartScheds_Company_PartNum_Plant(Company, PartNum, Plant, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartSched item
   Description: Call UpdateExt to delete PartSched item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartSched
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartScheds(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def get_PartScheds_Company_PartNum_Plant_PartSchedVends(Company, PartNum, Plant, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PartSchedVends items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PartSchedVends1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSchedVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartScheds(" + Company + "," + PartNum + "," + Plant + ")/PartSchedVends",headers=creds) as resp:
           return await resp.json()

async def get_PartScheds_Company_PartNum_Plant_PartSchedVends_Company_PartNum_Plant_VendorNum_PurPoint(Company, PartNum, Plant, VendorNum, PurPoint, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartSchedVend item
   Description: Calls GetByID to retrieve the PartSchedVend item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartSchedVend1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartSchedVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartScheds(" + Company + "," + PartNum + "," + Plant + ")/PartSchedVends(" + Company + "," + PartNum + "," + Plant + "," + VendorNum + "," + PurPoint + ")",headers=creds) as resp:
           return await resp.json()

async def get_PartScheds_Company_PartNum_Plant_PartSchedVendPOes(Company, PartNum, Plant, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PartSchedVendPOes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PartSchedVendPOes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSchedVendPORow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartScheds(" + Company + "," + PartNum + "," + Plant + ")/PartSchedVendPOes",headers=creds) as resp:
           return await resp.json()

async def get_PartScheds_Company_PartNum_Plant_PartSchedVendPOes_Company_PartNum_Plant_VendorNum_PurPoint_ContractPONum_ContractPOLine(Company, PartNum, Plant, VendorNum, PurPoint, ContractPONum, ContractPOLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartSchedVendPO item
   Description: Calls GetByID to retrieve the PartSchedVendPO item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartSchedVendPO1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ContractPONum: Desc: ContractPONum   Required: True
      :param ContractPOLine: Desc: ContractPOLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartSchedVendPORow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartScheds(" + Company + "," + PartNum + "," + Plant + ")/PartSchedVendPOes(" + Company + "," + PartNum + "," + Plant + "," + VendorNum + "," + PurPoint + "," + ContractPONum + "," + ContractPOLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_PartSchedVends(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartSchedVends items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartSchedVends
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSchedVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVends",headers=creds) as resp:
           return await resp.json()

async def post_PartSchedVends(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartSchedVends
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartSchedVendRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartSchedVendRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVends", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartSchedVends_Company_PartNum_Plant_VendorNum_PurPoint(Company, PartNum, Plant, VendorNum, PurPoint, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartSchedVend item
   Description: Calls GetByID to retrieve the PartSchedVend item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartSchedVend
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartSchedVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVends(" + Company + "," + PartNum + "," + Plant + "," + VendorNum + "," + PurPoint + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartSchedVends_Company_PartNum_Plant_VendorNum_PurPoint(Company, PartNum, Plant, VendorNum, PurPoint, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartSchedVend for the service
   Description: Calls UpdateExt to update PartSchedVend. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartSchedVend
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartSchedVendRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVends(" + Company + "," + PartNum + "," + Plant + "," + VendorNum + "," + PurPoint + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartSchedVends_Company_PartNum_Plant_VendorNum_PurPoint(Company, PartNum, Plant, VendorNum, PurPoint, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartSchedVend item
   Description: Call UpdateExt to delete PartSchedVend item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartSchedVend
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVends(" + Company + "," + PartNum + "," + Plant + "," + VendorNum + "," + PurPoint + ")",headers=creds) as resp:
           return await resp.json()

async def get_PartSchedVendPOes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartSchedVendPOes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartSchedVendPOes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSchedVendPORow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVendPOes",headers=creds) as resp:
           return await resp.json()

async def post_PartSchedVendPOes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartSchedVendPOes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartSchedVendPORow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartSchedVendPORow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVendPOes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartSchedVendPOes_Company_PartNum_Plant_VendorNum_PurPoint_ContractPONum_ContractPOLine(Company, PartNum, Plant, VendorNum, PurPoint, ContractPONum, ContractPOLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartSchedVendPO item
   Description: Calls GetByID to retrieve the PartSchedVendPO item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartSchedVendPO
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ContractPONum: Desc: ContractPONum   Required: True
      :param ContractPOLine: Desc: ContractPOLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartSchedVendPORow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVendPOes(" + Company + "," + PartNum + "," + Plant + "," + VendorNum + "," + PurPoint + "," + ContractPONum + "," + ContractPOLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartSchedVendPOes_Company_PartNum_Plant_VendorNum_PurPoint_ContractPONum_ContractPOLine(Company, PartNum, Plant, VendorNum, PurPoint, ContractPONum, ContractPOLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartSchedVendPO for the service
   Description: Calls UpdateExt to update PartSchedVendPO. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartSchedVendPO
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ContractPONum: Desc: ContractPONum   Required: True
      :param ContractPOLine: Desc: ContractPOLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartSchedVendPORow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVendPOes(" + Company + "," + PartNum + "," + Plant + "," + VendorNum + "," + PurPoint + "," + ContractPONum + "," + ContractPOLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartSchedVendPOes_Company_PartNum_Plant_VendorNum_PurPoint_ContractPONum_ContractPOLine(Company, PartNum, Plant, VendorNum, PurPoint, ContractPONum, ContractPOLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartSchedVendPO item
   Description: Call UpdateExt to delete PartSchedVendPO item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartSchedVendPO
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ContractPONum: Desc: ContractPONum   Required: True
      :param ContractPOLine: Desc: ContractPOLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVendPOes(" + Company + "," + PartNum + "," + Plant + "," + VendorNum + "," + PurPoint + "," + ContractPONum + "," + ContractPOLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSchedListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePartSched, whereClausePartSchedVend, whereClausePartSchedVendPO, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClausePartSched=" + whereClausePartSched
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartSchedVend=" + whereClausePartSchedVend
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartSchedVendPO=" + whereClausePartSchedVendPO
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, plant, epicorHeaders = None):
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
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "plant=" + plant

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetPartXRefInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCalendarID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCalendarID
   Description: Validate CalendarId value
   OperationID: OnChangeCalendarID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeInspNextDelivery(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeInspNextDelivery
   Description: Validate InspNextDelivery value
   OperationID: OnChangeInspNextDelivery
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInspNextDelivery_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInspNextDelivery_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMinDeliveryQty1(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMinDeliveryQty1
   Description: Validate MinDeliveryQty1 value
   OperationID: OnChangeMinDeliveryQty1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMinDeliveryQty1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMinDeliveryQty1_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMinDeliveryQty2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMinDeliveryQty2
   Description: Validate MinDeliveryQty2 value
   OperationID: OnChangeMinDeliveryQty2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMinDeliveryQty2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMinDeliveryQty2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMinForwardSpan(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMinForwardSpan
   Description: Validate MinForwardSpan value
   OperationID: OnChangeMinForwardSpan
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMinForwardSpan_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMinForwardSpan_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOrderCover(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOrderCover
   Description: Validate OrderCover value
   OperationID: OnChangeOrderCover
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOrderCover_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOrderCover_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: Validate PartNum value
   OperationID: OnChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePercentShare(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePercentShare
   Description: Validate PercentShare value
   OperationID: OnChangePercentShare
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePercentShare_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePercentShare_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePeriodicityCode1(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePeriodicityCode1
   Description: Validate PeriodicityCode1 value
   OperationID: OnChangePeriodicityCode1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePeriodicityCode1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePeriodicityCode1_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePeriodicityCode2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePeriodicityCode2
   Description: Validate PeriodicityCode2 value
   OperationID: OnChangePeriodicityCode2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePeriodicityCode2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePeriodicityCode2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePeriodShift(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePeriodShift
   Description: Validate PeriodShift value
   OperationID: OnChangePeriodShift
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePeriodShift_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePeriodShift_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePrintLength(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePrintLength
   Description: Validate PrintLength value
   OperationID: OnChangePrintLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePrintLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePrintLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePurPoint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePurPoint
   Description: Validate PurPoint value
   OperationID: OnChangePurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeScheduleFirm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeScheduleFirm
   Description: Validate ScheduleFirm value
   OperationID: OnChangeScheduleFirm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeScheduleFirm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeScheduleFirm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeScheduleLength(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeScheduleLength
   Description: Validate ScheduleLength value
   OperationID: OnChangeScheduleLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeScheduleLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeScheduleLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeVendorID
   Description: Validate VendorId value
   OperationID: OnChangeVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeVendorNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeVendorNum
   Description: Validate VendorNum value
   OperationID: OnChangeVendorNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendorNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendorNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PartPlantIsLinkedToContract(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PartPlantIsLinkedToContract
   Description: Read the Link To Contract flag from PartPlant.
   OperationID: PartPlantIsLinkedToContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartPlantIsLinkedToContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartPlantIsLinkedToContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindPart
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartFromRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartFromRowID
   OperationID: GetPartFromRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetValidAndProjectedWorkingDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetValidAndProjectedWorkingDate
   Description: Projects forwards the Days to add from the base date only counting working days, and then using existing function to ensure that projected date is valid
   OperationID: GetValidAndProjectedWorkingDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetValidAndProjectedWorkingDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetValidAndProjectedWorkingDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartSched(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartSched
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartSched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartSchedVend(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartSchedVend
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartSchedVend
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartSchedVend_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartSchedVend_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartSchedVendPO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartSchedVendPO
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartSchedVendPO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartSchedVendPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartSchedVendPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartSchedListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartSchedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedVendPORow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartSchedVendPORow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedVendRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartSchedVendRow] = obj["value"]
      pass

class Erp_Tablesets_PartSchedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.IsActive:bool = obj["IsActive"]
      """  Is this Part active within a Purchase Contract Schedule within this Site?  """  
      self.CalendarID:str = obj["CalendarID"]
      """   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  """  
      self.PeriodicityCode1:int = obj["PeriodicityCode1"]
      """  Periodicity Code.  Possible values are 1 = Semi-Weekly, 2 = Daily, 3 = Monthly Forward, 4 = Weekly Forward, 5 = Weekly Not Last Week of the Month, 6 = Nth Day of the Month  """  
      self.PeriodicityCode2:int = obj["PeriodicityCode2"]
      """  Periodicity Code.  Possible values are 1 = Semi-Weekly, 2 = Daily, 3 = Monthly Forward, 4 = Weekly Forward, 5 = Weekly Not Last Week of the Month, 6 = Nth Day of the Month  """  
      self.PeriodShift:int = obj["PeriodShift"]
      """  Defines when the scheduling system will shift the schedule from Periodicity Code 1 to Periodicity Code 2.  """  
      self.MinDeliveryQty1:int = obj["MinDeliveryQty1"]
      """  Minimum quantity for any given Purchase Contract Delivery relating to Periodicity Code 1.  """  
      self.MinDeliveryQty2:int = obj["MinDeliveryQty2"]
      """  Minimum quantity for any given Purchase Contract Delivery relating to Periodicity Code 2.  """  
      self.MinForwardSpan:int = obj["MinForwardSpan"]
      """  How far into the future the Minimum Delivery Quantity should be applied.  """  
      self.FirmIncrease:int = obj["FirmIncrease"]
      """  Used only when Periodicity Code 2 (Daily) is used - and defines how many days from the current date that no increases in quantity are allowed.  """  
      self.FirmDecrease:int = obj["FirmDecrease"]
      """  Used only when Periodicity Code 2 (Daily) is used - and defines how many days from the current date that no decreases in quantity are allowed.  """  
      self.OrderCover:int = obj["OrderCover"]
      """  How many days into the future Purchase Order Releases should be created for the Purchase Contract.  """  
      self.MaterialCover:int = obj["MaterialCover"]
      """  How many days of Material Costs will be honored on the Purchase Contract.  """  
      self.PrintLength:int = obj["PrintLength"]
      """  The Number of Days for which the Part Schedule will be printed.  """  
      self.ScheduleLength:int = obj["ScheduleLength"]
      """  The maximum period for which schedules will be created.  """  
      self.ScheduleFirm:int = obj["ScheduleFirm"]
      """  The number of days for which the current schedule is considered firm and will not be overwritten by a new proposed schedule.  If this value is zero, then all dates can be overwritten.  """  
      self.DevChar01:str = obj["DevChar01"]
      """  For development use only.  """  
      self.DevChar02:str = obj["DevChar02"]
      """  For development use only.  """  
      self.DevChar03:str = obj["DevChar03"]
      """  For development use only.  """  
      self.DevChar04:str = obj["DevChar04"]
      """  For development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  PartDesctiption  """  
      self.AreMinQuantitiesZero:bool = obj["AreMinQuantitiesZero"]
      """  Check if both MinDeliveryQty's are 0  """  
      self.IUM:str = obj["IUM"]
      """  Base UOM  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartSchedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.IsActive:bool = obj["IsActive"]
      """  Is this Part active within a Purchase Contract Schedule within this Site?  """  
      self.CalendarID:str = obj["CalendarID"]
      """   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  """  
      self.PeriodicityCode1:int = obj["PeriodicityCode1"]
      """  Periodicity Code.  Possible values are 1 = Semi-Weekly, 2 = Daily, 3 = Monthly Forward, 4 = Weekly Forward, 5 = Weekly Not Last Week of the Month, 6 = Nth Day of the Month  """  
      self.PeriodicityCode2:int = obj["PeriodicityCode2"]
      """  Periodicity Code.  Possible values are 1 = Semi-Weekly, 2 = Daily, 3 = Monthly Forward, 4 = Weekly Forward, 5 = Weekly Not Last Week of the Month, 6 = Nth Day of the Month  """  
      self.PeriodShift:int = obj["PeriodShift"]
      """  Defines when the scheduling system will shift the schedule from Periodicity Code 1 to Periodicity Code 2.  """  
      self.MinDeliveryQty1:int = obj["MinDeliveryQty1"]
      """  Minimum quantity for any given Purchase Contract Delivery relating to Periodicity Code 1.  """  
      self.MinDeliveryQty2:int = obj["MinDeliveryQty2"]
      """  Minimum quantity for any given Purchase Contract Delivery relating to Periodicity Code 2.  """  
      self.MinForwardSpan:int = obj["MinForwardSpan"]
      """  How far into the future the Minimum Delivery Quantity should be applied.  """  
      self.FirmIncrease:int = obj["FirmIncrease"]
      """  Used only when Periodicity Code 2 (Daily) is used - and defines how many days from the current date that no increases in quantity are allowed.  """  
      self.FirmDecrease:int = obj["FirmDecrease"]
      """  Used only when Periodicity Code 2 (Daily) is used - and defines how many days from the current date that no decreases in quantity are allowed.  """  
      self.OrderCover:int = obj["OrderCover"]
      """  How many days into the future Purchase Order Releases should be created for the Purchase Contract.  """  
      self.MaterialCover:int = obj["MaterialCover"]
      """  How many days of Material Costs will be honored on the Purchase Contract.  """  
      self.PrintLength:int = obj["PrintLength"]
      """  The Number of Days for which the Part Schedule will be printed.  """  
      self.ScheduleLength:int = obj["ScheduleLength"]
      """  The maximum period for which schedules will be created.  """  
      self.ScheduleFirm:int = obj["ScheduleFirm"]
      """  The number of days for which the current schedule is considered firm and will not be overwritten by a new proposed schedule.  If this value is zero, then all dates can be overwritten.  """  
      self.DevChar01:str = obj["DevChar01"]
      """  For development use only.  """  
      self.DevChar02:str = obj["DevChar02"]
      """  For development use only.  """  
      self.DevChar03:str = obj["DevChar03"]
      """  For development use only.  """  
      self.DevChar04:str = obj["DevChar04"]
      """  For development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  PartDesctiption  """  
      self.AreMinQuantitiesZero:bool = obj["AreMinQuantitiesZero"]
      """  Check if both MinDeliveryQty's are 0  """  
      self.IUM:str = obj["IUM"]
      """  Base UOM  """  
      self.LastRunDate:str = obj["LastRunDate"]
      self.BitFlag:int = obj["BitFlag"]
      self.PlantName:str = obj["PlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartSchedVendPORow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.PurPoint:str = obj["PurPoint"]
      """  PurPoint  """  
      self.ContractPONum:int = obj["ContractPONum"]
      """  ContractPONum  """  
      self.ContractPOLine:int = obj["ContractPOLine"]
      """  ContractPOLine  """  
      self.ContractStartDate:str = obj["ContractStartDate"]
      """  ContractStartDate  """  
      self.ContractEndDate:str = obj["ContractEndDate"]
      """  ContractEndDate  """  
      self.IsActive:bool = obj["IsActive"]
      """  IsActive  """  
      self.IsExpired:bool = obj["IsExpired"]
      """  IsExpired  """  
      self.IsApproved:bool = obj["IsApproved"]
      """  IsApproved  """  
      self.PercentShare:int = obj["PercentShare"]
      """  PercentShare  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ScheduleFirmDate:str = obj["ScheduleFirmDate"]
      self.MinPeriod1ShiftDate:str = obj["MinPeriod1ShiftDate"]
      self.MinForwardSpanDate:str = obj["MinForwardSpanDate"]
      self.LastRunDate:str = obj["LastRunDate"]
      self.BitFlag:int = obj["BitFlag"]
      self.PlantName:str = obj["PlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartSchedVendRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.PercentShare:int = obj["PercentShare"]
      """  Percentage Share of the Purchase Schedule for this Supplier.  Total of all Suppliers for this Part must equal 100 percent.  """  
      self.InspNextDelivery:int = obj["InspNextDelivery"]
      """  Should the Inspection flag be set when the Purchase Schedule is approved.  """  
      self.ContractPONum:int = obj["ContractPONum"]
      """  Purchase order number that uniquely identifies the Contract Purchase Order.  """  
      self.ContractPOLine:int = obj["ContractPOLine"]
      """  The line number of the detail record on the Contract Purchase Order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.DeliverMonday:bool = obj["DeliverMonday"]
      """  Does the Supplier make deliveries on Monday?  """  
      self.DeliverTuesday:bool = obj["DeliverTuesday"]
      """  Does the Supplier make deliveries on Tuesday?  """  
      self.DeliverWednesday:bool = obj["DeliverWednesday"]
      """  Does the Supplier make deliveries on Wednesday?  """  
      self.DeliverThursday:bool = obj["DeliverThursday"]
      """  Does the Supplier make deliveries on Thursday?  """  
      self.DeliverFriday:bool = obj["DeliverFriday"]
      """  Does the Supplier make deliveries on Friday?  """  
      self.DeliverSaturday:bool = obj["DeliverSaturday"]
      """  Does the Supplier make deliveries on Saturday?  """  
      self.DeliverSunday:bool = obj["DeliverSunday"]
      """  Does the Supplier make deliveries on Sunday?  """  
      self.DevChar01:str = obj["DevChar01"]
      """  For development use only.  """  
      self.DevChar02:str = obj["DevChar02"]
      """  For development use only.  """  
      self.DevChar03:str = obj["DevChar03"]
      """  For development use only.  """  
      self.DevChar04:str = obj["DevChar04"]
      """  For development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.VendorName:str = obj["VendorName"]
      """  VendorName  """  
      self.VendorID:str = obj["VendorID"]
      """  VendorID  """  
      self.IsActive:bool = obj["IsActive"]
      """  Indicates if the Supplier is active.  Supplier is inactive if PercentShare is 0.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PlantName:str = obj["PlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   partNum
   plant
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.plant:str = obj["plant"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PartSchedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.IsActive:bool = obj["IsActive"]
      """  Is this Part active within a Purchase Contract Schedule within this Site?  """  
      self.CalendarID:str = obj["CalendarID"]
      """   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  """  
      self.PeriodicityCode1:int = obj["PeriodicityCode1"]
      """  Periodicity Code.  Possible values are 1 = Semi-Weekly, 2 = Daily, 3 = Monthly Forward, 4 = Weekly Forward, 5 = Weekly Not Last Week of the Month, 6 = Nth Day of the Month  """  
      self.PeriodicityCode2:int = obj["PeriodicityCode2"]
      """  Periodicity Code.  Possible values are 1 = Semi-Weekly, 2 = Daily, 3 = Monthly Forward, 4 = Weekly Forward, 5 = Weekly Not Last Week of the Month, 6 = Nth Day of the Month  """  
      self.PeriodShift:int = obj["PeriodShift"]
      """  Defines when the scheduling system will shift the schedule from Periodicity Code 1 to Periodicity Code 2.  """  
      self.MinDeliveryQty1:int = obj["MinDeliveryQty1"]
      """  Minimum quantity for any given Purchase Contract Delivery relating to Periodicity Code 1.  """  
      self.MinDeliveryQty2:int = obj["MinDeliveryQty2"]
      """  Minimum quantity for any given Purchase Contract Delivery relating to Periodicity Code 2.  """  
      self.MinForwardSpan:int = obj["MinForwardSpan"]
      """  How far into the future the Minimum Delivery Quantity should be applied.  """  
      self.FirmIncrease:int = obj["FirmIncrease"]
      """  Used only when Periodicity Code 2 (Daily) is used - and defines how many days from the current date that no increases in quantity are allowed.  """  
      self.FirmDecrease:int = obj["FirmDecrease"]
      """  Used only when Periodicity Code 2 (Daily) is used - and defines how many days from the current date that no decreases in quantity are allowed.  """  
      self.OrderCover:int = obj["OrderCover"]
      """  How many days into the future Purchase Order Releases should be created for the Purchase Contract.  """  
      self.MaterialCover:int = obj["MaterialCover"]
      """  How many days of Material Costs will be honored on the Purchase Contract.  """  
      self.PrintLength:int = obj["PrintLength"]
      """  The Number of Days for which the Part Schedule will be printed.  """  
      self.ScheduleLength:int = obj["ScheduleLength"]
      """  The maximum period for which schedules will be created.  """  
      self.ScheduleFirm:int = obj["ScheduleFirm"]
      """  The number of days for which the current schedule is considered firm and will not be overwritten by a new proposed schedule.  If this value is zero, then all dates can be overwritten.  """  
      self.DevChar01:str = obj["DevChar01"]
      """  For development use only.  """  
      self.DevChar02:str = obj["DevChar02"]
      """  For development use only.  """  
      self.DevChar03:str = obj["DevChar03"]
      """  For development use only.  """  
      self.DevChar04:str = obj["DevChar04"]
      """  For development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  PartDesctiption  """  
      self.AreMinQuantitiesZero:bool = obj["AreMinQuantitiesZero"]
      """  Check if both MinDeliveryQty's are 0  """  
      self.IUM:str = obj["IUM"]
      """  Base UOM  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartSchedListTableset:
   def __init__(self, obj):
      self.PartSchedList:list[Erp_Tablesets_PartSchedListRow] = obj["PartSchedList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartSchedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.IsActive:bool = obj["IsActive"]
      """  Is this Part active within a Purchase Contract Schedule within this Site?  """  
      self.CalendarID:str = obj["CalendarID"]
      """   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  """  
      self.PeriodicityCode1:int = obj["PeriodicityCode1"]
      """  Periodicity Code.  Possible values are 1 = Semi-Weekly, 2 = Daily, 3 = Monthly Forward, 4 = Weekly Forward, 5 = Weekly Not Last Week of the Month, 6 = Nth Day of the Month  """  
      self.PeriodicityCode2:int = obj["PeriodicityCode2"]
      """  Periodicity Code.  Possible values are 1 = Semi-Weekly, 2 = Daily, 3 = Monthly Forward, 4 = Weekly Forward, 5 = Weekly Not Last Week of the Month, 6 = Nth Day of the Month  """  
      self.PeriodShift:int = obj["PeriodShift"]
      """  Defines when the scheduling system will shift the schedule from Periodicity Code 1 to Periodicity Code 2.  """  
      self.MinDeliveryQty1:int = obj["MinDeliveryQty1"]
      """  Minimum quantity for any given Purchase Contract Delivery relating to Periodicity Code 1.  """  
      self.MinDeliveryQty2:int = obj["MinDeliveryQty2"]
      """  Minimum quantity for any given Purchase Contract Delivery relating to Periodicity Code 2.  """  
      self.MinForwardSpan:int = obj["MinForwardSpan"]
      """  How far into the future the Minimum Delivery Quantity should be applied.  """  
      self.FirmIncrease:int = obj["FirmIncrease"]
      """  Used only when Periodicity Code 2 (Daily) is used - and defines how many days from the current date that no increases in quantity are allowed.  """  
      self.FirmDecrease:int = obj["FirmDecrease"]
      """  Used only when Periodicity Code 2 (Daily) is used - and defines how many days from the current date that no decreases in quantity are allowed.  """  
      self.OrderCover:int = obj["OrderCover"]
      """  How many days into the future Purchase Order Releases should be created for the Purchase Contract.  """  
      self.MaterialCover:int = obj["MaterialCover"]
      """  How many days of Material Costs will be honored on the Purchase Contract.  """  
      self.PrintLength:int = obj["PrintLength"]
      """  The Number of Days for which the Part Schedule will be printed.  """  
      self.ScheduleLength:int = obj["ScheduleLength"]
      """  The maximum period for which schedules will be created.  """  
      self.ScheduleFirm:int = obj["ScheduleFirm"]
      """  The number of days for which the current schedule is considered firm and will not be overwritten by a new proposed schedule.  If this value is zero, then all dates can be overwritten.  """  
      self.DevChar01:str = obj["DevChar01"]
      """  For development use only.  """  
      self.DevChar02:str = obj["DevChar02"]
      """  For development use only.  """  
      self.DevChar03:str = obj["DevChar03"]
      """  For development use only.  """  
      self.DevChar04:str = obj["DevChar04"]
      """  For development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  PartDesctiption  """  
      self.AreMinQuantitiesZero:bool = obj["AreMinQuantitiesZero"]
      """  Check if both MinDeliveryQty's are 0  """  
      self.IUM:str = obj["IUM"]
      """  Base UOM  """  
      self.LastRunDate:str = obj["LastRunDate"]
      self.BitFlag:int = obj["BitFlag"]
      self.PlantName:str = obj["PlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartSchedTableset:
   def __init__(self, obj):
      self.PartSched:list[Erp_Tablesets_PartSchedRow] = obj["PartSched"]
      self.PartSchedVend:list[Erp_Tablesets_PartSchedVendRow] = obj["PartSchedVend"]
      self.PartSchedVendPO:list[Erp_Tablesets_PartSchedVendPORow] = obj["PartSchedVendPO"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartSchedVendPORow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.PurPoint:str = obj["PurPoint"]
      """  PurPoint  """  
      self.ContractPONum:int = obj["ContractPONum"]
      """  ContractPONum  """  
      self.ContractPOLine:int = obj["ContractPOLine"]
      """  ContractPOLine  """  
      self.ContractStartDate:str = obj["ContractStartDate"]
      """  ContractStartDate  """  
      self.ContractEndDate:str = obj["ContractEndDate"]
      """  ContractEndDate  """  
      self.IsActive:bool = obj["IsActive"]
      """  IsActive  """  
      self.IsExpired:bool = obj["IsExpired"]
      """  IsExpired  """  
      self.IsApproved:bool = obj["IsApproved"]
      """  IsApproved  """  
      self.PercentShare:int = obj["PercentShare"]
      """  PercentShare  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ScheduleFirmDate:str = obj["ScheduleFirmDate"]
      self.MinPeriod1ShiftDate:str = obj["MinPeriod1ShiftDate"]
      self.MinForwardSpanDate:str = obj["MinForwardSpanDate"]
      self.LastRunDate:str = obj["LastRunDate"]
      self.BitFlag:int = obj["BitFlag"]
      self.PlantName:str = obj["PlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartSchedVendRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.PercentShare:int = obj["PercentShare"]
      """  Percentage Share of the Purchase Schedule for this Supplier.  Total of all Suppliers for this Part must equal 100 percent.  """  
      self.InspNextDelivery:int = obj["InspNextDelivery"]
      """  Should the Inspection flag be set when the Purchase Schedule is approved.  """  
      self.ContractPONum:int = obj["ContractPONum"]
      """  Purchase order number that uniquely identifies the Contract Purchase Order.  """  
      self.ContractPOLine:int = obj["ContractPOLine"]
      """  The line number of the detail record on the Contract Purchase Order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.DeliverMonday:bool = obj["DeliverMonday"]
      """  Does the Supplier make deliveries on Monday?  """  
      self.DeliverTuesday:bool = obj["DeliverTuesday"]
      """  Does the Supplier make deliveries on Tuesday?  """  
      self.DeliverWednesday:bool = obj["DeliverWednesday"]
      """  Does the Supplier make deliveries on Wednesday?  """  
      self.DeliverThursday:bool = obj["DeliverThursday"]
      """  Does the Supplier make deliveries on Thursday?  """  
      self.DeliverFriday:bool = obj["DeliverFriday"]
      """  Does the Supplier make deliveries on Friday?  """  
      self.DeliverSaturday:bool = obj["DeliverSaturday"]
      """  Does the Supplier make deliveries on Saturday?  """  
      self.DeliverSunday:bool = obj["DeliverSunday"]
      """  Does the Supplier make deliveries on Sunday?  """  
      self.DevChar01:str = obj["DevChar01"]
      """  For development use only.  """  
      self.DevChar02:str = obj["DevChar02"]
      """  For development use only.  """  
      self.DevChar03:str = obj["DevChar03"]
      """  For development use only.  """  
      self.DevChar04:str = obj["DevChar04"]
      """  For development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.VendorName:str = obj["VendorName"]
      """  VendorName  """  
      self.VendorID:str = obj["VendorID"]
      """  VendorID  """  
      self.IsActive:bool = obj["IsActive"]
      """  Indicates if the Supplier is active.  Supplier is inactive if PercentShare is 0.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PlantName:str = obj["PlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtPartSchedTableset:
   def __init__(self, obj):
      self.PartSched:list[Erp_Tablesets_PartSchedRow] = obj["PartSched"]
      self.PartSchedVend:list[Erp_Tablesets_PartSchedVendRow] = obj["PartSchedVend"]
      self.PartSchedVendPO:list[Erp_Tablesets_PartSchedVendPORow] = obj["PartSchedVendPO"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FindPart_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      pass

class FindPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      self.opMatchType:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   partNum
   plant
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.plant:str = obj["plant"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartSchedTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartSchedTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartSchedTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartSchedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPartSchedVendPO_input:
   """ Required : 
   ds
   partNum
   plant
   vendorNum
   purPoint
   contractPONum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.plant:str = obj["plant"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.contractPONum:int = obj["contractPONum"]
      pass

class GetNewPartSchedVendPO_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPartSchedVend_input:
   """ Required : 
   ds
   partNum
   plant
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.plant:str = obj["plant"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewPartSchedVend_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPartSched_input:
   """ Required : 
   ds
   partNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      pass

class GetNewPartSched_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartFromRowID_input:
   """ Required : 
   ipRowType
   ipRowID
   """  
   def __init__(self, obj):
      self.ipRowType:str = obj["ipRowType"]
      self.ipRowID:str = obj["ipRowID"]
      pass

class GetPartFromRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPartXRefInfo_input:
   """ Required : 
   partNum
   SysRowID
   rowType
   uomCode
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      pass

class GetPartXRefInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.uomCode:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePartSched
   whereClausePartSchedVend
   whereClausePartSchedVendPO
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartSched:str = obj["whereClausePartSched"]
      self.whereClausePartSchedVend:str = obj["whereClausePartSchedVend"]
      self.whereClausePartSchedVendPO:str = obj["whereClausePartSchedVendPO"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartSchedTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetValidAndProjectedWorkingDate_input:
   """ Required : 
   BaseDate
   DaysToAdd
   ProdCalID
   """  
   def __init__(self, obj):
      self.BaseDate:str = obj["BaseDate"]
      self.DaysToAdd:int = obj["DaysToAdd"]
      self.ProdCalID:str = obj["ProdCalID"]
      pass

class GetValidAndProjectedWorkingDate_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

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

class OnChangeCalendarID_input:
   """ Required : 
   ProposedCalendarId
   ds
   """  
   def __init__(self, obj):
      self.ProposedCalendarId:str = obj["ProposedCalendarId"]
      """  The proposed CalendarId value  """  
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

class OnChangeCalendarID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeInspNextDelivery_input:
   """ Required : 
   proposedInspNextDelivery
   ds
   """  
   def __init__(self, obj):
      self.proposedInspNextDelivery:int = obj["proposedInspNextDelivery"]
      """  The proposed InspNextDelivery value  """  
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

class OnChangeInspNextDelivery_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMinDeliveryQty1_input:
   """ Required : 
   ipMinDeliveryQty1
   ds
   """  
   def __init__(self, obj):
      self.ipMinDeliveryQty1:int = obj["ipMinDeliveryQty1"]
      """  The proposed MinDeliveryQty1 value  """  
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

class OnChangeMinDeliveryQty1_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMinDeliveryQty2_input:
   """ Required : 
   ipMinDeliveryQty2
   ds
   """  
   def __init__(self, obj):
      self.ipMinDeliveryQty2:int = obj["ipMinDeliveryQty2"]
      """  The proposed MinDeliveryQty2 value  """  
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

class OnChangeMinDeliveryQty2_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMinForwardSpan_input:
   """ Required : 
   ProposedMinForwardSpan
   ds
   """  
   def __init__(self, obj):
      self.ProposedMinForwardSpan:int = obj["ProposedMinForwardSpan"]
      """  The proposed MinForwardSpan value  """  
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

class OnChangeMinForwardSpan_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOrderCover_input:
   """ Required : 
   ProposedOrderCover
   ds
   """  
   def __init__(self, obj):
      self.ProposedOrderCover:int = obj["ProposedOrderCover"]
      """  The proposed OrderCover value  """  
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

class OnChangeOrderCover_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartNum_input:
   """ Required : 
   ProposedPartNum
   uomCode
   ds
   """  
   def __init__(self, obj):
      self.ProposedPartNum:str = obj["ProposedPartNum"]
      """  The proposed PartNum value  """  
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePercentShare_input:
   """ Required : 
   ProposedPercentShare
   ds
   """  
   def __init__(self, obj):
      self.ProposedPercentShare:int = obj["ProposedPercentShare"]
      """  The proposed PercentShare value  """  
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

class OnChangePercentShare_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePeriodShift_input:
   """ Required : 
   ProposedPeriodShift
   ds
   """  
   def __init__(self, obj):
      self.ProposedPeriodShift:int = obj["ProposedPeriodShift"]
      """  The proposed PeriodShift value  """  
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

class OnChangePeriodShift_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePeriodicityCode1_input:
   """ Required : 
   ProposedPeriodicityCode1
   ds
   """  
   def __init__(self, obj):
      self.ProposedPeriodicityCode1:int = obj["ProposedPeriodicityCode1"]
      """  The proposed PeriodicityCode1 value  """  
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

class OnChangePeriodicityCode1_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePeriodicityCode2_input:
   """ Required : 
   proposedPeriodicityCode2
   ds
   """  
   def __init__(self, obj):
      self.proposedPeriodicityCode2:int = obj["proposedPeriodicityCode2"]
      """  The proposed PeriodicityCode2 value  """  
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

class OnChangePeriodicityCode2_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePrintLength_input:
   """ Required : 
   ProposedPrintLength
   ds
   """  
   def __init__(self, obj):
      self.ProposedPrintLength:int = obj["ProposedPrintLength"]
      """  The proposed PrintLength value  """  
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

class OnChangePrintLength_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePurPoint_input:
   """ Required : 
   ProposedPurPoint
   ds
   """  
   def __init__(self, obj):
      self.ProposedPurPoint:str = obj["ProposedPurPoint"]
      """  The proposed Purchase Point value  """  
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

class OnChangePurPoint_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeScheduleFirm_input:
   """ Required : 
   proposedScheduleFirm
   ds
   """  
   def __init__(self, obj):
      self.proposedScheduleFirm:int = obj["proposedScheduleFirm"]
      """  The proposed ScheduleFirm value  """  
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

class OnChangeScheduleFirm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeScheduleLength_input:
   """ Required : 
   ProposedScheduleLength
   ds
   """  
   def __init__(self, obj):
      self.ProposedScheduleLength:int = obj["ProposedScheduleLength"]
      """  The proposed ScheduleLength value  """  
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

class OnChangeScheduleLength_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeVendorID_input:
   """ Required : 
   ProposedVendorID
   ds
   """  
   def __init__(self, obj):
      self.ProposedVendorID:str = obj["ProposedVendorID"]
      """  The proposed VendorId value  """  
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

class OnChangeVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeVendorNum_input:
   """ Required : 
   ProposedVendorNum
   ds
   """  
   def __init__(self, obj):
      self.ProposedVendorNum:int = obj["ProposedVendorNum"]
      """  The proposed VendorNum value  """  
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

class OnChangeVendorNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PartPlantIsLinkedToContract_input:
   """ Required : 
   company
   plant
   partNum
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.plant:str = obj["plant"]
      self.partNum:str = obj["partNum"]
      pass

class PartPlantIsLinkedToContract_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartSchedTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartSchedTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

