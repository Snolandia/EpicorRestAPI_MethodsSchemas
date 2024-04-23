import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PriceGroupSvc
# Description: This will define the product groups that are available and related for purposes
of order based discounting.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PriceGroups(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PriceGroups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PriceGroups
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/PriceGroups",headers=creds) as resp:
           return await resp.json()

async def post_PriceGroups(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PriceGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PriceGroupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PriceGroupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/PriceGroups", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PriceGroups_Company_PriceGroupCode(Company, PriceGroupCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PriceGroup item
   Description: Calls GetByID to retrieve the PriceGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PriceGroupCode: Desc: PriceGroupCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/PriceGroups(" + Company + "," + PriceGroupCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PriceGroups_Company_PriceGroupCode(Company, PriceGroupCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PriceGroup for the service
   Description: Calls UpdateExt to update PriceGroup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PriceGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PriceGroupCode: Desc: PriceGroupCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PriceGroupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/PriceGroups(" + Company + "," + PriceGroupCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PriceGroups_Company_PriceGroupCode(Company, PriceGroupCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PriceGroup item
   Description: Call UpdateExt to delete PriceGroup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PriceGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PriceGroupCode: Desc: PriceGroupCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/PriceGroups(" + Company + "," + PriceGroupCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PriceGroups_Company_PriceGroupCode_PriceGrpValBrks(Company, PriceGroupCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PriceGrpValBrks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PriceGrpValBrks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PriceGroupCode: Desc: PriceGroupCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceGrpValBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/PriceGroups(" + Company + "," + PriceGroupCode + ")/PriceGrpValBrks",headers=creds) as resp:
           return await resp.json()

async def get_PriceGroups_Company_PriceGroupCode_PriceGrpValBrks_Company_PriceGroupCode_OrderValue(Company, PriceGroupCode, OrderValue, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PriceGrpValBrk item
   Description: Calls GetByID to retrieve the PriceGrpValBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceGrpValBrk1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PriceGroupCode: Desc: PriceGroupCode   Required: True   Allow empty value : True
      :param OrderValue: Desc: OrderValue   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceGrpValBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/PriceGroups(" + Company + "," + PriceGroupCode + ")/PriceGrpValBrks(" + Company + "," + PriceGroupCode + "," + OrderValue + ")",headers=creds) as resp:
           return await resp.json()

async def get_PriceGroups_Company_PriceGroupCode_ProdGrups(Company, PriceGroupCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ProdGrups items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ProdGrups1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PriceGroupCode: Desc: PriceGroupCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdGrupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/PriceGroups(" + Company + "," + PriceGroupCode + ")/ProdGrups",headers=creds) as resp:
           return await resp.json()

async def get_PriceGroups_Company_PriceGroupCode_ProdGrups_Company_ProdCode(Company, PriceGroupCode, ProdCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProdGrup item
   Description: Calls GetByID to retrieve the ProdGrup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdGrup1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PriceGroupCode: Desc: PriceGroupCode   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ProdGrupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/PriceGroups(" + Company + "," + PriceGroupCode + ")/ProdGrups(" + Company + "," + ProdCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PriceGrpValBrks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PriceGrpValBrks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PriceGrpValBrks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceGrpValBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/PriceGrpValBrks",headers=creds) as resp:
           return await resp.json()

async def post_PriceGrpValBrks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PriceGrpValBrks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PriceGrpValBrkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PriceGrpValBrkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/PriceGrpValBrks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PriceGrpValBrks_Company_PriceGroupCode_OrderValue(Company, PriceGroupCode, OrderValue, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PriceGrpValBrk item
   Description: Calls GetByID to retrieve the PriceGrpValBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceGrpValBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PriceGroupCode: Desc: PriceGroupCode   Required: True   Allow empty value : True
      :param OrderValue: Desc: OrderValue   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceGrpValBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/PriceGrpValBrks(" + Company + "," + PriceGroupCode + "," + OrderValue + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PriceGrpValBrks_Company_PriceGroupCode_OrderValue(Company, PriceGroupCode, OrderValue, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PriceGrpValBrk for the service
   Description: Calls UpdateExt to update PriceGrpValBrk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PriceGrpValBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PriceGroupCode: Desc: PriceGroupCode   Required: True   Allow empty value : True
      :param OrderValue: Desc: OrderValue   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PriceGrpValBrkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/PriceGrpValBrks(" + Company + "," + PriceGroupCode + "," + OrderValue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PriceGrpValBrks_Company_PriceGroupCode_OrderValue(Company, PriceGroupCode, OrderValue, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PriceGrpValBrk item
   Description: Call UpdateExt to delete PriceGrpValBrk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PriceGrpValBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PriceGroupCode: Desc: PriceGroupCode   Required: True   Allow empty value : True
      :param OrderValue: Desc: OrderValue   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/PriceGrpValBrks(" + Company + "," + PriceGroupCode + "," + OrderValue + ")",headers=creds) as resp:
           return await resp.json()

async def get_ProdGrups(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ProdGrups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProdGrups
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdGrupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/ProdGrups",headers=creds) as resp:
           return await resp.json()

async def post_ProdGrups(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProdGrups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ProdGrupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ProdGrupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/ProdGrups", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ProdGrups_Company_ProdCode(Company, ProdCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProdGrup item
   Description: Calls GetByID to retrieve the ProdGrup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdGrup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ProdGrupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/ProdGrups(" + Company + "," + ProdCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ProdGrups_Company_ProdCode(Company, ProdCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ProdGrup for the service
   Description: Calls UpdateExt to update ProdGrup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProdGrup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ProdGrupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/ProdGrups(" + Company + "," + ProdCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ProdGrups_Company_ProdCode(Company, ProdCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ProdGrup item
   Description: Call UpdateExt to delete ProdGrup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProdGrup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/ProdGrups(" + Company + "," + ProdCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceGroupListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePriceGroup, whereClausePriceGrpValBrk, whereClauseProdGrup, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePriceGroup=" + whereClausePriceGroup
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePriceGrpValBrk=" + whereClausePriceGrpValBrk
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseProdGrup=" + whereClauseProdGrup
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(priceGroupCode, epicorHeaders = None):
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
   params += "priceGroupCode=" + priceGroupCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AddAllProdGroups(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddAllProdGroups
   Description: Add all available Product Groups to current Price Group
   OperationID: AddAllProdGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddAllProdGroups_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddAllProdGroups_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddNewProdToPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddNewProdToPrice
   Description: Add new Product Group to Price Group or replace old Product Group
   OperationID: AddNewProdToPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddNewProdToPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddNewProdToPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckNewProdCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckNewProdCode
   Description: Validation of new Product group before it'll be added to Price Group
   OperationID: CheckNewProdCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckNewProdCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckNewProdCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateNewProd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateNewProd
   Description: Add new Product Group as child record to Price Group with empty Prod Code
   OperationID: CreateNewProd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateNewProd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewProd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteProdGroupFromPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteProdGroupFromPrice
   Description: Delete link between Price and Product Group (delete child record)
   OperationID: DeleteProdGroupFromPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteProdGroupFromPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteProdGroupFromPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveAllProdGroups(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveAllProdGroups
   Description: Delete all links between Product Groups and current Price Group
   OperationID: RemoveAllProdGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveAllProdGroups_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveAllProdGroups_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPriceGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPriceGroup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPriceGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPriceGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPriceGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPriceGrpValBrk(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPriceGrpValBrk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPriceGrpValBrk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPriceGrpValBrk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPriceGrpValBrk_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewProdGrup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewProdGrup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewProdGrup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewProdGrup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProdGrup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceGroupListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PriceGroupListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceGroupRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PriceGroupRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceGrpValBrkRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PriceGrpValBrkRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdGrupRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ProdGrupRow] = obj["value"]
      pass

class Erp_Tablesets_PriceGroupListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  Unique identifier of the Price Group.  """  
      self.Description:str = obj["Description"]
      """  Price Group description  """  
      self.QuantityDiscount:bool = obj["QuantityDiscount"]
      """  Determines if Quantity based discounts are available to this price group.  """  
      self.ValueDiscount:bool = obj["ValueDiscount"]
      """  Determines if Value based discounts apply to this price group.  """  
      self.GlobalPriceGroup:bool = obj["GlobalPriceGroup"]
      """  Marks this PriceGroup as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProdGroupDescription:str = obj["ProdGroupDescription"]
      """  Product code description List  """  
      self.AvailProdGrp:str = obj["AvailProdGrp"]
      """  List of available product groups to choose from  """  
      self.AvailProdGrpDesc:str = obj["AvailProdGrpDesc"]
      """  List of available product group descriptions  """  
      self.dspProdGroupList:str = obj["dspProdGroupList"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  Unique identifier of the Price Group.  """  
      self.Description:str = obj["Description"]
      """  Price Group description  """  
      self.QuantityDiscount:bool = obj["QuantityDiscount"]
      """  Determines if Quantity based discounts are available to this price group.  """  
      self.ValueDiscount:bool = obj["ValueDiscount"]
      """  Determines if Value based discounts apply to this price group.  """  
      self.GlobalPriceGroup:bool = obj["GlobalPriceGroup"]
      """  Marks this PriceGroup as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProdGroupDescription:str = obj["ProdGroupDescription"]
      """  Product code description List  """  
      self.AvailProdGrp:str = obj["AvailProdGrp"]
      """  List of available product groups to choose from  """  
      self.AvailProdGrpDesc:str = obj["AvailProdGrpDesc"]
      """  List of available product group descriptions  """  
      self.dspProdGroupList:str = obj["dspProdGroupList"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceGrpValBrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the unique Price Group ID.  """  
      self.OrderValue:int = obj["OrderValue"]
      """  This is the Order Value break amount in base currency.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The discount percentage applicable to break amount.  """  
      self.GlobalPriceGrpValBrk:bool = obj["GlobalPriceGrpValBrk"]
      """  Marks this PriceGrpValBrk as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProdGrupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Descriptive code assigned by the user to uniquely identify a Product Group master. Can't be blank. Used as a foreign key in other files and may be used in displays/reports where space for the full description is not available.  """  
      self.Description:str = obj["Description"]
      """  Full description of Product Group.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the default Production Planner. This person is responsible for handling  the manufacturing suggestions of parts in this Product Group.
Used as the default for "new" manufacturing suggestions and on Job Header. Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty for this Product group  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax category master record.  Cannot be blank.  This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  Examples: SERV = Service, FRT = Freight, etc.  """  
      self.JobCompletionCode:str = obj["JobCompletionCode"]
      """  The default job completion code for this product group. This code is used in the auto-job completion process.  """  
      self.JobClosingCode:str = obj["JobClosingCode"]
      """  The default job closing code for this product group. This code is used in the auto-job closing process.  """  
      self.RoughCutCode:str = obj["RoughCutCode"]
      """  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for a part using this product code.  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  Specifies the Price Group Code where the current Product Group belongs  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.GlobalProdGrup:bool = obj["GlobalProdGrup"]
      """  Marks this ProdGrup as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.ProdFamilyID:str = obj["ProdFamilyID"]
      """  Descriptive code assigned by the user to uniquely identify a Product Family master.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Territory ID selected for the Product Group.  """  
      self.TerritoryDesc:str = obj["TerritoryDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.JobClosingCodeDescription:str = obj["JobClosingCodeDescription"]
      self.JobCompletionCodeDescription:str = obj["JobCompletionCodeDescription"]
      self.PersonIDName:str = obj["PersonIDName"]
      self.PlantName:str = obj["PlantName"]
      self.RASchedCdRADesc:str = obj["RASchedCdRADesc"]
      self.RoughCutParamDescription:str = obj["RoughCutParamDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.IgnoreInvoiceSch_c:bool = obj["IgnoreInvoiceSch_c"]
      self.IgnoreInUploadTool_c:bool = obj["IgnoreInUploadTool_c"]
      self.MustShipBeforeRevenue_c:bool = obj["MustShipBeforeRevenue_c"]
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddAllProdGroups_input:
   """ Required : 
   prPriceGroupCode
   ds
   """  
   def __init__(self, obj):
      self.prPriceGroupCode:str = obj["prPriceGroupCode"]
      """  Price Group Code  """  
      self.ds:list[Erp_Tablesets_PriceGroupTableset] = obj["ds"]
      pass

class AddAllProdGroups_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AddNewProdToPrice_input:
   """ Required : 
   prPriceGroupCode
   prProdCodeOld
   prProdCodeNew
   ds
   """  
   def __init__(self, obj):
      self.prPriceGroupCode:str = obj["prPriceGroupCode"]
      self.prProdCodeOld:str = obj["prProdCodeOld"]
      self.prProdCodeNew:str = obj["prProdCodeNew"]
      self.ds:list[Erp_Tablesets_PriceGroupTableset] = obj["ds"]
      pass

class AddNewProdToPrice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckNewProdCode_input:
   """ Required : 
   prPriceGroupCode
   prProdCodeNew
   """  
   def __init__(self, obj):
      self.prPriceGroupCode:str = obj["prPriceGroupCode"]
      """  Price Group Code  """  
      self.prProdCodeNew:str = obj["prProdCodeNew"]
      """  Product Group Code  """  
      pass

class CheckNewProdCode_output:
   def __init__(self, obj):
      pass

class CreateNewProd_input:
   """ Required : 
   prPriceGroupCode
   ds
   """  
   def __init__(self, obj):
      self.prPriceGroupCode:str = obj["prPriceGroupCode"]
      self.ds:list[Erp_Tablesets_PriceGroupTableset] = obj["ds"]
      pass

class CreateNewProd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   priceGroupCode
   """  
   def __init__(self, obj):
      self.priceGroupCode:str = obj["priceGroupCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteProdGroupFromPrice_input:
   """ Required : 
   prProdCode
   ds
   """  
   def __init__(self, obj):
      self.prProdCode:str = obj["prProdCode"]
      self.ds:list[Erp_Tablesets_PriceGroupTableset] = obj["ds"]
      pass

class DeleteProdGroupFromPrice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_PriceGroupListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  Unique identifier of the Price Group.  """  
      self.Description:str = obj["Description"]
      """  Price Group description  """  
      self.QuantityDiscount:bool = obj["QuantityDiscount"]
      """  Determines if Quantity based discounts are available to this price group.  """  
      self.ValueDiscount:bool = obj["ValueDiscount"]
      """  Determines if Value based discounts apply to this price group.  """  
      self.GlobalPriceGroup:bool = obj["GlobalPriceGroup"]
      """  Marks this PriceGroup as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProdGroupDescription:str = obj["ProdGroupDescription"]
      """  Product code description List  """  
      self.AvailProdGrp:str = obj["AvailProdGrp"]
      """  List of available product groups to choose from  """  
      self.AvailProdGrpDesc:str = obj["AvailProdGrpDesc"]
      """  List of available product group descriptions  """  
      self.dspProdGroupList:str = obj["dspProdGroupList"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceGroupListTableset:
   def __init__(self, obj):
      self.PriceGroupList:list[Erp_Tablesets_PriceGroupListRow] = obj["PriceGroupList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PriceGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  Unique identifier of the Price Group.  """  
      self.Description:str = obj["Description"]
      """  Price Group description  """  
      self.QuantityDiscount:bool = obj["QuantityDiscount"]
      """  Determines if Quantity based discounts are available to this price group.  """  
      self.ValueDiscount:bool = obj["ValueDiscount"]
      """  Determines if Value based discounts apply to this price group.  """  
      self.GlobalPriceGroup:bool = obj["GlobalPriceGroup"]
      """  Marks this PriceGroup as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProdGroupDescription:str = obj["ProdGroupDescription"]
      """  Product code description List  """  
      self.AvailProdGrp:str = obj["AvailProdGrp"]
      """  List of available product groups to choose from  """  
      self.AvailProdGrpDesc:str = obj["AvailProdGrpDesc"]
      """  List of available product group descriptions  """  
      self.dspProdGroupList:str = obj["dspProdGroupList"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceGroupTableset:
   def __init__(self, obj):
      self.PriceGroup:list[Erp_Tablesets_PriceGroupRow] = obj["PriceGroup"]
      self.PriceGrpValBrk:list[Erp_Tablesets_PriceGrpValBrkRow] = obj["PriceGrpValBrk"]
      self.ProdGrup:list[Erp_Tablesets_ProdGrupRow] = obj["ProdGrup"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PriceGrpValBrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the unique Price Group ID.  """  
      self.OrderValue:int = obj["OrderValue"]
      """  This is the Order Value break amount in base currency.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The discount percentage applicable to break amount.  """  
      self.GlobalPriceGrpValBrk:bool = obj["GlobalPriceGrpValBrk"]
      """  Marks this PriceGrpValBrk as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProdGrupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Descriptive code assigned by the user to uniquely identify a Product Group master. Can't be blank. Used as a foreign key in other files and may be used in displays/reports where space for the full description is not available.  """  
      self.Description:str = obj["Description"]
      """  Full description of Product Group.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the default Production Planner. This person is responsible for handling  the manufacturing suggestions of parts in this Product Group.
Used as the default for "new" manufacturing suggestions and on Job Header. Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty for this Product group  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax category master record.  Cannot be blank.  This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  Examples: SERV = Service, FRT = Freight, etc.  """  
      self.JobCompletionCode:str = obj["JobCompletionCode"]
      """  The default job completion code for this product group. This code is used in the auto-job completion process.  """  
      self.JobClosingCode:str = obj["JobClosingCode"]
      """  The default job closing code for this product group. This code is used in the auto-job closing process.  """  
      self.RoughCutCode:str = obj["RoughCutCode"]
      """  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for a part using this product code.  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  Specifies the Price Group Code where the current Product Group belongs  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.GlobalProdGrup:bool = obj["GlobalProdGrup"]
      """  Marks this ProdGrup as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.ProdFamilyID:str = obj["ProdFamilyID"]
      """  Descriptive code assigned by the user to uniquely identify a Product Family master.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Territory ID selected for the Product Group.  """  
      self.TerritoryDesc:str = obj["TerritoryDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.JobClosingCodeDescription:str = obj["JobClosingCodeDescription"]
      self.JobCompletionCodeDescription:str = obj["JobCompletionCodeDescription"]
      self.PersonIDName:str = obj["PersonIDName"]
      self.PlantName:str = obj["PlantName"]
      self.RASchedCdRADesc:str = obj["RASchedCdRADesc"]
      self.RoughCutParamDescription:str = obj["RoughCutParamDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.IgnoreInvoiceSch_c:bool = obj["IgnoreInvoiceSch_c"]
      self.IgnoreInUploadTool_c:bool = obj["IgnoreInUploadTool_c"]
      self.MustShipBeforeRevenue_c:bool = obj["MustShipBeforeRevenue_c"]
      pass

class Erp_Tablesets_UpdExtPriceGroupTableset:
   def __init__(self, obj):
      self.PriceGroup:list[Erp_Tablesets_PriceGroupRow] = obj["PriceGroup"]
      self.PriceGrpValBrk:list[Erp_Tablesets_PriceGrpValBrkRow] = obj["PriceGrpValBrk"]
      self.ProdGrup:list[Erp_Tablesets_ProdGrupRow] = obj["ProdGrup"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   priceGroupCode
   """  
   def __init__(self, obj):
      self.priceGroupCode:str = obj["priceGroupCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PriceGroupTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PriceGroupTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PriceGroupTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PriceGroupListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPriceGroup_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceGroupTableset] = obj["ds"]
      pass

class GetNewPriceGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPriceGrpValBrk_input:
   """ Required : 
   ds
   priceGroupCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceGroupTableset] = obj["ds"]
      self.priceGroupCode:str = obj["priceGroupCode"]
      pass

class GetNewPriceGrpValBrk_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewProdGrup_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceGroupTableset] = obj["ds"]
      pass

class GetNewProdGrup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePriceGroup
   whereClausePriceGrpValBrk
   whereClauseProdGrup
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePriceGroup:str = obj["whereClausePriceGroup"]
      self.whereClausePriceGrpValBrk:str = obj["whereClausePriceGrpValBrk"]
      self.whereClauseProdGrup:str = obj["whereClauseProdGrup"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PriceGroupTableset] = obj["returnObj"]
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

class RemoveAllProdGroups_input:
   """ Required : 
   prPriceGroupCode
   ds
   """  
   def __init__(self, obj):
      self.prPriceGroupCode:str = obj["prPriceGroupCode"]
      """  Price Group Code  """  
      self.ds:list[Erp_Tablesets_PriceGroupTableset] = obj["ds"]
      pass

class RemoveAllProdGroups_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPriceGroupTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPriceGroupTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceGroupTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

