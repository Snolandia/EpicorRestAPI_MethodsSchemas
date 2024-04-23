import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CCPartSelectUpdSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CCPartSelectUpds(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CCPartSelectUpds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCPartSelectUpds
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCHdrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPartSelectUpds",headers=creds) as resp:
           return await resp.json()

async def post_CCPartSelectUpds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCPartSelectUpds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCHdrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CCHdrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPartSelectUpds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CCPartSelectUpds_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CCPartSelectUpd item
   Description: Calls GetByID to retrieve the CCPartSelectUpd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCPartSelectUpd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param CCYear: Desc: CCYear   Required: True
      :param CCMonth: Desc: CCMonth   Required: True
      :param FullPhysical: Desc: FullPhysical   Required: True
      :param CycleSeq: Desc: CycleSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCHdrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPartSelectUpds(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CCPartSelectUpds_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CCPartSelectUpd for the service
   Description: Calls UpdateExt to update CCPartSelectUpd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCPartSelectUpd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param CCYear: Desc: CCYear   Required: True
      :param CCMonth: Desc: CCMonth   Required: True
      :param FullPhysical: Desc: FullPhysical   Required: True
      :param CycleSeq: Desc: CycleSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCHdrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPartSelectUpds(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CCPartSelectUpds_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CCPartSelectUpd item
   Description: Call UpdateExt to delete CCPartSelectUpd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCPartSelectUpd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param CCYear: Desc: CCYear   Required: True
      :param CCMonth: Desc: CCMonth   Required: True
      :param FullPhysical: Desc: FullPhysical   Required: True
      :param CycleSeq: Desc: CycleSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPartSelectUpds(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CCPartSelectUpds_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_CCDtls(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CCDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CCDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param CCYear: Desc: CCYear   Required: True
      :param CCMonth: Desc: CCMonth   Required: True
      :param FullPhysical: Desc: FullPhysical   Required: True
      :param CycleSeq: Desc: CycleSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPartSelectUpds(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")/CCDtls",headers=creds) as resp:
           return await resp.json()

async def get_CCPartSelectUpds_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_CCDtls_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PartNum_AttributeSetID(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, PartNum, AttributeSetID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CCDtl item
   Description: Calls GetByID to retrieve the CCDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param CCYear: Desc: CCYear   Required: True
      :param CCMonth: Desc: CCMonth   Required: True
      :param FullPhysical: Desc: FullPhysical   Required: True
      :param CycleSeq: Desc: CycleSeq   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPartSelectUpds(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")/CCDtls(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CCPartSelectUpds_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_CCPCIDs(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CCPCIDs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CCPCIDs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param CCYear: Desc: CCYear   Required: True
      :param CCMonth: Desc: CCMonth   Required: True
      :param FullPhysical: Desc: FullPhysical   Required: True
      :param CycleSeq: Desc: CycleSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCPCIDRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPartSelectUpds(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")/CCPCIDs",headers=creds) as resp:
           return await resp.json()

async def get_CCPartSelectUpds_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_CCPCIDs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PCID(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, PCID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CCPCID item
   Description: Calls GetByID to retrieve the CCPCID item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCPCID1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param CCYear: Desc: CCYear   Required: True
      :param CCMonth: Desc: CCMonth   Required: True
      :param FullPhysical: Desc: FullPhysical   Required: True
      :param CycleSeq: Desc: CycleSeq   Required: True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCPCIDRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPartSelectUpds(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")/CCPCIDs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PCID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CCDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CCDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCDtls",headers=creds) as resp:
           return await resp.json()

async def post_CCDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CCDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CCDtls_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PartNum_AttributeSetID(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, PartNum, AttributeSetID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CCDtl item
   Description: Calls GetByID to retrieve the CCDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param CCYear: Desc: CCYear   Required: True
      :param CCMonth: Desc: CCMonth   Required: True
      :param FullPhysical: Desc: FullPhysical   Required: True
      :param CycleSeq: Desc: CycleSeq   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCDtls(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CCDtls_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PartNum_AttributeSetID(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, PartNum, AttributeSetID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CCDtl for the service
   Description: Calls UpdateExt to update CCDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param CCYear: Desc: CCYear   Required: True
      :param CCMonth: Desc: CCMonth   Required: True
      :param FullPhysical: Desc: FullPhysical   Required: True
      :param CycleSeq: Desc: CycleSeq   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCDtls(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CCDtls_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PartNum_AttributeSetID(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, PartNum, AttributeSetID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CCDtl item
   Description: Call UpdateExt to delete CCDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param CCYear: Desc: CCYear   Required: True
      :param CCMonth: Desc: CCMonth   Required: True
      :param FullPhysical: Desc: FullPhysical   Required: True
      :param CycleSeq: Desc: CycleSeq   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCDtls(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CCPCIDs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CCPCIDs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCPCIDs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCPCIDRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDs",headers=creds) as resp:
           return await resp.json()

async def post_CCPCIDs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCPCIDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCPCIDRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CCPCIDRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CCPCIDs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PCID(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, PCID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CCPCID item
   Description: Calls GetByID to retrieve the CCPCID item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCPCID
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param CCYear: Desc: CCYear   Required: True
      :param CCMonth: Desc: CCMonth   Required: True
      :param FullPhysical: Desc: FullPhysical   Required: True
      :param CycleSeq: Desc: CycleSeq   Required: True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCPCIDRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PCID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CCPCIDs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PCID(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, PCID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CCPCID for the service
   Description: Calls UpdateExt to update CCPCID. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCPCID
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param CCYear: Desc: CCYear   Required: True
      :param CCMonth: Desc: CCMonth   Required: True
      :param FullPhysical: Desc: FullPhysical   Required: True
      :param CycleSeq: Desc: CycleSeq   Required: True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCPCIDRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PCID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CCPCIDs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PCID(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, PCID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CCPCID item
   Description: Call UpdateExt to delete CCPCID item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCPCID
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param CCYear: Desc: CCYear   Required: True
      :param CCMonth: Desc: CCMonth   Required: True
      :param FullPhysical: Desc: FullPhysical   Required: True
      :param CycleSeq: Desc: CycleSeq   Required: True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PCID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CCPCIDSelecteds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CCPCIDSelecteds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCPCIDSelecteds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCPCIDSelectedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDSelecteds",headers=creds) as resp:
           return await resp.json()

async def post_CCPCIDSelecteds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCPCIDSelecteds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCPCIDSelectedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CCPCIDSelectedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDSelecteds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CCPCIDSelecteds_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CCPCIDSelected item
   Description: Calls GetByID to retrieve the CCPCIDSelected item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCPCIDSelected
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCPCIDSelectedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDSelecteds(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CCPCIDSelecteds_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CCPCIDSelected for the service
   Description: Calls UpdateExt to update CCPCIDSelected. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCPCIDSelected
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCPCIDSelectedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDSelecteds(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CCPCIDSelecteds_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CCPCIDSelected item
   Description: Call UpdateExt to delete CCPCIDSelected item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCPCIDSelected
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDSelecteds(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCHdrListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCCHdr, whereClauseCCDtl, whereClauseCCPCID, whereClauseCCPCIDSelected, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseCCHdr=" + whereClauseCCHdr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCCDtl=" + whereClauseCCDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCCPCID=" + whereClauseCCPCID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCCPCIDSelected=" + whereClauseCCPCIDSelected
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(plant, warehouseCode, ccYear, ccMonth, fullPhysical, cycleSeq, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
   Required: True
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
   params += "plant=" + plant
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "warehouseCode=" + warehouseCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ccYear=" + ccYear
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ccMonth=" + ccMonth
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fullPhysical=" + fullPhysical
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "cycleSeq=" + cycleSeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_MoveParts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveParts
   Description: Purpose:
Parameters:  none
Notes:
/// <param name="moveToMonth">The move-to month</param>
/// <param name="moveToYear">The move-to month</param>
/// <param name="moveToCycle">The move-to month</param>
/// <param name="ds">CCPartSelectUpd dataset</param>
   OperationID: MoveParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: Purpose:
Parameters:  none
Notes:
///<param name="ipPartNum">Input Part Number</param>
/// <param name="ds">CCPartSelectUpd dataset</param>
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCID
   Description: Purpose:
Parameters:  none
Notes:
///<param name="ipPCID">Part Number</param>
/// <param name="ds">CCPartSelectUpd dataset</param>
   OperationID: OnChangePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveParts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveParts
   Description: Purpose: Deletes all CCDtl for a particular CCHdr
Parameters:  none
Notes:
/// <param name="ds">CCPartSelectUpd dataset</param>
   OperationID: RemoveParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemovePCIDs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemovePCIDs
   Description: Purpose: Deletes all PCIDs for a particular CCHdr
Parameters:  none
Notes:
/// <param name="ds">CCPartSelectUpd dataset</param>
   OperationID: RemovePCIDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemovePCIDs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemovePCIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MovePCIDs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MovePCIDs
   Description: Purpose:
Parameters:  none
Notes:
/// <param name="moveToMonth">The move-to month</param>
/// <param name="moveToYear">The move-to month</param>
/// <param name="moveToCycle">The move-to month</param>
/// <param name="ds">CCPartSelectUpd dataset</param>
   OperationID: MovePCIDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MovePCIDs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MovePCIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdatePCIDSelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePCIDSelected
   Description: Purpose: Updates CCPCIDSelected with values from WhseBin
Parameters:  none
Notes:
/// <param name="ds">CCPartSelectUpdTableset dataset</param>
   OperationID: UpdatePCIDSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePCIDSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePCIDSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreatePCIDSelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreatePCIDSelected
   Description: Purpose: Creates CCPCIDSelected from PkgControlHdr
Parameters:  none
Notes:
/// <param name="ds">CCPartSelectUpdTableset dataset</param>
/// <param name="whseCode" /> warehouse code
/// <param name="frBin" /> from bin
/// <param name="toBin" /> to bin
/// <param name="frZone" /> from zone
/// <param name="toZone" /> to zone
   OperationID: CreatePCIDSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreatePCIDSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePCIDSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MassAddPartAttributeSets(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MassAddPartAttributeSets
   Description: Purpose: Creates CCDtl records for all valid attribute sets for an attribute set tracked part
Parameters:  none
Notes:
<param name="ds">CCPartSelectUpdTableset dataset</param><param name="ccHdrSysRowID">SysRowID for the CCHdr to which the CCDtl will be added</param><param name="partNum">Part Number for which the attribute sets will be added</param>
   OperationID: MassAddPartAttributeSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassAddPartAttributeSets_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassAddPartAttributeSets_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddPCIDToCycle(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddPCIDToCycle
   Description: Purpose: Creates CCPCID records from PCCPCIDSelected
Parameters:  none
Notes:
/// <param name="ds">CCPartSelectUpdTableset dataset</param>
/// <param name="year"> year</param>
/// <param name="month"> month</param>
/// <param name="fullPhysical"> fullPhysical</param>
/// <param name="cycleSeq"> cycleSeq</param>
   OperationID: AddPCIDToCycle
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddPCIDToCycle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddPCIDToCycle_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Purpose: Deletes all CCDtl for a particular CCHdr
Parameters:  none
Notes:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCCHdr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCCHdr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCCHdr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCCHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCCHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCCDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCCDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCCDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCCDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCCDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCCPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCCPCID
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCCPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCCPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCCPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CCDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CCHdrListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CCHdrRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCPCIDRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CCPCIDRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCPCIDSelectedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CCPCIDSelectedRow] = obj["value"]
      pass

class Erp_Tablesets_CCDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.Plant:str = obj["Plant"]
      """  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year that this cycle count control record is for.  """  
      self.CCMonth:int = obj["CCMonth"]
      """  CCPeriodDefn.CycleSeq that this cycle count control record is for.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  """  
      self.AllocationVariance:bool = obj["AllocationVariance"]
      """  If the count of this part has a variance, and the part is allocated to a sales order, job or transfer order, this Allocation Variance flag will be set to TRUE.  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number selected for counting.  """  
      self.TotFrozenVal:int = obj["TotFrozenVal"]
      """  Total cost of the part at the time the inventory quantity was frozen, based on the frozen bin/lot quantity and the frozen cost of each bin/lot. Updated at the time the counts are posted.  """  
      self.TotFrozenQOH:int = obj["TotFrozenQOH"]
      """  Total quantity on hand in the warehouse at the time the inventory was frozen . Updated at the time the counts are posted. This quantity is expressed in the Part base UOM  """  
      self.PostStatus:int = obj["PostStatus"]
      """   The posting status of the part. 1 = the count for this part has been processed by the post final counts process, inventory adjustments were made.
2= the count for this part has been processed by the post final counts process and inventory adjustments were not made (no differences between count and frozen, or part was within Quantity Adjustment Tolerance)
 3= part was removed from the cycle after tags were generated, no posting required. 
Code/Desc:
0 ? Not posted
1 ? Adjustment posted
2 = No Adjustment required
3 = Voided  """  
      self.CDRCode:str = obj["CDRCode"]
      """  If the count/recount of the part is outside of tolerance, this reason code is required before the counts will be posted.  """  
      self.TotCountVal:int = obj["TotCountVal"]
      """  Total cost of the part at the time the final count was posted, based on the counted bin/lot quantity and the frozen cost of each bin/lot.  """  
      self.TotCountQOH:int = obj["TotCountQOH"]
      """  New on hand in the warehouse after the final count was posted This quantity is expressed in the Part base UOM.  """  
      self.DateRemoved:str = obj["DateRemoved"]
      """  The date the part was removed from  the cycle. (PostStatus=3)  """  
      self.RemovedBy:str = obj["RemovedBy"]
      """  This is the user id of the person that removed the part from the cycle (PostStatus=3)  """  
      self.MoveToCycle:str = obj["MoveToCycle"]
      """  There will be data here only if PostStatus =3 and the part was moved to another cycle at the time the tags were voided. The format will be YYYY*MM*CycleSeq where CycleSeq is the cycle the part was moved to.  """  
      self.PcntTolerance:int = obj["PcntTolerance"]
      """  This is the percent tolerance that was used for this part for this cycle cycle if PcntToleranceUsed = true. This data is created by the cycle count variance report process.  """  
      self.ABCCode:str = obj["ABCCode"]
      """  ABC Code for the part. Used in during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  """  
      self.QtyToleranceUsed:bool = obj["QtyToleranceUsed"]
      """  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  """  
      self.PcntToleranceUsed:bool = obj["PcntToleranceUsed"]
      """  Indicates whether a PcntTolerance was used by the cycle count variance report.  """  
      self.ValToleranceUsed:bool = obj["ValToleranceUsed"]
      """  Indicates whether a ValtTolerance was used by the cycle count variance report.  """  
      self.QtyAdjTolerance:int = obj["QtyAdjTolerance"]
      """  This is the quantity adjustment  tolerance that was used for this part for this cycle. If zero all quantity adjustments will be posted. This data is created by the cycle count variance report process.  """  
      self.VarToleranceStat:int = obj["VarToleranceStat"]
      """   Variance tolerance status. Indicates whether the counted qty for the part is within all variance tolerance parameters. 0 = tolerance has not yet been evaluated by the variance process.
1= the item is in tolerance.
2 =  the item is out of tolerance
This data is created by the cycle count variance report process. It is cleared if the part is selected for recount. The data is used by the posting process to determine if a CDR is required before posting. The posting process will not process this part if the value is zero.
Code/Desc:
0 = Not yet evaluated
1 = In tolerance
2 = Out of tolerance  """  
      self.PostAdjustment:int = obj["PostAdjustment"]
      """   This data is created by the cycle count variance report process.  It is cleared if the part is selected for recount. The data is used by the posting process to determine whether to post adjustments to inventory.
0 = tolerance has not yet been evaluated by the variance process.
1 = the part is within tolerance per the qty adjustment tolerance and no quantity adjustments should be posted.
2 = the part is outside of qty adjustment tolerance and adjustments should be posted

0 = Not yet evaluated
1 = Adjustment will not post
2 = Adjustment will post  """  
      self.QtyTolerance:int = obj["QtyTolerance"]
      """  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  """  
      self.ValueTolerance:int = obj["ValueTolerance"]
      """  This is the value tolerance that was used for this part for this cycle if ValToleranceUsed = trueThis data is created by the cycle count variance report process.  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """  The Base UOM for this part. All qty fields in this record are expressed in this UOM.Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.TotActivityBeforeCount:int = obj["TotActivityBeforeCount"]
      """  Total ActivityBeforeCount for related CCTag records. Updated at the time the counts are posted. This quantity is expressed in the Part base UOM.  """  
      self.TotActivityBeforeVal:int = obj["TotActivityBeforeVal"]
      """  Total ActivityBeforeValue for related CCTag records. Updated at the time the counts are posted..  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AddedByBlankTag:bool = obj["AddedByBlankTag"]
      """  True indicates this part was added to the physical Inventory cycle during count entry using a blank tag. Counts and inventory adjustments for the part will be made based only on the blank tags entered for the part, regardless of what other bins/lots/serial numbers, etc may exist for the part in the warehouse at the time of posting the counts for the part. This is only possible for a physical inventory count.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ABCSeq:int = obj["ABCSeq"]
      """  External field used during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  """  
      self.EnableCDRCode:bool = obj["EnableCDRCode"]
      """  Indicates wheter this CCDtl can have a CDR Code entered for it.  """  
      self.MovedToCycleSeq:int = obj["MovedToCycleSeq"]
      """  Moved To Cycle Seq  """  
      self.MovedToMonth:int = obj["MovedToMonth"]
      """  Moved to Month  """  
      self.MovedToYear:int = obj["MovedToYear"]
      """  Moved to Year  """  
      self.MovePart:bool = obj["MovePart"]
      """  Indicates whether the CCDtl was selected for move or delete in Cycle Count Part Selection Update  """  
      self.MoveToMonthName:str = obj["MoveToMonthName"]
      """  Month name of MonthToMonth field  """  
      self.PostStatusDesc:str = obj["PostStatusDesc"]
      """  Post Status Description  """  
      self.QtyAdjustmentStatus:str = obj["QtyAdjustmentStatus"]
      """  Its value is derived from PostAdjustment field value: 0-Not Yet Evaluated,1-Adjustment Will Not Post,2-Adjustment Will Post"  """  
      self.QtyVariance:int = obj["QtyVariance"]
      """  Qty Variance Value = TotCountQOH - (TotFrozenQOH + TotActivityBeforeCount)  """  
      self.ValueVariance:int = obj["ValueVariance"]
      """  Value Variance = TotCountVal - (TotFrozenVal + TotActivityBeforeVal)  """  
      self.VarToleranceStatDesc:str = obj["VarToleranceStatDesc"]
      """  Description of the CCDtl.VarToleranceStat; based on CCDtl.VarToleranceStat code/desc settings  """  
      self.VoidPartTags:bool = obj["VoidPartTags"]
      """  External field used to indicate that the VoidTagsByPart processing should be done for this part.  """  
      self.AddAllAttributeSets:bool = obj["AddAllAttributeSets"]
      """  Used in Cycle Count Part Selection update to indicate all attribute sets for an attribute set tracked part should be added to the cycle.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CCPeriodDefnPeriodDesc:str = obj["CCPeriodDefnPeriodDesc"]
      self.CCPeriodDefnPeriodStart:str = obj["CCPeriodDefnPeriodStart"]
      self.CCPeriodDefnPeriodEnd:str = obj["CCPeriodDefnPeriodEnd"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.WarehseDescription:str = obj["WarehseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CCHdrListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.Plant:str = obj["Plant"]
      """  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year that this cycle count control record is for.  """  
      self.CCMonth:int = obj["CCMonth"]
      """  CCPeriodDefn.CycleSeq that this cycle count control record is for.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  """  
      self.CycleDate:str = obj["CycleDate"]
      """  The date the cycle is scheduled to begin. This data is initialized in the warehouse cycle count scheduling process.  """  
      self.CycleStatus:int = obj["CycleStatus"]
      """   This code will indicate the status of the cycle. When status is zero the cycle is scheduled but not started. Inventory is frozen at sequence start.
Code/Desc:
0 = scheduled 
1 = tags generated
2 = Count started 
3 = counts entered
4 = recount tags generated 5 = (not used) 
6 = completed
7= canceled.  """  
      self.TagGenDate:str = obj["TagGenDate"]
      """  This is the date the tags were generated  """  
      self.SeqStartDate:str = obj["SeqStartDate"]
      """  This is the date the cycle sequence was started. This is when the inventory counts were frozen.  """  
      self.TimeSeqStarted:int = obj["TimeSeqStarted"]
      """  This is the time the cycle sequence was started and inventory counts were frozen.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  This is the date the cycle was completed or cancelled.  """  
      self.CompleteTime:int = obj["CompleteTime"]
      """  This is the time the cycle was completed or cancelled.  """  
      self.AdjustPosted:bool = obj["AdjustPosted"]
      """  Indicated whether adjustments have been posted to inventory. True =  the count posting process has been run at least once for this cycle. False = no adjustments have been posted to inventory.  """  
      self.SheetOrTag:int = obj["SheetOrTag"]
      """   Indicates whether sheets or tags were printed for this cycle.
Code/desc:
0 = no tags have been printed for the cycle
1 =  tags
2 = sheets  """  
      self.TotalParts:int = obj["TotalParts"]
      """  This is the total number of parts scheduled for this cycle at the time the count sequence was started.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TotalPCIDSelected:int = obj["TotalPCIDSelected"]
      """  The total number of top level PCIDs selected for this cycle.  """  
      self.NumOfBlankTags:int = obj["NumOfBlankTags"]
      """  field used by GenerateTags to indicate how many blank tags should be generated  """  
      self.BlankTagsOnly:bool = obj["BlankTagsOnly"]
      """  field used by Generate Tags logic to control when the user is limited to generating blank tags only  """  
      self.TagSortOption:int = obj["TagSortOption"]
      """  field to indicate the sort order for tag generation.  Enter data in the Code/Desc field: 0 = Bin/UOM.Lot 1 = PartClass/Bin/Part/UOM/Lot 2 = Part/Bin/UOM/Lot  """  
      self.PostTransDate:str = obj["PostTransDate"]
      """  External field to be used as the transaction date for the PartTran records created during post adjustments.  """  
      self.LogFileName:str = obj["LogFileName"]
      """  External field used to hold the Post Counts log filename.  """  
      self.EnablePrintTags:bool = obj["EnablePrintTags"]
      self.EnableReprintTags:bool = obj["EnableReprintTags"]
      self.EnableVoidTagsByPart:bool = obj["EnableVoidTagsByPart"]
      self.EnableVoidBlankTags:bool = obj["EnableVoidBlankTags"]
      self.EnableStartCountSeq:bool = obj["EnableStartCountSeq"]
      self.RemoveAllParts:bool = obj["RemoveAllParts"]
      """  Flag to indicate that all CCDtl (parts) should be removed from the CCHdr. Used by Cycle Count part Selection Update  """  
      self.CycleDateString:str = obj["CycleDateString"]
      self.CycleStatusDesc:str = obj["CycleStatusDesc"]
      """  0 = Scheduled, 1=Tags Generated, 2=Count Started,3=Counts Entered,4=Recount Tags Generated,5=Not Used,6=Completed,7=Cancelled  """  
      self.CancelPI:bool = obj["CancelPI"]
      """  Used to indicate to the BL that the physical inventory cycle should be cancelled.  """  
      self.MonthName:str = obj["MonthName"]
      """  Month Name  """  
      self.CCHdrWarehseDescription:str = obj["CCHdrWarehseDescription"]
      """  Description.  """  
      self.CCPeriodDefnPeriodEnd:str = obj["CCPeriodDefnPeriodEnd"]
      """  Defines the end date of the period  """  
      self.CCPeriodDefnPeriodStart:str = obj["CCPeriodDefnPeriodStart"]
      """  Defines the start date of the count period  """  
      self.CCPeriodDefnPeriodDesc:str = obj["CCPeriodDefnPeriodDesc"]
      """  Unique period description assigned by the user.  """  
      self.WhseCodeDescription:str = obj["WhseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CCHdrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.Plant:str = obj["Plant"]
      """  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year that this cycle count control record is for.  """  
      self.CCMonth:int = obj["CCMonth"]
      """  CCPeriodDefn.CycleSeq that this cycle count control record is for.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  """  
      self.CycleDate:str = obj["CycleDate"]
      """  The date the cycle is scheduled to begin. This data is initialized in the warehouse cycle count scheduling process.  """  
      self.CycleStatus:int = obj["CycleStatus"]
      """   This code will indicate the status of the cycle. When status is zero the cycle is scheduled but not started. Inventory is frozen at sequence start.
Code/Desc:
0 = scheduled 
1 = tags generated
2 = Count started 
3 = counts entered
4 = recount tags generated 5 = (not used) 
6 = completed
7= canceled.  """  
      self.TagGenDate:str = obj["TagGenDate"]
      """  This is the date the tags were generated  """  
      self.SeqStartDate:str = obj["SeqStartDate"]
      """  This is the date the cycle sequence was started. This is when the inventory counts were frozen.  """  
      self.TimeSeqStarted:int = obj["TimeSeqStarted"]
      """  This is the time the cycle sequence was started and inventory counts were frozen.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  This is the date the cycle was completed or cancelled.  """  
      self.CompleteTime:int = obj["CompleteTime"]
      """  This is the time the cycle was completed or cancelled.  """  
      self.AdjustPosted:bool = obj["AdjustPosted"]
      """  Indicated whether adjustments have been posted to inventory. True =  the count posting process has been run at least once for this cycle. False = no adjustments have been posted to inventory.  """  
      self.SheetOrTag:int = obj["SheetOrTag"]
      """   Indicates whether sheets or tags were printed for this cycle.
Code/desc:
0 = no tags have been printed for the cycle
1 =  tags
2 = sheets  """  
      self.TotalParts:int = obj["TotalParts"]
      """  This is the total number of parts scheduled for this cycle at the time the count sequence was started.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IncludeNonNettable:bool = obj["IncludeNonNettable"]
      """  IncludeNonNettable  """  
      self.TotalPCIDSelected:int = obj["TotalPCIDSelected"]
      """  The total number of top level PCIDs selected for this cycle.  """  
      self.NestedPCID:bool = obj["NestedPCID"]
      """  On the Generate Tags form, True = CCPDICTags are generated for the top level PCIDs already selected for this Cycle and for the related nested PCIDs and ItemPartNum. False = PCID tags will only be generated for the top level PCIDs already selected for this Cycle.  """  
      self.CancelPI:bool = obj["CancelPI"]
      """  Used to indicate to the BL that the physical inventory cycle should be cancelled.  """  
      self.CycleDateString:str = obj["CycleDateString"]
      self.CycleStatusDesc:str = obj["CycleStatusDesc"]
      """  0 = Scheduled, 1=Tags Generated, 2=Count Started,3=Counts Entered,4=Recount Tags Generated,5=Not Used,6=Completed,7=Cancelled  """  
      self.EnablePrintTags:bool = obj["EnablePrintTags"]
      self.EnableReprintTags:bool = obj["EnableReprintTags"]
      self.EnableStartCountSeq:bool = obj["EnableStartCountSeq"]
      self.EnableVoidBlankTags:bool = obj["EnableVoidBlankTags"]
      self.EnableVoidTagsByPart:bool = obj["EnableVoidTagsByPart"]
      self.LogFileName:str = obj["LogFileName"]
      """  External field used to hold the Post Counts log filename.  """  
      self.MonthName:str = obj["MonthName"]
      """  Month Name  """  
      self.NumOfBlankTags:int = obj["NumOfBlankTags"]
      """  field used by GenerateTags to indicate how many blank tags should be generated  """  
      self.PostTransDate:str = obj["PostTransDate"]
      """  External field to be used as the transaction date for the PartTran records created during post adjustments.  """  
      self.RemoveAllParts:bool = obj["RemoveAllParts"]
      """  Flag to indicate that all CCDtl (parts) should be removed from the CCHdr. Used by Cycle Count part Selection Update  """  
      self.TagSortOption:int = obj["TagSortOption"]
      """  field to indicate the sort order for tag generation.  Enter data in the Code/Desc field: 0 = Bin/UOM.Lot 1 = PartClass/Bin/Part/UOM/Lot 2 = Part/Bin/UOM/Lot  """  
      self.BlankTagsOnly:bool = obj["BlankTagsOnly"]
      """  field used by Generate Tags logic to control when the user is limited to generating blank tags only  """  
      self.NumOfBlankPCIDTags:int = obj["NumOfBlankPCIDTags"]
      """  field used by GenerateTags to indicate how many blank PCID tags should be generated  """  
      self.PartPostedExists:bool = obj["PartPostedExists"]
      self.TrackedNumberSerialPart:bool = obj["TrackedNumberSerialPart"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates that any PartNumTrackSerialNum = true exist in details  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CCHdrWarehseDescription:str = obj["CCHdrWarehseDescription"]
      self.CCPeriodDefnPeriodStart:str = obj["CCPeriodDefnPeriodStart"]
      self.CCPeriodDefnPeriodDesc:str = obj["CCPeriodDefnPeriodDesc"]
      self.CCPeriodDefnPeriodEnd:str = obj["CCPeriodDefnPeriodEnd"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CCPCIDRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse identifier  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year that this cycle count is for  """  
      self.CCMonth:int = obj["CCMonth"]
      """  CCPeriodDefn.CycleSeq that this cycle count control record is for.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  True = full physical inventory count cycle, false = cycle count cycle  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  Cycle Sequence  """  
      self.PCID:str = obj["PCID"]
      """  Equates to a PkgControlHeader PCID. It could be top level or a nested PCID.  """  
      self.ParentPCID:str = obj["ParentPCID"]
      """  The Parent PCID defined for this CCPCID.PCID  """  
      self.TopLevelPCID:str = obj["TopLevelPCID"]
      """  The outermost PCID that contains this CCPCID.PCID  """  
      self.AddedByBlankTag:bool = obj["AddedByBlankTag"]
      """  True indicates this PCID was added to the cycle during count entry using a blank tag.  """  
      self.AllocationVariance:bool = obj["AllocationVariance"]
      """  If any ItemPartNum count of this PCID has a variance, and the part is allocated to a sales order, job or transfer order, this Allocation Variance flag will be set to TRUE. For consistency with CCDtl, not currently used  """  
      self.BinNum:str = obj["BinNum"]
      """  Bin number defaulted from PkgControlHeader or entered on a blank tag  """  
      self.MoveToCycle:str = obj["MoveToCycle"]
      """  There will be data here only if PostStatus =3 and the PCID was moved to another cycle at the time the tags were voided. The format will be YYYY*MM*CycleSeq where CycleSeq is the cycle the part was moved to.  """  
      self.DateRemoved:str = obj["DateRemoved"]
      """  The date the PCID was removed from  the cycle. (PostStatus=3)  """  
      self.RemovedBy:str = obj["RemovedBy"]
      """  This is the user id of the person that removed the PCID from the cycle (PostStatus=3)  """  
      self.PostAdjustment:int = obj["PostAdjustment"]
      """  This data is created by the cycle count variance report process.  Used by the posting process to determine whether to post adjustments to inventory.  Code Desc: 0`Not Yet Evaluated~1`Adjustment Will Not Post~2`Adjustment Will Post  """  
      self.PostStatus:int = obj["PostStatus"]
      """  The posting status of the PCID. 1 = the count for this part has been processed by the post final counts process, inventory adjustments were made. 2= the count for this PCID has been processed by the post final counts process and inventory adjustments were not made 3= PCID was removed from the cycle after tags were generated, no posting required Code Desc: 0`Not Posted~1`Adjustment Posted~2`No Adjustment  Required~3`Voided  """  
      self.CCPCIDBoolean01:bool = obj["CCPCIDBoolean01"]
      """  Reserved for development use.  """  
      self.CCPCIDBoolean02:bool = obj["CCPCIDBoolean02"]
      """  Reserved for development use.  """  
      self.CCPCIDCharacter01:str = obj["CCPCIDCharacter01"]
      """  Reserved for development use.  """  
      self.CCPCIDCharacter02:str = obj["CCPCIDCharacter02"]
      """  Reserved for development use.  """  
      self.CCPCIDCharacter03:str = obj["CCPCIDCharacter03"]
      """  Reserved for development use.  """  
      self.CCPCIDCharacter04:str = obj["CCPCIDCharacter04"]
      """  Reserved for development use.  """  
      self.CCPCIDCharacter05:str = obj["CCPCIDCharacter05"]
      """  Reserved for development use.  """  
      self.CCPCIDDate01:str = obj["CCPCIDDate01"]
      """  Reserved for development use.  """  
      self.CCPCIDDate02:str = obj["CCPCIDDate02"]
      """  Reserved for development use.  """  
      self.CCPCIDDecimal01:int = obj["CCPCIDDecimal01"]
      """  Reserved for development use.  """  
      self.CCPCIDDecimal02:int = obj["CCPCIDDecimal02"]
      """  Reserved for development use.  """  
      self.CCPCIDInteger01:int = obj["CCPCIDInteger01"]
      """  Used for indicating the level at which this PCIDis nested below the top level it is associated to  """  
      self.CCPCIDInteger02:int = obj["CCPCIDInteger02"]
      """  Reserved for development use.  """  
      self.MoveToWarehouseCode:str = obj["MoveToWarehouseCode"]
      """  The warehouse to which the PCID should be moved during posting.  """  
      self.MoveToBinNum:str = obj["MoveToBinNum"]
      """  The warehouse bin to which the PCID should be moved during posting.  """  
      self.AddToPCID:str = obj["AddToPCID"]
      """  The PCID to which this PCID should be added during posting.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.MovePCID:bool = obj["MovePCID"]
      """  Indicates if the CCPCID was selected for move or delete in Cycle Count Part / PCID Selection Update.  """  
      self.MovetoMonthName:str = obj["MovetoMonthName"]
      """  Needed if the user will be able to move PCID from one cycle to another in Part Selection Update  """  
      self.VoidPCIDTags:bool = obj["VoidPCIDTags"]
      """  Used to indicate that the VoidTagsByPCID processing should be done for this PCID.  """  
      self.MovedToMonth:int = obj["MovedToMonth"]
      """  The Month that this PCID was moved to during posting.  Format consistent with CCPeriodDefn.PeriodSeq.  """  
      self.MovedToYear:int = obj["MovedToYear"]
      """  The Year that this PCID was moved to during posting.  Format consistent with CCPeriodDefn.PeriodYear.  """  
      self.MovedToCycleSeq:int = obj["MovedToCycleSeq"]
      """  The Cycle that this PCID was moved to during posting.  Format consistent with CCHdr.CycleSeq.  """  
      self.QtyAdjustmentStatus:str = obj["QtyAdjustmentStatus"]
      """  Its value is derived from PostAdjustment field value: 0-Not Yet Evaluated,1-Adjustment Will Not Post,2-Adjustment Will Post"  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CCPeriodDefnPeriodEnd:str = obj["CCPeriodDefnPeriodEnd"]
      self.CCPeriodDefnPeriodStart:str = obj["CCPeriodDefnPeriodStart"]
      self.CCPeriodDefnPeriodDesc:str = obj["CCPeriodDefnPeriodDesc"]
      self.WarehseDescription:str = obj["WarehseDescription"]
      self.WhseBinDescription:str = obj["WhseBinDescription"]
      self.WhseBinAisle:str = obj["WhseBinAisle"]
      self.WhseBinZoneID:str = obj["WhseBinZoneID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CCPCIDSelectedRow:
   def __init__(self, obj):
      self.Aisle:str = obj["Aisle"]
      """  Optional, used to specify the aisle that the bin is located in. Disable if Portable = true  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin where the PCID is currently located.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Elevation:int = obj["Elevation"]
      """  Optional. Used to specify the elevation of the bin. Normally the bin on the gound level would be 1, the bin above that would be 2, and so on.  """  
      self.Face:str = obj["Face"]
      """  Optional, used to specify the face within the aisle that the bin is located on. Disable if Portable = true  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.Plant:str = obj["Plant"]
      """  Site where the PCID is currently located.  """  
      self.Selected:bool = obj["Selected"]
      """  Set to true if selected by the user.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse where the PCID is currently located.  """  
      self.ZoneID:str = obj["ZoneID"]
      """  The ZoneID is the reference to the WhseZone record. Optional, but if entered must be valid.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddPCIDToCycle_input:
   """ Required : 
   ds
   year
   month
   fullPhysical
   cycleSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      self.year:int = obj["year"]
      self.month:int = obj["month"]
      self.fullPhysical:bool = obj["fullPhysical"]
      self.cycleSeq:int = obj["cycleSeq"]
      pass

class AddPCIDToCycle_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreatePCIDSelected_input:
   """ Required : 
   ds
   whseCode
   frBin
   toBin
   frZone
   toZone
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      self.whseCode:str = obj["whseCode"]
      self.frBin:str = obj["frBin"]
      self.toBin:str = obj["toBin"]
      self.frZone:str = obj["frZone"]
      self.toZone:str = obj["toZone"]
      pass

class CreatePCIDSelected_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   plant
   warehouseCode
   ccYear
   ccMonth
   fullPhysical
   cycleSeq
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.ccYear:int = obj["ccYear"]
      self.ccMonth:int = obj["ccMonth"]
      self.fullPhysical:bool = obj["fullPhysical"]
      self.cycleSeq:int = obj["cycleSeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CCDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.Plant:str = obj["Plant"]
      """  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year that this cycle count control record is for.  """  
      self.CCMonth:int = obj["CCMonth"]
      """  CCPeriodDefn.CycleSeq that this cycle count control record is for.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  """  
      self.AllocationVariance:bool = obj["AllocationVariance"]
      """  If the count of this part has a variance, and the part is allocated to a sales order, job or transfer order, this Allocation Variance flag will be set to TRUE.  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number selected for counting.  """  
      self.TotFrozenVal:int = obj["TotFrozenVal"]
      """  Total cost of the part at the time the inventory quantity was frozen, based on the frozen bin/lot quantity and the frozen cost of each bin/lot. Updated at the time the counts are posted.  """  
      self.TotFrozenQOH:int = obj["TotFrozenQOH"]
      """  Total quantity on hand in the warehouse at the time the inventory was frozen . Updated at the time the counts are posted. This quantity is expressed in the Part base UOM  """  
      self.PostStatus:int = obj["PostStatus"]
      """   The posting status of the part. 1 = the count for this part has been processed by the post final counts process, inventory adjustments were made.
2= the count for this part has been processed by the post final counts process and inventory adjustments were not made (no differences between count and frozen, or part was within Quantity Adjustment Tolerance)
 3= part was removed from the cycle after tags were generated, no posting required. 
Code/Desc:
0 ? Not posted
1 ? Adjustment posted
2 = No Adjustment required
3 = Voided  """  
      self.CDRCode:str = obj["CDRCode"]
      """  If the count/recount of the part is outside of tolerance, this reason code is required before the counts will be posted.  """  
      self.TotCountVal:int = obj["TotCountVal"]
      """  Total cost of the part at the time the final count was posted, based on the counted bin/lot quantity and the frozen cost of each bin/lot.  """  
      self.TotCountQOH:int = obj["TotCountQOH"]
      """  New on hand in the warehouse after the final count was posted This quantity is expressed in the Part base UOM.  """  
      self.DateRemoved:str = obj["DateRemoved"]
      """  The date the part was removed from  the cycle. (PostStatus=3)  """  
      self.RemovedBy:str = obj["RemovedBy"]
      """  This is the user id of the person that removed the part from the cycle (PostStatus=3)  """  
      self.MoveToCycle:str = obj["MoveToCycle"]
      """  There will be data here only if PostStatus =3 and the part was moved to another cycle at the time the tags were voided. The format will be YYYY*MM*CycleSeq where CycleSeq is the cycle the part was moved to.  """  
      self.PcntTolerance:int = obj["PcntTolerance"]
      """  This is the percent tolerance that was used for this part for this cycle cycle if PcntToleranceUsed = true. This data is created by the cycle count variance report process.  """  
      self.ABCCode:str = obj["ABCCode"]
      """  ABC Code for the part. Used in during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  """  
      self.QtyToleranceUsed:bool = obj["QtyToleranceUsed"]
      """  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  """  
      self.PcntToleranceUsed:bool = obj["PcntToleranceUsed"]
      """  Indicates whether a PcntTolerance was used by the cycle count variance report.  """  
      self.ValToleranceUsed:bool = obj["ValToleranceUsed"]
      """  Indicates whether a ValtTolerance was used by the cycle count variance report.  """  
      self.QtyAdjTolerance:int = obj["QtyAdjTolerance"]
      """  This is the quantity adjustment  tolerance that was used for this part for this cycle. If zero all quantity adjustments will be posted. This data is created by the cycle count variance report process.  """  
      self.VarToleranceStat:int = obj["VarToleranceStat"]
      """   Variance tolerance status. Indicates whether the counted qty for the part is within all variance tolerance parameters. 0 = tolerance has not yet been evaluated by the variance process.
1= the item is in tolerance.
2 =  the item is out of tolerance
This data is created by the cycle count variance report process. It is cleared if the part is selected for recount. The data is used by the posting process to determine if a CDR is required before posting. The posting process will not process this part if the value is zero.
Code/Desc:
0 = Not yet evaluated
1 = In tolerance
2 = Out of tolerance  """  
      self.PostAdjustment:int = obj["PostAdjustment"]
      """   This data is created by the cycle count variance report process.  It is cleared if the part is selected for recount. The data is used by the posting process to determine whether to post adjustments to inventory.
0 = tolerance has not yet been evaluated by the variance process.
1 = the part is within tolerance per the qty adjustment tolerance and no quantity adjustments should be posted.
2 = the part is outside of qty adjustment tolerance and adjustments should be posted

0 = Not yet evaluated
1 = Adjustment will not post
2 = Adjustment will post  """  
      self.QtyTolerance:int = obj["QtyTolerance"]
      """  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  """  
      self.ValueTolerance:int = obj["ValueTolerance"]
      """  This is the value tolerance that was used for this part for this cycle if ValToleranceUsed = trueThis data is created by the cycle count variance report process.  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """  The Base UOM for this part. All qty fields in this record are expressed in this UOM.Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.TotActivityBeforeCount:int = obj["TotActivityBeforeCount"]
      """  Total ActivityBeforeCount for related CCTag records. Updated at the time the counts are posted. This quantity is expressed in the Part base UOM.  """  
      self.TotActivityBeforeVal:int = obj["TotActivityBeforeVal"]
      """  Total ActivityBeforeValue for related CCTag records. Updated at the time the counts are posted..  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AddedByBlankTag:bool = obj["AddedByBlankTag"]
      """  True indicates this part was added to the physical Inventory cycle during count entry using a blank tag. Counts and inventory adjustments for the part will be made based only on the blank tags entered for the part, regardless of what other bins/lots/serial numbers, etc may exist for the part in the warehouse at the time of posting the counts for the part. This is only possible for a physical inventory count.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ABCSeq:int = obj["ABCSeq"]
      """  External field used during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  """  
      self.EnableCDRCode:bool = obj["EnableCDRCode"]
      """  Indicates wheter this CCDtl can have a CDR Code entered for it.  """  
      self.MovedToCycleSeq:int = obj["MovedToCycleSeq"]
      """  Moved To Cycle Seq  """  
      self.MovedToMonth:int = obj["MovedToMonth"]
      """  Moved to Month  """  
      self.MovedToYear:int = obj["MovedToYear"]
      """  Moved to Year  """  
      self.MovePart:bool = obj["MovePart"]
      """  Indicates whether the CCDtl was selected for move or delete in Cycle Count Part Selection Update  """  
      self.MoveToMonthName:str = obj["MoveToMonthName"]
      """  Month name of MonthToMonth field  """  
      self.PostStatusDesc:str = obj["PostStatusDesc"]
      """  Post Status Description  """  
      self.QtyAdjustmentStatus:str = obj["QtyAdjustmentStatus"]
      """  Its value is derived from PostAdjustment field value: 0-Not Yet Evaluated,1-Adjustment Will Not Post,2-Adjustment Will Post"  """  
      self.QtyVariance:int = obj["QtyVariance"]
      """  Qty Variance Value = TotCountQOH - (TotFrozenQOH + TotActivityBeforeCount)  """  
      self.ValueVariance:int = obj["ValueVariance"]
      """  Value Variance = TotCountVal - (TotFrozenVal + TotActivityBeforeVal)  """  
      self.VarToleranceStatDesc:str = obj["VarToleranceStatDesc"]
      """  Description of the CCDtl.VarToleranceStat; based on CCDtl.VarToleranceStat code/desc settings  """  
      self.VoidPartTags:bool = obj["VoidPartTags"]
      """  External field used to indicate that the VoidTagsByPart processing should be done for this part.  """  
      self.AddAllAttributeSets:bool = obj["AddAllAttributeSets"]
      """  Used in Cycle Count Part Selection update to indicate all attribute sets for an attribute set tracked part should be added to the cycle.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CCPeriodDefnPeriodDesc:str = obj["CCPeriodDefnPeriodDesc"]
      self.CCPeriodDefnPeriodStart:str = obj["CCPeriodDefnPeriodStart"]
      self.CCPeriodDefnPeriodEnd:str = obj["CCPeriodDefnPeriodEnd"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.WarehseDescription:str = obj["WarehseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CCHdrListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.Plant:str = obj["Plant"]
      """  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year that this cycle count control record is for.  """  
      self.CCMonth:int = obj["CCMonth"]
      """  CCPeriodDefn.CycleSeq that this cycle count control record is for.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  """  
      self.CycleDate:str = obj["CycleDate"]
      """  The date the cycle is scheduled to begin. This data is initialized in the warehouse cycle count scheduling process.  """  
      self.CycleStatus:int = obj["CycleStatus"]
      """   This code will indicate the status of the cycle. When status is zero the cycle is scheduled but not started. Inventory is frozen at sequence start.
Code/Desc:
0 = scheduled 
1 = tags generated
2 = Count started 
3 = counts entered
4 = recount tags generated 5 = (not used) 
6 = completed
7= canceled.  """  
      self.TagGenDate:str = obj["TagGenDate"]
      """  This is the date the tags were generated  """  
      self.SeqStartDate:str = obj["SeqStartDate"]
      """  This is the date the cycle sequence was started. This is when the inventory counts were frozen.  """  
      self.TimeSeqStarted:int = obj["TimeSeqStarted"]
      """  This is the time the cycle sequence was started and inventory counts were frozen.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  This is the date the cycle was completed or cancelled.  """  
      self.CompleteTime:int = obj["CompleteTime"]
      """  This is the time the cycle was completed or cancelled.  """  
      self.AdjustPosted:bool = obj["AdjustPosted"]
      """  Indicated whether adjustments have been posted to inventory. True =  the count posting process has been run at least once for this cycle. False = no adjustments have been posted to inventory.  """  
      self.SheetOrTag:int = obj["SheetOrTag"]
      """   Indicates whether sheets or tags were printed for this cycle.
Code/desc:
0 = no tags have been printed for the cycle
1 =  tags
2 = sheets  """  
      self.TotalParts:int = obj["TotalParts"]
      """  This is the total number of parts scheduled for this cycle at the time the count sequence was started.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TotalPCIDSelected:int = obj["TotalPCIDSelected"]
      """  The total number of top level PCIDs selected for this cycle.  """  
      self.NumOfBlankTags:int = obj["NumOfBlankTags"]
      """  field used by GenerateTags to indicate how many blank tags should be generated  """  
      self.BlankTagsOnly:bool = obj["BlankTagsOnly"]
      """  field used by Generate Tags logic to control when the user is limited to generating blank tags only  """  
      self.TagSortOption:int = obj["TagSortOption"]
      """  field to indicate the sort order for tag generation.  Enter data in the Code/Desc field: 0 = Bin/UOM.Lot 1 = PartClass/Bin/Part/UOM/Lot 2 = Part/Bin/UOM/Lot  """  
      self.PostTransDate:str = obj["PostTransDate"]
      """  External field to be used as the transaction date for the PartTran records created during post adjustments.  """  
      self.LogFileName:str = obj["LogFileName"]
      """  External field used to hold the Post Counts log filename.  """  
      self.EnablePrintTags:bool = obj["EnablePrintTags"]
      self.EnableReprintTags:bool = obj["EnableReprintTags"]
      self.EnableVoidTagsByPart:bool = obj["EnableVoidTagsByPart"]
      self.EnableVoidBlankTags:bool = obj["EnableVoidBlankTags"]
      self.EnableStartCountSeq:bool = obj["EnableStartCountSeq"]
      self.RemoveAllParts:bool = obj["RemoveAllParts"]
      """  Flag to indicate that all CCDtl (parts) should be removed from the CCHdr. Used by Cycle Count part Selection Update  """  
      self.CycleDateString:str = obj["CycleDateString"]
      self.CycleStatusDesc:str = obj["CycleStatusDesc"]
      """  0 = Scheduled, 1=Tags Generated, 2=Count Started,3=Counts Entered,4=Recount Tags Generated,5=Not Used,6=Completed,7=Cancelled  """  
      self.CancelPI:bool = obj["CancelPI"]
      """  Used to indicate to the BL that the physical inventory cycle should be cancelled.  """  
      self.MonthName:str = obj["MonthName"]
      """  Month Name  """  
      self.CCHdrWarehseDescription:str = obj["CCHdrWarehseDescription"]
      """  Description.  """  
      self.CCPeriodDefnPeriodEnd:str = obj["CCPeriodDefnPeriodEnd"]
      """  Defines the end date of the period  """  
      self.CCPeriodDefnPeriodStart:str = obj["CCPeriodDefnPeriodStart"]
      """  Defines the start date of the count period  """  
      self.CCPeriodDefnPeriodDesc:str = obj["CCPeriodDefnPeriodDesc"]
      """  Unique period description assigned by the user.  """  
      self.WhseCodeDescription:str = obj["WhseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CCHdrListTableset:
   def __init__(self, obj):
      self.CCHdrList:list[Erp_Tablesets_CCHdrListRow] = obj["CCHdrList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CCHdrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.Plant:str = obj["Plant"]
      """  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year that this cycle count control record is for.  """  
      self.CCMonth:int = obj["CCMonth"]
      """  CCPeriodDefn.CycleSeq that this cycle count control record is for.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  """  
      self.CycleDate:str = obj["CycleDate"]
      """  The date the cycle is scheduled to begin. This data is initialized in the warehouse cycle count scheduling process.  """  
      self.CycleStatus:int = obj["CycleStatus"]
      """   This code will indicate the status of the cycle. When status is zero the cycle is scheduled but not started. Inventory is frozen at sequence start.
Code/Desc:
0 = scheduled 
1 = tags generated
2 = Count started 
3 = counts entered
4 = recount tags generated 5 = (not used) 
6 = completed
7= canceled.  """  
      self.TagGenDate:str = obj["TagGenDate"]
      """  This is the date the tags were generated  """  
      self.SeqStartDate:str = obj["SeqStartDate"]
      """  This is the date the cycle sequence was started. This is when the inventory counts were frozen.  """  
      self.TimeSeqStarted:int = obj["TimeSeqStarted"]
      """  This is the time the cycle sequence was started and inventory counts were frozen.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  This is the date the cycle was completed or cancelled.  """  
      self.CompleteTime:int = obj["CompleteTime"]
      """  This is the time the cycle was completed or cancelled.  """  
      self.AdjustPosted:bool = obj["AdjustPosted"]
      """  Indicated whether adjustments have been posted to inventory. True =  the count posting process has been run at least once for this cycle. False = no adjustments have been posted to inventory.  """  
      self.SheetOrTag:int = obj["SheetOrTag"]
      """   Indicates whether sheets or tags were printed for this cycle.
Code/desc:
0 = no tags have been printed for the cycle
1 =  tags
2 = sheets  """  
      self.TotalParts:int = obj["TotalParts"]
      """  This is the total number of parts scheduled for this cycle at the time the count sequence was started.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IncludeNonNettable:bool = obj["IncludeNonNettable"]
      """  IncludeNonNettable  """  
      self.TotalPCIDSelected:int = obj["TotalPCIDSelected"]
      """  The total number of top level PCIDs selected for this cycle.  """  
      self.NestedPCID:bool = obj["NestedPCID"]
      """  On the Generate Tags form, True = CCPDICTags are generated for the top level PCIDs already selected for this Cycle and for the related nested PCIDs and ItemPartNum. False = PCID tags will only be generated for the top level PCIDs already selected for this Cycle.  """  
      self.CancelPI:bool = obj["CancelPI"]
      """  Used to indicate to the BL that the physical inventory cycle should be cancelled.  """  
      self.CycleDateString:str = obj["CycleDateString"]
      self.CycleStatusDesc:str = obj["CycleStatusDesc"]
      """  0 = Scheduled, 1=Tags Generated, 2=Count Started,3=Counts Entered,4=Recount Tags Generated,5=Not Used,6=Completed,7=Cancelled  """  
      self.EnablePrintTags:bool = obj["EnablePrintTags"]
      self.EnableReprintTags:bool = obj["EnableReprintTags"]
      self.EnableStartCountSeq:bool = obj["EnableStartCountSeq"]
      self.EnableVoidBlankTags:bool = obj["EnableVoidBlankTags"]
      self.EnableVoidTagsByPart:bool = obj["EnableVoidTagsByPart"]
      self.LogFileName:str = obj["LogFileName"]
      """  External field used to hold the Post Counts log filename.  """  
      self.MonthName:str = obj["MonthName"]
      """  Month Name  """  
      self.NumOfBlankTags:int = obj["NumOfBlankTags"]
      """  field used by GenerateTags to indicate how many blank tags should be generated  """  
      self.PostTransDate:str = obj["PostTransDate"]
      """  External field to be used as the transaction date for the PartTran records created during post adjustments.  """  
      self.RemoveAllParts:bool = obj["RemoveAllParts"]
      """  Flag to indicate that all CCDtl (parts) should be removed from the CCHdr. Used by Cycle Count part Selection Update  """  
      self.TagSortOption:int = obj["TagSortOption"]
      """  field to indicate the sort order for tag generation.  Enter data in the Code/Desc field: 0 = Bin/UOM.Lot 1 = PartClass/Bin/Part/UOM/Lot 2 = Part/Bin/UOM/Lot  """  
      self.BlankTagsOnly:bool = obj["BlankTagsOnly"]
      """  field used by Generate Tags logic to control when the user is limited to generating blank tags only  """  
      self.NumOfBlankPCIDTags:int = obj["NumOfBlankPCIDTags"]
      """  field used by GenerateTags to indicate how many blank PCID tags should be generated  """  
      self.PartPostedExists:bool = obj["PartPostedExists"]
      self.TrackedNumberSerialPart:bool = obj["TrackedNumberSerialPart"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates that any PartNumTrackSerialNum = true exist in details  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CCHdrWarehseDescription:str = obj["CCHdrWarehseDescription"]
      self.CCPeriodDefnPeriodStart:str = obj["CCPeriodDefnPeriodStart"]
      self.CCPeriodDefnPeriodDesc:str = obj["CCPeriodDefnPeriodDesc"]
      self.CCPeriodDefnPeriodEnd:str = obj["CCPeriodDefnPeriodEnd"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CCPCIDRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse identifier  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year that this cycle count is for  """  
      self.CCMonth:int = obj["CCMonth"]
      """  CCPeriodDefn.CycleSeq that this cycle count control record is for.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  True = full physical inventory count cycle, false = cycle count cycle  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  Cycle Sequence  """  
      self.PCID:str = obj["PCID"]
      """  Equates to a PkgControlHeader PCID. It could be top level or a nested PCID.  """  
      self.ParentPCID:str = obj["ParentPCID"]
      """  The Parent PCID defined for this CCPCID.PCID  """  
      self.TopLevelPCID:str = obj["TopLevelPCID"]
      """  The outermost PCID that contains this CCPCID.PCID  """  
      self.AddedByBlankTag:bool = obj["AddedByBlankTag"]
      """  True indicates this PCID was added to the cycle during count entry using a blank tag.  """  
      self.AllocationVariance:bool = obj["AllocationVariance"]
      """  If any ItemPartNum count of this PCID has a variance, and the part is allocated to a sales order, job or transfer order, this Allocation Variance flag will be set to TRUE. For consistency with CCDtl, not currently used  """  
      self.BinNum:str = obj["BinNum"]
      """  Bin number defaulted from PkgControlHeader or entered on a blank tag  """  
      self.MoveToCycle:str = obj["MoveToCycle"]
      """  There will be data here only if PostStatus =3 and the PCID was moved to another cycle at the time the tags were voided. The format will be YYYY*MM*CycleSeq where CycleSeq is the cycle the part was moved to.  """  
      self.DateRemoved:str = obj["DateRemoved"]
      """  The date the PCID was removed from  the cycle. (PostStatus=3)  """  
      self.RemovedBy:str = obj["RemovedBy"]
      """  This is the user id of the person that removed the PCID from the cycle (PostStatus=3)  """  
      self.PostAdjustment:int = obj["PostAdjustment"]
      """  This data is created by the cycle count variance report process.  Used by the posting process to determine whether to post adjustments to inventory.  Code Desc: 0`Not Yet Evaluated~1`Adjustment Will Not Post~2`Adjustment Will Post  """  
      self.PostStatus:int = obj["PostStatus"]
      """  The posting status of the PCID. 1 = the count for this part has been processed by the post final counts process, inventory adjustments were made. 2= the count for this PCID has been processed by the post final counts process and inventory adjustments were not made 3= PCID was removed from the cycle after tags were generated, no posting required Code Desc: 0`Not Posted~1`Adjustment Posted~2`No Adjustment  Required~3`Voided  """  
      self.CCPCIDBoolean01:bool = obj["CCPCIDBoolean01"]
      """  Reserved for development use.  """  
      self.CCPCIDBoolean02:bool = obj["CCPCIDBoolean02"]
      """  Reserved for development use.  """  
      self.CCPCIDCharacter01:str = obj["CCPCIDCharacter01"]
      """  Reserved for development use.  """  
      self.CCPCIDCharacter02:str = obj["CCPCIDCharacter02"]
      """  Reserved for development use.  """  
      self.CCPCIDCharacter03:str = obj["CCPCIDCharacter03"]
      """  Reserved for development use.  """  
      self.CCPCIDCharacter04:str = obj["CCPCIDCharacter04"]
      """  Reserved for development use.  """  
      self.CCPCIDCharacter05:str = obj["CCPCIDCharacter05"]
      """  Reserved for development use.  """  
      self.CCPCIDDate01:str = obj["CCPCIDDate01"]
      """  Reserved for development use.  """  
      self.CCPCIDDate02:str = obj["CCPCIDDate02"]
      """  Reserved for development use.  """  
      self.CCPCIDDecimal01:int = obj["CCPCIDDecimal01"]
      """  Reserved for development use.  """  
      self.CCPCIDDecimal02:int = obj["CCPCIDDecimal02"]
      """  Reserved for development use.  """  
      self.CCPCIDInteger01:int = obj["CCPCIDInteger01"]
      """  Used for indicating the level at which this PCIDis nested below the top level it is associated to  """  
      self.CCPCIDInteger02:int = obj["CCPCIDInteger02"]
      """  Reserved for development use.  """  
      self.MoveToWarehouseCode:str = obj["MoveToWarehouseCode"]
      """  The warehouse to which the PCID should be moved during posting.  """  
      self.MoveToBinNum:str = obj["MoveToBinNum"]
      """  The warehouse bin to which the PCID should be moved during posting.  """  
      self.AddToPCID:str = obj["AddToPCID"]
      """  The PCID to which this PCID should be added during posting.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.MovePCID:bool = obj["MovePCID"]
      """  Indicates if the CCPCID was selected for move or delete in Cycle Count Part / PCID Selection Update.  """  
      self.MovetoMonthName:str = obj["MovetoMonthName"]
      """  Needed if the user will be able to move PCID from one cycle to another in Part Selection Update  """  
      self.VoidPCIDTags:bool = obj["VoidPCIDTags"]
      """  Used to indicate that the VoidTagsByPCID processing should be done for this PCID.  """  
      self.MovedToMonth:int = obj["MovedToMonth"]
      """  The Month that this PCID was moved to during posting.  Format consistent with CCPeriodDefn.PeriodSeq.  """  
      self.MovedToYear:int = obj["MovedToYear"]
      """  The Year that this PCID was moved to during posting.  Format consistent with CCPeriodDefn.PeriodYear.  """  
      self.MovedToCycleSeq:int = obj["MovedToCycleSeq"]
      """  The Cycle that this PCID was moved to during posting.  Format consistent with CCHdr.CycleSeq.  """  
      self.QtyAdjustmentStatus:str = obj["QtyAdjustmentStatus"]
      """  Its value is derived from PostAdjustment field value: 0-Not Yet Evaluated,1-Adjustment Will Not Post,2-Adjustment Will Post"  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CCPeriodDefnPeriodEnd:str = obj["CCPeriodDefnPeriodEnd"]
      self.CCPeriodDefnPeriodStart:str = obj["CCPeriodDefnPeriodStart"]
      self.CCPeriodDefnPeriodDesc:str = obj["CCPeriodDefnPeriodDesc"]
      self.WarehseDescription:str = obj["WarehseDescription"]
      self.WhseBinDescription:str = obj["WhseBinDescription"]
      self.WhseBinAisle:str = obj["WhseBinAisle"]
      self.WhseBinZoneID:str = obj["WhseBinZoneID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CCPCIDSelectedRow:
   def __init__(self, obj):
      self.Aisle:str = obj["Aisle"]
      """  Optional, used to specify the aisle that the bin is located in. Disable if Portable = true  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin where the PCID is currently located.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Elevation:int = obj["Elevation"]
      """  Optional. Used to specify the elevation of the bin. Normally the bin on the gound level would be 1, the bin above that would be 2, and so on.  """  
      self.Face:str = obj["Face"]
      """  Optional, used to specify the face within the aisle that the bin is located on. Disable if Portable = true  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.Plant:str = obj["Plant"]
      """  Site where the PCID is currently located.  """  
      self.Selected:bool = obj["Selected"]
      """  Set to true if selected by the user.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse where the PCID is currently located.  """  
      self.ZoneID:str = obj["ZoneID"]
      """  The ZoneID is the reference to the WhseZone record. Optional, but if entered must be valid.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CCPartSelectUpdTableset:
   def __init__(self, obj):
      self.CCHdr:list[Erp_Tablesets_CCHdrRow] = obj["CCHdr"]
      self.CCDtl:list[Erp_Tablesets_CCDtlRow] = obj["CCDtl"]
      self.CCPCID:list[Erp_Tablesets_CCPCIDRow] = obj["CCPCID"]
      self.CCPCIDSelected:list[Erp_Tablesets_CCPCIDSelectedRow] = obj["CCPCIDSelected"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCCPartSelectUpdTableset:
   def __init__(self, obj):
      self.CCHdr:list[Erp_Tablesets_CCHdrRow] = obj["CCHdr"]
      self.CCDtl:list[Erp_Tablesets_CCDtlRow] = obj["CCDtl"]
      self.CCPCID:list[Erp_Tablesets_CCPCIDRow] = obj["CCPCID"]
      self.CCPCIDSelected:list[Erp_Tablesets_CCPCIDSelectedRow] = obj["CCPCIDSelected"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   plant
   warehouseCode
   ccYear
   ccMonth
   fullPhysical
   cycleSeq
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.ccYear:int = obj["ccYear"]
      self.ccMonth:int = obj["ccMonth"]
      self.fullPhysical:bool = obj["fullPhysical"]
      self.cycleSeq:int = obj["cycleSeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CCHdrListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCCDtl_input:
   """ Required : 
   ds
   plant
   warehouseCode
   ccYear
   ccMonth
   fullPhysical
   cycleSeq
   partNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.ccYear:int = obj["ccYear"]
      self.ccMonth:int = obj["ccMonth"]
      self.fullPhysical:bool = obj["fullPhysical"]
      self.cycleSeq:int = obj["cycleSeq"]
      self.partNum:str = obj["partNum"]
      pass

class GetNewCCDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCCHdr_input:
   """ Required : 
   ds
   plant
   warehouseCode
   ccYear
   ccMonth
   fullPhysical
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.ccYear:int = obj["ccYear"]
      self.ccMonth:int = obj["ccMonth"]
      self.fullPhysical:bool = obj["fullPhysical"]
      pass

class GetNewCCHdr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCCPCID_input:
   """ Required : 
   ds
   plant
   warehouseCode
   ccYear
   ccMonth
   fullPhysical
   cycleSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.ccYear:int = obj["ccYear"]
      self.ccMonth:int = obj["ccMonth"]
      self.fullPhysical:bool = obj["fullPhysical"]
      self.cycleSeq:int = obj["cycleSeq"]
      pass

class GetNewCCPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCCHdr
   whereClauseCCDtl
   whereClauseCCPCID
   whereClauseCCPCIDSelected
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCCHdr:str = obj["whereClauseCCHdr"]
      self.whereClauseCCDtl:str = obj["whereClauseCCDtl"]
      self.whereClauseCCPCID:str = obj["whereClauseCCPCID"]
      self.whereClauseCCPCIDSelected:str = obj["whereClauseCCPCIDSelected"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["returnObj"]
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

class MassAddPartAttributeSets_input:
   """ Required : 
   ds
   ccHdrSysRowID
   partNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      self.ccHdrSysRowID:str = obj["ccHdrSysRowID"]
      self.partNum:str = obj["partNum"]
      pass

class MassAddPartAttributeSets_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MovePCIDs_input:
   """ Required : 
   moveToMonth
   moveToYear
   moveToCycle
   ds
   """  
   def __init__(self, obj):
      self.moveToMonth:int = obj["moveToMonth"]
      self.moveToYear:int = obj["moveToYear"]
      self.moveToCycle:int = obj["moveToCycle"]
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

class MovePCIDs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MoveParts_input:
   """ Required : 
   moveToMonth
   moveToYear
   moveToCycle
   ds
   """  
   def __init__(self, obj):
      self.moveToMonth:int = obj["moveToMonth"]
      self.moveToYear:int = obj["moveToYear"]
      self.moveToCycle:int = obj["moveToCycle"]
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

class MoveParts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCID_input:
   """ Required : 
   ipPCID
   ds
   """  
   def __init__(self, obj):
      self.ipPCID:str = obj["ipPCID"]
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

class OnChangePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartNum_input:
   """ Required : 
   ipPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingAttributeSet_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

class OnChangingAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

class OnChangingRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RemovePCIDs_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

class RemovePCIDs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RemoveParts_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

class RemoveParts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCCPartSelectUpdTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCCPartSelectUpdTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdatePCIDSelected_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

class UpdatePCIDSelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCPartSelectUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

