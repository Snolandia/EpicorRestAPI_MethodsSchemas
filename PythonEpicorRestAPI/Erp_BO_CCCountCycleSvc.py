import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CCCountCycleSvc
# Description: Count Cycle program.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CCCountCycles(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CCCountCycles items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCCountCycles
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCCountCycles",headers=creds) as resp:
           return await resp.json()

async def post_CCCountCycles(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCCountCycles
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCCountCycles", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CCCountCycles_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CCCountCycle item
   Description: Calls GetByID to retrieve the CCCountCycle item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCCountCycle
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCCountCycles(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CCCountCycles_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CCCountCycle for the service
   Description: Calls UpdateExt to update CCCountCycle. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCCountCycle
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCCountCycles(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CCCountCycles_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CCCountCycle item
   Description: Call UpdateExt to delete CCCountCycle item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCCountCycle
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCCountCycles(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CCCountCycles_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_CCDtls(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCCountCycles(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")/CCDtls",headers=creds) as resp:
           return await resp.json()

async def get_CCCountCycles_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_CCDtls_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PartNum_AttributeSetID(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, PartNum, AttributeSetID, select = None, filter = None, epicorHeaders = None):
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCCountCycles(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")/CCDtls(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CCCountCycles_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_CCPCIDs(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCCountCycles(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")/CCPCIDs",headers=creds) as resp:
           return await resp.json()

async def get_CCCountCycles_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_CCPCIDs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PCID(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, PCID, select = None, filter = None, epicorHeaders = None):
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCCountCycles(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")/CCPCIDs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PCID + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCDtls",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCDtls", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCDtls(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCDtls(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCDtls(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCPCIDs",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCPCIDs", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCPCIDs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PCID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCPCIDs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PCID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/CCPCIDs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PCID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/LegalNumGenOpts",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCCHdr, whereClauseCCDtl, whereClauseCCPCID, whereClauseLegalNumGenOpts, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CancelPI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CancelPI
   Description: This procedure will delete all records relating to any inventory cycle where no parts have been posted.
   OperationID: CancelPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CloseCCDtlNoTags(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseCCDtlNoTags
   Description: Closes Parts on the Cycle with no associated Tags if the user indicates to do so after Post Counts.
   OperationID: CloseCCDtlNoTags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseCCDtlNoTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseCCDtlNoTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateRecountTags(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateRecountTags
   OperationID: GenerateRecountTags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateRecountTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateRecountTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateTags(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateTags
   OperationID: GenerateTags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBlankTags(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBlankTags
   OperationID: GetBlankTags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBlankTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBlankTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCycles(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCycles
   Description: Purpose:
Parameters:  none
Notes:
/// <param name="ipWarehouseCode">Selected Warehouse.</param>
/// <param name="ipPeriod">period.</param>
/// <param name="ipYear">Year.</param>
/// <param name="opCycles">opCycles.</param>
   OperationID: GetCycles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCycles_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCycles_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLegalNumGenOpts
   Description: Returns the legal number generation options.
   OperationID: GetLegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartTranPKs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartTranPKs
   Description: Return a parameters for the inventory movement logic to generate a whereClause for generated PartTran records.
   OperationID: GetPartTranPKs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartTranPKs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartTranPKs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPeriods(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPeriods
   Description: Purpose:
Parameters:  none
Notes:
/// <param name="ipWarehouseCode">Selected Warehouse.</param>
/// <param name="ipYear">Selected Year</param>
/// <param name="opPeriodList">list of periods.</param>
   OperationID: GetPeriods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPeriods_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPeriods_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetWarehouses(epicorHeaders = None):
   """  
   Summary: Invoke method GetWarehouses
   Description: Purpose:
Parameters:  none
Notes:
<param name="opWhseList">list of warehouses.</param>
   OperationID: GetWarehouses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWarehouses_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetYears(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetYears
   Description: Purpose:
Parameters:  none
Notes:
/// <param name="ipWarehouseCode">Selected Warehouse.</param>
/// <param name="opYears">opYears.</param>
   OperationID: GetYears
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetYears_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetYears_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PostCount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PostCount
   Description: Post Count.
   OperationID: PostCount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReverseStartCount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReverseStartCount
   OperationID: ReverseStartCount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReverseStartCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReverseStartCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StartCountSequence(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StartCountSequence
   OperationID: StartCountSequence
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartCountSequence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartCountSequence_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateWarehouse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateWarehouse
   OperationID: ValidateWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateYear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateYear
   OperationID: ValidateYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateMonth(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateMonth
   OperationID: ValidateMonth
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateMonth_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMonth_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCycleNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCycleNumber
   OperationID: ValidateCycleNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCycleNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCycleNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateVoidPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateVoidPartNum
   Description: Validate void tags by part number
   OperationID: ValidateVoidPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateVoidPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateVoidPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidBlankTags(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidBlankTags
   OperationID: VoidBlankTags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidBlankTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidBlankTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidTagsByPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidTagsByPart
   Description: Validate void tags by part number
   OperationID: VoidTagsByPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidTagsByPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidTagsByPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidTagsByPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidTagsByPCID
   Description: Validate and void tags by PCID
   OperationID: VoidTagsByPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidTagsByPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidTagsByPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   Description: GetAvailTranDocTypes
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ExistCycleCount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistCycleCount
   Description: Verify if the record exist.
   OperationID: ExistCycleCount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistCycleCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistCycleCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnWarehouseCodeChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnWarehouseCodeChanged
   OperationID: OnWarehouseCodeChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnWarehouseCodeChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnWarehouseCodeChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnYearChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnYearChanged
   OperationID: OnYearChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnYearChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnYearChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnMonthChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnMonthChanged
   OperationID: OnMonthChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnMonthChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnMonthChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCCountCycleSvc/List", json=requestBody,headers=creds) as resp:
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

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
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

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CancelPI_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

class CancelPI_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CloseCCDtlNoTags_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

class CloseCCDtlNoTags_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

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

class Erp_Tablesets_CCCountCycleTableset:
   def __init__(self, obj):
      self.CCHdr:list[Erp_Tablesets_CCHdrRow] = obj["CCHdr"]
      self.CCDtl:list[Erp_Tablesets_CCDtlRow] = obj["CCDtl"]
      self.CCPCID:list[Erp_Tablesets_CCPCIDRow] = obj["CCPCID"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class Erp_Tablesets_CCTagRow:
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
      self.PartNum:str = obj["PartNum"]
      """  Part Number selected for counting.  """  
      self.TagNum:str = obj["TagNum"]
      """  Tag number. This will be generated from Warehse and will be in the format of tagNum.countseq where countSeq is the count/recount sequence. First count for example would be tag 000000001.1 recount generate tag 000000001.2 from tag 000000001.1, second recount would generate tag 000000001.3  the same part, etc.  """  
      self.BinNum:str = obj["BinNum"]
      """  Bin number for the tag  """  
      self.CountedBy:str = obj["CountedBy"]
      """  Person that counted the parts on the Count Tag.  """  
      self.CountedQty:int = obj["CountedQty"]
      """  Quantity counted for the tag. Like PartBin.OnHandQty except no negative allowed. This is expressed in the qty per the CCTag.UOM unit of measure, which may not be the Part base UOM.  """  
      self.CountedTime:str = obj["CountedTime"]
      """  Optional field that Indicates when the count took place to aid in determining what activity took place before the actual count.  """  
      self.TagNote:str = obj["TagNote"]
      """  Tag Note  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This field is set equal to the Login ID variable.  System Set when a user enters a counted amount for the tag or voids the tag.  """  
      self.TagPrinted:bool = obj["TagPrinted"]
      """  Indicates that the Count Tag has been printed.  Manually entered tags are set to "Printed" when they are entered.  System Set.  """  
      self.TagReturned:bool = obj["TagReturned"]
      """  Indicates the Count Tag has been returned and the results entered into the count.  This is set when during Tag Entry when the user keys in a counted amount (or voids the tag).  System Set.  """  
      self.CountedDate:str = obj["CountedDate"]
      """  Date the count was performed.  """  
      self.TagStatus:int = obj["TagStatus"]
      """   Tag status.
Code/Desc:
0 = open
1 = posted
2 = voided 3=Closed/Recount.  """  
      self.BlankTag:bool = obj["BlankTag"]
      """  True = this tag was generated as a blank tag. This will control whether bin/lot/serial data can be changed on the tag and whether the tag can be voided independent of other tags generated for an part.  """  
      self.LotNum:str = obj["LotNum"]
      """  LotNum for the tag  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number.  """  
      self.UOM:str = obj["UOM"]
      """  The PartBin Unit of measure for this tag.  """  
      self.FrozenQOH:int = obj["FrozenQOH"]
      """  QOH in PartBin at the time the inventory was frozen. This is expressed in the qty per the CCTag.UOM unit of measure, which may not be the Part base UOM. For blank tags this will be zero.  """  
      self.FrozenCost:int = obj["FrozenCost"]
      """  The per unit part cost at the time the quantity was frozen, based on the costing method for the part/Site. This is the unit cost based on the part base UOM, which might not be the CCTag.UOM so to get total frozen cost for this tag, the CCTag quantities wi  """  
      self.EntryDate:str = obj["EntryDate"]
      """  The date the count was entered or tag was voided  """  
      self.EntryTime:int = obj["EntryTime"]
      """  The time the count was entered or tag was voided  """  
      self.SheetNum:int = obj["SheetNum"]
      """  The sheet number the tag is assigned to. If the sheet is being accessed by enter count by sheet, tags tied to that sheet cannot be accessed individually until the sheet record is unlocked.  """  
      self.FrozenTranDate:str = obj["FrozenTranDate"]
      """  The PartTran.SysDate for the last PartTran for this part when  the quantity was frozen, used with FrozentTranNum and FrozenTranTime to determine what activity has taken place after the freeze.  """  
      self.FrozenTranTime:int = obj["FrozenTranTime"]
      """  The PartTran.SysTime for the last PartTran for this part when  the quantity was frozen, used with FrozentTranDate and FrozenTranNum to determine what activity has taken place after the freeze.  """  
      self.ActivityBeforeCount:int = obj["ActivityBeforeCount"]
      """  Manually entered by the user to account for ongoing activity that took place during the count.  Inventory activity that took place AFTER the start of the count FrozenQOH), but BEFORE the actual count.  This number is used to adjust the "FrozenQOH" when determining the variance between the Frozen Quantity and the Actual Counted Quantity.  Example:  At 1:00 the count is started and the computer has 250 units on hand for part XYZ.  At 1:30 75 units are issued to a job.  At 2:30 John counts 175 units.  The variance report would report a variance of 75 units and show the issue as activity.  The user could then decide that the issue took place before the count took place and enter 75 units into the Activity Before Count field in Tag Maintenance.  The variance report would then "expect" 175 units and have a count of 175 units for a variance of zero(0).  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCIDTag:bool = obj["PCIDTag"]
      """  True indicates this tag is associated with a PCID, false indicates this tag is associated to loose inventory (non-PCID)  """  
      self.TopLevelPCID:str = obj["TopLevelPCID"]
      """  The outermost PCID that contains this CCPDICTag.PCID  """  
      self.PCID:str = obj["PCID"]
      """  Parent PCID that this tag is associated with. Equates similar to the way PkgControlItem.PCID relates to PkgControlHeader.PCID  """  
      self.ItemPCID:str = obj["ItemPCID"]
      """  Child PCID, equates to a PkgControlItem.ItemPCID. Either ItemPCID or ItemPartNum will be populated but never both, as is done in PkgControlItem table.  """  
      self.ReturnNestedPCID:bool = obj["ReturnNestedPCID"]
      """  Only applies if ItemPCID has data. True = indicates in Count Entry that all of the related CCPCIDTag records for this CCPCIDTag.ItemPCID and all lower level nested child PCIDs/Parts should be set to TagReturned = true and  for ItemPartNum records set CountedQty = FrozenQty as if the user had accessed each of the tags and manually entered.  """  
      self.CCTagBoolean01:bool = obj["CCTagBoolean01"]
      """  CCTagBoolean01  """  
      self.CCTagBoolean02:bool = obj["CCTagBoolean02"]
      """  CCTagBoolean02  """  
      self.CCTagCharacter01:str = obj["CCTagCharacter01"]
      """  Move To Bin for the tag  """  
      self.CCTagCharacter02:str = obj["CCTagCharacter02"]
      """  Tag Type for PCID tag  """  
      self.CCTagCharacter03:str = obj["CCTagCharacter03"]
      """  CCTagCharacter03  """  
      self.CCTagCharacter04:str = obj["CCTagCharacter04"]
      """  CCTagCharacter04  """  
      self.CCTagCharacter05:str = obj["CCTagCharacter05"]
      """  Source data used to generate the default serial tag when no standard tag is generated from SerialNo, PartBinQOH or  PrimaryBin  """  
      self.CCTagDate01:str = obj["CCTagDate01"]
      """  CCTagDate01  """  
      self.CCTagDate02:str = obj["CCTagDate02"]
      """  CCTagDate02  """  
      self.CCTagDecimal01:int = obj["CCTagDecimal01"]
      """  CCTagDecimal01  """  
      self.CCTagDecimal02:int = obj["CCTagDecimal02"]
      """  CCTagDecimal02  """  
      self.CCTagInteger01:int = obj["CCTagInteger01"]
      """  CCTagInteger01  """  
      self.CCTagInteger02:int = obj["CCTagInteger02"]
      """  CCTagInteger02  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.CountedQtyWarn:str = obj["CountedQtyWarn"]
      self.EnableLotNo:bool = obj["EnableLotNo"]
      self.EnableSerialNo:bool = obj["EnableSerialNo"]
      self.EnableUOMWorksheet:bool = obj["EnableUOMWorksheet"]
      """  True when UOM Worksheet must be enabled  """  
      self.HasActivity:str = obj["HasActivity"]
      """  This field is to indicate there is data in the activity grid to cue the user to consult the detail sheet before entering counts.  """  
      self.SavedBlankTag:bool = obj["SavedBlankTag"]
      self.SelectedForVoid:bool = obj["SelectedForVoid"]
      """  External field. Used by the Void Blank Tags processing to indicate the tag was selected for void.  """  
      self.TagStatusDesc:str = obj["TagStatusDesc"]
      """  Tag Status Description  """  
      self.UOMDO:str = obj["UOMDO"]
      """  Display Only Unit Of Measure.  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.EnablePCID:bool = obj["EnablePCID"]
      self.EnableItemPCID:bool = obj["EnableItemPCID"]
      self.IsNestedPCID:bool = obj["IsNestedPCID"]
      self.IsItemQty:bool = obj["IsItemQty"]
      self.MoveToBinDescription:str = obj["MoveToBinDescription"]
      self.TagTypeDescList:str = obj["TagTypeDescList"]
      """  Used for Code Desc list to allow changing this list by manually setting in code logic.  """  
      self.TagTypeDescription:str = obj["TagTypeDescription"]
      """  Tag Type Description  """  
      self.EnableTagType:bool = obj["EnableTagType"]
      self.EnableGenLowerNestedPCID:bool = obj["EnableGenLowerNestedPCID"]
      self.HHNumOfBlankPCIDTags:int = obj["HHNumOfBlankPCIDTags"]
      """  This field used by GenerateTags to indicate how many blank PCID tags should be generated in the HH Count Entry. Field was added because cycle header is not used in HH Count Entry so cannot use similar field from CCHdr table  """  
      self.HHNumOfBlankTags:int = obj["HHNumOfBlankTags"]
      """  This field used by GenerateTags to indicate how many blank tags should be generated in the HH Count Entry. Field was added because cycle header is not used in HH Count Entry so cannot use similar field from CCHdr table  """  
      self.EnableBinNum:bool = obj["EnableBinNum"]
      """  Flag to set row rule to know if CCTag.BinNum should be enabled in UI  """  
      self.EnableReturnNestedPCID:bool = obj["EnableReturnNestedPCID"]
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.DisableRevisionNum:bool = obj["DisableRevisionNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CCPeriodDefnPeriodEnd:str = obj["CCPeriodDefnPeriodEnd"]
      self.CCPeriodDefnPeriodDesc:str = obj["CCPeriodDefnPeriodDesc"]
      self.CCPeriodDefnPeriodStart:str = obj["CCPeriodDefnPeriodStart"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.WarehseDescription:str = obj["WarehseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CCTagTableset:
   def __init__(self, obj):
      self.CCTag:list[Erp_Tablesets_CCTagRow] = obj["CCTag"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtCCCountCycleTableset:
   def __init__(self, obj):
      self.CCHdr:list[Erp_Tablesets_CCHdrRow] = obj["CCHdr"]
      self.CCDtl:list[Erp_Tablesets_CCDtlRow] = obj["CCDtl"]
      self.CCPCID:list[Erp_Tablesets_CCPCIDRow] = obj["CCPCID"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExistCycleCount_input:
   """ Required : 
   Company
   Plant
   WhseCode
   CCYear
   CCMonth
   CycleSeq
   FullPhys
   """  
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.WhseCode:str = obj["WhseCode"]
      """  Warehouse Code  """  
      self.CCYear:int = obj["CCYear"]
      """  CCYear  """  
      self.CCMonth:int = obj["CCMonth"]
      """  CCMonth  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  Cycle Sequence  """  
      self.FullPhys:bool = obj["FullPhys"]
      """  Full Physical  """  
      pass

class ExistCycleCount_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True/False  """  
      pass

class GenerateRecountTags_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

class GenerateRecountTags_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GenerateTags_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

class GenerateTags_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vFirstTag:int = obj["parameters"]
      self.vLastTag:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.AvailTranDocTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetBlankTags_input:
   """ Required : 
   vBlankTagsAvail
   ds
   ds1
   """  
   def __init__(self, obj):
      self.vBlankTagsAvail:bool = obj["vBlankTagsAvail"]
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_CCTagTableset] = obj["ds1"]
      pass

class GetBlankTags_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vBlankTagsAvail:bool = obj["vBlankTagsAvail"]
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_CCTagTableset] = obj["ds1"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_CCCountCycleTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CCCountCycleTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CCCountCycleTableset] = obj["returnObj"]
      pass

class GetCycles_input:
   """ Required : 
   ipWarehouseCode
   ipYear
   ipPeriod
   """  
   def __init__(self, obj):
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      self.ipYear:int = obj["ipYear"]
      self.ipPeriod:int = obj["ipPeriod"]
      pass

class GetCycles_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCycles:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetLegalNumGenOpts_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

class GetLegalNumGenOpts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
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
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartTranPKs_input:
   """ Required : 
   ipWarehouseCode
   ipCCYear
   ipCCMonth
   ipCycleSeq
   """  
   def __init__(self, obj):
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  The Warehouse Code  """  
      self.ipCCYear:int = obj["ipCCYear"]
      """  The CCYear  """  
      self.ipCCMonth:int = obj["ipCCMonth"]
      """  The CCMonth  """  
      self.ipCycleSeq:int = obj["ipCycleSeq"]
      """  The CycleSeq  """  
      pass

class GetPartTranPKs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPeriods_input:
   """ Required : 
   ipWarehouseCode
   ipYear
   """  
   def __init__(self, obj):
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      self.ipYear:int = obj["ipYear"]
      pass

class GetPeriods_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPeriodList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCCHdr
   whereClauseCCDtl
   whereClauseCCPCID
   whereClauseLegalNumGenOpts
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCCHdr:str = obj["whereClauseCCHdr"]
      self.whereClauseCCDtl:str = obj["whereClauseCCDtl"]
      self.whereClauseCCPCID:str = obj["whereClauseCCPCID"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CCCountCycleTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetWarehouses_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opWhseList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetYears_input:
   """ Required : 
   ipWarehouseCode
   """  
   def __init__(self, obj):
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      pass

class GetYears_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opYears:str = obj["parameters"]
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

class OnMonthChanged_input:
   """ Required : 
   warehouseCode
   year
   month
   """  
   def __init__(self, obj):
      self.warehouseCode:str = obj["warehouseCode"]
      self.year:int = obj["year"]
      self.month:int = obj["month"]
      pass

class OnMonthChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.seq:int = obj["parameters"]
      pass

      """  output parameters  """  

class OnWarehouseCodeChanged_input:
   """ Required : 
   warehouseCode
   """  
   def __init__(self, obj):
      self.warehouseCode:str = obj["warehouseCode"]
      pass

class OnWarehouseCodeChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.year:int = obj["parameters"]
      self.month:int = obj["parameters"]
      self.seq:int = obj["parameters"]
      pass

      """  output parameters  """  

class OnYearChanged_input:
   """ Required : 
   warehouseCode
   year
   """  
   def __init__(self, obj):
      self.warehouseCode:str = obj["warehouseCode"]
      self.year:int = obj["year"]
      pass

class OnYearChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.month:int = obj["parameters"]
      self.seq:int = obj["parameters"]
      pass

      """  output parameters  """  

class PostCount_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

class PostCount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      self.noTags:bool = obj["noTags"]
      pass

      """  output parameters  """  

class ReverseStartCount_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

class ReverseStartCount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class StartCountSequence_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

class StartCountSequence_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCCCountCycleTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCCCountCycleTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateCycleNumber_input:
   """ Required : 
   warehouse
   year
   month
   cycleNum
   """  
   def __init__(self, obj):
      self.warehouse:str = obj["warehouse"]
      self.year:int = obj["year"]
      self.month:int = obj["month"]
      self.cycleNum:int = obj["cycleNum"]
      pass

class ValidateCycleNumber_output:
   def __init__(self, obj):
      pass

class ValidateMonth_input:
   """ Required : 
   warehouse
   year
   month
   """  
   def __init__(self, obj):
      self.warehouse:str = obj["warehouse"]
      self.year:int = obj["year"]
      self.month:int = obj["month"]
      pass

class ValidateMonth_output:
   def __init__(self, obj):
      pass

class ValidateVoidPartNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

class ValidateVoidPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warnmsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateWarehouse_input:
   """ Required : 
   warehouseCode
   """  
   def __init__(self, obj):
      self.warehouseCode:str = obj["warehouseCode"]
      pass

class ValidateWarehouse_output:
   def __init__(self, obj):
      pass

class ValidateYear_input:
   """ Required : 
   warehouse
   year
   """  
   def __init__(self, obj):
      self.warehouse:str = obj["warehouse"]
      self.year:int = obj["year"]
      pass

class ValidateYear_output:
   def __init__(self, obj):
      pass

class VoidBlankTags_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCTagTableset] = obj["ds"]
      pass

class VoidBlankTags_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCTagTableset] = obj["ds"]
      self.vTextMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class VoidTagsByPCID_input:
   """ Required : 
   voidConfirmed
   ds
   """  
   def __init__(self, obj):
      self.voidConfirmed:bool = obj["voidConfirmed"]
      """  flag to confirm if user received warning and wants to continue on second pass  """  
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

class VoidTagsByPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warnmsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VoidTagsByPart_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

class VoidTagsByPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCCountCycleTableset] = obj["ds"]
      pass

      """  output parameters  """  

