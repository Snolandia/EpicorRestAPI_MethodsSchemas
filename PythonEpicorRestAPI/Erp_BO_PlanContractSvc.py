import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PlanContractSvc
# Description: Plan Contract Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PlanContracts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlanContracts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanContracts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractHdrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContracts",headers=creds) as resp:
           return await resp.json()

async def post_PlanContracts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanContracts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlanContractHdrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlanContractHdrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContracts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlanContracts_Company_ContractID(Company, ContractID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlanContract item
   Description: Calls GetByID to retrieve the PlanContract item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContract
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractID: Desc: ContractID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractHdrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContracts(" + Company + "," + ContractID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlanContracts_Company_ContractID(Company, ContractID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlanContract for the service
   Description: Calls UpdateExt to update PlanContract. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanContract
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractID: Desc: ContractID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlanContractHdrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContracts(" + Company + "," + ContractID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlanContracts_Company_ContractID(Company, ContractID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlanContract item
   Description: Call UpdateExt to delete PlanContract item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanContract
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractID: Desc: ContractID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContracts(" + Company + "," + ContractID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlanContracts_Company_ContractID_PlanContractDtls(Company, ContractID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PlanContractDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlanContractDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractID: Desc: ContractID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContracts(" + Company + "," + ContractID + ")/PlanContractDtls",headers=creds) as resp:
           return await resp.json()

async def get_PlanContracts_Company_ContractID_PlanContractDtls_Company_ContractID_LineNum(Company, ContractID, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlanContractDtl item
   Description: Calls GetByID to retrieve the PlanContractDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractID: Desc: ContractID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContracts(" + Company + "," + ContractID + ")/PlanContractDtls(" + Company + "," + ContractID + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlanContracts_Company_ContractID_PlanContractWhseBins(Company, ContractID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PlanContractWhseBins items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlanContractWhseBins1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractID: Desc: ContractID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractWhseBinRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContracts(" + Company + "," + ContractID + ")/PlanContractWhseBins",headers=creds) as resp:
           return await resp.json()

async def get_PlanContracts_Company_ContractID_PlanContractWhseBins_Company_ContractID_WarehouseCode_BinNum(Company, ContractID, WarehouseCode, BinNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlanContractWhseBin item
   Description: Calls GetByID to retrieve the PlanContractWhseBin item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractWhseBin1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractID: Desc: ContractID   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractWhseBinRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContracts(" + Company + "," + ContractID + ")/PlanContractWhseBins(" + Company + "," + ContractID + "," + WarehouseCode + "," + BinNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlanContractDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlanContractDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanContractDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDtls",headers=creds) as resp:
           return await resp.json()

async def post_PlanContractDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanContractDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlanContractDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlanContractDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlanContractDtls_Company_ContractID_LineNum(Company, ContractID, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlanContractDtl item
   Description: Calls GetByID to retrieve the PlanContractDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractID: Desc: ContractID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDtls(" + Company + "," + ContractID + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlanContractDtls_Company_ContractID_LineNum(Company, ContractID, LineNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlanContractDtl for the service
   Description: Calls UpdateExt to update PlanContractDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanContractDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractID: Desc: ContractID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlanContractDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDtls(" + Company + "," + ContractID + "," + LineNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlanContractDtls_Company_ContractID_LineNum(Company, ContractID, LineNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlanContractDtl item
   Description: Call UpdateExt to delete PlanContractDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanContractDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractID: Desc: ContractID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDtls(" + Company + "," + ContractID + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlanContractWhseBins(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlanContractWhseBins items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanContractWhseBins
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractWhseBinRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractWhseBins",headers=creds) as resp:
           return await resp.json()

async def post_PlanContractWhseBins(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanContractWhseBins
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlanContractWhseBinRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlanContractWhseBinRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractWhseBins", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlanContractWhseBins_Company_ContractID_WarehouseCode_BinNum(Company, ContractID, WarehouseCode, BinNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlanContractWhseBin item
   Description: Calls GetByID to retrieve the PlanContractWhseBin item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractWhseBin
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractID: Desc: ContractID   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractWhseBinRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractWhseBins(" + Company + "," + ContractID + "," + WarehouseCode + "," + BinNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlanContractWhseBins_Company_ContractID_WarehouseCode_BinNum(Company, ContractID, WarehouseCode, BinNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlanContractWhseBin for the service
   Description: Calls UpdateExt to update PlanContractWhseBin. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanContractWhseBin
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractID: Desc: ContractID   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlanContractWhseBinRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractWhseBins(" + Company + "," + ContractID + "," + WarehouseCode + "," + BinNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlanContractWhseBins_Company_ContractID_WarehouseCode_BinNum(Company, ContractID, WarehouseCode, BinNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlanContractWhseBin item
   Description: Call UpdateExt to delete PlanContractWhseBin item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanContractWhseBin
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractID: Desc: ContractID   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractWhseBins(" + Company + "," + ContractID + "," + WarehouseCode + "," + BinNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlanContractDmdDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlanContractDmdDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanContractDmdDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractDmdDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdDtls",headers=creds) as resp:
           return await resp.json()

async def post_PlanContractDmdDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanContractDmdDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlanContractDmdDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlanContractDmdDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlanContractDmdDtls_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlanContractDmdDtl item
   Description: Calls GetByID to retrieve the PlanContractDmdDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractDmdDtl
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractDmdDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdDtls(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlanContractDmdDtls_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlanContractDmdDtl for the service
   Description: Calls UpdateExt to update PlanContractDmdDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanContractDmdDtl
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlanContractDmdDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdDtls(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlanContractDmdDtls_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlanContractDmdDtl item
   Description: Call UpdateExt to delete PlanContractDmdDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanContractDmdDtl
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdDtls(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlanContractDmdHdrs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlanContractDmdHdrs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanContractDmdHdrs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractDmdHdrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdHdrs",headers=creds) as resp:
           return await resp.json()

async def post_PlanContractDmdHdrs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanContractDmdHdrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlanContractDmdHdrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlanContractDmdHdrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdHdrs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlanContractDmdHdrs_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlanContractDmdHdr item
   Description: Calls GetByID to retrieve the PlanContractDmdHdr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractDmdHdr
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractDmdHdrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdHdrs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlanContractDmdHdrs_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlanContractDmdHdr for the service
   Description: Calls UpdateExt to update PlanContractDmdHdr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanContractDmdHdr
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlanContractDmdHdrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdHdrs(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlanContractDmdHdrs_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlanContractDmdHdr item
   Description: Call UpdateExt to delete PlanContractDmdHdr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanContractDmdHdr
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdHdrs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlanContractSplyDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlanContractSplyDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanContractSplyDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractSplyDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyDtls",headers=creds) as resp:
           return await resp.json()

async def post_PlanContractSplyDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanContractSplyDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlanContractSplyDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlanContractSplyDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlanContractSplyDtls_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlanContractSplyDtl item
   Description: Calls GetByID to retrieve the PlanContractSplyDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractSplyDtl
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractSplyDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyDtls(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlanContractSplyDtls_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlanContractSplyDtl for the service
   Description: Calls UpdateExt to update PlanContractSplyDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanContractSplyDtl
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlanContractSplyDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyDtls(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlanContractSplyDtls_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlanContractSplyDtl item
   Description: Call UpdateExt to delete PlanContractSplyDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanContractSplyDtl
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyDtls(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlanContractSplyHdrs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlanContractSplyHdrs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanContractSplyHdrs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractSplyHdrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyHdrs",headers=creds) as resp:
           return await resp.json()

async def post_PlanContractSplyHdrs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanContractSplyHdrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlanContractSplyHdrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlanContractSplyHdrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyHdrs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlanContractSplyHdrs_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlanContractSplyHdr item
   Description: Calls GetByID to retrieve the PlanContractSplyHdr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractSplyHdr
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractSplyHdrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyHdrs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlanContractSplyHdrs_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlanContractSplyHdr for the service
   Description: Calls UpdateExt to update PlanContractSplyHdr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanContractSplyHdr
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlanContractSplyHdrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyHdrs(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlanContractSplyHdrs_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlanContractSplyHdr item
   Description: Call UpdateExt to delete PlanContractSplyHdr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanContractSplyHdr
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyHdrs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlanContractTranDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlanContractTranDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanContractTranDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractTranDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranDtls",headers=creds) as resp:
           return await resp.json()

async def post_PlanContractTranDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanContractTranDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlanContractTranDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlanContractTranDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlanContractTranDtls_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlanContractTranDtl item
   Description: Calls GetByID to retrieve the PlanContractTranDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractTranDtl
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractTranDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranDtls(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlanContractTranDtls_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlanContractTranDtl for the service
   Description: Calls UpdateExt to update PlanContractTranDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanContractTranDtl
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlanContractTranDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranDtls(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlanContractTranDtls_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlanContractTranDtl item
   Description: Call UpdateExt to delete PlanContractTranDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanContractTranDtl
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranDtls(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlanContractTranHdrs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlanContractTranHdrs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanContractTranHdrs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractTranHdrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranHdrs",headers=creds) as resp:
           return await resp.json()

async def post_PlanContractTranHdrs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanContractTranHdrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlanContractTranHdrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlanContractTranHdrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranHdrs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlanContractTranHdrs_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlanContractTranHdr item
   Description: Calls GetByID to retrieve the PlanContractTranHdr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractTranHdr
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractTranHdrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranHdrs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlanContractTranHdrs_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlanContractTranHdr for the service
   Description: Calls UpdateExt to update PlanContractTranHdr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanContractTranHdr
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlanContractTranHdrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranHdrs(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlanContractTranHdrs_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlanContractTranHdr item
   Description: Call UpdateExt to delete PlanContractTranHdr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanContractTranHdr
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranHdrs(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractHdrListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePlanContractHdr, whereClausePlanContractDtl, whereClausePlanContractWhseBin, whereClausePlanContractDmdDtl, whereClausePlanContractDmdHdr, whereClausePlanContractSplyDtl, whereClausePlanContractSplyHdr, whereClausePlanContractTranDtl, whereClausePlanContractTranHdr, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClausePlanContractHdr=" + whereClausePlanContractHdr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePlanContractDtl=" + whereClausePlanContractDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePlanContractWhseBin=" + whereClausePlanContractWhseBin
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePlanContractDmdDtl=" + whereClausePlanContractDmdDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePlanContractDmdHdr=" + whereClausePlanContractDmdHdr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePlanContractSplyDtl=" + whereClausePlanContractSplyDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePlanContractSplyHdr=" + whereClausePlanContractSplyHdr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePlanContractTranDtl=" + whereClausePlanContractTranDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePlanContractTranHdr=" + whereClausePlanContractTranHdr
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(contractID, epicorHeaders = None):
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
   params += "contractID=" + contractID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ExistsInventoryOrReceivingBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistsInventoryOrReceivingBin
   Description: Validates PlanContractHdr.Active column changing:
1.-If a contract is flagged as inactive and there is stock in the warehouse / bin location defined at the contract, then a warning message should be shown.
   OperationID: ExistsInventoryOrReceivingBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsInventoryOrReceivingBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsInventoryOrReceivingBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeActive(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeActive
   Description: Validates PlanContractHdr.Active column changing:
1.-If a contract is flagged as inactive and there is stock in the warehouse / bin location defined at the contract, then a warning message should be shown.
   OperationID: OnChangeActive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeActive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeActive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeWhseBinDefaultInvWhseBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeWhseBinDefaultInvWhseBin
   Description: Validates PlanContractWhseBin.DefaultInvWhseBin column changing:
   OperationID: OnChangeWhseBinDefaultInvWhseBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWhseBinDefaultInvWhseBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWhseBinDefaultInvWhseBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeWhseBinDefaultRcvWhseBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeWhseBinDefaultRcvWhseBin
   Description: Validates PlanContractWhseBin.DefaultRcvWhseBin column changing:
   OperationID: OnChangeWhseBinDefaultRcvWhseBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWhseBinDefaultRcvWhseBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWhseBinDefaultRcvWhseBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeWhseBinBackflushBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeWhseBinBackflushBin
   Description: Validates PlanContractWhseBin.BackflushBin column changing:
   OperationID: OnChangeWhseBinBackflushBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWhseBinBackflushBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWhseBinBackflushBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeWhseBinWarehouseCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeWhseBinWarehouseCode
   Description: Validates PlanContractWhseBin.WarehouseCode column changing:
1.- The WarehouseCode field should only allow warehouses with at least one bin location flagged as contract bin.
2.-The same combination of warehouse/bin is only allowed once for all the active contracts.
   OperationID: OnChangeWhseBinWarehouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWhseBinWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWhseBinWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePlanContractDtlWarehouseCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePlanContractDtlWarehouseCode
   Description: Validates PlanContractDtl.WarehouseCode column changing:
1.- The WarehouseCode field should only allow warehouses with at least one bin location flagged as contract bin.
2.-The same combination of warehouse/bin must exist in PlanContractWhseBin
   OperationID: OnChangePlanContractDtlWarehouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePlanContractDtlWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePlanContractDtlWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlBinNum
   Description: Validates PlanContractDtl.BinNum column changing:
1.-The BinNum field should only allow bins that have a “Contract” Type.
2.-The same combination of warehouse/bin is only allowed once for all the active contracts.
   OperationID: OnChangeDtlBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeWhseBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeWhseBinNum
   Description: Validates PlanContractWhseBin.BinNum column changing:
1.-The BinNum field should only allow bins that have a “Contract” Type.
2.-The same combination of warehouse/bin is only allowed once for all the active contracts.
   OperationID: OnChangeWhseBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWhseBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWhseBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: Validates PlanContractDtl.PartNum column changing:
1.-	Sales Kits parts are not allowed in contract lines.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingAttributeSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContractHdrDmdRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContractHdrDmdRows
   Description: Get the dataset of Contract Demand Header.
   OperationID: GetContractHdrDmdRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContractHdrDmdRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractHdrDmdRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContractDtlDmdRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContractDtlDmdRows
   Description: Get the dataset of Contract Demand Lines.
   OperationID: GetContractDtlDmdRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContractDtlDmdRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractDtlDmdRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContractHdrTranRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContractHdrTranRows
   Description: Get the dataset of Contract Transaction Header.
   OperationID: GetContractHdrTranRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContractHdrTranRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractHdrTranRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContractDtlTranRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContractDtlTranRows
   Description: Get the dataset of Contract Transaction Header.
   OperationID: GetContractDtlTranRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContractDtlTranRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractDtlTranRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContractSplyRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContractSplyRows
   Description: Get the dataset for Plan Contract Supply (Hdr or Dtl).
If param sPart has value you get PlanContractSplyDtl table otherwhise PlanContractSplyHdr table(all parts).
   OperationID: GetContractSplyRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContractSplyRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractSplyRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePlanContractHdrinDiffPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePlanContractHdrinDiffPlant
   Description: Validate whether the ContractID belongs to another plant.
   OperationID: ValidatePlanContractHdrinDiffPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePlanContractHdrinDiffPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePlanContractHdrinDiffPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeContractDemandQuantities(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeContractDemandQuantities
   Description: Update Plan Contract Detail information when the Contract UOM or Contrcat Qty changes
   OperationID: ChangeContractDemandQuantities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeContractDemandQuantities_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeContractDemandQuantities_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPlanContractHdr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPlanContractHdr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlanContractHdr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlanContractHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlanContractHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPlanContractDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPlanContractDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlanContractDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlanContractDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlanContractDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPlanContractWhseBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPlanContractWhseBin
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlanContractWhseBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlanContractWhseBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlanContractWhseBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractDmdDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlanContractDmdDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractDmdHdrRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlanContractDmdHdrRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlanContractDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractHdrListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlanContractHdrListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractHdrRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlanContractHdrRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractSplyDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlanContractSplyDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractSplyHdrRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlanContractSplyHdrRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractTranDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlanContractTranDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractTranHdrRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlanContractTranHdrRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractWhseBinRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlanContractWhseBinRow] = obj["value"]
      pass

class Erp_Tablesets_PlanContractDmdDtlRow:
   def __init__(self, obj):
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.Company:str = obj["Company"]
      self.ContractID:str = obj["ContractID"]
      self.DueDate:str = obj["DueDate"]
      self.IUM:str = obj["IUM"]
      self.JobNum:str = obj["JobNum"]
      self.LineNum:int = obj["LineNum"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.RequiredQty:int = obj["RequiredQty"]
      self.SourceName:str = obj["SourceName"]
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.TFLineNum:str = obj["TFLineNum"]
      self.PartNum:str = obj["PartNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetDesc:str = obj["AttributeSetDesc"]
      """  Description of values in set  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDesc:str = obj["AttributeSetShortDesc"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlanContractDmdHdrRow:
   def __init__(self, obj):
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.Company:str = obj["Company"]
      self.ContractID:str = obj["ContractID"]
      self.DueDate:str = obj["DueDate"]
      self.IUM:str = obj["IUM"]
      self.JobNum:str = obj["JobNum"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.RequiredQty:int = obj["RequiredQty"]
      self.SourceName:str = obj["SourceName"]
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.TFLineNum:str = obj["TFLineNum"]
      self.PartNum:str = obj["PartNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetDesc:str = obj["AttributeSetDesc"]
      """  Description of values in set  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDesc:str = obj["AttributeSetShortDesc"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlanContractDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractID:str = obj["ContractID"]
      """  The unique identifier of the planning contract.  """  
      self.LineNum:int = obj["LineNum"]
      """  The unique identifier of the planning contract line.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part. Sales Kits not allowed. Same part number can only be entered once in the same contract.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.ContractQty:int = obj["ContractQty"]
      """  The quantity that the user defined that the planning contract needs to plan ahead.  """  
      self.ContractUOM:str = obj["ContractUOM"]
      """  ContractUOM  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the planning contract line.  """  
      self.Comments:str = obj["Comments"]
      """  The planning contract line comments.  """  
      self.OurContractQty:int = obj["OurContractQty"]
      """  OurContractQty  """  
      self.ConsumedQty:int = obj["ConsumedQty"]
      """  The portion of the contract quantity that has been consumed for the demands linked to this planning contract. This is calculated when MRP is executed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CompletedQty:int = obj["CompletedQty"]
      """  The portion of the demand linked to the contract that has been already satisfied.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the Job Material warehouse location. Optional. Warehouse must exist in PlanContractWhseBin.  """  
      self.BinNum:str = obj["BinNum"]
      """  Indicates the Job Material bin location. Optional. Bin must exist in PlanContractWhseBin.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.UnconsumedQty:int = obj["UnconsumedQty"]
      """  The portion of the contract quantity that has not been consumed yet. Calculated as Contract Qty – Consumed Qty.  """  
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  Inventory UOM that the Plan ContractDetail Part is allocated against.  """  
      self.ThisContractInvtyQty:int = obj["ThisContractInvtyQty"]
      """  The Contract Quantity expressed in the Inventory Unit of Measure  """  
      self.ThisOpenQty:int = obj["ThisOpenQty"]
      """  The portion of the contract quantity that has been Consumed but it is not yet been Completed. Calculated as Completed Qty - Consumed Qty.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetDesc:str = obj["AttributeSetDesc"]
      """  Description of values in set  """  
      self.AttributeSetShortDesc:str = obj["AttributeSetShortDesc"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.Plant:str = obj["Plant"]
      """  Site identifier.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlanContractHdrListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractID:str = obj["ContractID"]
      """  The unique identifier of the planning contract.  """  
      self.Description:str = obj["Description"]
      """  Planning Contract Description.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Comments:str = obj["Comments"]
      """  The planning contract header comments.  """  
      self.PlannerID:str = obj["PlannerID"]
      """  The ID of the Planner.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this planning contract.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the planning contract have been approved.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse location. This location is defaulted from the setting at the site level but it can be changed at the contract level. Only warehouses with at least one bin location flagged as contract bin are allowed.  """  
      self.BinNum:str = obj["BinNum"]
      """  Indicates the inventory bin location. Only bins of “Contract” Type are allowed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlanContractHdrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractID:str = obj["ContractID"]
      """  The unique identifier of the planning contract.  """  
      self.Description:str = obj["Description"]
      """  Planning Contract Description.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Comments:str = obj["Comments"]
      """  The planning contract header comments.  """  
      self.PlannerID:str = obj["PlannerID"]
      """  The ID of the Planner.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this planning contract.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the planning contract have been approved.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse location. This location is defaulted from the setting at the site level but it can be changed at the contract level. Only warehouses with at least one bin location flagged as contract bin are allowed.  """  
      self.BinNum:str = obj["BinNum"]
      """  Indicates the inventory bin location. Only bins of “Contract” Type are allowed.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the planning contract is active.  """  
      self.NonPCBinAction:str = obj["NonPCBinAction"]
      """  Controls the action that is to be taken when an inventory move (receipt, issue, return) is going to be done to a bin other than the contract bin selected for the contract.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The ID of the Buyer.  """  
      self.RcvWhse:str = obj["RcvWhse"]
      """  Default Warehouse that received the item.  Only warehouses with at least one bin location flagged as contract bin are allowed.  """  
      self.RcvBin:str = obj["RcvBin"]
      """  Default Bin location of the warehouse which received the item. Only bins of “Contract” Type are allowed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.NonPCOutsideAction:str = obj["NonPCOutsideAction"]
      """  Controls the action that is to be taken when an inventory move (issue, shipment) is going to be done from a contract bin to other location outside the contract.  """  
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.PersonName:str = obj["PersonName"]
      self.PlantName:str = obj["PlantName"]
      self.RcvBinDescription:str = obj["RcvBinDescription"]
      self.RcvWhseDescription:str = obj["RcvWhseDescription"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlanContractSplyDtlRow:
   def __init__(self, obj):
      self.BinDescription:str = obj["BinDescription"]
      self.BinNum:str = obj["BinNum"]
      self.Company:str = obj["Company"]
      self.ContractID:str = obj["ContractID"]
      self.LineNum:int = obj["LineNum"]
      self.LotNum:str = obj["LotNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.PartNum:str = obj["PartNum"]
      self.Plant:str = obj["Plant"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      self.PlantName:str = obj["PlantName"]
      self.DueDate:str = obj["DueDate"]
      self.JobNum:str = obj["JobNum"]
      self.POLine:int = obj["POLine"]
      self.PONum:int = obj["PONum"]
      self.IUM:str = obj["IUM"]
      self.PORelNum:int = obj["PORelNum"]
      self.ReceiptQty:int = obj["ReceiptQty"]
      self.SourceName:str = obj["SourceName"]
      self.SugNum:int = obj["SugNum"]
      self.TFLineNum:str = obj["TFLineNum"]
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetDesc:str = obj["AttributeSetDesc"]
      """  Description of values in set  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDesc:str = obj["AttributeSetShortDesc"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlanContractSplyHdrRow:
   def __init__(self, obj):
      self.BinDescription:str = obj["BinDescription"]
      self.BinNum:str = obj["BinNum"]
      self.Company:str = obj["Company"]
      self.ContractID:str = obj["ContractID"]
      self.LotNum:str = obj["LotNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.PartNum:str = obj["PartNum"]
      self.Plant:str = obj["Plant"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      self.PlantName:str = obj["PlantName"]
      self.DueDate:str = obj["DueDate"]
      self.IUM:str = obj["IUM"]
      self.JobNum:str = obj["JobNum"]
      self.POLine:int = obj["POLine"]
      self.PONum:int = obj["PONum"]
      self.PORelNum:int = obj["PORelNum"]
      self.ReceiptQty:int = obj["ReceiptQty"]
      self.SourceName:str = obj["SourceName"]
      self.SugNum:int = obj["SugNum"]
      self.TFLineNum:str = obj["TFLineNum"]
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetDesc:str = obj["AttributeSetDesc"]
      """  Description of values in set  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDesc:str = obj["AttributeSetShortDesc"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlanContractTranDtlRow:
   def __init__(self, obj):
      self.ActTranQty:int = obj["ActTranQty"]
      """  Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM. Related to PartTran. TranQty which is the ActTranQty converted into the Parts Primary Inventory UO  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.BinDescription:str = obj["BinDescription"]
      """  Bin Description  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.BinType:str = obj["BinType"]
      """  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.CallNum:int = obj["CallNum"]
      """  Reference to the service call that the material is being issued for.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractID:str = obj["ContractID"]
      """  The unique identifier of the planning contract.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DimCodeDesc:str = obj["DimCodeDesc"]
      """  Dim Code Description  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """  Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure. Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.DimQty:int = obj["DimQty"]
      """  Dimension Quantity  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit. This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended Cost is calculated as (TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  """  
      self.InventoryTrans:bool = obj["InventoryTrans"]
      """  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.LotNum:str = obj["LotNum"]
      self.MiscShipPackID:int = obj["MiscShipPackID"]
      """  Miscelaneous Shipment Entry Packing ID  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The sales order number that this detail shipment line is linked to. This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  """  
      self.Packer:str = obj["Packer"]
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part description that this transaction is for.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transaction is for.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PlantName:str = obj["PlantName"]
      """  Plant Name.  """  
      self.PONum:int = obj["PONum"]
      """  Created by Purchase Order Receipt Process.  """  
      self.ReasonDesc:str = obj["ReasonDesc"]
      """  Full description of Reason... used on displays/reports.  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number  """  
      self.RunningTotal:int = obj["RunningTotal"]
      """  Calculated Running Total  """  
      self.RunningTotalUOM:str = obj["RunningTotalUOM"]
      """  RunningTotal UOM  """  
      self.SubConShipPackID:int = obj["SubConShipPackID"]
      """  Subcontractor Shipment Packing ID  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.TOPackID:int = obj["TOPackID"]
      """  PackID from Transfer Order Packing type  """  
      self.TranDate:str = obj["TranDate"]
      """  Date of transaction.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.TranQty:int = obj["TranQty"]
      """  Transaction Quantity. Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran. UM This is the UOM that the unit costs are based on. The actual Transaction quatity is found in ActTranQty  """  
      self.TranReference:str = obj["TranReference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.TranType:str = obj["TranType"]
      """  Field that indicates the type of transaction: ADJ-CST -  Adjustment to Stock Cost. ADJ-DEM - Adjustment to Demand Quantity. ADJ-MTL - Adjustment to Job Cost Material. ADJ-PUR - Purchase Price variance (created by A/P invoice) ADJ-QTY - Adjustment to  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      """  Warehouse description.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDesc:str = obj["AttributeSetShortDesc"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlanContractTranHdrRow:
   def __init__(self, obj):
      self.ActTranQty:int = obj["ActTranQty"]
      """  Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM. Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UO  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.BinDescription:str = obj["BinDescription"]
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.BinType:str = obj["BinType"]
      """  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.CallNum:int = obj["CallNum"]
      """  Reference to the service call that the material is being issued for.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractID:str = obj["ContractID"]
      """  The unique identifier of the planning contract.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DimCodeDesc:str = obj["DimCodeDesc"]
      """  Dim Code Description  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """  Dimension conversion factor. This conversion factor is used to convert the qty to the base part unit of measure. Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.DimQty:int = obj["DimQty"]
      """  Dimension Quantity  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit. This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended Cost is calculated as (TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  """  
      self.InventoryTrans:bool = obj["InventoryTrans"]
      """  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.MiscShipPackID:int = obj["MiscShipPackID"]
      """  Miscelaneous Shipment Entry Packing ID  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The sales order number that this detail shipment line is linked to. This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  """  
      self.Packer:str = obj["Packer"]
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part description that this transaction is for.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transaction is for.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PlantName:str = obj["PlantName"]
      """  Plant Name.  """  
      self.PONum:int = obj["PONum"]
      """  Created by Purchase Order Receipt Process.  """  
      self.ReasonDesc:str = obj["ReasonDesc"]
      """  Full description of Reason... used on displays/reports.  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number  """  
      self.RunningTotal:int = obj["RunningTotal"]
      """  Calculated Running Total  """  
      self.RunningTotalUOM:str = obj["RunningTotalUOM"]
      """  RunningTotal UOM  """  
      self.SubConShipPackID:int = obj["SubConShipPackID"]
      """  Subcontractor Shipment Packing ID  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.TOPackID:int = obj["TOPackID"]
      """  PackID from Transfer Order Packing type  """  
      self.TranDate:str = obj["TranDate"]
      """  Date of transaction.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.TranQty:int = obj["TranQty"]
      """  Transaction Quantity. Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran. UM This is the UOM that the unit costs are based on. The actual Transaction quatity is found in ActTranQty  """  
      self.TranReference:str = obj["TranReference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.TranType:str = obj["TranType"]
      """  Field that indicates the type of transaction: ADJ-CST -  Adjustment to Stock Cost. ADJ-DEM - Adjustment to Demand Quantity. ADJ-MTL - Adjustment to Job Cost Material. ADJ-PUR - Purchase Price variance (created by A/P invoice) ADJ-QTY - Adjustment to  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      """  Warehouse description.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDesc:str = obj["AttributeSetShortDesc"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlanContractWhseBinRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractID:str = obj["ContractID"]
      """  The unique identifier of the planning contract.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the warehouse location. Only warehouses with at least one bin location flagged as contract bin are allowed.  """  
      self.BinNum:str = obj["BinNum"]
      """  Indicates the bin location. Only bins of “Contract” Type are allowed.  """  
      self.DefaultInvWhseBin:bool = obj["DefaultInvWhseBin"]
      """  Indicates if the warehouse/bin combination is the default Inventory warehouse/bin.  """  
      self.DefaultRcvWhseBin:bool = obj["DefaultRcvWhseBin"]
      """  Indicates if the warehouse/bin combination is the default Receiving warehouse/bin.  """  
      self.BackflushBin:bool = obj["BackflushBin"]
      """  Indicates if the warehouse/bin combination is the Backflush warehouse/bin.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Plant:str = obj["Plant"]
      """  Site identifier.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeContractDemandQuantities_input:
   """ Required : 
   partNum
   contractQty
   contractUOM
   consumedQty
   completedQty
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  partNum  """  
      self.contractQty:int = obj["contractQty"]
      """  contractQty  """  
      self.contractUOM:str = obj["contractUOM"]
      """  contractUOM  """  
      self.consumedQty:int = obj["consumedQty"]
      """  consumedQty  """  
      self.completedQty:int = obj["completedQty"]
      """  completedQty  """  
      pass

class ChangeContractDemandQuantities_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outThisContractInvtyQty:int = obj["parameters"]
      self.outThisOpenQty:int = obj["parameters"]
      self.outUnconsumedQty:int = obj["parameters"]
      self.outCompletedQty:int = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   contractID
   """  
   def __init__(self, obj):
      self.contractID:str = obj["contractID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PlanContractDmdDtlRow:
   def __init__(self, obj):
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.Company:str = obj["Company"]
      self.ContractID:str = obj["ContractID"]
      self.DueDate:str = obj["DueDate"]
      self.IUM:str = obj["IUM"]
      self.JobNum:str = obj["JobNum"]
      self.LineNum:int = obj["LineNum"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.RequiredQty:int = obj["RequiredQty"]
      self.SourceName:str = obj["SourceName"]
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.TFLineNum:str = obj["TFLineNum"]
      self.PartNum:str = obj["PartNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetDesc:str = obj["AttributeSetDesc"]
      """  Description of values in set  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDesc:str = obj["AttributeSetShortDesc"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlanContractDmdHdrRow:
   def __init__(self, obj):
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.Company:str = obj["Company"]
      self.ContractID:str = obj["ContractID"]
      self.DueDate:str = obj["DueDate"]
      self.IUM:str = obj["IUM"]
      self.JobNum:str = obj["JobNum"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.RequiredQty:int = obj["RequiredQty"]
      self.SourceName:str = obj["SourceName"]
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.TFLineNum:str = obj["TFLineNum"]
      self.PartNum:str = obj["PartNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetDesc:str = obj["AttributeSetDesc"]
      """  Description of values in set  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDesc:str = obj["AttributeSetShortDesc"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlanContractDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractID:str = obj["ContractID"]
      """  The unique identifier of the planning contract.  """  
      self.LineNum:int = obj["LineNum"]
      """  The unique identifier of the planning contract line.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part. Sales Kits not allowed. Same part number can only be entered once in the same contract.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.ContractQty:int = obj["ContractQty"]
      """  The quantity that the user defined that the planning contract needs to plan ahead.  """  
      self.ContractUOM:str = obj["ContractUOM"]
      """  ContractUOM  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the planning contract line.  """  
      self.Comments:str = obj["Comments"]
      """  The planning contract line comments.  """  
      self.OurContractQty:int = obj["OurContractQty"]
      """  OurContractQty  """  
      self.ConsumedQty:int = obj["ConsumedQty"]
      """  The portion of the contract quantity that has been consumed for the demands linked to this planning contract. This is calculated when MRP is executed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CompletedQty:int = obj["CompletedQty"]
      """  The portion of the demand linked to the contract that has been already satisfied.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the Job Material warehouse location. Optional. Warehouse must exist in PlanContractWhseBin.  """  
      self.BinNum:str = obj["BinNum"]
      """  Indicates the Job Material bin location. Optional. Bin must exist in PlanContractWhseBin.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.UnconsumedQty:int = obj["UnconsumedQty"]
      """  The portion of the contract quantity that has not been consumed yet. Calculated as Contract Qty – Consumed Qty.  """  
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  Inventory UOM that the Plan ContractDetail Part is allocated against.  """  
      self.ThisContractInvtyQty:int = obj["ThisContractInvtyQty"]
      """  The Contract Quantity expressed in the Inventory Unit of Measure  """  
      self.ThisOpenQty:int = obj["ThisOpenQty"]
      """  The portion of the contract quantity that has been Consumed but it is not yet been Completed. Calculated as Completed Qty - Consumed Qty.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetDesc:str = obj["AttributeSetDesc"]
      """  Description of values in set  """  
      self.AttributeSetShortDesc:str = obj["AttributeSetShortDesc"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.Plant:str = obj["Plant"]
      """  Site identifier.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlanContractHdrListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractID:str = obj["ContractID"]
      """  The unique identifier of the planning contract.  """  
      self.Description:str = obj["Description"]
      """  Planning Contract Description.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Comments:str = obj["Comments"]
      """  The planning contract header comments.  """  
      self.PlannerID:str = obj["PlannerID"]
      """  The ID of the Planner.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this planning contract.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the planning contract have been approved.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse location. This location is defaulted from the setting at the site level but it can be changed at the contract level. Only warehouses with at least one bin location flagged as contract bin are allowed.  """  
      self.BinNum:str = obj["BinNum"]
      """  Indicates the inventory bin location. Only bins of “Contract” Type are allowed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlanContractHdrListTableset:
   def __init__(self, obj):
      self.PlanContractHdrList:list[Erp_Tablesets_PlanContractHdrListRow] = obj["PlanContractHdrList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PlanContractHdrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractID:str = obj["ContractID"]
      """  The unique identifier of the planning contract.  """  
      self.Description:str = obj["Description"]
      """  Planning Contract Description.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Comments:str = obj["Comments"]
      """  The planning contract header comments.  """  
      self.PlannerID:str = obj["PlannerID"]
      """  The ID of the Planner.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this planning contract.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the planning contract have been approved.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse location. This location is defaulted from the setting at the site level but it can be changed at the contract level. Only warehouses with at least one bin location flagged as contract bin are allowed.  """  
      self.BinNum:str = obj["BinNum"]
      """  Indicates the inventory bin location. Only bins of “Contract” Type are allowed.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the planning contract is active.  """  
      self.NonPCBinAction:str = obj["NonPCBinAction"]
      """  Controls the action that is to be taken when an inventory move (receipt, issue, return) is going to be done to a bin other than the contract bin selected for the contract.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The ID of the Buyer.  """  
      self.RcvWhse:str = obj["RcvWhse"]
      """  Default Warehouse that received the item.  Only warehouses with at least one bin location flagged as contract bin are allowed.  """  
      self.RcvBin:str = obj["RcvBin"]
      """  Default Bin location of the warehouse which received the item. Only bins of “Contract” Type are allowed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.NonPCOutsideAction:str = obj["NonPCOutsideAction"]
      """  Controls the action that is to be taken when an inventory move (issue, shipment) is going to be done from a contract bin to other location outside the contract.  """  
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.PersonName:str = obj["PersonName"]
      self.PlantName:str = obj["PlantName"]
      self.RcvBinDescription:str = obj["RcvBinDescription"]
      self.RcvWhseDescription:str = obj["RcvWhseDescription"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlanContractSplyDtlRow:
   def __init__(self, obj):
      self.BinDescription:str = obj["BinDescription"]
      self.BinNum:str = obj["BinNum"]
      self.Company:str = obj["Company"]
      self.ContractID:str = obj["ContractID"]
      self.LineNum:int = obj["LineNum"]
      self.LotNum:str = obj["LotNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.PartNum:str = obj["PartNum"]
      self.Plant:str = obj["Plant"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      self.PlantName:str = obj["PlantName"]
      self.DueDate:str = obj["DueDate"]
      self.JobNum:str = obj["JobNum"]
      self.POLine:int = obj["POLine"]
      self.PONum:int = obj["PONum"]
      self.IUM:str = obj["IUM"]
      self.PORelNum:int = obj["PORelNum"]
      self.ReceiptQty:int = obj["ReceiptQty"]
      self.SourceName:str = obj["SourceName"]
      self.SugNum:int = obj["SugNum"]
      self.TFLineNum:str = obj["TFLineNum"]
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetDesc:str = obj["AttributeSetDesc"]
      """  Description of values in set  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDesc:str = obj["AttributeSetShortDesc"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlanContractSplyHdrRow:
   def __init__(self, obj):
      self.BinDescription:str = obj["BinDescription"]
      self.BinNum:str = obj["BinNum"]
      self.Company:str = obj["Company"]
      self.ContractID:str = obj["ContractID"]
      self.LotNum:str = obj["LotNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.PartNum:str = obj["PartNum"]
      self.Plant:str = obj["Plant"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      self.PlantName:str = obj["PlantName"]
      self.DueDate:str = obj["DueDate"]
      self.IUM:str = obj["IUM"]
      self.JobNum:str = obj["JobNum"]
      self.POLine:int = obj["POLine"]
      self.PONum:int = obj["PONum"]
      self.PORelNum:int = obj["PORelNum"]
      self.ReceiptQty:int = obj["ReceiptQty"]
      self.SourceName:str = obj["SourceName"]
      self.SugNum:int = obj["SugNum"]
      self.TFLineNum:str = obj["TFLineNum"]
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetDesc:str = obj["AttributeSetDesc"]
      """  Description of values in set  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDesc:str = obj["AttributeSetShortDesc"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlanContractTableset:
   def __init__(self, obj):
      self.PlanContractHdr:list[Erp_Tablesets_PlanContractHdrRow] = obj["PlanContractHdr"]
      self.PlanContractDtl:list[Erp_Tablesets_PlanContractDtlRow] = obj["PlanContractDtl"]
      self.PlanContractWhseBin:list[Erp_Tablesets_PlanContractWhseBinRow] = obj["PlanContractWhseBin"]
      self.PlanContractDmdDtl:list[Erp_Tablesets_PlanContractDmdDtlRow] = obj["PlanContractDmdDtl"]
      self.PlanContractDmdHdr:list[Erp_Tablesets_PlanContractDmdHdrRow] = obj["PlanContractDmdHdr"]
      self.PlanContractSplyDtl:list[Erp_Tablesets_PlanContractSplyDtlRow] = obj["PlanContractSplyDtl"]
      self.PlanContractSplyHdr:list[Erp_Tablesets_PlanContractSplyHdrRow] = obj["PlanContractSplyHdr"]
      self.PlanContractTranDtl:list[Erp_Tablesets_PlanContractTranDtlRow] = obj["PlanContractTranDtl"]
      self.PlanContractTranHdr:list[Erp_Tablesets_PlanContractTranHdrRow] = obj["PlanContractTranHdr"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PlanContractTranDtlRow:
   def __init__(self, obj):
      self.ActTranQty:int = obj["ActTranQty"]
      """  Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM. Related to PartTran. TranQty which is the ActTranQty converted into the Parts Primary Inventory UO  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.BinDescription:str = obj["BinDescription"]
      """  Bin Description  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.BinType:str = obj["BinType"]
      """  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.CallNum:int = obj["CallNum"]
      """  Reference to the service call that the material is being issued for.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractID:str = obj["ContractID"]
      """  The unique identifier of the planning contract.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DimCodeDesc:str = obj["DimCodeDesc"]
      """  Dim Code Description  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """  Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure. Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.DimQty:int = obj["DimQty"]
      """  Dimension Quantity  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit. This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended Cost is calculated as (TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  """  
      self.InventoryTrans:bool = obj["InventoryTrans"]
      """  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.LotNum:str = obj["LotNum"]
      self.MiscShipPackID:int = obj["MiscShipPackID"]
      """  Miscelaneous Shipment Entry Packing ID  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The sales order number that this detail shipment line is linked to. This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  """  
      self.Packer:str = obj["Packer"]
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part description that this transaction is for.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transaction is for.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PlantName:str = obj["PlantName"]
      """  Plant Name.  """  
      self.PONum:int = obj["PONum"]
      """  Created by Purchase Order Receipt Process.  """  
      self.ReasonDesc:str = obj["ReasonDesc"]
      """  Full description of Reason... used on displays/reports.  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number  """  
      self.RunningTotal:int = obj["RunningTotal"]
      """  Calculated Running Total  """  
      self.RunningTotalUOM:str = obj["RunningTotalUOM"]
      """  RunningTotal UOM  """  
      self.SubConShipPackID:int = obj["SubConShipPackID"]
      """  Subcontractor Shipment Packing ID  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.TOPackID:int = obj["TOPackID"]
      """  PackID from Transfer Order Packing type  """  
      self.TranDate:str = obj["TranDate"]
      """  Date of transaction.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.TranQty:int = obj["TranQty"]
      """  Transaction Quantity. Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran. UM This is the UOM that the unit costs are based on. The actual Transaction quatity is found in ActTranQty  """  
      self.TranReference:str = obj["TranReference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.TranType:str = obj["TranType"]
      """  Field that indicates the type of transaction: ADJ-CST -  Adjustment to Stock Cost. ADJ-DEM - Adjustment to Demand Quantity. ADJ-MTL - Adjustment to Job Cost Material. ADJ-PUR - Purchase Price variance (created by A/P invoice) ADJ-QTY - Adjustment to  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      """  Warehouse description.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDesc:str = obj["AttributeSetShortDesc"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlanContractTranHdrRow:
   def __init__(self, obj):
      self.ActTranQty:int = obj["ActTranQty"]
      """  Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM. Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UO  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.BinDescription:str = obj["BinDescription"]
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.BinType:str = obj["BinType"]
      """  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.CallNum:int = obj["CallNum"]
      """  Reference to the service call that the material is being issued for.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractID:str = obj["ContractID"]
      """  The unique identifier of the planning contract.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DimCodeDesc:str = obj["DimCodeDesc"]
      """  Dim Code Description  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """  Dimension conversion factor. This conversion factor is used to convert the qty to the base part unit of measure. Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.DimQty:int = obj["DimQty"]
      """  Dimension Quantity  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit. This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended Cost is calculated as (TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  """  
      self.InventoryTrans:bool = obj["InventoryTrans"]
      """  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.MiscShipPackID:int = obj["MiscShipPackID"]
      """  Miscelaneous Shipment Entry Packing ID  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The sales order number that this detail shipment line is linked to. This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  """  
      self.Packer:str = obj["Packer"]
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part description that this transaction is for.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transaction is for.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PlantName:str = obj["PlantName"]
      """  Plant Name.  """  
      self.PONum:int = obj["PONum"]
      """  Created by Purchase Order Receipt Process.  """  
      self.ReasonDesc:str = obj["ReasonDesc"]
      """  Full description of Reason... used on displays/reports.  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number  """  
      self.RunningTotal:int = obj["RunningTotal"]
      """  Calculated Running Total  """  
      self.RunningTotalUOM:str = obj["RunningTotalUOM"]
      """  RunningTotal UOM  """  
      self.SubConShipPackID:int = obj["SubConShipPackID"]
      """  Subcontractor Shipment Packing ID  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.TOPackID:int = obj["TOPackID"]
      """  PackID from Transfer Order Packing type  """  
      self.TranDate:str = obj["TranDate"]
      """  Date of transaction.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.TranQty:int = obj["TranQty"]
      """  Transaction Quantity. Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran. UM This is the UOM that the unit costs are based on. The actual Transaction quatity is found in ActTranQty  """  
      self.TranReference:str = obj["TranReference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.TranType:str = obj["TranType"]
      """  Field that indicates the type of transaction: ADJ-CST -  Adjustment to Stock Cost. ADJ-DEM - Adjustment to Demand Quantity. ADJ-MTL - Adjustment to Job Cost Material. ADJ-PUR - Purchase Price variance (created by A/P invoice) ADJ-QTY - Adjustment to  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      """  Warehouse description.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDesc:str = obj["AttributeSetShortDesc"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlanContractWhseBinRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractID:str = obj["ContractID"]
      """  The unique identifier of the planning contract.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the warehouse location. Only warehouses with at least one bin location flagged as contract bin are allowed.  """  
      self.BinNum:str = obj["BinNum"]
      """  Indicates the bin location. Only bins of “Contract” Type are allowed.  """  
      self.DefaultInvWhseBin:bool = obj["DefaultInvWhseBin"]
      """  Indicates if the warehouse/bin combination is the default Inventory warehouse/bin.  """  
      self.DefaultRcvWhseBin:bool = obj["DefaultRcvWhseBin"]
      """  Indicates if the warehouse/bin combination is the default Receiving warehouse/bin.  """  
      self.BackflushBin:bool = obj["BackflushBin"]
      """  Indicates if the warehouse/bin combination is the Backflush warehouse/bin.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Plant:str = obj["Plant"]
      """  Site identifier.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtPlanContractTableset:
   def __init__(self, obj):
      self.PlanContractHdr:list[Erp_Tablesets_PlanContractHdrRow] = obj["PlanContractHdr"]
      self.PlanContractDtl:list[Erp_Tablesets_PlanContractDtlRow] = obj["PlanContractDtl"]
      self.PlanContractWhseBin:list[Erp_Tablesets_PlanContractWhseBinRow] = obj["PlanContractWhseBin"]
      self.PlanContractDmdDtl:list[Erp_Tablesets_PlanContractDmdDtlRow] = obj["PlanContractDmdDtl"]
      self.PlanContractDmdHdr:list[Erp_Tablesets_PlanContractDmdHdrRow] = obj["PlanContractDmdHdr"]
      self.PlanContractSplyDtl:list[Erp_Tablesets_PlanContractSplyDtlRow] = obj["PlanContractSplyDtl"]
      self.PlanContractSplyHdr:list[Erp_Tablesets_PlanContractSplyHdrRow] = obj["PlanContractSplyHdr"]
      self.PlanContractTranDtl:list[Erp_Tablesets_PlanContractTranDtlRow] = obj["PlanContractTranDtl"]
      self.PlanContractTranHdr:list[Erp_Tablesets_PlanContractTranHdrRow] = obj["PlanContractTranHdr"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExistsInventoryOrReceivingBin_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      pass

class ExistsInventoryOrReceivingBin_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      self.invOrRec:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   contractID
   """  
   def __init__(self, obj):
      self.contractID:str = obj["contractID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PlanContractTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PlanContractTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PlanContractTableset] = obj["returnObj"]
      pass

class GetContractDtlDmdRows_input:
   """ Required : 
   sCompany
   sContractID
   sPart
   sAttributeSetID
   """  
   def __init__(self, obj):
      self.sCompany:str = obj["sCompany"]
      self.sContractID:str = obj["sContractID"]
      self.sPart:str = obj["sPart"]
      self.sAttributeSetID:int = obj["sAttributeSetID"]
      pass

class GetContractDtlDmdRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PlanContractTableset] = obj["returnObj"]
      pass

class GetContractDtlTranRows_input:
   """ Required : 
   sCompany
   sContractID
   sPart
   sAttributeSetID
   """  
   def __init__(self, obj):
      self.sCompany:str = obj["sCompany"]
      self.sContractID:str = obj["sContractID"]
      self.sPart:str = obj["sPart"]
      self.sAttributeSetID:int = obj["sAttributeSetID"]
      pass

class GetContractDtlTranRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PlanContractTableset] = obj["returnObj"]
      pass

class GetContractHdrDmdRows_input:
   """ Required : 
   sCompany
   sContractID
   """  
   def __init__(self, obj):
      self.sCompany:str = obj["sCompany"]
      self.sContractID:str = obj["sContractID"]
      pass

class GetContractHdrDmdRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PlanContractTableset] = obj["returnObj"]
      pass

class GetContractHdrTranRows_input:
   """ Required : 
   sCompany
   sContractID
   """  
   def __init__(self, obj):
      self.sCompany:str = obj["sCompany"]
      self.sContractID:str = obj["sContractID"]
      pass

class GetContractHdrTranRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PlanContractTableset] = obj["returnObj"]
      pass

class GetContractSplyRows_input:
   """ Required : 
   sCompany
   sContractID
   sPart
   sAttributeSetID
   """  
   def __init__(self, obj):
      self.sCompany:str = obj["sCompany"]
      self.sContractID:str = obj["sContractID"]
      self.sPart:str = obj["sPart"]
      self.sAttributeSetID:int = obj["sAttributeSetID"]
      pass

class GetContractSplyRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PlanContractTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PlanContractHdrListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPlanContractDtl_input:
   """ Required : 
   ds
   contractID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      self.contractID:str = obj["contractID"]
      pass

class GetNewPlanContractDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPlanContractHdr_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      pass

class GetNewPlanContractHdr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPlanContractWhseBin_input:
   """ Required : 
   ds
   contractID
   warehouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      self.contractID:str = obj["contractID"]
      self.warehouseCode:str = obj["warehouseCode"]
      pass

class GetNewPlanContractWhseBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePlanContractHdr
   whereClausePlanContractDtl
   whereClausePlanContractWhseBin
   whereClausePlanContractDmdDtl
   whereClausePlanContractDmdHdr
   whereClausePlanContractSplyDtl
   whereClausePlanContractSplyHdr
   whereClausePlanContractTranDtl
   whereClausePlanContractTranHdr
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePlanContractHdr:str = obj["whereClausePlanContractHdr"]
      self.whereClausePlanContractDtl:str = obj["whereClausePlanContractDtl"]
      self.whereClausePlanContractWhseBin:str = obj["whereClausePlanContractWhseBin"]
      self.whereClausePlanContractDmdDtl:str = obj["whereClausePlanContractDmdDtl"]
      self.whereClausePlanContractDmdHdr:str = obj["whereClausePlanContractDmdHdr"]
      self.whereClausePlanContractSplyDtl:str = obj["whereClausePlanContractSplyDtl"]
      self.whereClausePlanContractSplyHdr:str = obj["whereClausePlanContractSplyHdr"]
      self.whereClausePlanContractTranDtl:str = obj["whereClausePlanContractTranDtl"]
      self.whereClausePlanContractTranHdr:str = obj["whereClausePlanContractTranHdr"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PlanContractTableset] = obj["returnObj"]
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

class OnChangeActive_input:
   """ Required : 
   ds
   Active
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      self.Active:bool = obj["Active"]
      pass

class OnChangeActive_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlBinNum_input:
   """ Required : 
   ds
   sBinNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      self.sBinNum:str = obj["sBinNum"]
      pass

class OnChangeDtlBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      self.sBinNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangePartNum_input:
   """ Required : 
   ds
   sPartNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      self.sPartNum:str = obj["sPartNum"]
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      self.sPartNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangePlanContractDtlWarehouseCode_input:
   """ Required : 
   ds
   WarehouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      pass

class OnChangePlanContractDtlWarehouseCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeWhseBinBackflushBin_input:
   """ Required : 
   ds
   ipBackflushBin
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      self.ipBackflushBin:bool = obj["ipBackflushBin"]
      pass

class OnChangeWhseBinBackflushBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeWhseBinDefaultInvWhseBin_input:
   """ Required : 
   ds
   ipDefaultInvWhseBin
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      self.ipDefaultInvWhseBin:bool = obj["ipDefaultInvWhseBin"]
      pass

class OnChangeWhseBinDefaultInvWhseBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeWhseBinDefaultRcvWhseBin_input:
   """ Required : 
   ds
   ipDefaultRcvWhseBin
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      self.ipDefaultRcvWhseBin:bool = obj["ipDefaultRcvWhseBin"]
      pass

class OnChangeWhseBinDefaultRcvWhseBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeWhseBinNum_input:
   """ Required : 
   ds
   sBinNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      self.sBinNum:str = obj["sBinNum"]
      pass

class OnChangeWhseBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      self.sBinNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeWhseBinWarehouseCode_input:
   """ Required : 
   ds
   WarehouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      pass

class OnChangeWhseBinWarehouseCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingAttributeSet_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      pass

class OnChangingAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      pass

class OnChangingRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_UpdExtPlanContractTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPlanContractTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidatePlanContractHdrinDiffPlant_input:
   """ Required : 
   sCompany
   sPlant
   sContractID
   """  
   def __init__(self, obj):
      self.sCompany:str = obj["sCompany"]
      self.sPlant:str = obj["sPlant"]
      self.sContractID:str = obj["sContractID"]
      pass

class ValidatePlanContractHdrinDiffPlant_output:
   def __init__(self, obj):
      pass

