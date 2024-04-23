import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CustShipSvc
# Description: Customer Shipment Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CustShips(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CustShips items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustShips
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips",headers=creds) as resp:
           return await resp.json()

async def post_CustShips(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustShips
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CustShips_Company_PackNum(Company, PackNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustShip item
   Description: Calls GetByID to retrieve the CustShip item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustShip
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CustShips_Company_PackNum(Company, PackNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CustShip for the service
   Description: Calls UpdateExt to update CustShip. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustShip
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CustShips_Company_PackNum(Company, PackNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CustShip item
   Description: Call UpdateExt to delete CustShip item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustShip
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustShips_Company_PackNum_CartonTrkDtls(Company, PackNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CartonTrkDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CartonTrkDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CartonTrkDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/CartonTrkDtls",headers=creds) as resp:
           return await resp.json()

async def get_CustShips_Company_PackNum_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company, PackNum, ShipmentType, CaseNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CartonTrkDtl item
   Description: Calls GetByID to retrieve the CartonTrkDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CartonTrkDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param ShipmentType: Desc: ShipmentType   Required: True   Allow empty value : True
      :param CaseNum: Desc: CaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustShips_Company_PackNum_ShipDtls(Company, PackNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ShipDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipDtls",headers=creds) as resp:
           return await resp.json()

async def get_CustShips_Company_PackNum_ShipDtls_Company_PackNum_PackLine(Company, PackNum, PackLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipDtl item
   Description: Calls GetByID to retrieve the ShipDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustShips_Company_PackNum_ShipHeadInsurances(Company, PackNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ShipHeadInsurances items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipHeadInsurances1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipHeadInsuranceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipHeadInsurances",headers=creds) as resp:
           return await resp.json()

async def get_CustShips_Company_PackNum_ShipHeadInsurances_Company_PackNum_InsuranceSeq(Company, PackNum, InsuranceSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipHeadInsurance item
   Description: Calls GetByID to retrieve the ShipHeadInsurance item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipHeadInsurance1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param InsuranceSeq: Desc: InsuranceSeq   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipHeadInsuranceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipHeadInsurances(" + Company + "," + PackNum + "," + InsuranceSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustShips_Company_PackNum_ShipMiscs(Company, PackNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ShipMiscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipMiscs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipMiscs",headers=creds) as resp:
           return await resp.json()

async def get_CustShips_Company_PackNum_ShipMiscs_Company_PackNum_PackLine_SeqNum_SysRowID(Company, PackNum, PackLine, SeqNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipMisc item
   Description: Calls GetByID to retrieve the ShipMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipMisc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipMiscs(" + Company + "," + PackNum + "," + PackLine + "," + SeqNum + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustShips_Company_PackNum_ReplicatedPacks(Company, PackNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ReplicatedPacks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ReplicatedPacks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReplicatedPacksRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ReplicatedPacks",headers=creds) as resp:
           return await resp.json()

async def get_CustShips_Company_PackNum_ReplicatedPacks_SysRowID(Company, PackNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReplicatedPack item
   Description: Calls GetByID to retrieve the ReplicatedPack item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReplicatedPack1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ReplicatedPacksRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ReplicatedPacks(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustShips_Company_PackNum_ShipHeadTrailers(Company, PackNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ShipHeadTrailers items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipHeadTrailers1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipHeadTrailerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipHeadTrailers",headers=creds) as resp:
           return await resp.json()

async def get_CustShips_Company_PackNum_ShipHeadTrailers_Company_PackNum_LicensePlate(Company, PackNum, LicensePlate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipHeadTrailer item
   Description: Calls GetByID to retrieve the ShipHeadTrailer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipHeadTrailer1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param LicensePlate: Desc: LicensePlate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipHeadTrailerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipHeadTrailers(" + Company + "," + PackNum + "," + LicensePlate + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustShips_Company_PackNum_ShipUPS(Company, PackNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ShipUPS items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipUPS1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipUPSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipUPS",headers=creds) as resp:
           return await resp.json()

async def get_CustShips_Company_PackNum_ShipUPS_Company_PackNum_UPSQVSeq(Company, PackNum, UPSQVSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipUP item
   Description: Calls GetByID to retrieve the ShipUP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipUP1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipUPSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustShips_Company_PackNum_ShipHeadAttches(Company, PackNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ShipHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipHeadAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipHeadAttches",headers=creds) as resp:
           return await resp.json()

async def get_CustShips_Company_PackNum_ShipHeadAttches_Company_PackNum_DrawingSeq(Company, PackNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipHeadAttch item
   Description: Calls GetByID to retrieve the ShipHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipHeadAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipHeadAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CartonTrkDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CartonTrkDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CartonTrkDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CartonTrkDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CartonTrkDtls",headers=creds) as resp:
           return await resp.json()

async def post_CartonTrkDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CartonTrkDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CartonTrkDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company, ShipmentType, PackNum, CaseNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CartonTrkDtl item
   Description: Calls GetByID to retrieve the CartonTrkDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CartonTrkDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipmentType: Desc: ShipmentType   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param CaseNum: Desc: CaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company, ShipmentType, PackNum, CaseNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CartonTrkDtl for the service
   Description: Calls UpdateExt to update CartonTrkDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CartonTrkDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipmentType: Desc: ShipmentType   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param CaseNum: Desc: CaseNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company, ShipmentType, PackNum, CaseNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CartonTrkDtl item
   Description: Call UpdateExt to delete CartonTrkDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CartonTrkDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipmentType: Desc: ShipmentType   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param CaseNum: Desc: CaseNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipDtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls",headers=creds) as resp:
           return await resp.json()

async def post_ShipDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipDtls_Company_PackNum_PackLine(Company, PackNum, PackLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipDtl item
   Description: Calls GetByID to retrieve the ShipDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipDtls_Company_PackNum_PackLine(Company, PackNum, PackLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipDtl for the service
   Description: Calls UpdateExt to update ShipDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipDtls_Company_PackNum_PackLine(Company, PackNum, PackLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipDtl item
   Description: Call UpdateExt to delete ShipDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipDtls_Company_PackNum_PackLine_ShipCOOs(Company, PackNum, PackLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ShipCOOs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipCOOs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipCOORow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipCOOs",headers=creds) as resp:
           return await resp.json()

async def get_ShipDtls_Company_PackNum_PackLine_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company, PackNum, PackLine, RelatedToFile, OrigCountry, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipCOO item
   Description: Calls GetByID to retrieve the ShipCOO item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipCOO1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param OrigCountry: Desc: OrigCountry   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipCOORow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipDtls_Company_PackNum_PackLine_ShipDtlPackagings(Company, PackNum, PackLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ShipDtlPackagings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipDtlPackagings1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlPackagingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipDtlPackagings",headers=creds) as resp:
           return await resp.json()

async def get_ShipDtls_Company_PackNum_PackLine_ShipDtlPackagings_Company_PackNum_PackLine(Company, PackNum, PackLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipDtlPackaging item
   Description: Calls GetByID to retrieve the ShipDtlPackaging item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipDtlPackaging1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipDtlPackagingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipDtlPackagings(" + Company + "," + PackNum + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipDtls_Company_PackNum_PackLine_ShipDtlTaxes(Company, PackNum, PackLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ShipDtlTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipDtlTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipDtlTaxes",headers=creds) as resp:
           return await resp.json()

async def get_ShipDtls_Company_PackNum_PackLine_ShipDtlTaxes_Company_PackNum_PackLine_TaxCode_RateCode_ECAcquisitionSeq(Company, PackNum, PackLine, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipDtlTax item
   Description: Calls GetByID to retrieve the ShipDtlTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipDtlTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipDtlTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipDtlTaxes(" + Company + "," + PackNum + "," + PackLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipDtls_Company_PackNum_PackLine_ShipDtlAttches(Company, PackNum, PackLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ShipDtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipDtlAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipDtlAttches",headers=creds) as resp:
           return await resp.json()

async def get_ShipDtls_Company_PackNum_PackLine_ShipDtlAttches_Company_PackNum_PackLine_DrawingSeq(Company, PackNum, PackLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipDtlAttch item
   Description: Calls GetByID to retrieve the ShipDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipDtlAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipDtlAttches(" + Company + "," + PackNum + "," + PackLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipCOOs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipCOOs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipCOOs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipCOORow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipCOOs",headers=creds) as resp:
           return await resp.json()

async def post_ShipCOOs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipCOOs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipCOORow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipCOORow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipCOOs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company, RelatedToFile, PackNum, PackLine, OrigCountry, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipCOO item
   Description: Calls GetByID to retrieve the ShipCOO item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipCOO
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param OrigCountry: Desc: OrigCountry   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipCOORow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company, RelatedToFile, PackNum, PackLine, OrigCountry, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipCOO for the service
   Description: Calls UpdateExt to update ShipCOO. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipCOO
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param OrigCountry: Desc: OrigCountry   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipCOORow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company, RelatedToFile, PackNum, PackLine, OrigCountry, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipCOO item
   Description: Call UpdateExt to delete ShipCOO item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipCOO
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param OrigCountry: Desc: OrigCountry   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipDtlPackagings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipDtlPackagings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipDtlPackagings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlPackagingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlPackagings",headers=creds) as resp:
           return await resp.json()

async def post_ShipDtlPackagings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipDtlPackagings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipDtlPackagingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipDtlPackagingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlPackagings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipDtlPackagings_Company_PackNum_PackLine(Company, PackNum, PackLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipDtlPackaging item
   Description: Calls GetByID to retrieve the ShipDtlPackaging item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipDtlPackaging
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipDtlPackagingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlPackagings(" + Company + "," + PackNum + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipDtlPackagings_Company_PackNum_PackLine(Company, PackNum, PackLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipDtlPackaging for the service
   Description: Calls UpdateExt to update ShipDtlPackaging. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipDtlPackaging
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipDtlPackagingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlPackagings(" + Company + "," + PackNum + "," + PackLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipDtlPackagings_Company_PackNum_PackLine(Company, PackNum, PackLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipDtlPackaging item
   Description: Call UpdateExt to delete ShipDtlPackaging item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipDtlPackaging
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlPackagings(" + Company + "," + PackNum + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipDtlTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipDtlTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipDtlTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlTaxes",headers=creds) as resp:
           return await resp.json()

async def post_ShipDtlTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipDtlTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipDtlTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipDtlTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipDtlTaxes_Company_PackNum_PackLine_TaxCode_RateCode_ECAcquisitionSeq(Company, PackNum, PackLine, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipDtlTax item
   Description: Calls GetByID to retrieve the ShipDtlTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipDtlTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipDtlTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlTaxes(" + Company + "," + PackNum + "," + PackLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipDtlTaxes_Company_PackNum_PackLine_TaxCode_RateCode_ECAcquisitionSeq(Company, PackNum, PackLine, TaxCode, RateCode, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipDtlTax for the service
   Description: Calls UpdateExt to update ShipDtlTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipDtlTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipDtlTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlTaxes(" + Company + "," + PackNum + "," + PackLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipDtlTaxes_Company_PackNum_PackLine_TaxCode_RateCode_ECAcquisitionSeq(Company, PackNum, PackLine, TaxCode, RateCode, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipDtlTax item
   Description: Call UpdateExt to delete ShipDtlTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipDtlTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlTaxes(" + Company + "," + PackNum + "," + PackLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipDtlAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipDtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipDtlAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlAttches",headers=creds) as resp:
           return await resp.json()

async def post_ShipDtlAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipDtlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipDtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipDtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipDtlAttches_Company_PackNum_PackLine_DrawingSeq(Company, PackNum, PackLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipDtlAttch item
   Description: Calls GetByID to retrieve the ShipDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlAttches(" + Company + "," + PackNum + "," + PackLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipDtlAttches_Company_PackNum_PackLine_DrawingSeq(Company, PackNum, PackLine, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipDtlAttch for the service
   Description: Calls UpdateExt to update ShipDtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipDtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlAttches(" + Company + "," + PackNum + "," + PackLine + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipDtlAttches_Company_PackNum_PackLine_DrawingSeq(Company, PackNum, PackLine, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipDtlAttch item
   Description: Call UpdateExt to delete ShipDtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlAttches(" + Company + "," + PackNum + "," + PackLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipHeadInsurances(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipHeadInsurances items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipHeadInsurances
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipHeadInsuranceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadInsurances",headers=creds) as resp:
           return await resp.json()

async def post_ShipHeadInsurances(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipHeadInsurances
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipHeadInsuranceRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipHeadInsuranceRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadInsurances", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipHeadInsurances_Company_PackNum_InsuranceSeq(Company, PackNum, InsuranceSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipHeadInsurance item
   Description: Calls GetByID to retrieve the ShipHeadInsurance item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipHeadInsurance
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param InsuranceSeq: Desc: InsuranceSeq   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipHeadInsuranceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadInsurances(" + Company + "," + PackNum + "," + InsuranceSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipHeadInsurances_Company_PackNum_InsuranceSeq(Company, PackNum, InsuranceSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipHeadInsurance for the service
   Description: Calls UpdateExt to update ShipHeadInsurance. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipHeadInsurance
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param InsuranceSeq: Desc: InsuranceSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipHeadInsuranceRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadInsurances(" + Company + "," + PackNum + "," + InsuranceSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipHeadInsurances_Company_PackNum_InsuranceSeq(Company, PackNum, InsuranceSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipHeadInsurance item
   Description: Call UpdateExt to delete ShipHeadInsurance item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipHeadInsurance
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param InsuranceSeq: Desc: InsuranceSeq   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadInsurances(" + Company + "," + PackNum + "," + InsuranceSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipMiscs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipMiscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipMiscs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipMiscs",headers=creds) as resp:
           return await resp.json()

async def post_ShipMiscs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipMiscs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipMiscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipMiscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipMiscs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipMiscs_Company_PackNum_PackLine_SeqNum_SysRowID(Company, PackNum, PackLine, SeqNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipMisc item
   Description: Calls GetByID to retrieve the ShipMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipMiscs(" + Company + "," + PackNum + "," + PackLine + "," + SeqNum + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipMiscs_Company_PackNum_PackLine_SeqNum_SysRowID(Company, PackNum, PackLine, SeqNum, SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipMisc for the service
   Description: Calls UpdateExt to update ShipMisc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipMiscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipMiscs(" + Company + "," + PackNum + "," + PackLine + "," + SeqNum + "," + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipMiscs_Company_PackNum_PackLine_SeqNum_SysRowID(Company, PackNum, PackLine, SeqNum, SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipMisc item
   Description: Call UpdateExt to delete ShipMisc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipMiscs(" + Company + "," + PackNum + "," + PackLine + "," + SeqNum + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ReplicatedPacks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ReplicatedPacks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReplicatedPacks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReplicatedPacksRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ReplicatedPacks",headers=creds) as resp:
           return await resp.json()

async def post_ReplicatedPacks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReplicatedPacks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ReplicatedPacksRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ReplicatedPacksRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ReplicatedPacks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ReplicatedPacks_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReplicatedPack item
   Description: Calls GetByID to retrieve the ReplicatedPack item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReplicatedPack
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ReplicatedPacksRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ReplicatedPacks(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ReplicatedPacks_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ReplicatedPack for the service
   Description: Calls UpdateExt to update ReplicatedPack. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReplicatedPack
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ReplicatedPacksRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ReplicatedPacks(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ReplicatedPacks_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ReplicatedPack item
   Description: Call UpdateExt to delete ReplicatedPack item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReplicatedPack
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ReplicatedPacks(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipHeadTrailers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipHeadTrailers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipHeadTrailers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipHeadTrailerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadTrailers",headers=creds) as resp:
           return await resp.json()

async def post_ShipHeadTrailers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipHeadTrailers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipHeadTrailerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipHeadTrailerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadTrailers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipHeadTrailers_Company_PackNum_LicensePlate(Company, PackNum, LicensePlate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipHeadTrailer item
   Description: Calls GetByID to retrieve the ShipHeadTrailer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipHeadTrailer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param LicensePlate: Desc: LicensePlate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipHeadTrailerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadTrailers(" + Company + "," + PackNum + "," + LicensePlate + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipHeadTrailers_Company_PackNum_LicensePlate(Company, PackNum, LicensePlate, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipHeadTrailer for the service
   Description: Calls UpdateExt to update ShipHeadTrailer. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipHeadTrailer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param LicensePlate: Desc: LicensePlate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipHeadTrailerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadTrailers(" + Company + "," + PackNum + "," + LicensePlate + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipHeadTrailers_Company_PackNum_LicensePlate(Company, PackNum, LicensePlate, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipHeadTrailer item
   Description: Call UpdateExt to delete ShipHeadTrailer item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipHeadTrailer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param LicensePlate: Desc: LicensePlate   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadTrailers(" + Company + "," + PackNum + "," + LicensePlate + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipUPS(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipUPS items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipUPS
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipUPSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipUPS",headers=creds) as resp:
           return await resp.json()

async def post_ShipUPS(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipUPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipUPSRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipUPSRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipUPS", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipUPS_Company_PackNum_UPSQVSeq(Company, PackNum, UPSQVSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipUP item
   Description: Calls GetByID to retrieve the ShipUP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipUP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipUPSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipUPS_Company_PackNum_UPSQVSeq(Company, PackNum, UPSQVSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipUP for the service
   Description: Calls UpdateExt to update ShipUP. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipUP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipUPSRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipUPS_Company_PackNum_UPSQVSeq(Company, PackNum, UPSQVSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipUP item
   Description: Call UpdateExt to delete ShipUP item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipUP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipHeadAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipHeadAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadAttches",headers=creds) as resp:
           return await resp.json()

async def post_ShipHeadAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipHeadAttches_Company_PackNum_DrawingSeq(Company, PackNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipHeadAttch item
   Description: Calls GetByID to retrieve the ShipHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipHeadAttches_Company_PackNum_DrawingSeq(Company, PackNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipHeadAttch for the service
   Description: Calls UpdateExt to update ShipHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipHeadAttches_Company_PackNum_DrawingSeq(Company, PackNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipHeadAttch item
   Description: Call UpdateExt to delete ShipHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumberGenerates(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumberGenerates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumberGenerates
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumberGenerateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumberGenerates",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumberGenerates(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumberGenerates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumberGenerateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumberGenerateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumberGenerates", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumberGenerates_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumberGenerate item
   Description: Calls GetByID to retrieve the LegalNumberGenerate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumberGenerate
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumberGenerateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumberGenerates(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumberGenerates_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumberGenerate for the service
   Description: Calls UpdateExt to update LegalNumberGenerate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumberGenerate
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumberGenerateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumberGenerates(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumberGenerates_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumberGenerate item
   Description: Call UpdateExt to delete LegalNumberGenerate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumberGenerate
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumberGenerates(" + SysRowID + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumGenOpts",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesKitCompIssues(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SalesKitCompIssues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SalesKitCompIssues
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesKitCompIssueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SalesKitCompIssues",headers=creds) as resp:
           return await resp.json()

async def post_SalesKitCompIssues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SalesKitCompIssues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SalesKitCompIssueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SalesKitCompIssueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SalesKitCompIssues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SalesKitCompIssues_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SalesKitCompIssue item
   Description: Calls GetByID to retrieve the SalesKitCompIssue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesKitCompIssue
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesKitCompIssueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SalesKitCompIssues(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SalesKitCompIssues_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SalesKitCompIssue for the service
   Description: Calls UpdateExt to update SalesKitCompIssue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SalesKitCompIssue
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SalesKitCompIssueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SalesKitCompIssues(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SalesKitCompIssues_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SalesKitCompIssue item
   Description: Call UpdateExt to delete SalesKitCompIssue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SalesKitCompIssue
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SalesKitCompIssues(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SelectedIDNumbers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SelectedIDNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SelectedIDNumbers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedIDNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedIDNumbers",headers=creds) as resp:
           return await resp.json()

async def post_SelectedIDNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SelectedIDNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SelectedIDNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SelectedIDNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedIDNumbers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SelectedIDNumbers_Company_PackNum_PackLine_SeqNum(Company, PackNum, PackLine, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SelectedIDNumber item
   Description: Calls GetByID to retrieve the SelectedIDNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SelectedIDNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SelectedIDNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedIDNumbers(" + Company + "," + PackNum + "," + PackLine + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SelectedIDNumbers_Company_PackNum_PackLine_SeqNum(Company, PackNum, PackLine, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SelectedIDNumber for the service
   Description: Calls UpdateExt to update SelectedIDNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SelectedIDNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SelectedIDNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedIDNumbers(" + Company + "," + PackNum + "," + PackLine + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SelectedIDNumbers_Company_PackNum_PackLine_SeqNum(Company, PackNum, PackLine, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SelectedIDNumber item
   Description: Call UpdateExt to delete SelectedIDNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SelectedIDNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedIDNumbers(" + Company + "," + PackNum + "," + PackLine + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SelectedSerialNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SelectedSerialNumbers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedSerialNumbers",headers=creds) as resp:
           return await resp.json()

async def post_SelectedSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedSerialNumbers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SelectedSerialNumber item
   Description: Calls GetByID to retrieve the SelectedSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SelectedSerialNumber for the service
   Description: Calls UpdateExt to update SelectedSerialNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SelectedSerialNumber item
   Description: Call UpdateExt to delete SelectedSerialNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipTaxSums(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipTaxSums items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipTaxSums
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipTaxSumRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipTaxSums",headers=creds) as resp:
           return await resp.json()

async def post_ShipTaxSums(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipTaxSums
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipTaxSumRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipTaxSumRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipTaxSums", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipTaxSums_Company_PackNum_PackLIne_TaxCode_RateCode(Company, PackNum, PackLIne, TaxCode, RateCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipTaxSum item
   Description: Calls GetByID to retrieve the ShipTaxSum item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipTaxSum
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLIne: Desc: PackLIne   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipTaxSumRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipTaxSums(" + Company + "," + PackNum + "," + PackLIne + "," + TaxCode + "," + RateCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipTaxSums_Company_PackNum_PackLIne_TaxCode_RateCode(Company, PackNum, PackLIne, TaxCode, RateCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipTaxSum for the service
   Description: Calls UpdateExt to update ShipTaxSum. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipTaxSum
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLIne: Desc: PackLIne   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipTaxSumRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipTaxSums(" + Company + "," + PackNum + "," + PackLIne + "," + TaxCode + "," + RateCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipTaxSums_Company_PackNum_PackLIne_TaxCode_RateCode(Company, PackNum, PackLIne, TaxCode, RateCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipTaxSum item
   Description: Call UpdateExt to delete ShipTaxSum item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipTaxSum
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLIne: Desc: PackLIne   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipTaxSums(" + Company + "," + PackNum + "," + PackLIne + "," + TaxCode + "," + RateCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_SNFormats(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SNFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SNFormats
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SNFormats",headers=creds) as resp:
           return await resp.json()

async def post_SNFormats(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SNFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SNFormats", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SNFormat item
   Description: Calls GetByID to retrieve the SNFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SNFormat for the service
   Description: Calls UpdateExt to update SNFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SNFormat item
   Description: Call UpdateExt to delete SNFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SNFormat
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseShipHead, whereClauseShipHeadAttch, whereClauseCartonTrkDtl, whereClauseShipDtl, whereClauseShipDtlAttch, whereClauseShipCOO, whereClauseShipDtlPackaging, whereClauseShipDtlTax, whereClauseShipHeadInsurance, whereClauseShipMisc, whereClauseReplicatedPacks, whereClauseShipHeadTrailer, whereClauseShipUPS, whereClauseLegalNumberGenerate, whereClauseLegalNumGenOpts, whereClauseSalesKitCompIssue, whereClauseSelectedIDNumbers, whereClauseSelectedSerialNumbers, whereClauseShipTaxSum, whereClauseSNFormat, pageSize, absolutePage, epicorHeaders = None):
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseShipHead=" + whereClauseShipHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseShipHeadAttch=" + whereClauseShipHeadAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCartonTrkDtl=" + whereClauseCartonTrkDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseShipDtl=" + whereClauseShipDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseShipDtlAttch=" + whereClauseShipDtlAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseShipCOO=" + whereClauseShipCOO
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseShipDtlPackaging=" + whereClauseShipDtlPackaging
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseShipDtlTax=" + whereClauseShipDtlTax
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseShipHeadInsurance=" + whereClauseShipHeadInsurance
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseShipMisc=" + whereClauseShipMisc
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseReplicatedPacks=" + whereClauseReplicatedPacks
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseShipHeadTrailer=" + whereClauseShipHeadTrailer
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseShipUPS=" + whereClauseShipUPS
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLegalNumberGenerate=" + whereClauseLegalNumberGenerate
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
   params += "whereClauseSalesKitCompIssue=" + whereClauseSalesKitCompIssue
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSelectedIDNumbers=" + whereClauseSelectedIDNumbers
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSelectedSerialNumbers=" + whereClauseSelectedSerialNumbers
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseShipTaxSum=" + whereClauseShipTaxSum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSNFormat=" + whereClauseSNFormat
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(packNum, epicorHeaders = None):
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
   params += "packNum=" + packNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckAttributeSetsOnShipDtlLines(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckAttributeSetsOnShipDtlLines
   Description: Purpose:     validate shipDtl lines for valid attribute sets
Notes:
<param name="iPackNum">current packNum</param><param name="markAsShipped">mark as shipped true or false</param><param name="cErrorMsg">any errors returned to user</param>
   OperationID: CheckAttributeSetsOnShipDtlLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAttributeSetsOnShipDtlLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAttributeSetsOnShipDtlLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StageWarning(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StageWarning
   Description: Purpose:
Parameters:  none
Notes:
<param name="iPackNum">Serial number to validate.</param><param name="ipShipmentType">shipment type</param><param name="iWarning">Serial Number Voided flag</param>
   OperationID: StageWarning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StageWarning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StageWarning_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UndoShipAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UndoShipAll
   Description: This method re-sets all the temp-table records shipped (Undo Ship all button selected)
   OperationID: UndoShipAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UndoShipAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UndoShipAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateManifestChargeAmts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateManifestChargeAmts
   Description: Purpose:  Calculate the CODAmount and DeclaredAmt
<param name="ipAmountType">COD or DeclaredAmt</param><param name="ipAction">Yes = recalculate No = reset to zero</param><param name="ds">Customer Shipment data set </param>
Notes:  Update the COD Amount and/or Declared Insurance amounts for manifesting purposes.
   OperationID: UpdateManifestChargeAmts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateManifestChargeAmts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateManifestChargeAmts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateMaster(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateMaster
   Description: <param name="ds"></param>
<param name="doValidateCreditHold">If true run validate credit hold logic</param>
<param name="doCheckShipDtl">If true run checkShipDtl logic</param>
<param name="doLotValidation">If true run lot validation logic</param>
<param name="doCheckOrderComplete">If true run Check Order Complete logic</param>
<param name="doPostUpdate">If true perform post update logic</param>
<param name="doCheckCompliance">If true perform check compliance logic</param>
<param name="ipShippedFlagChanged">If true then refresh data for ReadyToInvoice changed</param>
<param name="ipPackNum">PackNum being updated</param>
<param name="ipBTCustNum">Bill to customer number for credit hold validation</param>
<param name="opReleaseMessage">If the Order release is closed, this asks if the user wants to continue</param>
<param name="opCompleteMessage">If the order complete status has changed, this would alert the user to any problems (yes/no)</param>
<param name="opShippingMessage">Alerts to any potential shipping error </param>
<param name="opLotMessage">If the lot doesn't exist, ask the user if they'd like to create it </param>
<param name="opInventoryMessage">If the inventory will go negative, ask user if they want to continue </param>
<param name="opLockQtyMessage">If the OrderDtl.LockQty=true and release 1 is being set to ship complete, ask user if they want to continue </param>
<param name="opAllocationMessage">If this transaction overrides a allocation, ask user if they want to continue </param>
<param name="opPartListNeedsAttr">List of parts that require lot attributes entered</param>
<param name="opLotListNeedsAttr">List of lots related to opPartListNeedsAttr that require lot attributes entered</param>
<param name="shipCreditMsg">possible output message from validateCreditHoldCore</param>
<param name="cError">Will be true if a hard error is encountered in validateCreditHoldCore</param>
<param name="compError">Will be true if a hard error is encountered in checkOrderCompleteCore</param>
<param name="msg">possible output message from checkOrderCompleteCore</param>
<param name="opPostUpdMessage">possible output message from postUpdateCore or checkOrderCore</param>
<param name="updateComplete">Indicates that the Update process did run</param>
<param name="checkComplianceError">Indicates whether the check compliance logic encountered non-compliance lines</param>
<param name="changeStatusError">Indicates whether the change status logic encountered errors</param>
<param name="checkShipDtlAgain">Whether to check ShipDtl records for errors</param>
   OperationID: UpdateMaster
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdatePackCODWithCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePackCODWithCarton
   Description: Purpose: Update pack COD amounts
<param name="ipPackNum">Pack Number to process</param><param name="ipCaseNum">Case Number to set value to zero</param><param name="ipOldCOD">Previous COD</param><param name="ipCOD">Current Case COD</param><param name="ipFlag">Current COD flag value</param><param name="ds">Customer Shipment data set</param>
Notes:
   OperationID: UpdatePackCODWithCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePackCODWithCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePackCODWithCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdatePackDeclaredWithCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePackDeclaredWithCarton
   Description: Purpose:  Update Pack Delcared Value Amounts
<param name="ipPackNum">Pack Number to process</param><param name="ipCaseNum">Case Number to set value to zero </param><param name="ipOldDeclared">Previous COD</param><param name="ipDeclared">Current Case COD</param><param name="ipDeclaredFlag">current setting of declared insurance</param><param name="ds">Customer Shipment data set</param>
Notes:
   OperationID: UpdatePackDeclaredWithCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePackDeclaredWithCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePackDeclaredWithCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdatePackWeightWithCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePackWeightWithCarton
   Description: Purpose:Update the Pack Weight with the carton weight
<param name="ipPackNum">Pack Number to process</param><param name="ipOldWeight">Previous weight</param><param name="ipWeight">Current Case weight</param><param name="ds">Customer Shipment data set</param>
Notes:
   OperationID: UpdatePackWeightWithCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePackWeightWithCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePackWeightWithCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateBinCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateBinCode
   Description: Purpose: Validate the bin.
<param name="ipWhse">Warehouse code used to edit bin</param><param name="ipBinNum">Bin Code to validate</param>
Notes:
   OperationID: ValidateBinCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBinCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBinCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePackNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePackNum
   Description: Purpose:  Validate PCID VOid Pack List
Parameters:  none
Notes:
<param name="ipPackNum">Packing Slip Number </param><param name="_success">Error flag.</param>
   OperationID: ValidatePackNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePackNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePackNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCreditHold(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCreditHold
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipValPackNum">Packing Slip Number </param><param name="ipValBTCustNum">Bill To Customer Number.</param><param name="opCreditMessage">Credit Message.</param><param name="opcError">Error flag.</param>
   OperationID: ValidateCreditHold
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCreditHold_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCreditHold_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCreditHoldPO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCreditHoldPO
   Description: Purpose:
Notes:
<param name="ipOrderNum">Order Number </param><param name="ipPackNum">Pack Number</param><param name="opCreditMessage">Credit Message.</param><param name="opAgingMessage">aging message</param>
   OperationID: ValidateCreditHoldPO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCreditHoldPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCreditHoldPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCreditHoldSSC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCreditHoldSSC
   Description: Purpose:     THIS IS CALLED FROM STAGE SHIP CONFIRM UI
Parameters:  none
Notes:
<param name="ipPackNum">Packing Slip Number </param><param name="ipShipmentType">Shipment Type </param><param name="opCreditMessage">Credit Message.</param><param name="opcError">Error flag.</param>
   OperationID: ValidateCreditHoldSSC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCreditHoldSSC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCreditHoldSSC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateKitPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateKitPart
   Description: This method will validate the kit part when changing lines in the Sales Kit
Component Issue grid
   OperationID: ValidateKitPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateKitPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateKitPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateLocationIDNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateLocationIDNumbers
   Description: Purpose:  Validate if the Location IDNum already exist for the Part.
Parameters:  none
Notes:
<param name="IDNumList">ID Number List </param><param name="ipPartNum">Part Number </param><param name="ipIDNumProposed">ID Number Proposed </param><param name="ipPackNum">PackNum</param><param name="ipPackLine">PackLine</param>
   OperationID: ValidateLocationIDNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateLocationIDNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateLocationIDNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSN
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipSerialNum">Serial number to validate.</param><param name="ipPartNum">Part number</param><param name="ipAttributeSetID">Attribute Set</param><param name="ipJobNum">Job number</param><param name="ipOurJobshipQty">Job Ship Quantity</param><param name="ipOurInvShipQty">Inventory Ship Quantity</param><param name="ipOrderNum">Order number</param><param name="ipOrderLine">Order Line number</param><param name="ipOrderRelNum">OrderRelease number</param><param name="ipShipFromWIP">Flag to indicate shipping from WIP</param><param name="ipWarehouseCode">Ship from warehouse</param><param name="ipBinNum">Ship from bin</param><param name="isVoided">Serial Number Voided flag</param>
   OperationID: ValidateSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidLegalNumber
   Description: Voids the legal number.
   OperationID: VoidLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_NegativeInventoryTest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method NegativeInventoryTest
   Description: NegativeInventoryTest
   OperationID: NegativeInventoryTest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NegativeInventoryTest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NegativeInventoryTest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPCBinOutLocation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPCBinOutLocation
   Description: Validate the shipment from location does not belong to a Planning Contract
   OperationID: CheckPCBinOutLocation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPCBinOutLocation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPCBinOutLocation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPackageCodeAllocNegQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPackageCodeAllocNegQty
   OperationID: CheckPackageCodeAllocNegQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackageCodeAllocNegQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackageCodeAllocNegQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPkgCodeQtyList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPkgCodeQtyList
   OperationID: GetPkgCodeQtyList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPkgCodeQtyList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPkgCodeQtyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessNegQtyTest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessNegQtyTest
   Description: This was created for Kinetic UI
   OperationID: ProcessNegQtyTest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessNegQtyTest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessNegQtyTest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateDigitalSignature(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateDigitalSignature
   Description: Generate Digital Signature
   OperationID: GenerateDigitalSignature
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateDigitalSignature_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateDigitalSignature_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePCIDPackVerify(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePCIDPackVerify
   Description: Overload to ChangePCID, will Check for every line of the Pack if it requires if it is compliant, or return a flag if the PCID was already scanned.
And Calculates the number of PCIDs with qty in a pack and/or the item part number for a given PCID if the ChangePCID logic is successful
   OperationID: ChangePCIDPackVerify
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCIDPackVerify_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCIDPackVerify_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PackVerifyCalcPackPCIDCount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PackVerifyCalcPackPCIDCount
   Description: Calculates the number of PCIDs with qty in a pack
   OperationID: PackVerifyCalcPackPCIDCount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PackVerifyCalcPackPCIDCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PackVerifyCalcPackPCIDCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PackVerifyPerformPackVerification(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PackVerifyPerformPackVerification
   Description: For the pack verify UI form: performs the pack verification to indicate if the verification is complete
   OperationID: PackVerifyPerformPackVerification
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PackVerifyPerformPackVerification_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PackVerifyPerformPackVerification_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingDispNumberOfPieces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingDispNumberOfPieces
   Description: Logic for when the number of pieces is changing
   OperationID: OnChangingDispNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingDispNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingDispNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingRevisionNumPackOut(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingRevisionNumPackOut
   OperationID: OnChangingRevisionNumPackOut
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNumPackOut_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNumPackOut_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPackTaxID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPackTaxID
   Description: Customer Tax Id check
   OperationID: CheckPackTaxID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPackTaxIDForPackNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPackTaxIDForPackNum
   Description: Customer Tax Id check for a given pack number
   OperationID: CheckPackTaxIDForPackNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackTaxIDForPackNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackTaxIDForPackNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetShippedFromPackout(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetShippedFromPackout
   Description: Updates shipped status on customer shipment when set from Pack out
   OperationID: SetShippedFromPackout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetShippedFromPackout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetShippedFromPackout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipHeadAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCartonTrkDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCartonTrkDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCartonTrkDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCartonTrkDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCartonTrkDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipDtlAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipDtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipDtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipCOO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipCOO
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipCOO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipCOO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipCOO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipDtlTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipDtlTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipDtlTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipDtlTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipDtlTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipHeadInsurance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipHeadInsurance
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipHeadInsurance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipHeadInsurance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipHeadInsurance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipMisc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipMisc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipMisc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipMisc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipMisc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipHeadTrailer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipHeadTrailer
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipHeadTrailer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipHeadTrailer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipHeadTrailer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipUPS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipUPS
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipUPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipUPS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipUPS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExpireDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExpireDate
   OperationID: ExpireDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExpireDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExpireDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CallsCreateCustomerCartons(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CallsCreateCustomerCartons
   Description: Purpose:  Create Phantom Customer Cartons
Parameters:
<param name="ipPackNum">Current packNum</param><param name="ipNbrCartonsToCreate">Number of cartons or cases to create</param><param name="ipPkgCode">Package Code to use when creating cartons</param><param name="ipPkgLength">length to use when creating cartons</param><param name="ipPkgWidth">Width to use when creating cartons</param><param name="ipPkgHeight">Height to use when creating cartons</param><param name="ipRecalcAmts">Logical indicating if the amounts are to be recalculated</param><param name="ipZeroWeight">Logical indicating if the weights are recalculated</param><param name="ds"></param>
Notes:  Called from Kinetic so first need to dirty rows
   OperationID: CallsCreateCustomerCartons
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CallsCreateCustomerCartons_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CallsCreateCustomerCartons_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateCustomerCartons(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateCustomerCartons
   Description: Purpose:  Create Phantom Customer Cartons
Parameters:
<param name="ipNbrCartonsToCreate">Number of cartons or cases to create</param><param name="ipPkgCode">Package Code to use when creating cartons</param><param name="ipPkgLength">length to use when creating cartons</param><param name="ipPkgWidth">Width to use when creating cartons</param><param name="ipPkgHeight">Height to use when creating cartons</param><param name="ipRecalcAmts">Logical indicating if the amounts are to be recalculated</param><param name="ipZeroWeight">Logical indicating if the weights are recalculated</param><param name="ds"></param>
Notes:
   OperationID: CreateCustomerCartons
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateCustomerCartons_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateCustomerCartons_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AllowUndoExternalDN(epicorHeaders = None):
   """  
   Summary: Invoke method AllowUndoExternalDN
   Description: This method exists soley for the purpose of allowing security for
unchecking the external delivery note flag to be defined
   OperationID: AllowUndoExternalDN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllowUndoExternalDN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_AskForShipToChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AskForShipToChange
   Description: Checks if user must be asked for take a different Shipping Information
   OperationID: AskForShipToChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AskForShipToChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AskForShipToChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the customer shipment.
   OperationID: AssignLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPackageControlPackVoid(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPackageControlPackVoid
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipPackNum">ipPackNum</param>
   OperationID: GetPackageControlPackVoid
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackageControlPackVoid_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackageControlPackVoid_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidPackSlip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidPackSlip
   Description: Purpose:
Parameters:  none
Notes:
<param name="packNum">Pack Num</param><param name="ds">Package Control pack Void data set</param>
   OperationID: VoidPackSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidPackSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidPackSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildCompSerMatch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildCompSerMatch
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipPartNum">ipPartNum</param><param name="ipRevNum">ipRevNum</param><param name="ipSerialNumbers">ipSerialNumbers</param>
   OperationID: BuildCompSerMatch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildCompSerMatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildCompSerMatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildSerialMatchingParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildSerialMatchingParams
   Description: This method fills the SerialMatchingParams Dataset with information
   OperationID: BuildSerialMatchingParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildSerialMatchingParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildSerialMatchingParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildShipToCustomerList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildShipToCustomerList
   Description: If the Order has releases to multiple Customers, this will return the list of available
Customer shiptos to select from
   OperationID: BuildShipToCustomerList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildShipToCustomerList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildShipToCustomerList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildShipToList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildShipToList
   Description: If the Order has releases to multiple shipto's, this will return the list of available
shiptos to select from
   OperationID: BuildShipToList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildShipToList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildShipToList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalculateWeight(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateWeight
   Description: Purpose:  calculate the weight of a carton based upon Part.Weight.
<param name="cartonNumber">PackID </param><param name="calculatedWeight">calculated weight</param>
   OperationID: CalculateWeight
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CancelVoid(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CancelVoid
   Description: This method clears the void flag on the Pack Slip
   OperationID: CancelVoid
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelVoid_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelVoid_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CanStage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CanStage
   Description: This method check that a shipment can be staged
   OperationID: CanStage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CanStage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CanStage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CartonValidateWeight(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CartonValidateWeight
   Description: Purpose:
<param name="ipWeight"> weight to validate</param>
Notes:
   OperationID: CartonValidateWeight
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CartonValidateWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CartonValidateWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeIncotermCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeIncotermCode
   Description: This method checks incoterm
   OperationID: ChangeIncotermCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeIncotermCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeIncotermCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeShipCmpl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeShipCmpl
   Description: This method performs validations when the ShipDtl.ShipCmpl field changes
   OperationID: ChangeShipCmpl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipCmpl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipCmpl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeShipDtlMFCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeShipDtlMFCustID
   Description: Method to call when changing the Mark For Customer ID on the ShipDtl record.
Validates the Mark For Customer ID and ressets the ShipToNum to the Customer default.
   OperationID: ChangeShipDtlMFCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipDtlMFCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipDtlMFCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeShipDtlMFShipToNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeShipDtlMFShipToNum
   Description: Update ShipDtl information with values from the Mark For when the Mark For is changed.
   OperationID: ChangeShipDtlMFShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipDtlMFShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipDtlMFShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeShipDtlUseOTMF(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeShipDtlUseOTMF
   Description: Method to call when changing the UseOTMF field the ShipDtl record.
Refreshes the address list and contact info
   OperationID: ChangeShipDtlUseOTMF
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipDtlUseOTMF_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipDtlUseOTMF_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeShipHeadShipToCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeShipHeadShipToCustID
   Description: Executed when ShipToCustID has changed in the Ship Header
   OperationID: ChangeShipHeadShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipHeadShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipHeadShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeShipMiscPrcnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeShipMiscPrcnt
   Description: This method populates the miscellaneous amount fields after
a miscellaneous charge percentage has been changed
   OperationID: ChangeShipMiscPrcnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipMiscPrcnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipMiscPrcnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeShipMiscAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeShipMiscAmount
   Description: This method populates the miscellaneous amount fields after
a miscellaneous charge amount has been changed, if doc amount is changed a new non-doc amount is calculated, and vice versa
DspMiscAmt is the base currency amount column, DocMiscAmt is the ShipHead currency amount column.
"DocDspMiscAmt" column is not  because there is no "InDocMiscAmt" column, the DocMiscAmt is simply the currency equivalent of
DspMiscAmt which in turn is either the MiscAmt or InMiscAmt value depending on the InPrice setting
   OperationID: ChangeShipMiscAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipMiscAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipMiscAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeStatus
   Description: This method will be called to perform a change in the header status.
   OperationID: ChangeStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePCID
   Description: NOTE - Customer Shipment Entry and HHPackOutEnty are now calling ChangePCIDPackVerify rather than ChangePCID
in order to give more functionality of 'Removing' a PCID when entered more than once.
Check for every line of the Pack if it requires if it is compliant.
   OperationID: ChangePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeWarrantyToFSA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeWarrantyToFSA
   Description: This method will update the value of the warrantySendToFSA field, if the warranty is sync with the FSA Integration.
   OperationID: ChangeWarrantyToFSA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeWarrantyToFSA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeWarrantyToFSA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemovePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemovePCID
   Description: Back out pack detail lines related to a PCID
   OperationID: RemovePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemovePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemovePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCompliance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCompliance
   Description: Check for every line of the Pack if it requires if it is compliant.
   OperationID: CheckCompliance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCompliance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCompliance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCOOPercents(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCOOPercents
   Description: Checks to see if the Qty percent and value percent fields total 100 percent.
   OperationID: CheckCOOPercents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCOOPercents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCOOPercents_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCNCustomsDeclarationBillLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCNCustomsDeclarationBillLine
   Description: Purpose:  Check Declaration Bill Line
Parameters:
<param name="bBeforeUpdate">if True - method is called before updating</param><param name="sMessage">Warning</param><param name="ds"></param>
   OperationID: CheckCNCustomsDeclarationBillLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCNCustomsDeclarationBillLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCNCustomsDeclarationBillLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckOrder
   Description: This method check releases related with this pack were refused to close because non shipped pack existing.
   OperationID: CheckOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckOrderComplete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckOrderComplete
   Description: This method is to be run before update Shipped flag (true) to check if order or line of the pack needs
to be shipped complete, and ask the user if he wants to continue. If the user answers no, then the update method should not be called.
   OperationID: CheckOrderComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOrderComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOrderComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPrePartInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPrePartInfo
   OperationID: CheckPrePartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPrePartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPrePartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckReadyToInvoice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckReadyToInvoice
   OperationID: CheckReadyToInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckReadyToInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckReadyToInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckShipDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckShipDtl
   OperationID: CheckShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckValidCartonWeight(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckValidCartonWeight
   Description: Purpose: Ensure the carton weight is valid.
<param name="ipPackNum">Pack Num to validate weights</param>
Notes:
   OperationID: CheckValidCartonWeight
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckValidCartonWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckValidCartonWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearConvertedManifestUOMFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearConvertedManifestUOMFields
   Description: Purpose: Clear ShipHead Manifest fields when Unfreighting.
<param name="ipPackNum">Pack Num to clear Manifest fields</param>
Notes:
   OperationID: ClearConvertedManifestUOMFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearConvertedManifestUOMFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearConvertedManifestUOMFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConvertToManifestUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConvertToManifestUOM
   Description: Purpose: Populate ShipHead Manifest fields.
<param name="ipPackNum">Pack Num to populate Manifest fields</param>
Notes:
   OperationID: ConvertToManifestUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertToManifestUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertToManifestUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConvertUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConvertUOM
   Description: This method converts a qty from one UOM to another
   OperationID: ConvertUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateLot(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateLot
   Description: Necessary method to create New Lot numbers for parts without attributes during the process of creating a pack.
   OperationID: CreateLot
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateLot_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateLot_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateMassShipDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateMassShipDtl
   Description: This method copies the available Order Release lines to the ShipDtl datatable
for update
   OperationID: CreateMassShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateMassShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMassShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeletePhantomPacks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeletePhantomPacks
   Description: Purpose:
<param name="ds">Customer Shipment data set </param>
Notes:
   OperationID: DeletePhantomPacks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeletePhantomPacks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeletePhantomPacks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteRangePhantomPacks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteRangePhantomPacks
   Description: Purpose:
<param name="ipFromCase">First case number to start deletes</param><param name="ipToCase">Last case number to delete</param><param name="ds">Customer Shipment data set </param>
Notes:
   OperationID: DeleteRangePhantomPacks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRangePhantomPacks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRangePhantomPacks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExpressShip(epicorHeaders = None):
   """  
   Summary: Invoke method ExpressShip
   Description: This method checks if the shipment is able to ship.
   OperationID: ExpressShip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExpressShip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetCartonPackaging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCartonPackaging
   Description: Purpose: Obtain the carton pacakcing specs
<param name="ipPkgCode">package code</param><param name="opPkgHeight">package height</param><param name="opPkgWidth">package width</param><param name="opPkgLength">package length</param>
Notes:
   OperationID: GetCartonPackaging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCartonPackaging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCartonPackaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCustShipOrdTrk(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustShipOrdTrk
   Description: Get Customer Shipments for the Order.
   OperationID: GetCustShipOrdTrk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustShipOrdTrk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustShipOrdTrk_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetHeadOrderInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetHeadOrderInfo
   Description: This method displays the customer/address information when the OrderNum field
in the header changes. Should only be called for new Customer Shipments, or
Customer Shipments w/o lines
   OperationID: GetHeadOrderInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHeadOrderInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHeadOrderInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEnablePackageControl(epicorHeaders = None):
   """  
   Summary: Invoke method GetEnablePackageControl
   OperationID: GetEnablePackageControl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEnablePackageControl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDisablePackOut(epicorHeaders = None):
   """  
   Summary: Invoke method GetDisablePackOut
   Description: Get value of DisablePackOut from Plant Configuration.
   OperationID: GetDisablePackOut
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDisablePackOut_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetJobDtlInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetJobDtlInfo
   Description: This method defaults the ShipDtl fields with the JobNum field changes
   OperationID: GetJobDtlInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobDtlInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobDtlInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetJobInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetJobInfo
   Description: This method populates the Order and Address fields after the JobNum field has been populated
   OperationID: GetJobInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetJobSupOpSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetJobSupOpSeq
   Description: This method Gets the Job Suboperations Sequence Numbers to retrive the Serial Numbers Selected for the PartNum
   OperationID: GetJobSupOpSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobSupOpSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobSupOpSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POGetLegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POGetLegalNumGenOpts
   Description: Returns the legal number generation options.
   OperationID: POGetLegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POGetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POGetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AfterChangedShipDtlOrderNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AfterChangedShipDtlOrderNum
   Description: Purpose:
<param name="ipSalesOrder">Sales Order</param><param name="ipPackNum">Pack Number</param><param name="ds">Customer Shipment data set</param>
Notes:  Default manifest information from the sales order. Used from Kinetic UI.
   OperationID: AfterChangedShipDtlOrderNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AfterChangedShipDtlOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AfterChangedShipDtlOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetManifestInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetManifestInfo
   Description: Purpose:
<param name="ipSalesOrder">Sales Order</param><param name="ipPackNum">Pack Number</param><param name="ds">Customer Shipment data set</param>
Notes:  Default manifest information from the sales order.
   OperationID: GetManifestInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetManifestInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetManifestInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewOrdrShipDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewOrdrShipDtl
   Description: Creates a new ShipDtl record, but defaulting the order number (if provided) as well
as other data from the OrderHed record.
   OperationID: GetNewOrdrShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOrdrShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOrdrShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewOrdrShipUPS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewOrdrShipUPS
   Description: Creates a new ShipUS record,
   OperationID: GetNewOrdrShipUPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOrdrShipUPS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOrdrShipUPS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOrderInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOrderInfo
   Description: This method displays the customer/address information when the OrderNum field changes
Should only be called for new Customer Shipments, or Customer Shipments w/o lines
   OperationID: GetOrderInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOrderInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOrderLineInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOrderLineInfo
   Description: This method defaults the ShipDtl fields with the OrderLine fields
change
   OperationID: GetOrderLineInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOrderLineInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderLineInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOrderRelInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOrderRelInfo
   Description: This method defaults the ShipDtl fields with the OrderRel fields
change
   OperationID: GetOrderRelInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOrderRelInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderRelInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPackaging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPackaging
   Description: Purpose:
<param name="ipPkgCode">package code</param><param name="ds">Customer Shipment data set </param>
Notes:
   OperationID: GetPackaging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackaging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPackClass(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPackClass
   Description: Purpose:
<param name="ipPkgClass">package class</param><param name="ds">Customer Shipment data set </param>
Notes:
   OperationID: GetPackClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPackOutPartXRef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPackOutPartXRef
   Description: This method defaults PackOut fields when the PartNum field changes
   OperationID: GetPackOutPartXRef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackOutPartXRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackOutPartXRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PartNumChangeUserPrompts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PartNumChangeUserPrompts
   Description: This method is called before GetPartInfo to determine if the user wants to continue based on questionString prompt
   OperationID: PartNumChangeUserPrompts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartNumChangeUserPrompts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartNumChangeUserPrompts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartInfo
   Description: This method defaults ShipDtl fields when the PartNum field changes
   OperationID: GetPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPayBTFlagDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPayBTFlagDefaults
   Description: Purpose:
<param name="ipOrderNum">First sales order on shipment</param><param name="ipPayFlag"> Pay Flag to retrieve defaults</param><param name="ds">The customer shipment data set </param>
Notes:
   OperationID: GetPayBTFlagDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPayBTFlagDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPayBTFlagDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPOPackaging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPOPackaging
   Description: Purpose:
<param name="ipPkgCode">package code</param><param name="ds">Customer PackOut data set </param>
Notes:
   OperationID: GetPOPackaging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPOPackaging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOPackaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPOPackClass(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPOPackClass
   Description: Purpose:
<param name="ipPkgClass">package class</param><param name="ds">Packout data set </param>
Notes:
   OperationID: GetPOPackClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPOPackClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOPackClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQtyInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQtyInfo
   Description: This method defaults the ShipDtl Netweight and Quantity fields when the
ShipDtl.DisplayInvQty or ShipDtl.OurJobShipQty fields change
   OperationID: GetQtyInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQtyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQtyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsContactTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsContactTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Head/Dtl fields for the contact tracker.
   OperationID: GetRowsContactTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustomerTrackerAndSort(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomerTrackerAndSort
   Description: Calls the normal GetRows method and then constructs a custom data set combining Job and Order fields for the customer tracker.
   OperationID: GetRowsCustomerTrackerAndSort
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTrackerAndSort_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTrackerAndSort_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustomerTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomerTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Head/Dtl fields for the customer tracker.
   OperationID: GetRowsCustomerTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForCashReceipt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForCashReceipt
   Description: Invokes GetRows filtering on shipments for the specified Cash Receipt
   OperationID: GetRowsForCashReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForCashReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForCashReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForInvoice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForInvoice
   Description: Invokes GetRows filtering on shipments for the specified Invoice
   OperationID: GetRowsForInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForQuote(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForQuote
   Description: Invokes GetRows filtering on shipments for the specified Quote
   OperationID: GetRowsForQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetScale(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetScale
   Description: Calls GetDefaultScale
   OperationID: GetScale
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetScale_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetScale_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectIDNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectIDNumbersParams
   Description: Returns specific data needed to continue with selecting ID Numbers
   OperationID: GetSelectIDNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectIDNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectIDNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipPartNum">ipPartNum</param><param name="ipAttributeSetID">ipAttributeSetID</param><param name="ipQuantity">ipQuantity</param><param name="ipUOM">ipUOM</param><param name="ipPackNum">ipPackNum</param><param name="ipPackLine">ipPackLine</param><param name="ipTranType">ipTranType</param><param name="ipJobNum">ipJobNum</param><param name="ipWhseCode">ipWhseCode</param><param name="ipBinNum">ipBinNum</param><param name="ipLotNum">ipLotNum</param><param name="ipFromPO">ipFromPO</param><param name="ipOrderNum">ipOrderNum</param><param name="ipOrderLine">ipOrderLine</param><param name="ipOrderRelNum">ipOrderRelNum</param><param name="ipSysRowID">ipSysRowID</param><returns></returns>
   OperationID: GetSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetShipmentRelationshipMap(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetShipmentRelationshipMap
   Description: Returns a serialized json string to show a Relationship Map for Shipment
   OperationID: GetShipmentRelationshipMap
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipmentRelationshipMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipmentRelationshipMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateSelectIDNumParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateSelectIDNumParams
   Description: Purpose: Generate Select ID Number Parameters related to Location Management.
Parameters:  none
Notes:
<param name="SNList">Serial Number List </param><param name="ipPartNum">PartNum</param><param name="ipPackNum">PackNum</param><param name="ipPackLine">PackLine</param><param name="ipJobNum">JobNum</param><param name="ipUom">UOM</param><param name="ipFromMfg">Called from Mfg</param>
   OperationID: GenerateSelectIDNumParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateSelectIDNumParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateSelectIDNumParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateLocationIDNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateLocationIDNum
   Description: This method will be used to create records in LocationIDNum table
   OperationID: GenerateLocationIDNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateLocationIDNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateLocationIDNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetShipMiscDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetShipMiscDefaults
   Description: This method populates the Description and miscellaneous amount fields after
a miscellaneous charge code has been selected
   OperationID: GetShipMiscDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipMiscDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipMiscDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetShipToAddr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetShipToAddr
   Description: This method displays the shipto address information when the ShipToNum field changes
Should only be called on new Shipments or if the Shipment has no lines and if
the MultipleShippers flag is yes
   OperationID: GetShipToAddr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipToAddr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipToAddr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTranDocTypeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTranDocTypeID
   Description: Sets default values when the TranDocTypeID changes
   OperationID: GetTranDocTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalculateWarrantyExpiration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateWarrantyExpiration
   Description: Calculates the expiration date fields based on effective date to the specified line/rel
   OperationID: CalculateWarrantyExpiration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateWarrantyExpiration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateWarrantyExpiration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetWarrantyInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWarrantyInfo
   Description: set warranty info to ship detail fields related to warranty
   OperationID: GetWarrantyInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWarrantyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWarrantyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearWarrantyInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearWarrantyInfo
   Description: clears warranty fields on the specified orderLine/orderrelnum
   OperationID: ClearWarrantyInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearWarrantyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearWarrantyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetWhseInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWhseInfo
   Description: This method defaults the ShipDtl Warehouse and bin fields when the warehousecode changes
   OperationID: GetWhseInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWhseInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWhseInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HHCreateMassShipDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HHCreateMassShipDtl
   Description: This method copies the available Order Release lines to the ShipDtl datatable
for update
   OperationID: HHCreateMassShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HHCreateMassShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HHCreateMassShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HHGetOrderInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HHGetOrderInfo
   Description: This method sets the defaults quantities and Primary Bins fields as CreateMassShipment complements
This method is used for HandHelds Version
   OperationID: HHGetOrderInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HHGetOrderInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HHGetOrderInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HHSetDtlDefaultValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HHSetDtlDefaultValues
   Description: OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE
Use MarkShipmentLines instead (the same logic that is used by the regular screen)
OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE
This method sets the defaults quantities and Primary Bins fields as CreateMassShipment complements
This method is used for HandHelds Version
   OperationID: HHSetDtlDefaultValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HHSetDtlDefaultValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HHSetDtlDefaultValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MarkShipmentLines(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MarkShipmentLines
   Description: This method sets all the temp-table records to be shipped (Ship all button selected)
   OperationID: MarkShipmentLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MarkShipmentLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MarkShipmentLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PhantomStatusCheck(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PhantomStatusCheck
   Description: Purpose :Check the phantom status
<param name="ipPackNum">pack number to check status</param>
Notes:
   OperationID: PhantomStatusCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PhantomStatusCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PhantomStatusCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POChangeStage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POChangeStage
   Description: This method will be called to perform a change in the pack stage.
   OperationID: POChangeStage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POChangeStage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POChangeStage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POChangeStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POChangeStatus
   Description: This method will be called to perform a change in the header status from the pack Out
screen.
   OperationID: POChangeStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POChangeStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POChangeStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POFindBuffer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POFindBuffer
   Description: This method returns a count order of lines that match the incomming scanned criteria.
If there is only 1 match, it will copy the order dtl data into the returning record.
If there is no unique match, logical fields are updated to que the UI as to what need
to be prompted in order to find a matching order dtl.
   OperationID: POFindBuffer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POFindBuffer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POFindBuffer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POFindBufWhseBinLot(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POFindBufWhseBinLot
   Description: The purpose of this method is to return a unique PackOut.PackLine number if the
warehouse or bin or lot changes.  If it finds the match of an available shipdtl
then it will return the rowident of the matching shipdtl. IF not the line number
of the PackOut is incremented.
   OperationID: POFindBufWhseBinLot
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POFindBufWhseBinLot_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POFindBufWhseBinLot_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POGetDtlList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POGetDtlList
   Description: This method copies the available Order Release lines to the PackOut datatable for update
from HHVerifyForm (advanced PCID): ipPackMode = blank, ipOrderNum = 0, PCID = blank
   OperationID: POGetDtlList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POGetDtlList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POGetDtlList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POGetNew(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POGetNew
   Description: This method creates a new packout record for the customer shipment packout
screen. can pass in a OrderNum or PackNum or Both.
   OperationID: POGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreatePackForChangePCID(epicorHeaders = None):
   """  
   Summary: Invoke method CreatePackForChangePCID
   Description: This method executes GetNewShipHead and saves to the db and returns the new PackNum to support the entry
of a PCID in packout entry when the pack has not yet been created. Not called by Classic UIApp
   OperationID: CreatePackForChangePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePackForChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_POGetNewWithDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POGetNewWithDtl
   Description: Return a tableset populated with PackOut header and detail list.
   OperationID: POGetNewWithDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POGetNewWithDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POGetNewWithDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteKitComponents(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteKitComponents
   Description: Delete the kit components when the line/release is changed
   OperationID: DeleteKitComponents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteKitComponents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteKitComponents_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateOrderRelOnKitChildren(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateOrderRelOnKitChildren
   Description: Update the kit components with new release number
   OperationID: UpdateOrderRelOnKitChildren
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateOrderRelOnKitChildren_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateOrderRelOnKitChildren_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POGetShipTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POGetShipTo
   Description: This method sets the ttPackOut ShipTo name/address display fields
screen
   OperationID: POGetShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POGetShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POGetShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PostUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PostUpdate
   Description: This method will return a message if a credit card shipment was processed
during update or there are warning messages regarding outbound lower level serial tracking
   OperationID: PostUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POUpdate
   Description: This method creates a new packout record to create Shiphead and shipdtl records
   OperationID: POUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POUpdateAndDisplay(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POUpdateAndDisplay
   Description: This method creates a new packout record to create Shiphead and shipdtl records
   OperationID: POUpdateAndDisplay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POUpdateAndDisplay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POUpdateAndDisplay_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POValidateOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POValidateOrder
   Description: This method sets the service contract invoiced flag to match the shiphead flag
   OperationID: POValidateOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POValidateOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POValidateOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POValidateOrderRel(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POValidateOrderRel
   Description: Purpose: Verify the newly entered order rel is for the same bill to and shipto
Parameters:
<param name="ipPackNum">pack number</param><param name="ipOrderNum">sales order number</param><param name="ipOrderLine">sales order line number</param><param name="ipOrderRelNum">sales order release number</param>
Notes:
   OperationID: POValidateOrderRel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POValidateOrderRel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POValidateOrderRel_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POValidatePart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POValidatePart
   Description: Validates whether the provided part is valid or not for a given sales order.
   OperationID: POValidatePart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POValidatePart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POValidatePart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreCreateMassShipDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreCreateMassShipDtl
   Description: This method checks to see if it's okay to copy the available Order Release lines
to the ShipDtl datatable for update in Mass Shipments
   OperationID: PreCreateMassShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreCreateMassShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreCreateMassShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePickeOrdersIsSelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePickeOrdersIsSelected
   Description: This method executes the picked order view OnChanging logic for PickedOrders.IsSelected for the CustShip Kinetic UI / Picked Orders form
WinForm does all of this within the UIApps MaintTransaction IsSelected OnChanging method. This method executes the logic for
ProcessKitChildren plus the logic to select/deselect any related PickedOrders rows in the ds per the logic in UIapps
   OperationID: OnChangePickeOrdersIsSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePickeOrdersIsSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePickeOrdersIsSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessKitChildern(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessKitChildern
   Description: This method checks if UI should process the components of the kit parent
   OperationID: ProcessKitChildern
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessKitChildern_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessKitChildern_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePickedOrders(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePickedOrders
   Description: This method is run right before PickedOrders.  If not all of the line details have
been picked to ship a question will be returned to the user.  If yes, then
call PickedOrders, if no allow the user to pick another order
   OperationID: PrePickedOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePickedOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePickedOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrintSlip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrintSlip
   Description: This method prints the Customer Packing Slip
   OperationID: PrintSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrintSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrintSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessMassShipKit(epicorHeaders = None):
   """  
   Summary: Invoke method ProcessMassShipKit
   Description: Purpose:
Parameters:  none
Notes:
   OperationID: ProcessMassShipKit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessMassShipKit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ProcessPickedOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessPickedOrder
   Description: This method creates the packing slip for the selected picked order (desktop)
Will only process picked orders marked as selected.
   OperationID: ProcessPickedOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessPickedOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessPickedOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessPickedOrderHH(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessPickedOrderHH
   Description: This method creates the packing slip for the selected picked order (handheld)
Will also process other releases for the same order
   OperationID: ProcessPickedOrderHH
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessPickedOrderHH_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessPickedOrderHH_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RebuildShipUPS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RebuildShipUPS
   Description: Purpose: Rebuild the shipUPS records
<param name="ipPackNum">Packnum to update</param><param name="ds">The customer shipment data set </param>
   OperationID: RebuildShipUPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RebuildShipUPS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RebuildShipUPS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetUPSQVEnable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetUPSQVEnable
   Description: Purpose:
<param name="ipQVEnable">logical indicating if the quantum view is to enabled/disabled</param><param name="ds">The customer shipment data set </param>
Notes:
   OperationID: SetUPSQVEnable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUPSQVEnable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUPSQVEnable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeUPSQuantumView(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeUPSQuantumView
   Description: Purpose:
<param name="ipPackNum">current packNum</param><param name="ipQVEnable">logical indicating if the quantum view is to enabled/disabled</param><param name="ds">The customer shipment data set </param>
Notes:  This was created for Kinetic UI
   OperationID: OnChangeUPSQuantumView
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUPSQuantumView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUPSQuantumView_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeShipViaCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeShipViaCode
   Description: Function to set default values related to ShipVia
   OperationID: OnChangeShipViaCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeShipViaCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShipViaCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetUPSQVShipStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetUPSQVShipStatus
   Description: Purpose:
<param name="ipShipStatus">Shipment status</param><param name="ds">The customer shipment data set </param>
Notes:
   OperationID: SetUPSQVShipStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUPSQVShipStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUPSQVShipStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CartonTrkDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CartonTrkDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumberGenerateRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumberGenerateRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReplicatedPacksRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ReplicatedPacksRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SNFormatRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesKitCompIssueRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SalesKitCompIssueRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedIDNumbersRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SelectedIDNumbersRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipCOORow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipCOORow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipDtlAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlPackagingRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipDtlPackagingRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipDtlTaxRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipHeadAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadInsuranceRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipHeadInsuranceRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadTrailerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipHeadTrailerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipMiscRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipMiscRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipTaxSumRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipTaxSumRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipUPSRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipUPSRow] = obj["value"]
      pass

class Erp_Tablesets_CartonTrkDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company ID  """  
      self.ShipmentType:str = obj["ShipmentType"]
      """  Defines the type of shipment the tracking number is for.  Shipment type is either Misc for miscellaneous, Sales for Customer shipments, Sub for subcontractor shipments Transfer for Transfer order shipment or Master for Masterpack Shipments.  """  
      self.PackNum:int = obj["PackNum"]
      """  The pack number associated with the tracking number.  """  
      self.CaseNum:int = obj["CaseNum"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last CartonTrkDtl record for PackNum and add 1. This number is not displayed to the user.  The case number the user sees is the concatenation of the Packnum and this number separated by a dash.  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.PkgWeight:int = obj["PkgWeight"]
      """  Package Weight  """  
      self.CODFlag:bool = obj["CODFlag"]
      """  Prefer COD delivery.  Reserved for future development.  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery
Reserved for future development.  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order.  Reserved for future development.  """  
      self.DeclaredValueFlag:bool = obj["DeclaredValueFlag"]
      """  Flag to indicate that an insurance value was declared on delivery.  Reserved for future development.  """  
      self.DeclaredValue:int = obj["DeclaredValue"]
      """  Declared Insurance Amount.  Reserved for future development.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.CODValue:int = obj["CODValue"]
      """  Collect On Delivery Value  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CaseID:str = obj["CaseID"]
      """  Concatenated field consisting of PackNum and CaseNum separated by a dash.  """  
      self.PackStatus:str = obj["PackStatus"]
      """  Status of the shipment.  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  logical used by UI for row rules  """  
      self.CapturePt:str = obj["CapturePt"]
      self.EnablePhantom:bool = obj["EnablePhantom"]
      """  Logical indicating if the phantom cartonTrkDtl fields are to be enabled.  This is based upon whether or not the workstation is setup for manifesting.  """  
      self.KitPartAttrClassID:str = obj["KitPartAttrClassID"]
      self.BitFlag:int = obj["BitFlag"]
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

class Erp_Tablesets_LegalNumberGenerateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.NumberType:str = obj["NumberType"]
      self.NumberYear:int = obj["NumberYear"]
      self.NumberPrefix:str = obj["NumberPrefix"]
      """  The legal number prefix  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      self.PrefixList:str = obj["PrefixList"]
      self.GenerationType:str = obj["GenerationType"]
      self.EnableNumberPrefix:bool = obj["EnableNumberPrefix"]
      self.EnableNumberSuffix:bool = obj["EnableNumberSuffix"]
      self.NumberOption:str = obj["NumberOption"]
      self.LegalNumberNum:int = obj["LegalNumberNum"]
      """  Unique identifier of the Legal Number record  """  
      self.DocumentDate:str = obj["DocumentDate"]
      self.AdditionalParams:str = obj["AdditionalParams"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReplicatedPacksRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company ID  """  
      self.PackNum:int = obj["PackNum"]
      """  Parent Pack ID that is used to create the replicated packs.  """  
      self.ReplicatedPackNum:int = obj["ReplicatedPackNum"]
      """  This is the pack num that was generated based upon the parent pack num.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat1:str = obj["SNFormat1"]
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesKitCompIssueRow:
   def __init__(self, obj):
      self.KitPartNum:str = obj["KitPartNum"]
      self.KitDescription:str = obj["KitDescription"]
      self.KitWarehouseCodeDesc:str = obj["KitWarehouseCodeDesc"]
      self.KitWarehouse:str = obj["KitWarehouse"]
      self.KitWhseList:str = obj["KitWhseList"]
      self.PackNum:int = obj["PackNum"]
      self.PackLine:int = obj["PackLine"]
      self.KitQtyFromInv:int = obj["KitQtyFromInv"]
      self.KitIUM:str = obj["KitIUM"]
      self.KitLotNum:str = obj["KitLotNum"]
      self.KitBinNum:str = obj["KitBinNum"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.KitBinNumEnabled:bool = obj["KitBinNumEnabled"]
      self.KitTrackLots:bool = obj["KitTrackLots"]
      self.KitSerialTracked:bool = obj["KitSerialTracked"]
      self.KitQtyFromInvEnabled:bool = obj["KitQtyFromInvEnabled"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectedIDNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.IDNumber:str = obj["IDNumber"]
      self.JobNum:str = obj["JobNum"]
      self.PackLine:int = obj["PackLine"]
      self.PackNum:int = obj["PackNum"]
      self.PartNum:str = obj["PartNum"]
      self.SeqNum:int = obj["SeqNum"]
      self.SerialNumber:str = obj["SerialNumber"]
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this ID number  """  
      self.TransType:str = obj["TransType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipCOORow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.OrigCountry:int = obj["OrigCountry"]
      """  CountryNum for Country of Origin  """  
      self.QtyPerc:int = obj["QtyPerc"]
      """  Qty percent of this part which is from this country of origin.  """  
      self.ValuePerc:int = obj["ValuePerc"]
      """  Value percent of this part from this country of origin.  """  
      self.Primary:bool = obj["Primary"]
      """  Is this the primary country of origin for this part  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the country of origin is related. ?ShipDtl?, ?MscShpDt?, ?TFShipDtl?, and ?SubShipD?  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipDtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PackNum:int = obj["PackNum"]
      self.PackLine:int = obj["PackLine"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipDtlPackagingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PackNum:int = obj["PackNum"]
      self.PackLine:int = obj["PackLine"]
      self.ParentPkgNum:int = obj["ParentPkgNum"]
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeDesc:str = obj["TranDocTypeDesc"]
      self.PkgCode:str = obj["PkgCode"]
      self.PkgCodeDesc:str = obj["PkgCodeDesc"]
      self.PkgSerialNum:str = obj["PkgSerialNum"]
      self.PkgLength:int = obj["PkgLength"]
      self.PkgWidth:int = obj["PkgWidth"]
      self.PkgHeight:int = obj["PkgHeight"]
      self.SizeUOM:str = obj["SizeUOM"]
      self.Weight:int = obj["Weight"]
      self.WeightUOM:str = obj["WeightUOM"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.PartNum:str = obj["PartNum"]
      self.OurQty:int = obj["OurQty"]
      self.IUM:str = obj["IUM"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable, It is carried forward through from the ShipHead.OrderNum field.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this shipment detail line is linked to.  Must be valid in the OrderDtl file.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.OurInventoryShipQty:int = obj["OurInventoryShipQty"]
      """  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand.  This quantity is in the IUM unit of measure.  """  
      self.OurJobShipQty:int = obj["OurJobShipQty"]
      """  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This quantity is in the IUM unit of measure.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that supplied the quantity that was shipped. Defaulted from OrderRel.JobNum.  """  
      self.Packages:int = obj["Packages"]
      """  Number of Packages  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Description  """  
      self.IUM:str = obj["IUM"]
      """  Unit of measure...duplicated from the OrderDtl.IUM...Not user maintainable.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  """  
      self.ShipComment:str = obj["ShipComment"]
      """   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  """  
      self.ShipCmpl:bool = obj["ShipCmpl"]
      """  Indicates if this shipment should mark the order release as being shipped complete. Only one ShipDtl for a release can be marked as being complete. As the user toggles this field it also sets the OrderRel.ShipCmpl field and adjusts the PartBin.OnHand, PartWhse.AllocQty if necessary.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """   Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.

The default should be retrieved from the OrderDtl.WareHseCode. .  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.UpdatedInventory:bool = obj["UpdatedInventory"]
      """  Indicates if this transaction affected inventory at time of creation.  """  
      self.XPartNum:str = obj["XPartNum"]
      """   An optional field that is used if the customer has a different  Part number  than the users internal part number.
This field is defaulted from the OrderDtl.XPartNum.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the OrderDtl.XRevisionNum field.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table. This is duplicated from the OrderRel.ShpConNum.  """  
      self.TMBilling:bool = obj["TMBilling"]
      """  Indicates if this shipment line item will be invoiced for time and materials. This is not maintainable from within shipment entry. It is duplicated from the OrderDtl.TMBilling. The "Get Shipments" function of Invoice Entry uses this flag to automatically create invoices in a "On Hold" status. The idea is that these type of invoices need to be generated to act as a method of tracking invoice requirements, but they cannot yet be invoiced until all the costs are known. At which time the user will enter the appropriate charges, take it off "Hold" and complete the billing process.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  A flag which indicates "invoicing" status. This is a mirror image of ShipHead.Invoiced field. See ShipHead.Invoiced for further info.  """  
      self.WUM:str = obj["WUM"]
      """  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...). Defaulted from XASyst.DefaultWUM  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number is for Inventory Shipments.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  These comments will be copied into the Invoice detail.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the shipment is for.  Duplicated from ShipHead.CustNum.  Used to allow efficient browsing of the ShipDtl records for a specific customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The shipto number. Used for warranty validation.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  For Warranty shipments.  Defaults as Shiphead.shipdate. But can be maintained from the Service Call center.  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The # of days, months, years the material is covered by warranty  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The # of days, months, years the Labor is covered by warranty  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The # of days, months, years the Misc. Charges are covered by warranty  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Whether the duration of warranty  is for "Days", " Months", "years".  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Whether the duration of warranty  is "Days"," Months"," years".  """  
      self.MiscMod:str = obj["MiscMod"]
      """  Whether the duration of warranty  is for "Days"," Months"," years".  """  
      self.MaterialExpiration:str = obj["MaterialExpiration"]
      """  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.LaborExpiration:str = obj["LaborExpiration"]
      """  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.MiscExpiration:str = obj["MiscExpiration"]
      """  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.LastExpiration:str = obj["LastExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.Onsite:bool = obj["Onsite"]
      """  This warranty covers On site visits  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.Plant:str = obj["Plant"]
      """  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the Packing Slip is complete and ready for invoicing.  This is a mirror image of ShipHead.ReadyToInvoice.  """  
      self.SellingInventoryShipQty:int = obj["SellingInventoryShipQty"]
      """  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand. This quantity is a mirror of field OurInventoryShipQty except it is in the SUM unit of measure.  """  
      self.SellingJobShipQty:int = obj["SellingJobShipQty"]
      """  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This field is a mirror of OurJobShipQty except it is in the SUM unit of measure.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit of Measure...duplicated from the OrderDtl.SUM...Not user maintainable.  """  
      self.TotalNetWeight:int = obj["TotalNetWeight"]
      """  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  """  
      self.WIPWarehouseCode:str = obj["WIPWarehouseCode"]
      """   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  """  
      self.WIPBinNum:str = obj["WIPBinNum"]
      """   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.HeaderShipComment:str = obj["HeaderShipComment"]
      """  Packing slip comments.  These are comments off of the invoice header.  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  The packline of the kit parent  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.InventoryShipUOM:str = obj["InventoryShipUOM"]
      """  Unit of Measure of the quantity shipped from Inventory (OurInventoryShipQty). Must be a valid UOM. If Part is Multi-UOM tracking then only the Tracking UOMs are valid otherwise all UOM's of the Parts UOMClass are valid.  """  
      self.JobShipUOM:str = obj["JobShipUOM"]
      """  Unit of Measure of the quantity shipped from the Job (OurJobShipQty)  """  
      self.TrackSerialNum:bool = obj["TrackSerialNum"]
      """  Indicates whether the ShipDtl.PartNum is serial tracked. Required as a db field rather than using the link to PartNumTrackSerialNum to allow validations based on the ShipDtl table rather than the ttShipDtl table. Default is No.  """  
      self.JobLotNum:str = obj["JobLotNum"]
      """  Lot Number is for Job Shipments.  """  
      self.BinType:str = obj["BinType"]
      """  Identifies the type of Bin is being used (valid values are 'Std', 'Cust', 'Supp').  Associated with field ShipDtl.BinNum  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  Unit price discount percent.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item.  It can be zero.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.PickedAutoAllocatedQty:int = obj["PickedAutoAllocatedQty"]
      """  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Order.  This quantity is in the IUM unit of measure.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InDiscount:int = obj["InDiscount"]
      """  A flat discount amount for the line item includes taxes.  It can be zero.  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """  A flat discount amount for the line item includes taxes.  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reporting currency value of this field  """  
      self.InExtPrice:int = obj["InExtPrice"]
      """  Extended Price for the invoice line item including taxes.  """  
      self.DocInExtPrice:int = obj["DocInExtPrice"]
      """  Extended Price for the invoice line item including taxes.  """  
      self.Rpt1InExtPrice:int = obj["Rpt1InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtPrice:int = obj["Rpt2InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtPrice:int = obj["Rpt3InExtPrice"]
      """  Reporting currency value of this field  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """  Unit Price including taxes.  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Unit Price including taxes.  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.MFCustNum:int = obj["MFCustNum"]
      """  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  """  
      self.MFShipToNum:str = obj["MFShipToNum"]
      """  The ShipTo ID to be used for this record. This MUST BE VALID IN THE SHIPTO file.  """  
      self.UseOTMF:bool = obj["UseOTMF"]
      """  Indicates that the One Time Mark For information defined for this record should be used.  """  
      self.OTMFName:str = obj["OTMFName"]
      """  One Time Mark For Name of the ShipTo.  """  
      self.OTMFAddress1:str = obj["OTMFAddress1"]
      """  One Time Mark For first line of the ShipTo address.  """  
      self.OTMFAddress2:str = obj["OTMFAddress2"]
      """  One Time Mark For second line of the ShipTo address.  """  
      self.OTMFAddress3:str = obj["OTMFAddress3"]
      """  One Time Mark For third line of the ShipTo address.  """  
      self.OTMFCity:str = obj["OTMFCity"]
      """  City portion of the One Time Mark For address.  """  
      self.OTMFState:str = obj["OTMFState"]
      """  The state or province portion of the One Time Mark For address.  """  
      self.OTMFZIP:str = obj["OTMFZIP"]
      """  The zip or postal code portion of the One Time Mark For address.  """  
      self.OTMFContact:str = obj["OTMFContact"]
      """  One Time Mark For Contact Name  """  
      self.OTMFFaxNum:str = obj["OTMFFaxNum"]
      """  Fax number for the One Time Mark For.  """  
      self.OTMFPhoneNum:str = obj["OTMFPhoneNum"]
      """  Phone number for the One Time Mark For  """  
      self.OTMFCountryNum:int = obj["OTMFCountryNum"]
      """  Country number for the One Time Mark For  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.ShipOvers:bool = obj["ShipOvers"]
      """  ShipOvers  """  
      self.AllowedOvers:int = obj["AllowedOvers"]
      """  AllowedOvers  """  
      self.AllowedUnders:int = obj["AllowedUnders"]
      """  AllowedUnders  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NotAllocatedQty:int = obj["NotAllocatedQty"]
      """  This is the quantity being shipped that was not already previously allocated, and could not be auto allocated.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.PCIDItemSeq:int = obj["PCIDItemSeq"]
      """  PCID Item Sequence  """  
      self.DockingStation:str = obj["DockingStation"]
      """  The dockingstation of the shipto address.  For future use.  """  
      self.UseShipDtlInfo:bool = obj["UseShipDtlInfo"]
      """  For future use.  """  
      self.PkgCodePartNum:str = obj["PkgCodePartNum"]
      """  PkgCodePartNum  """  
      self.CustContainerPartNum:str = obj["CustContainerPartNum"]
      """  CustContainerPartNum  """  
      self.LabelType:str = obj["LabelType"]
      """  LabelType  """  
      self.WarrantySendToFSA:bool = obj["WarrantySendToFSA"]
      """  Indicates that the warranty will be sent to FSA  """  
      self.FSAEquipment:bool = obj["FSAEquipment"]
      """  When the shipment line is marked as "send as equipment", it will create an Installation in Epicor FSA.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.InventoryNumberOfPieces:int = obj["InventoryNumberOfPieces"]
      """  Number of pieces for this attribute set based on OurInventoryShipQty.  """  
      self.JobNumberOfPieces:int = obj["JobNumberOfPieces"]
      """  Number of pieces for this attribute set based on OurJobShipQty.  """  
      self.MXEstValue:int = obj["MXEstValue"]
      """  Estimated Value  """  
      self.MXEstValueCurrencyCode:str = obj["MXEstValueCurrencyCode"]
      """  Estimated Value Currency  """  
      self.MXHazardousShipment:bool = obj["MXHazardousShipment"]
      """  Hazardous Shipment  """  
      self.MXHazardousType:str = obj["MXHazardousType"]
      """  Hazardous Type  """  
      self.MXPackageType:str = obj["MXPackageType"]
      """  Package Type  """  
      self.CNDeclarationBillLine:int = obj["CNDeclarationBillLine"]
      """  CNDeclarationBillLine  """  
      self.JobNotAllocatedQty:int = obj["JobNotAllocatedQty"]
      """  This is the quantity being shipped from manufacturing that was not already previously allocated, and could not be auto allocated.  """  
      self.JobPickedAutoAllocatedQty:int = obj["JobPickedAutoAllocatedQty"]
      """  Quantity picked from manufacturing that was not manually allocated.  """  
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  Flag to indicate if Order/Line/Rel is Buy To Order  """  
      self.ChangeDateTime:str = obj["ChangeDateTime"]
      """  The date and time that the record was last changed  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DimCodeList:str = obj["DimCodeList"]
      """  Delimited list of available Dimension codes for line  """  
      self.DisplayInvQty:int = obj["DisplayInvQty"]
      """  OurInventoryShipQty * DimConvFactor - update inplace of OurInventoryShipQty  """  
      self.DocLineTax:int = obj["DocLineTax"]
      self.DropShip:bool = obj["DropShip"]
      """  Is Drop Shipment.  """  
      self.DtlError:bool = obj["DtlError"]
      """  Indicates if a detail line has errors to be corrected before leaving packing slip  """  
      self.EnableInvIDBtn:bool = obj["EnableInvIDBtn"]
      self.EnableInvSerialBtn:bool = obj["EnableInvSerialBtn"]
      self.EnableJobFields:bool = obj["EnableJobFields"]
      """  Logical indicating if receipt to a job is allowed.  This is determined by either the xasyst.shipnojob field or whether or not the sales order is linked to a job.  """  
      self.EnableKitIDBtn:bool = obj["EnableKitIDBtn"]
      self.EnableMfgIDBtn:bool = obj["EnableMfgIDBtn"]
      self.EnableMfgSerialBtn:bool = obj["EnableMfgSerialBtn"]
      self.EnableOBInvSerialBtn:bool = obj["EnableOBInvSerialBtn"]
      self.EnableOBMfgSerialBtn:bool = obj["EnableOBMfgSerialBtn"]
      self.EnablePackageControl:bool = obj["EnablePackageControl"]
      """  Boolean indicating if the package control functionality should be enabled.  """  
      self.EnablePOSerialBtn:bool = obj["EnablePOSerialBtn"]
      self.ExtJobNum:str = obj["ExtJobNum"]
      self.FSAInstallationCost:int = obj["FSAInstallationCost"]
      self.FSAInstallationOrderLine:int = obj["FSAInstallationOrderLine"]
      self.FSAInstallationOrderNum:int = obj["FSAInstallationOrderNum"]
      self.FSAInstallationRequired:bool = obj["FSAInstallationRequired"]
      """  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  """  
      self.FSAInstallationType:str = obj["FSAInstallationType"]
      self.GetLocIDNum:bool = obj["GetLocIDNum"]
      """  Equal to true if opening Location ID Diaglog  """  
      self.InvLegalNumber:str = obj["InvLegalNumber"]
      """  The invoice legal number.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  External field to be used in the SalesOrder Tracker to show the user the InvoiceNum linked to the shipment.  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      self.KitBinNum:str = obj["KitBinNum"]
      self.KitCompIssue:bool = obj["KitCompIssue"]
      self.KitCompShipComplete:bool = obj["KitCompShipComplete"]
      self.KitDescription:str = obj["KitDescription"]
      self.KitFlag:str = obj["KitFlag"]
      """  Sales Kit flag.  C = 'Component'  P = 'Parent'.  """  
      self.KitIUM:str = obj["KitIUM"]
      self.KitLotNum:str = obj["KitLotNum"]
      self.KitMassIssue:bool = obj["KitMassIssue"]
      self.KitParentIssue:bool = obj["KitParentIssue"]
      self.KitPartNum:str = obj["KitPartNum"]
      self.KitQtyFromInv:int = obj["KitQtyFromInv"]
      self.KitQtyFromInvEnabled:bool = obj["KitQtyFromInvEnabled"]
      self.KitSerialTracked:bool = obj["KitSerialTracked"]
      self.KitTrackLots:bool = obj["KitTrackLots"]
      self.KitWarehouse:str = obj["KitWarehouse"]
      self.KitWarehouseCodeDesc:str = obj["KitWarehouseCodeDesc"]
      self.KitWhseList:str = obj["KitWhseList"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.   This field comes directly from the table ShipHead.  """  
      self.LineContentValue:int = obj["LineContentValue"]
      """  Individual line content value that is used by the freight web service to calculate the total order value.  """  
      self.LineTax:int = obj["LineTax"]
      self.LinkMsg:str = obj["LinkMsg"]
      self.MarkForAddrList:str = obj["MarkForAddrList"]
      """  Contains the Mark For Address  """  
      self.MFCustID:str = obj["MFCustID"]
      self.OrderHold:bool = obj["OrderHold"]
      """  Indicates if Order is on Hold  """  
      self.OrderRelOurReqQty:int = obj["OrderRelOurReqQty"]
      self.OurJobShipIUM:str = obj["OurJobShipIUM"]
      self.OurJobShippedQty:int = obj["OurJobShippedQty"]
      self.OurRemainQty:int = obj["OurRemainQty"]
      self.OurRemainUM:str = obj["OurRemainUM"]
      self.OurReqQty:int = obj["OurReqQty"]
      self.OurReqUM:str = obj["OurReqUM"]
      self.OurShippedQty:int = obj["OurShippedQty"]
      self.OurShippedUM:str = obj["OurShippedUM"]
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      self.PackSlip:str = obj["PackSlip"]
      """  Packing slip for drop shipment.  """  
      self.PartAESExp:str = obj["PartAESExp"]
      """  Used by freight web service  """  
      self.PartCompany:str = obj["PartCompany"]
      self.PartECNNumber:str = obj["PartECNNumber"]
      """  Used by freight web service  """  
      self.PartExpLicNumber:str = obj["PartExpLicNumber"]
      """  Used by freight web service  """  
      self.PartExpLicType:str = obj["PartExpLicType"]
      """  Used by freight web service  """  
      self.PartHazClass:str = obj["PartHazClass"]
      """  Used by freight web service  """  
      self.PartHazGvrnmtID:str = obj["PartHazGvrnmtID"]
      """  Used by freight web service  """  
      self.PartHazItem:bool = obj["PartHazItem"]
      """  Used by freight web service  """  
      self.PartHazPackInstr:str = obj["PartHazPackInstr"]
      """  Used by freight web service  """  
      self.PartHazSub:str = obj["PartHazSub"]
      """  Used by freight web service  """  
      self.PartHazTechName:str = obj["PartHazTechName"]
      """  Used by freight web service  """  
      self.PartHTS:str = obj["PartHTS"]
      """  Used by freight web service  """  
      self.PartNAFTAOrigCountry:str = obj["PartNAFTAOrigCountry"]
      """  Used by freight web service  """  
      self.PartNAFTAPref:str = obj["PartNAFTAPref"]
      """  Used by freight web service  """  
      self.PartNAFTAProd:str = obj["PartNAFTAProd"]
      """  Used by freight web service  """  
      self.PartOrigCountry:str = obj["PartOrigCountry"]
      """  Used by freight web service  """  
      self.PartPartNum:str = obj["PartPartNum"]
      self.PartSchedBcode:str = obj["PartSchedBcode"]
      """  Used by freight web service  """  
      self.PartUseHTSDesc:bool = obj["PartUseHTSDesc"]
      """  Used by freight web service  """  
      self.PONum:str = obj["PONum"]
      self.ProjectID:str = obj["ProjectID"]
      """  Project of the related Order Line  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point ID.  """  
      self.RequestDate:str = obj["RequestDate"]
      self.Rpt1LineTax:int = obj["Rpt1LineTax"]
      self.Rpt2LineTax:int = obj["Rpt2LineTax"]
      self.Rpt3LineTax:int = obj["Rpt3LineTax"]
      self.SelectedLocationIDQty:int = obj["SelectedLocationIDQty"]
      self.SellingRemainQty:int = obj["SellingRemainQty"]
      self.SellingRemainUM:str = obj["SellingRemainUM"]
      self.SellingReqQty:int = obj["SellingReqQty"]
      self.SellingReqUM:str = obj["SellingReqUM"]
      self.SellingShipmentQty:int = obj["SellingShipmentQty"]
      self.SellingShipmentUM:str = obj["SellingShipmentUM"]
      self.SellingShippedQty:int = obj["SellingShippedQty"]
      self.SellingShippedUM:str = obj["SellingShippedUM"]
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  This field comes directly from the ShipHead table.  """  
      self.ShipToWarning:str = obj["ShipToWarning"]
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  This field comes directly from the ShipHead table.  """  
      self.StockPart:bool = obj["StockPart"]
      """  Indicates if Part is a stock Part  """  
      self.TrackID:bool = obj["TrackID"]
      self.TranLocationIDQty:int = obj["TranLocationIDQty"]
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier that drops shipped the good from their inventory to our customer.  """  
      self.WhseList:str = obj["WhseList"]
      self.KitAttributeSetID:int = obj["KitAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.KitAttributeSetDescription:str = obj["KitAttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.KitAttributeSetShortDescription:str = obj["KitAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.KitPartAttrClassID:str = obj["KitPartAttrClassID"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.MarkForAddrFormatted:str = obj["MarkForAddrFormatted"]
      """  Mark For address formatted for kinetic.  """  
      self.DispInventoryNumberOfPieces:int = obj["DispInventoryNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.DispJobNumberOfPieces:int = obj["DispJobNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.KitRevisionNum:str = obj["KitRevisionNum"]
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.CustNumSendToFSA:bool = obj["CustNumSendToFSA"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.DimensionDimCodeDescription:str = obj["DimensionDimCodeDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.LotPartLotDescription:str = obj["LotPartLotDescription"]
      self.MFShipToNumInactive:bool = obj["MFShipToNumInactive"]
      self.OrderLineProdCode:str = obj["OrderLineProdCode"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumPSCurrCode:str = obj["OrderNumPSCurrCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OTMFCountryDescription:str = obj["OTMFCountryDescription"]
      self.PackNumUseOTS:bool = obj["PackNumUseOTS"]
      self.PackNumShipStatus:str = obj["PackNumShipStatus"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumSendToFSA:bool = obj["PartNumSendToFSA"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumWarrantyCode:str = obj["PartNumWarrantyCode"]
      self.PartNumFSAEquipment:bool = obj["PartNumFSAEquipment"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PlantName:str = obj["PlantName"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.WarrantyCodeSendToFSA:bool = obj["WarrantyCodeSendToFSA"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.WIPWarehouseCodeDescription:str = obj["WIPWarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.PCID2_c:str = obj["PCID2_c"]
      self.PCID3_c:str = obj["PCID3_c"]
      self.PCID4_c:str = obj["PCID4_c"]
      self.PCID5_c:str = obj["PCID5_c"]
      self.PCIDType1_c:str = obj["PCIDType1_c"]
      self.PCIDType2_c:str = obj["PCIDType2_c"]
      self.PCIDType3_c:str = obj["PCIDType3_c"]
      self.PCIDType4_c:str = obj["PCIDType4_c"]
      self.PCIDType5_c:str = obj["PCIDType5_c"]
      pass

class Erp_Tablesets_ShipDtlTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  InvcDtl.TaxCode and InvcDtl/InvcMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount ((Qty*unitprice)-discount) or if this is for a InvcMisc record InvcMisc.Amount.  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  InvcDtl.TaxCode and InvcDtl/InvcMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount ((Qty*unitprice)-discount) or if this is for a InvcMisc record InvcMisc.Amount.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Reverse Charge.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution Date  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Tax Rate Date  """  
      self.DefTaxableAmt:int = obj["DefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.DocDefTaxableAmt:int = obj["DocDefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.Rpt1DefTaxableAmt:int = obj["Rpt1DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxableAmt:int = obj["Rpt2DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxableAmt:int = obj["Rpt3DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.DefTaxAmt:int = obj["DefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.DocDefTaxAmt:int = obj["DocDefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.Rpt1DefTaxAmt:int = obj["Rpt1DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxAmt:int = obj["Rpt2DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxAmt:int = obj["Rpt3DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.ManAdd:bool = obj["ManAdd"]
      """  This record was manually added (not in Liability) but will use the standard calculations  """  
      self.DedTaxAmt:int = obj["DedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.DocDedTaxAmt:int = obj["DocDedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.Rpt1DedTaxAmt:int = obj["Rpt1DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DedTaxAmt:int = obj["Rpt2DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DedTaxAmt:int = obj["Rpt3DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  """  
      self.FixedAmount:int = obj["FixedAmount"]
      """  Fixed Tax Amount  """  
      self.DocFixedAmount:int = obj["DocFixedAmount"]
      """  Document Fixed Tax Amount  """  
      self.Rpt1FixedAmount:int = obj["Rpt1FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2FixedAmount:int = obj["Rpt2FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3FixedAmount:int = obj["Rpt3FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the tax.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the tax converted to the customers currency.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DescCollectionType:str = obj["DescCollectionType"]
      self.TaxDescription:str = obj["TaxDescription"]
      self.TaxTotal:int = obj["TaxTotal"]
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      self.ChangeDateTime:str = obj["ChangeDateTime"]
      """  The date and time that the record was last changed  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.SalesTaxDescDescription:str = obj["SalesTaxDescDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PackNum:int = obj["PackNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipHeadInsuranceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing Slip  """  
      self.InsuranceSeq:int = obj["InsuranceSeq"]
      """  InsuranceSeq  """  
      self.Type:str = obj["Type"]
      """  Insurance Type  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Insurance Company Name  """  
      self.PolicyNum:str = obj["PolicyNum"]
      """  Insurance Policy Number  """  
      self.Premium:int = obj["Premium"]
      """  Insurance Premium  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  """  
      self.ShipLog:str = obj["ShipLog"]
      """  An optional field which can be used to enter a shipping log reference #.  """  
      self.LabelComment:str = obj["LabelComment"]
      """  An optional field that will be printed on the shipping labels for this packing slip.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Packing slip comments.  This will print on the Packing Slip.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Voided:bool = obj["Voided"]
      """  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External  ID  """  
      self.ICReceived:bool = obj["ICReceived"]
      """  Iinter Company Received flag  """  
      self.XRefPackNum:str = obj["XRefPackNum"]
      """  Cross reference Packing Slip number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Populated from OrderHed.BTCustNum.  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.ShipGroup:str = obj["ShipGroup"]
      """  Group the shipment belongs to for "Staging"  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Package Code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.VerbalConf:bool = obj["VerbalConf"]
      """  Verbal Confirmation required  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.MFTransNum:str = obj["MFTransNum"]
      """  Transaction Number returned by the Manifest Engine  """  
      self.MFCallTag:str = obj["MFCallTag"]
      """  Manifest Call Tag Number  """  
      self.MFPickupNum:str = obj["MFPickupNum"]
      """  Manifest Pickup Number  """  
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      """  Manifest Discount Freight Amount  """  
      self.MFTemplate:str = obj["MFTemplate"]
      """  Manifest Template Code  """  
      self.MFUse3B:bool = obj["MFUse3B"]
      """  Manifest flag to use 3 party billing  """  
      self.MF3BAccount:str = obj["MF3BAccount"]
      """  Manifest's 3rd Party Billing Account  """  
      self.MFDimWeight:int = obj["MFDimWeight"]
      """  Manifest Dimension Weight  """  
      self.MFZone:str = obj["MFZone"]
      """  Manifest Delivery Zone  """  
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      """  Manifest Published Freight Amount  """  
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      """  Manifest Other Amount  """  
      self.MFOversized:bool = obj["MFOversized"]
      """  Manifest Oversized flag  """  
      self.ServSatDelivery:bool = obj["ServSatDelivery"]
      """  Is a Service Saturday delivery acceptable  """  
      self.ServSatPickup:bool = obj["ServSatPickup"]
      """  Is a Service Saturday pickup available  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServPOD:bool = obj["ServPOD"]
      """  Service Auto POD flag  """  
      self.ServAOD:bool = obj["ServAOD"]
      """  AOD  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.PayFlag:str = obj["PayFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping, The city portion of the Payer main address.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  The state or province portion of the shipment payer main address.  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  The zip or postal code portion of the shipping payers main address.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  The country of the main shipping payers address.  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder Country portion of the address  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country portion of the address  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Payer Bill To Third Address line  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Payer Bill To Country Number  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Payer Bill To Phone Number  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View From Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  """  
      self.ReplicatedFrom:int = obj["ReplicatedFrom"]
      """  Pack ID of the pack this pack was replicated from.  This is used as a debugging tool and is not presented to the end user.  """  
      self.ReplicatedStat:str = obj["ReplicatedStat"]
      """  Informational field containing either Complete or Partial.  This is only popluated if the ReplicatedFrom field has a value.  This is used as a debugging tool and is not presented to the user.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.OTSOrderNum:int = obj["OTSOrderNum"]
      """  The Sales Order number which contains the One Time ShipTo data. The OTSOrderNum along with the values ShipToNum are used to find the OrderHed or OrderRel to obtain the OTS.  """  
      self.TaxCalculated:bool = obj["TaxCalculated"]
      """  Indicates whether or not the taxes for this shipment have been calculated.  This field is used to identify those situations where the tax engine was called but did not generate any taxes because none were needed.  """  
      self.TaxCalcDate:str = obj["TaxCalcDate"]
      """  Date the taxes were calculated.  Used for informational and audit tracking purposes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.OrderAmt:int = obj["OrderAmt"]
      """  Total order Amount. This field is an accumulation of the extended net amounts of the detail line items  """  
      self.DocOrderAmt:int = obj["DocOrderAmt"]
      """  Total order Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  """  
      self.Rpt1OrderAmt:int = obj["Rpt1OrderAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrderAmt:int = obj["Rpt2OrderAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrderAmt:int = obj["Rpt3OrderAmt"]
      """  Reporting currency value of this field  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.TotalWHTax:int = obj["TotalWHTax"]
      """   Order Total Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalWHTax:int = obj["DocTotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalWHTax:int = obj["Rpt1TotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalWHTax:int = obj["Rpt2TotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalWHTax:int = obj["Rpt3TotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """   Order Total Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.TotalTax:int = obj["TotalTax"]
      """   Order Total Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.TotalDiscount:int = obj["TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalDiscount:int = obj["Rpt1TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalDiscount:int = obj["Rpt2TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalDiscount:int = obj["Rpt3TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.DocTotalDiscount:int = obj["DocTotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.DeviceUOM:str = obj["DeviceUOM"]
      """  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.PBHoldNoInv:bool = obj["PBHoldNoInv"]
      """  Flag to indicate that project billing Hold Product Invoice flag is true, it prevents this pack slip from being selected for invoicing.  """  
      self.ReconcileQty:int = obj["ReconcileQty"]
      """  Reconciled quantity for the packing slip  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  Last trading partner demand schedule processed that affected this packing slip  """  
      self.CounterASN:int = obj["CounterASN"]
      """  Number of times the customer shipment has been shipped, that means it changed from non shipped status to shipped  """  
      self.OurBank:str = obj["OurBank"]
      """  Bank for Cash Receipts. Default is from 1) Sales Order 2)Bill To Customer 3) System Default(Company).  """  
      self.ERSOrder:bool = obj["ERSOrder"]
      """  It will be used to identify that the shipment will generate an invoice when it got shipped. If the first order release added to a pack belongs to an ERS order, then non ERS order releases will not be allowed in that pack and if the first order release added to a pack belongs to a non ERS order, then ERS order releases will not be allowed in that pack.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OrderDate:str = obj["OrderDate"]
      self.SlipStatus:str = obj["SlipStatus"]
      """  Comma delimited list of status types for lookup  """  
      self.AddrList:str = obj["AddrList"]
      """  Shipping Address  """  
      self.BillAddr:str = obj["BillAddr"]
      """  Billing Address  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates if Customer is on Credit Hold  """  
      self.OrderHold:bool = obj["OrderHold"]
      """  Indicates if Order is on Hold  """  
      self.MultipleShippers:bool = obj["MultipleShippers"]
      """  Flag indicating OrderRel's going to more than one shipTo  """  
      self.SendShipment:bool = obj["SendShipment"]
      """  Indicates whether to hide/view ExternalDeliveryNote field  """  
      self.BTCustID:str = obj["BTCustID"]
      """  CustID associated with ShipHeadHead.BTCustNum.  """  
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  CustName associated with ShipHead.BTCustNum.  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  Used by the manifest system.  Sum of the value of items in the carton.  Item price - discount + sales tax.  """  
      self.LastCartonFlag:bool = obj["LastCartonFlag"]
      """  Set to Y if the carton is the last one being shiped to the customer.  If the sum of the quantity packed does not equal the quantity ordered for each line in the carton the value is No.  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage Number.  """  
      self.EnableShipped:bool = obj["EnableShipped"]
      self.OrderNum:int = obj["OrderNum"]
      """  Order Number for new cartons.  """  
      self.HasCartonLines:bool = obj["HasCartonLines"]
      """  Indicates whether the Carton has lines or not.  """  
      self.StagingReq:bool = obj["StagingReq"]
      """  Displays the contents of XaSyst.StagingReq  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  """  
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  A zero indicates the Packing height is to be enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Indicates if package length is to be enabled.  If the value is zero the prompt is enabled.  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  A zero indicates the packaging width field is to be enabled.  """  
      self.CtnPkgCode:str = obj["CtnPkgCode"]
      """  Used to enable users to default the Carton Trk Dtl package settings.  Initial value defaults to the ShipHead.PkgCode.  However, this field does NOT have to be the same as the ShipHead.PkgCode.  """  
      self.ReplicateCount:int = obj["ReplicateCount"]
      """  Number of packs to replicate  """  
      self.PhantomCasesExist:bool = obj["PhantomCasesExist"]
      """  Logical indicating if CartonTrkDtl records exist for this pack.  Used by the UI for row rules.  """  
      self.EnablePhantom:bool = obj["EnablePhantom"]
      """  Logical indicating if the PhantomPack checkbox is to be enabled.  """  
      self.MasterpackPackNum:int = obj["MasterpackPackNum"]
      """  Pack ID of the Masterpack this shipment is on.  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for customer shipments  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Document Total tax amount from ShipDtl Tax for Collection type 'Invoice'  """  
      self.DocWithholdingTaxAmt:int = obj["DocWithholdingTaxAmt"]
      self.EnableTax:bool = obj["EnableTax"]
      """  Intended for internal UI use.  Identifies whether or not taxes are generated for shipdtls.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.DisplayInPrice:bool = obj["DisplayInPrice"]
      """  The flag to indicate if Tax Inclusive Pricing should be on display  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      """  Description of delivery type  """  
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.OurBankDescription:str = obj["OurBankDescription"]
      """  Full description of the bank account.  """  
      self.OurBankBankName:str = obj["OurBankBankName"]
      """  The Bank's full name.  """  
      self.PackToMasterpackDtlPackNum:int = obj["PackToMasterpackDtlPackNum"]
      """  Master pack packnum  """  
      self.ShipToCustName:str = obj["ShipToCustName"]
      """  The full name of the customer.  """  
      self.ShipToCustBTName:str = obj["ShipToCustBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.ShipToCustCustID:str = obj["ShipToCustCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      """  Full description for the Tax Region.  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  """  
      self.ShipLog:str = obj["ShipLog"]
      """  An optional field which can be used to enter a shipping log reference #.  """  
      self.LabelComment:str = obj["LabelComment"]
      """  An optional field that will be printed on the shipping labels for this packing slip.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Packing slip comments.  This will print on the Packing Slip.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Voided:bool = obj["Voided"]
      """  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External  ID  """  
      self.ICReceived:bool = obj["ICReceived"]
      """  Iinter Company Received flag  """  
      self.XRefPackNum:str = obj["XRefPackNum"]
      """  Cross reference Packing Slip number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Populated from OrderHed.BTCustNum.  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.ShipGroup:str = obj["ShipGroup"]
      """  Group the shipment belongs to for "Staging"  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Package Code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.VerbalConf:bool = obj["VerbalConf"]
      """  Verbal Confirmation required  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.MFTransNum:str = obj["MFTransNum"]
      """  Transaction Number returned by the Manifest Engine  """  
      self.MFCallTag:str = obj["MFCallTag"]
      """  Manifest Call Tag Number  """  
      self.MFPickupNum:str = obj["MFPickupNum"]
      """  Manifest Pickup Number  """  
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      """  Manifest Discount Freight Amount  """  
      self.MFTemplate:str = obj["MFTemplate"]
      """  Manifest Template Code  """  
      self.MFUse3B:bool = obj["MFUse3B"]
      """  Manifest flag to use 3 party billing  """  
      self.MF3BAccount:str = obj["MF3BAccount"]
      """  Manifest's 3rd Party Billing Account  """  
      self.MFDimWeight:int = obj["MFDimWeight"]
      """  Manifest Dimension Weight  """  
      self.MFZone:str = obj["MFZone"]
      """  Manifest Delivery Zone  """  
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      """  Manifest Published Freight Amount  """  
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      """  Manifest Other Amount  """  
      self.MFOversized:bool = obj["MFOversized"]
      """  Manifest Oversized flag  """  
      self.ServSatDelivery:bool = obj["ServSatDelivery"]
      """  Is a Service Saturday delivery acceptable  """  
      self.ServSatPickup:bool = obj["ServSatPickup"]
      """  Is a Service Saturday pickup available  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServPOD:bool = obj["ServPOD"]
      """  Service Auto POD flag  """  
      self.ServAOD:bool = obj["ServAOD"]
      """  AOD  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.PayFlag:str = obj["PayFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping, The city portion of the Payer main address.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  The state or province portion of the shipment payer main address.  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  The zip or postal code portion of the shipping payers main address.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  The country of the main shipping payers address.  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder Country portion of the address  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country portion of the address  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Payer Bill To Third Address line  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Payer Bill To Country Number  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Payer Bill To Phone Number  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View From Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  """  
      self.ReplicatedFrom:int = obj["ReplicatedFrom"]
      """  Pack ID of the pack this pack was replicated from.  This is used as a debugging tool and is not presented to the end user.  """  
      self.ReplicatedStat:str = obj["ReplicatedStat"]
      """  Informational field containing either Complete or Partial.  This is only popluated if the ReplicatedFrom field has a value.  This is used as a debugging tool and is not presented to the user.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.OTSOrderNum:int = obj["OTSOrderNum"]
      """  The Sales Order number which contains the One Time ShipTo data. The OTSOrderNum along with the values ShipToNum are used to find the OrderHed or OrderRel to obtain the OTS.  """  
      self.TaxCalculated:bool = obj["TaxCalculated"]
      """  Indicates whether or not the taxes for this shipment have been calculated.  This field is used to identify those situations where the tax engine was called but did not generate any taxes because none were needed.  """  
      self.TaxCalcDate:str = obj["TaxCalcDate"]
      """  Date the taxes were calculated.  Used for informational and audit tracking purposes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.OrderAmt:int = obj["OrderAmt"]
      """  Total order Amount. This field is an accumulation of the extended net amounts of the detail line items  """  
      self.DocOrderAmt:int = obj["DocOrderAmt"]
      """  Total order Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  """  
      self.Rpt1OrderAmt:int = obj["Rpt1OrderAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrderAmt:int = obj["Rpt2OrderAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrderAmt:int = obj["Rpt3OrderAmt"]
      """  Reporting currency value of this field  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.TotalWHTax:int = obj["TotalWHTax"]
      """   Order Total Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalWHTax:int = obj["DocTotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalWHTax:int = obj["Rpt1TotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalWHTax:int = obj["Rpt2TotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalWHTax:int = obj["Rpt3TotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """   Order Total Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.TotalTax:int = obj["TotalTax"]
      """   Order Total Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.TotalDiscount:int = obj["TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalDiscount:int = obj["Rpt1TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalDiscount:int = obj["Rpt2TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalDiscount:int = obj["Rpt3TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.DocTotalDiscount:int = obj["DocTotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.DeviceUOM:str = obj["DeviceUOM"]
      """  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.PBHoldNoInv:bool = obj["PBHoldNoInv"]
      """  Flag to indicate that project billing Hold Product Invoice flag is true, it prevents this pack slip from being selected for invoicing.  """  
      self.ReconcileQty:int = obj["ReconcileQty"]
      """  Reconciled quantity for the packing slip  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  Last trading partner demand schedule processed that affected this packing slip  """  
      self.CounterASN:int = obj["CounterASN"]
      """  Number of times the customer shipment has been shipped, that means it changed from non shipped status to shipped  """  
      self.OurBank:str = obj["OurBank"]
      """  Bank for Cash Receipts. Default is from 1) Sales Order 2)Bill To Customer 3) System Default(Company).  """  
      self.ERSOrder:bool = obj["ERSOrder"]
      """  It will be used to identify that the shipment will generate an invoice when it got shipped. If the first order release added to a pack belongs to an ERS order, then non ERS order releases will not be allowed in that pack and if the first order release added to a pack belongs to a non ERS order, then ERS order releases will not be allowed in that pack.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.ShipOvers:bool = obj["ShipOvers"]
      """  ShipOvers  """  
      self.WIPackSlipCreated:bool = obj["WIPackSlipCreated"]
      """  WIPackSlipCreated  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAuthorizationCode:str = obj["AGAuthorizationCode"]
      """  AGAuthorizationCode  """  
      self.AGAuthorizationDate:str = obj["AGAuthorizationDate"]
      """  AGAuthorizationDate  """  
      self.AGCarrierCUIT:str = obj["AGCarrierCUIT"]
      """  AGCarrierCUIT  """  
      self.AGCOTMark:bool = obj["AGCOTMark"]
      """  AGCOTMark  """  
      self.AGDocumentLetter:str = obj["AGDocumentLetter"]
      """  AGDocumentLetter  """  
      self.AGInvoicingPoint:str = obj["AGInvoicingPoint"]
      """  AGInvoicingPoint  """  
      self.AGLegalNumber:str = obj["AGLegalNumber"]
      """  AGLegalNumber  """  
      self.AGPrintingControlType:str = obj["AGPrintingControlType"]
      """  AGPrintingControlType  """  
      self.AGTrackLicense:str = obj["AGTrackLicense"]
      """  AGTrackLicense  """  
      self.DispatchReason:str = obj["DispatchReason"]
      """  DispatchReason  """  
      self.AGShippingWay:str = obj["AGShippingWay"]
      """  AGShippingWay  """  
      self.OurSupplierCode:str = obj["OurSupplierCode"]
      """  Our Supplier Code  """  
      self.ASNPrintedDate:str = obj["ASNPrintedDate"]
      """  ASNPrintedDate  """  
      self.EDIShipToNum:str = obj["EDIShipToNum"]
      """  EDIShipToNum  """  
      self.MXIncoterm:str = obj["MXIncoterm"]
      """  MXIncoterm  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.DigitalSignature:str = obj["DigitalSignature"]
      """  DigitalSignature  """  
      self.SignedOn:str = obj["SignedOn"]
      """  SignedOn  """  
      self.SignedBy:str = obj["SignedBy"]
      """  SignedBy  """  
      self.FirstPrintDate:str = obj["FirstPrintDate"]
      """  FirstPrintDate  """  
      self.DocCopyNum:int = obj["DocCopyNum"]
      """  DocCopyNum  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      """  Declaration Bill  """  
      self.CNSample:bool = obj["CNSample"]
      """  Sample  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  Bonded  """  
      self.MXCertifiedTimestamp:str = obj["MXCertifiedTimestamp"]
      """  Creation date and time  """  
      self.MXCertificateSN:str = obj["MXCertificateSN"]
      """  Certificate Serial Number  """  
      self.MXCertificate:str = obj["MXCertificate"]
      """  Certificate  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  Fiscal Folio (UUID)  """  
      self.MXSATCertificateSN:str = obj["MXSATCertificateSN"]
      """  SAT Certificate Serial Number  """  
      self.MXDigitalSeal:str = obj["MXDigitalSeal"]
      """  Digital Seal  """  
      self.MXSATSeal:str = obj["MXSATSeal"]
      """  SAT Seal  """  
      self.MXOriginalString:str = obj["MXOriginalString"]
      """  Original String  """  
      self.MXOriginalStringTFD:str = obj["MXOriginalStringTFD"]
      """  TFD Original String  """  
      self.MXSerie:str = obj["MXSerie"]
      """  Serie  """  
      self.MXFolio:str = obj["MXFolio"]
      """  Folio  """  
      self.MXETD:str = obj["MXETD"]
      """  Estimated Date and Time of Departure  """  
      self.MXETA:str = obj["MXETA"]
      """  Estimated Date and Time of Arrival  """  
      self.MXDistance:int = obj["MXDistance"]
      """  Distance in Km  """  
      self.MXPermitType:str = obj["MXPermitType"]
      """  Permit Type  """  
      self.MXPermitNum:str = obj["MXPermitNum"]
      """  Permit Number  """  
      self.MXCartaPorteStatus:str = obj["MXCartaPorteStatus"]
      """  Carta Porte Status  """  
      self.VehicleLicensePlate:str = obj["VehicleLicensePlate"]
      """  Vehicle License Plate  """  
      self.VehicleType:str = obj["VehicleType"]
      """  Vehicle Type  """  
      self.VehicleYear:int = obj["VehicleYear"]
      """  Vehicle Year  """  
      self.DriverID:str = obj["DriverID"]
      """  Driver  """  
      self.MXCancelFiscalFolio:str = obj["MXCancelFiscalFolio"]
      """  MXCancelFiscalFolio  """  
      self.IncotermCode:str = obj["IncotermCode"]
      """  Incoterm Code  """  
      self.IncotermLocation:str = obj["IncotermLocation"]
      """  Incoterm Location  """  
      self.AddrList:str = obj["AddrList"]
      """  Shipping Address  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.BillAddr:str = obj["BillAddr"]
      """  Billing Address  """  
      self.BTCustID:str = obj["BTCustID"]
      """  CustID associated with ShipHeadHead.BTCustNum.  """  
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  CustName associated with ShipHead.BTCustNum.  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  Used by the manifest system.  Sum of the value of items in the carton.  Item price - discount + sales tax.  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage Number.  """  
      self.ChangeDateTime:str = obj["ChangeDateTime"]
      """  The date and time that the record was last changed  """  
      self.CheckOrderMessage:str = obj["CheckOrderMessage"]
      """  Internal field for temporary storage of check order messages.  """  
      self.CreditCardMessage:str = obj["CreditCardMessage"]
      """  This field temporarily holds certain message(s) returned by credit card processing logic for internal processing.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates if Customer is on Credit Hold  """  
      self.CtnPkgCode:str = obj["CtnPkgCode"]
      """  Used to enable users to default the Carton Trk Dtl package settings.  Initial value defaults to the ShipHead.PkgCode.  However, this field does NOT have to be the same as the ShipHead.PkgCode.  """  
      self.DisplayInPrice:bool = obj["DisplayInPrice"]
      """  The flag to indicate if Tax Inclusive Pricing should be on display  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Document Total tax amount from ShipDtl Tax for Collection type 'Invoice'  """  
      self.DocWithholdingTaxAmt:int = obj["DocWithholdingTaxAmt"]
      self.DoPostUpdate:bool = obj["DoPostUpdate"]
      """  Internal flag to indicate if post update processing should be done.  """  
      self.DspDigitalSignature:str = obj["DspDigitalSignature"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnablePackageControl:bool = obj["EnablePackageControl"]
      """  Logical indicating if the package control functionality should be enabled.  """  
      self.EnablePhantom:bool = obj["EnablePhantom"]
      """  Logical indicating if the PhantomPack checkbox is to be enabled.  """  
      self.EnableShipped:bool = obj["EnableShipped"]
      self.EnableTax:bool = obj["EnableTax"]
      """  Intended for internal UI use.  Identifies whether or not taxes are generated for shipdtls.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  """  
      self.FromMasterPack:bool = obj["FromMasterPack"]
      """  True if the update is being called from Master Pack (needed for validation)  """  
      self.HasCartonLines:bool = obj["HasCartonLines"]
      """  Indicates whether the Carton has lines or not.  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for customer shipments  """  
      self.LastCartonFlag:bool = obj["LastCartonFlag"]
      """  Set to Y if the carton is the last one being shiped to the customer.  If the sum of the quantity packed does not equal the quantity ordered for each line in the carton the value is No.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.MasterpackPackNum:int = obj["MasterpackPackNum"]
      """  Pack ID of the Masterpack this shipment is on.  """  
      self.MultipleShippers:bool = obj["MultipleShippers"]
      """  Flag indicating OrderRel's going to more than one shipTo  """  
      self.OrderDate:str = obj["OrderDate"]
      self.OrderHold:bool = obj["OrderHold"]
      """  Indicates if Order is on Hold  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order Number for new cartons.  """  
      self.PCID:str = obj["PCID"]
      self.PhantomCasesExist:bool = obj["PhantomCasesExist"]
      """  Logical indicating if CartonTrkDtl records exist for this pack.  Used by the UI for row rules.  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  A zero indicates the Packing height is to be enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Indicates if package length is to be enabled.  If the value is zero the prompt is enabled.  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  A zero indicates the packaging width field is to be enabled.  """  
      self.PostUpdMessage:str = obj["PostUpdMessage"]
      """  Internal field for temporary storage of post update messages.  """  
      self.QSUseBOL:bool = obj["QSUseBOL"]
      self.QSUseCO:bool = obj["QSUseCO"]
      self.QSUseIntl:bool = obj["QSUseIntl"]
      self.ReadyToInvoiceChanged:bool = obj["ReadyToInvoiceChanged"]
      """  Internal field for update processing that is true if ReadyToInvoice has been changed.  """  
      self.ReplicateCount:int = obj["ReplicateCount"]
      """  Number of packs to replicate  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      self.SendShipment:bool = obj["SendShipment"]
      """  Indicates whether to hide/view ExternalDeliveryNote field  """  
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.SlipStatus:str = obj["SlipStatus"]
      """  Comma delimited list of status types for lookup  """  
      self.StageShipped:bool = obj["StageShipped"]
      """  Carton Stage Ship Status  """  
      self.StagingReq:bool = obj["StagingReq"]
      """  Displays the contents of XaSyst.StagingReq  """  
      self.StatusChgMessage:str = obj["StatusChgMessage"]
      """  Internal field for temporary storage of status change messages.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      self.AutoInvoiceMessage:str = obj["AutoInvoiceMessage"]
      """  Internal field for temporary storage of auto invoicing messages.  """  
      self.ShipToAddressFormatted:str = obj["ShipToAddressFormatted"]
      """  Ship To address formatted for Kinetic.  """  
      self.SoldToAddressFormatted:str = obj["SoldToAddressFormatted"]
      """  Sold To address formatted  """  
      self.MXETADate:str = obj["MXETADate"]
      """  Estimated Date of Arrival  """  
      self.MXETATime:int = obj["MXETATime"]
      """  Estimated Time of Arrival  """  
      self.MXETDDate:str = obj["MXETDDate"]
      """  Estimated Date of Departure  """  
      self.MXETDTime:int = obj["MXETDTime"]
      """  Estimated Time of Departure  """  
      self.EnableIncotermLocation:bool = obj["EnableIncotermLocation"]
      """  Flag indicating whether to enable Incoterm Location  """  
      self.MXVehicleWeight:int = obj["MXVehicleWeight"]
      """  Vehicle Weight (in tons)  """  
      self.MXIdCCP:str = obj["MXIdCCP"]
      """  A unique Carta Porte identification number assigned by Epicor  """  
      self.MXCustomsRegime:str = obj["MXCustomsRegime"]
      """  Customs Regime for Export transaction  """  
      self.MXReverseLogistics:bool = obj["MXReverseLogistics"]
      """  Check box to specify the use of reverse logistic, collection or devolution services when shipping goods.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AGInvoicingPointDescription:str = obj["AGInvoicingPointDescription"]
      self.BTCustNumInactive:bool = obj["BTCustNumInactive"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CustomerSendToFSA:bool = obj["CustomerSendToFSA"]
      self.CustomerInactive:bool = obj["CustomerInactive"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      self.IncotermsDescription:str = obj["IncotermsDescription"]
      self.OurBankBankName:str = obj["OurBankBankName"]
      self.OurBankDescription:str = obj["OurBankDescription"]
      self.ShipToCustInactive:bool = obj["ShipToCustInactive"]
      self.ShipToCustBTName:str = obj["ShipToCustBTName"]
      self.ShipToCustCustID:str = obj["ShipToCustCustID"]
      self.ShipToCustName:str = obj["ShipToCustName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.Review_c:bool = obj["Review_c"]
      pass

class Erp_Tablesets_ShipHeadTrailerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing Slip  """  
      self.LicensePlate:str = obj["LicensePlate"]
      """  License Plate for Trailer  """  
      self.Type:str = obj["Type"]
      """  Type of Trailer  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipMiscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number of the ShipHead record that this record is related to.  """  
      self.PackLine:int = obj["PackLine"]
      """   The packing slip line number of the ShipDtl record that this record is related to.
NOTE: This is always zero.  Currently ShipMisc records are only related to the ShipHead record.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  An integer assigned by the system which is used as one of the components of the unique index for this record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. This will be printed on the Packing Slip and transferred over to invoice processing. The default is provided by MiscChrg.Description, but it's overrideable by the user. This can't be blank.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit. Can't be zero. Use MiscChrg.MiscAmt as a default.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.InMiscAmt:int = obj["InMiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit including taxes. Can't be zero. Use MiscChrg.MiscAmt as a default.  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.WIIsAutoCreatedMisc:bool = obj["WIIsAutoCreatedMisc"]
      """  WIIsAutoCreatedMisc  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  The amount of the MiscAmt converted to the ShipHead CurrencyCode  """  
      self.ChangeDateTime:str = obj["ChangeDateTime"]
      """  The date and time that the record was last changed  """  
      self.DspMiscAmt:int = obj["DspMiscAmt"]
      """  The amount of misc charge on display. If the Tax Liability is flagged as Tax Inclusive Pricing then this amount is InMiscAmount else this amount is MiscAmt.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.PackNumShipStatus:str = obj["PackNumShipStatus"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipTaxSumRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency display switch  """  
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency display symbol  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  DocDisplaySymbol  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  Document reportable amount.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Document taxable amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Document tax amount.  """  
      self.PackNum:int = obj["PackNum"]
      """  Pack ID  """  
      self.PackLIne:int = obj["PackLIne"]
      """  pack line  """  
      self.Percent:int = obj["Percent"]
      """  Percent  """  
      self.RateCode:str = obj["RateCode"]
      self.ReportableAmt:int = obj["ReportableAmt"]
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      self.TaxableAmt:int = obj["TaxableAmt"]
      self.TaxAmt:int = obj["TaxAmt"]
      self.TaxCode:str = obj["TaxCode"]
      self.TaxDescription:str = obj["TaxDescription"]
      self.RateCodeDesc:str = obj["RateCodeDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipUPSRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.UPSQVSeq:int = obj["UPSQVSeq"]
      """  UPS Quantum View Sequence  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  UPS Emailaddress  """  
      self.ShipmentNotify:bool = obj["ShipmentNotify"]
      """  Notify Emailaddress when shipped  """  
      self.FailureNotify:bool = obj["FailureNotify"]
      """  Logical indicating if the Email Address is to be notified of a failed shipment.  """  
      self.DeliveryNotify:bool = obj["DeliveryNotify"]
      """  Logical indicating if the Email Address is to be notified of delivery.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableQuantumView:bool = obj["EnableQuantumView"]
      """  Logical indicating if the UPS email fields are to be enabled.  """  
      self.ShipStatus:str = obj["ShipStatus"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AfterChangedShipDtlOrderNum_input:
   """ Required : 
   ipSalesOrder
   ipPackNum
   ds
   """  
   def __init__(self, obj):
      self.ipSalesOrder:int = obj["ipSalesOrder"]
      self.ipPackNum:int = obj["ipPackNum"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class AfterChangedShipDtlOrderNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AllowUndoExternalDN_output:
   def __init__(self, obj):
      pass

class AskForShipToChange_input:
   """ Required : 
   iPackNum
   iOrderNum
   iOrderLine
   iOrderRelNum
   askUser
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      """  Pack Number  """  
      self.iOrderNum:int = obj["iOrderNum"]
      """  Order Number  """  
      self.iOrderLine:int = obj["iOrderLine"]
      """  Order Line Number  """  
      self.iOrderRelNum:int = obj["iOrderRelNum"]
      """  Release Number  """  
      self.askUser:bool = obj["askUser"]
      """  Tells if the user must be asked for changing the Shipping Information  """  
      pass

class AskForShipToChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.askUser:bool = obj["askUser"]
      pass

      """  output parameters  """  

class AssignLegalNumber_input:
   """ Required : 
   ipPackNum
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Packing Slip number  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class AssignLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.opLegalNumMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class BuildCompSerMatch_input:
   """ Required : 
   ipPartNum
   ipRevNum
   ipSerialNumbers
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      self.ipRevNum:str = obj["ipRevNum"]
      self.ipSerialNumbers:str = obj["ipSerialNumbers"]
      pass

class BuildCompSerMatch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LLCompSerMatchTableset] = obj["returnObj"]
      pass

class BuildSerialMatchingParams_input:
   """ Required : 
   ds
   ds1
   packLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialMatchingParamsTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_CustShipTableset] = obj["ds1"]
      self.packLine:int = obj["packLine"]
      """  Detail Line Number to update  """  
      pass

class BuildSerialMatchingParams_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialMatchingParamsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BuildShipToCustomerList_input:
   """ Required : 
   orderNum
   """  
   def __init__(self, obj):
      self.orderNum:int = obj["orderNum"]
      """  Order Number  """  
      pass

class BuildShipToCustomerList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.shipToCustomerList:str = obj["parameters"]
      pass

      """  output parameters  """  

class BuildShipToList_input:
   """ Required : 
   orderNum
   iShipToCustNum
   """  
   def __init__(self, obj):
      self.orderNum:int = obj["orderNum"]
      """  Order Number  """  
      self.iShipToCustNum:int = obj["iShipToCustNum"]
      """  Ship To Customer ID  """  
      pass

class BuildShipToList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.shipToList:str = obj["parameters"]
      pass

      """  output parameters  """  

class CalculateWarrantyExpiration_input:
   """ Required : 
   ds
   orderLine
   orderRelNum
   effectiveDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.orderLine:int = obj["orderLine"]
      self.orderRelNum:int = obj["orderRelNum"]
      self.effectiveDate:str = obj["effectiveDate"]
      pass

class CalculateWarrantyExpiration_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CalculateWeight_input:
   """ Required : 
   cartonNumber
   """  
   def __init__(self, obj):
      self.cartonNumber:int = obj["cartonNumber"]
      pass

class CalculateWeight_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.calculatedWeight:int = obj["parameters"]
      pass

      """  output parameters  """  

class CallsCreateCustomerCartons_input:
   """ Required : 
   ipPackNum
   ipNbrCartonsToCreate
   ipPkgCode
   ipPkgLength
   ipPkgWidth
   ipPkgHeight
   ipRecalcAmts
   ipZeroWeight
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipNbrCartonsToCreate:int = obj["ipNbrCartonsToCreate"]
      self.ipPkgCode:str = obj["ipPkgCode"]
      self.ipPkgLength:int = obj["ipPkgLength"]
      self.ipPkgWidth:int = obj["ipPkgWidth"]
      self.ipPkgHeight:int = obj["ipPkgHeight"]
      self.ipRecalcAmts:bool = obj["ipRecalcAmts"]
      self.ipZeroWeight:bool = obj["ipZeroWeight"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class CallsCreateCustomerCartons_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CanStage_input:
   """ Required : 
   ipShipHedRowID
   """  
   def __init__(self, obj):
      self.ipShipHedRowID:str = obj["ipShipHedRowID"]
      """  Unique Identifier for the Transfer Order Shipment  """  
      pass

class CanStage_output:
   def __init__(self, obj):
      pass

class CancelVoid_input:
   """ Required : 
   packNum
   ds
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      """  Packing Slip Number  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class CancelVoid_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CartonValidateWeight_input:
   """ Required : 
   ipWeight
   """  
   def __init__(self, obj):
      self.ipWeight:int = obj["ipWeight"]
      pass

class CartonValidateWeight_output:
   def __init__(self, obj):
      pass

class ChangeIncotermCode_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class ChangeIncotermCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePCIDPackVerify_input:
   """ Required : 
   ipSource
   ipPackNum
   ipPCID
   ds
   """  
   def __init__(self, obj):
      self.ipSource:str = obj["ipSource"]
      """  ipSource  """  
      self.ipPackNum:int = obj["ipPackNum"]
      """  ipPackNum  """  
      self.ipPCID:str = obj["ipPCID"]
      """  ipPCID  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class ChangePCIDPackVerify_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.opAlreadyScannedPackNum:int = obj["parameters"]
      self.opPCIDCount:int = obj["parameters"]
      self.opItemPartNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangePCID_input:
   """ Required : 
   ipSource
   ipPackNum
   ipPCID
   ds
   """  
   def __init__(self, obj):
      self.ipSource:str = obj["ipSource"]
      """  ipSource  """  
      self.ipPackNum:int = obj["ipPackNum"]
      """  ipPackNum  """  
      self.ipPCID:str = obj["ipPCID"]
      """  ipPCID  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class ChangePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeShipCmpl_input:
   """ Required : 
   ds
   packLine
   shipCmpl
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.packLine:int = obj["packLine"]
      """  Detail Line Number to update  """  
      self.shipCmpl:bool = obj["shipCmpl"]
      """  Proposed ShipCmpl change  """  
      pass

class ChangeShipCmpl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.questionString:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeShipDtlMFCustID_input:
   """ Required : 
   ipMFCustID
   ds
   """  
   def __init__(self, obj):
      self.ipMFCustID:str = obj["ipMFCustID"]
      """  The proposed Mark For Customer ID  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class ChangeShipDtlMFCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeShipDtlMFShipToNum_input:
   """ Required : 
   ProposedMFShipToNum
   ds
   """  
   def __init__(self, obj):
      self.ProposedMFShipToNum:str = obj["ProposedMFShipToNum"]
      """  The Proposed Mark For ShipToNum  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class ChangeShipDtlMFShipToNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeShipDtlUseOTMF_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class ChangeShipDtlUseOTMF_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeShipHeadShipToCustID_input:
   """ Required : 
   iShipToCustID
   ds
   """  
   def __init__(self, obj):
      self.iShipToCustID:str = obj["iShipToCustID"]
      """  Ship To Customer ID  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class ChangeShipHeadShipToCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeShipMiscAmount_input:
   """ Required : 
   ds
   newMiscAmt
   docAmtChanged
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.newMiscAmt:int = obj["newMiscAmt"]
      """  Proposed Miscellaneous Change Percentage  """  
      self.docAmtChanged:bool = obj["docAmtChanged"]
      """  True if the change was to the DocMiscAmt, false if the change is to DspMiscAmt  """  
      pass

class ChangeShipMiscAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeShipMiscPrcnt_input:
   """ Required : 
   ds
   newPrcnt
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.newPrcnt:int = obj["newPrcnt"]
      """  Proposed Miscellaneous Change Percentage  """  
      pass

class ChangeShipMiscPrcnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeStatus_input:
   """ Required : 
   ipShipHedRowID
   ipStatus
   ipResetCODCharges
   ipResetInsCharges
   ds
   """  
   def __init__(self, obj):
      self.ipShipHedRowID:str = obj["ipShipHedRowID"]
      """  Unique Identifier for the Transfer Order Shipment  """  
      self.ipStatus:str = obj["ipStatus"]
      """  Selected Status.
           Valid Options: Open, Close, Void, UnVoid, Freight, UnFreight, Stage  """  
      self.ipResetCODCharges:bool = obj["ipResetCODCharges"]
      """  Indicates if the CODAmount is to be reset to zero  """  
      self.ipResetInsCharges:bool = obj["ipResetInsCharges"]
      """  Indicates if the DeclaredAmt is to be reset to zero  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class ChangeStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeWarrantyToFSA_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class ChangeWarrantyToFSA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckAttributeSetsOnShipDtlLines_input:
   """ Required : 
   iPackNum
   markAsShipped
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      self.markAsShipped:bool = obj["markAsShipped"]
      pass

class CheckAttributeSetsOnShipDtlLines_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cErrorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckCNCustomsDeclarationBillLine_input:
   """ Required : 
   bBeforeUpdate
   ds
   """  
   def __init__(self, obj):
      self.bBeforeUpdate:bool = obj["bBeforeUpdate"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class CheckCNCustomsDeclarationBillLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckCOOPercents_input:
   """ Required : 
   iPackNum
   iPackLine
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      """  The current PackNum  """  
      self.iPackLine:int = obj["iPackLine"]
      """  The current PackLine  """  
      pass

class CheckCOOPercents_output:
   def __init__(self, obj):
      pass

class CheckCompliance_input:
   """ Required : 
   ipPackNum
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Current PackNum.  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class CheckCompliance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCompliant:bool = obj["opCompliant"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckOrderComplete_input:
   """ Required : 
   ds
   ipPackNum
   ipShipmentType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.ipPackNum:int = obj["ipPackNum"]
      """  Pack Num to validate  """  
      self.ipShipmentType:str = obj["ipShipmentType"]
      """  Type of shipment to validate  """  
      pass

class CheckOrderComplete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.msg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckOrder_input:
   """ Required : 
   packNum
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      """  The Pack Number to check out  """  
      pass

class CheckOrder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.msg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPCBinOutLocation_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class CheckPCBinOutLocation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.lineNum:int = obj["parameters"]
      self.belongToAnotherPC:bool = obj["belongToAnotherPC"]
      self.pcOutsideMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPackTaxIDForPackNum_input:
   """ Required : 
   packNum
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      pass

class CheckPackTaxIDForPackNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errorMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPackTaxID_input:
   """ Required : 
   packNum
   shipToNum
   otsOrderNum
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      self.shipToNum:str = obj["shipToNum"]
      self.otsOrderNum:int = obj["otsOrderNum"]
      pass

class CheckPackTaxID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPackageCodeAllocNegQty_input:
   """ Required : 
   ipcalledFrom
   ipPackNumList
   ipPkgCode
   ipPkgCodeQty
   """  
   def __init__(self, obj):
      self.ipcalledFrom:str = obj["ipcalledFrom"]
      self.ipPackNumList:object
      self.ipPkgCode:str = obj["ipPkgCode"]
      self.ipPkgCodeQty:int = obj["ipPkgCodeQty"]
      pass

class CheckPackageCodeAllocNegQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opWarning:str = obj["parameters"]
      self.opAction:str = obj["parameters"]
      self.opAllocWarning:str = obj["parameters"]
      self.opAllocAction:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPrePartInfo_input:
   """ Required : 
   partNum
   orderNum
   orderLine
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Customer Shipment data set  """  
      self.orderNum:int = obj["orderNum"]
      """  Pack Num to validate  """  
      self.orderLine:int = obj["orderLine"]
      """  Type of shipment to validate  """  
      pass

class CheckPrePartInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.vMsgText:str = obj["parameters"]
      self.vSubAvail:bool = obj["vSubAvail"]
      self.vMsgType:str = obj["parameters"]
      self.origPartNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckReadyToInvoice_input:
   """ Required : 
   readyToInvoice
   ds
   """  
   def __init__(self, obj):
      self.readyToInvoice:bool = obj["readyToInvoice"]
      """  Customer Shipment data set  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class CheckReadyToInvoice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.legalNumberMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckShipDtl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class CheckShipDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.releaseMessage:str = obj["parameters"]
      self.completeMessage:str = obj["parameters"]
      self.shippingMessage:str = obj["parameters"]
      self.lotMessage:str = obj["parameters"]
      self.inventoryMessage:str = obj["parameters"]
      self.lockQtyMessage:str = obj["parameters"]
      self.allocationMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckValidCartonWeight_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      pass

class CheckValidCartonWeight_output:
   def __init__(self, obj):
      pass

class ClearConvertedManifestUOMFields_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      pass

class ClearConvertedManifestUOMFields_output:
   def __init__(self, obj):
      pass

class ClearWarrantyInfo_input:
   """ Required : 
   ds
   orderLine
   orderRelNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.orderLine:int = obj["orderLine"]
      self.orderRelNum:int = obj["orderRelNum"]
      pass

class ClearWarrantyInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ConvertToManifestUOM_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      pass

class ConvertToManifestUOM_output:
   def __init__(self, obj):
      pass

class ConvertUOM_input:
   """ Required : 
   partNum
   baseQty
   baseUOM
   convUOM
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number  """  
      self.baseQty:int = obj["baseQty"]
      """  Qty you wish to convert  """  
      self.baseUOM:str = obj["baseUOM"]
      """  UOM baseQty is specified in  """  
      self.convUOM:str = obj["convUOM"]
      """  UOM to convert to  """  
      pass

class ConvertUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.convQty:int = obj["parameters"]
      pass

      """  output parameters  """  

class CreateCustomerCartons_input:
   """ Required : 
   ipNbrCartonsToCreate
   ipPkgCode
   ipPkgLength
   ipPkgWidth
   ipPkgHeight
   ipRecalcAmts
   ipZeroWeight
   ds
   """  
   def __init__(self, obj):
      self.ipNbrCartonsToCreate:int = obj["ipNbrCartonsToCreate"]
      self.ipPkgCode:str = obj["ipPkgCode"]
      self.ipPkgLength:int = obj["ipPkgLength"]
      self.ipPkgWidth:int = obj["ipPkgWidth"]
      self.ipPkgHeight:int = obj["ipPkgHeight"]
      self.ipRecalcAmts:bool = obj["ipRecalcAmts"]
      self.ipZeroWeight:bool = obj["ipZeroWeight"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class CreateCustomerCartons_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateLot_input:
   """ Required : 
   LotMessage
   PartListNeedsAttr
   LotListNeedsAttr
   ds
   """  
   def __init__(self, obj):
      self.LotMessage:str = obj["LotMessage"]
      """  Lot Message presented to the user showing lines that needed to be created  """  
      self.PartListNeedsAttr:str = obj["PartListNeedsAttr"]
      """  Parts requiring attributes to know if to exclude from the partlot create  """  
      self.LotListNeedsAttr:str = obj["LotListNeedsAttr"]
      """  Lots requiring attributes to know if to exclude from the partlot create  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class CreateLot_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateMassShipDtl_input:
   """ Required : 
   packNum
   orderNum
   ds
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      """  Pack Number to add new shipment lines to  """  
      self.orderNum:int = obj["orderNum"]
      """  Order Number to create shipment lines from  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class CreateMassShipDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreatePackForChangePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPackNum:int = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   packNum
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteKitComponents_input:
   """ Required : 
   ipPackNum
   ipPackLine
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipPackLine:int = obj["ipPackLine"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class DeleteKitComponents_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeletePhantomPacks_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class DeletePhantomPacks_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteRangePhantomPacks_input:
   """ Required : 
   ipFromCase
   ipToCase
   ds
   """  
   def __init__(self, obj):
      self.ipFromCase:int = obj["ipFromCase"]
      self.ipToCase:int = obj["ipToCase"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class DeleteRangePhantomPacks_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_CartonTrkDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company ID  """  
      self.ShipmentType:str = obj["ShipmentType"]
      """  Defines the type of shipment the tracking number is for.  Shipment type is either Misc for miscellaneous, Sales for Customer shipments, Sub for subcontractor shipments Transfer for Transfer order shipment or Master for Masterpack Shipments.  """  
      self.PackNum:int = obj["PackNum"]
      """  The pack number associated with the tracking number.  """  
      self.CaseNum:int = obj["CaseNum"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last CartonTrkDtl record for PackNum and add 1. This number is not displayed to the user.  The case number the user sees is the concatenation of the Packnum and this number separated by a dash.  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.PkgWeight:int = obj["PkgWeight"]
      """  Package Weight  """  
      self.CODFlag:bool = obj["CODFlag"]
      """  Prefer COD delivery.  Reserved for future development.  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery
Reserved for future development.  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order.  Reserved for future development.  """  
      self.DeclaredValueFlag:bool = obj["DeclaredValueFlag"]
      """  Flag to indicate that an insurance value was declared on delivery.  Reserved for future development.  """  
      self.DeclaredValue:int = obj["DeclaredValue"]
      """  Declared Insurance Amount.  Reserved for future development.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.CODValue:int = obj["CODValue"]
      """  Collect On Delivery Value  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CaseID:str = obj["CaseID"]
      """  Concatenated field consisting of PackNum and CaseNum separated by a dash.  """  
      self.PackStatus:str = obj["PackStatus"]
      """  Status of the shipment.  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  logical used by UI for row rules  """  
      self.CapturePt:str = obj["CapturePt"]
      self.EnablePhantom:bool = obj["EnablePhantom"]
      """  Logical indicating if the phantom cartonTrkDtl fields are to be enabled.  This is based upon whether or not the workstation is setup for manifesting.  """  
      self.KitPartAttrClassID:str = obj["KitPartAttrClassID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustShipCustTrkRow:
   def __init__(self, obj):
      self.PackNum:int = obj["PackNum"]
      """  From ShipHead.PackNum  """  
      self.ShipDate:str = obj["ShipDate"]
      """  From ShipHead.ShipDate  """  
      self.OrderNum:int = obj["OrderNum"]
      """  From ShipHead.OrderNum  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  From ShipHead.ReadyToInvoice  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  From ShipHead.Invoiced  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  From ShipHead.ShipViaCode  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  From ShipHead.TrackingNumber  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  From ShipHead.ShipPerson  """  
      self.Plant:str = obj["Plant"]
      """  From ShipHead.Plant  """  
      self.CustNum:int = obj["CustNum"]
      """  From ShipHead.CustNum  """  
      self.PackLine:int = obj["PackLine"]
      """  From ShipDtl.PackLine  """  
      self.OrderLine:int = obj["OrderLine"]
      """  From ShipDtl.OrderLine  """  
      self.PartNum:str = obj["PartNum"]
      """  From ShipDtl.PartNum  """  
      self.LineDesc:str = obj["LineDesc"]
      """  From ShipDtl.LineDesc  """  
      self.SellingInventoryShipQty:int = obj["SellingInventoryShipQty"]
      """  From ShipDtl.SellingInventoryShipQty  """  
      self.SellingJobShipQty:int = obj["SellingJobShipQty"]
      """  From ShipDtl.SellingJobShipQty  """  
      self.SalesUM:str = obj["SalesUM"]
      """  From ShipDtl.SalesUM  """  
      self.RequestDate:str = obj["RequestDate"]
      """  From OrderRel.ReqDate  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  From OrderRel.NeedByDate  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  From ShipDtl.ShipToNum  """  
      self.OnTime:int = obj["OnTime"]
      """  Calculated as ShipHead.ShipDate - OrderRel.ReqDate  """  
      self.Company:str = obj["Company"]
      """  From ShipHead.Company  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  from ShipHead.LegalNumber  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  from ShipDtl.RevisionNum  """  
      self.XPartNum:str = obj["XPartNum"]
      """  from ShipDtl.XPartNum  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  from ShipDtl.XRevisionNum  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Populated from OrderHed.BTCustNum  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  """  
      self.BTCustID:str = obj["BTCustID"]
      """  CustID associated with ShipHeadHead.BTCustNum.  """  
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  CustName associated with ShipHead.BTCustNum  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full customer's name.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  The name for the ship to location.  """  
      self.CustID:str = obj["CustID"]
      """  The customer ID.  """  
      self.InventoryShipUOM:str = obj["InventoryShipUOM"]
      self.JobShipUOM:str = obj["JobShipUOM"]
      self.OurInventoryShipQty:int = obj["OurInventoryShipQty"]
      self.OurJobShipQty:int = obj["OurJobShipQty"]
      self.SellingShipmentQty:int = obj["SellingShipmentQty"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PackSlip:str = obj["PackSlip"]
      self.DropShip:bool = obj["DropShip"]
      self.InvoiceNum:int = obj["InvoiceNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustShipCustTrkTableset:
   def __init__(self, obj):
      self.CustShipCustTrk:list[Erp_Tablesets_CustShipCustTrkRow] = obj["CustShipCustTrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CustShipOrdTrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  """  
      self.ShipLog:str = obj["ShipLog"]
      """  An optional field which can be used to enter a shipping log reference #.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  """  
      self.Plant:str = obj["Plant"]
      """  The Plant that shipment was made from.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Voided:bool = obj["Voided"]
      """  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Populated from OrderHed.BTCustNum.  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  """  
      self.ShipStatus:str = obj["ShipStatus"]
      self.ShipGroup:str = obj["ShipGroup"]
      self.PkgCode:str = obj["PkgCode"]
      self.PkgClass:str = obj["PkgClass"]
      self.Weight:int = obj["Weight"]
      self.ResDelivery:bool = obj["ResDelivery"]
      self.SatDelivery:bool = obj["SatDelivery"]
      self.SatPickup:bool = obj["SatPickup"]
      self.VerbalConf:bool = obj["VerbalConf"]
      self.Hazmat:bool = obj["Hazmat"]
      self.DocOnly:bool = obj["DocOnly"]
      self.RefNotes:str = obj["RefNotes"]
      self.ApplyChrg:bool = obj["ApplyChrg"]
      self.ChrgAmount:int = obj["ChrgAmount"]
      self.COD:bool = obj["COD"]
      self.CODFreight:bool = obj["CODFreight"]
      self.CODCheck:bool = obj["CODCheck"]
      self.CODAmount:int = obj["CODAmount"]
      self.GroundType:str = obj["GroundType"]
      self.NotifyFlag:bool = obj["NotifyFlag"]
      self.NotifyEMail:str = obj["NotifyEMail"]
      self.DeclaredIns:bool = obj["DeclaredIns"]
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      self.MFTransNum:str = obj["MFTransNum"]
      self.MFCallTag:str = obj["MFCallTag"]
      self.MFPickupNum:str = obj["MFPickupNum"]
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      self.MFTemplate:str = obj["MFTemplate"]
      self.MFUse3B:bool = obj["MFUse3B"]
      self.MF3BAccount:str = obj["MF3BAccount"]
      self.MFDimWeight:int = obj["MFDimWeight"]
      self.MFZone:str = obj["MFZone"]
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      self.MFOversized:bool = obj["MFOversized"]
      self.ServSatDelivery:bool = obj["ServSatDelivery"]
      self.ServSatPickup:bool = obj["ServSatPickup"]
      self.ServSignature:bool = obj["ServSignature"]
      self.ServAlert:bool = obj["ServAlert"]
      self.ServPOD:bool = obj["ServPOD"]
      self.ServAOD:bool = obj["ServAOD"]
      self.ServHomeDel:bool = obj["ServHomeDel"]
      self.DeliveryType:str = obj["DeliveryType"]
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      self.ServPhone:str = obj["ServPhone"]
      self.ServInstruct:str = obj["ServInstruct"]
      self.ServRelease:bool = obj["ServRelease"]
      self.ServAuthNum:str = obj["ServAuthNum"]
      self.ServRef1:str = obj["ServRef1"]
      self.ServRef2:str = obj["ServRef2"]
      self.ServRef3:str = obj["ServRef3"]
      self.ServRef4:str = obj["ServRef4"]
      self.ServRef5:str = obj["ServRef5"]
      self.BOLNum:int = obj["BOLNum"]
      self.BOLLine:int = obj["BOLLine"]
      self.PONum:str = obj["PONum"]
      self.OrderHold:bool = obj["OrderHold"]
      """  Indicates if Order is on Hold  """  
      self.JobNum:str = obj["JobNum"]
      self.BTCustID:str = obj["BTCustID"]
      """  CustID associated with ShipHeadHead.BTCustNum.  """  
      self.CartonHeight:int = obj["CartonHeight"]
      """  Carton Height  """  
      self.CartonWidth:int = obj["CartonWidth"]
      """  Carton Width  """  
      self.CartonLength:int = obj["CartonLength"]
      """  Carton Length  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  Used by the manifest system.  Sum of the value of items in the carton.  Item price - discount + sales tax.  """  
      self.LastCartonFlag:bool = obj["LastCartonFlag"]
      """  Set to Y if the carton is the last one being shiped to the customer.  If the sum of the quantity packed does not equal the quantity ordered for each line in the carton the value is No.  """  
      self.ManifestShipToName:str = obj["ManifestShipToName"]
      """  Ship to name for the manifest  """  
      self.ManifestShipToAddress:str = obj["ManifestShipToAddress"]
      """  Manifest Ship To Addres  """  
      self.ManifestShipToCity:str = obj["ManifestShipToCity"]
      """  Manifest ship to city  """  
      self.ManifestShipToRegion:str = obj["ManifestShipToRegion"]
      """  State or region value  """  
      self.ManifestShipToPostalCode:str = obj["ManifestShipToPostalCode"]
      """  Zip Code  """  
      self.ManifestShipToCountry:str = obj["ManifestShipToCountry"]
      """  ship to country  """  
      self.ManifestShipToTerritory:str = obj["ManifestShipToTerritory"]
      """  Ship to Territory  """  
      self.ManifestShipToAttention:str = obj["ManifestShipToAttention"]
      """  Ship to Attention  """  
      self.ManifestShipToPhone:str = obj["ManifestShipToPhone"]
      """  Phone number  """  
      self.ManifestShipToFax:str = obj["ManifestShipToFax"]
      """  Fax Number  """  
      self.ManifestSoldToName:str = obj["ManifestSoldToName"]
      """  Sold To Name  """  
      self.ManifestSoldToAddress:str = obj["ManifestSoldToAddress"]
      """  Sold To Address  """  
      self.ManifestSoldToCity:str = obj["ManifestSoldToCity"]
      """  Sold To City  """  
      self.ManifestSoldToRegion:str = obj["ManifestSoldToRegion"]
      """  Sold To State/Region  """  
      self.ManifestSoldToPostalCode:str = obj["ManifestSoldToPostalCode"]
      """  Sold To Postal Cod  """  
      self.ManifestSoldToCountry:str = obj["ManifestSoldToCountry"]
      """  Sold To Country  """  
      self.ManifestSoldToTerritory:str = obj["ManifestSoldToTerritory"]
      self.ManifestSoldToAttention:str = obj["ManifestSoldToAttention"]
      """  Sold To Attention  """  
      self.ManifestSoldToPhone:str = obj["ManifestSoldToPhone"]
      """  Sold to Phone number  """  
      self.ManifestSoldToFax:str = obj["ManifestSoldToFax"]
      """  Sold To Fax Number  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage Number.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable, It is carried forward through from the ShipHead.OrderNum field.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this shipment detail line is linked to.  Must be valid in the OrderDtl file.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      self.PkgLength:int = obj["PkgLength"]
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      self.PkgWidth:int = obj["PkgWidth"]
      self.WeightUOM:str = obj["WeightUOM"]
      self.DropShip:bool = obj["DropShip"]
      self.PackSlip:str = obj["PackSlip"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustShipOrdTrkTableset:
   def __init__(self, obj):
      self.CustShipOrdTrk:list[Erp_Tablesets_CustShipOrdTrkRow] = obj["CustShipOrdTrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CustShipPickedOrdersTableset:
   def __init__(self, obj):
      self.PickedOrders:list[Erp_Tablesets_PickedOrdersRow] = obj["PickedOrders"]
      self.MtlQueue:list[Erp_Tablesets_MtlQueueRow] = obj["MtlQueue"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CustShipTableset:
   def __init__(self, obj):
      self.ShipHead:list[Erp_Tablesets_ShipHeadRow] = obj["ShipHead"]
      self.ShipHeadAttch:list[Erp_Tablesets_ShipHeadAttchRow] = obj["ShipHeadAttch"]
      self.CartonTrkDtl:list[Erp_Tablesets_CartonTrkDtlRow] = obj["CartonTrkDtl"]
      self.ShipDtl:list[Erp_Tablesets_ShipDtlRow] = obj["ShipDtl"]
      self.ShipDtlAttch:list[Erp_Tablesets_ShipDtlAttchRow] = obj["ShipDtlAttch"]
      self.ShipCOO:list[Erp_Tablesets_ShipCOORow] = obj["ShipCOO"]
      self.ShipDtlPackaging:list[Erp_Tablesets_ShipDtlPackagingRow] = obj["ShipDtlPackaging"]
      self.ShipDtlTax:list[Erp_Tablesets_ShipDtlTaxRow] = obj["ShipDtlTax"]
      self.ShipHeadInsurance:list[Erp_Tablesets_ShipHeadInsuranceRow] = obj["ShipHeadInsurance"]
      self.ShipMisc:list[Erp_Tablesets_ShipMiscRow] = obj["ShipMisc"]
      self.ReplicatedPacks:list[Erp_Tablesets_ReplicatedPacksRow] = obj["ReplicatedPacks"]
      self.ShipHeadTrailer:list[Erp_Tablesets_ShipHeadTrailerRow] = obj["ShipHeadTrailer"]
      self.ShipUPS:list[Erp_Tablesets_ShipUPSRow] = obj["ShipUPS"]
      self.LegalNumberGenerate:list[Erp_Tablesets_LegalNumberGenerateRow] = obj["LegalNumberGenerate"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SalesKitCompIssue:list[Erp_Tablesets_SalesKitCompIssueRow] = obj["SalesKitCompIssue"]
      self.SelectedIDNumbers:list[Erp_Tablesets_SelectedIDNumbersRow] = obj["SelectedIDNumbers"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.ShipTaxSum:list[Erp_Tablesets_ShipTaxSumRow] = obj["ShipTaxSum"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LLComSerMatchRow:
   def __init__(self, obj):
      self.ParentPartNum:str = obj["ParentPartNum"]
      self.ParentPartDesc:str = obj["ParentPartDesc"]
      self.ChildPartNum:str = obj["ChildPartNum"]
      self.ChildPartDesc:str = obj["ChildPartDesc"]
      self.SerialNumber:str = obj["SerialNumber"]
      self.ParentSerialNum:str = obj["ParentSerialNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LLCompSerMatchTableset:
   def __init__(self, obj):
      self.LLComSerMatch:list[Erp_Tablesets_LLComSerMatchRow] = obj["LLComSerMatch"]
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

class Erp_Tablesets_LegalNumberGenerateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.NumberType:str = obj["NumberType"]
      self.NumberYear:int = obj["NumberYear"]
      self.NumberPrefix:str = obj["NumberPrefix"]
      """  The legal number prefix  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      self.PrefixList:str = obj["PrefixList"]
      self.GenerationType:str = obj["GenerationType"]
      self.EnableNumberPrefix:bool = obj["EnableNumberPrefix"]
      self.EnableNumberSuffix:bool = obj["EnableNumberSuffix"]
      self.NumberOption:str = obj["NumberOption"]
      self.LegalNumberNum:int = obj["LegalNumberNum"]
      """  Unique identifier of the Legal Number record  """  
      self.DocumentDate:str = obj["DocumentDate"]
      self.AdditionalParams:str = obj["AdditionalParams"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MtlQueueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time(seconds since midnight) when transaction was created.  """  
      self.MtlQueueSeq:int = obj["MtlQueueSeq"]
      """  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity  """  
      self.TranType:str = obj["TranType"]
      """   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  """  
      self.ReferencePrefix:str = obj["ReferencePrefix"]
      """   Used as a translatable prefix for the Reference field.
For example for a purchase receipt of stock it has "PS", (Packing Slip). For display purposes this is field is translated, then concatenated with the value in the Refernce field. 
Other values are "Job",  """  
      self.Reference:str = obj["Reference"]
      """  Contains a reference about the request. May contain Job/Asm/Seq, WrkCtr,  Packing Slip #,  Sales Order, etc...depending on the TranType.  """  
      self.RequestedByEmpID:str = obj["RequestedByEmpID"]
      """  Employee ID that made the request.  """  
      self.SelectedByEmpID:str = obj["SelectedByEmpID"]
      """  Employee ID that has selected this record from the queue for processing.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the request is related to.  This allows sorting by Job, which provides the user a method of working on all the requests for a specific job.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "O" = Job Operation (JobOper).  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of the related specific material or operation record.  For WIP parts it's the operation sequence that created the part. For raw materials it's the related JobMtl.MtlSeq.  """  
      self.FromWhse:str = obj["FromWhse"]
      """  Warehouse Code where item is to be found. For example a Get Raw Material request of a stocked part  would be the warehouse  the requirement was allocated against (JobMtl.WareHouseCode).  A "Move of a WIP part" will contain the Warehouse defined by the WrkCenter.PutWhse...  """  
      self.FromBinNum:str = obj["FromBinNum"]
      """  Warehouse bin where item is to be found. For example a Get Raw Material request of a stocked part  would be the Primary Bin of the part/warehouse, if no primary bin, then the first Bin in the warehouse which contains this part, else blank.  A "Move of a WIP part" will contain the bin defined by the WrkCenter.PutBin...  """  
      self.ToWhse:str = obj["ToWhse"]
      """  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  """  
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      """  Assembly sequence of the operation that completed quantity of the job operation  will be moved to.  """  
      self.NextJobSeq:int = obj["NextJobSeq"]
      """  Sequence of the operation that completed quantity of the job operation will be moved to.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date the this request is needed by.  Defaults, to current system date.  """  
      self.NeedByTime:int = obj["NeedByTime"]
      """  Time (seconds since midnight) that request is need by.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor number of the related purchase receipt (RcvDtl).  Company,VendorNum, PurPoint, PackSlip,Packline are used to provide the link to the related RcvDtl record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point id of the related purchase receipt (RcvDtl).  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip # of the related RcvDtl.  """  
      self.PackLine:int = obj["PackLine"]
      """  Vendors Packing Slip line  # of the related RcvDtl.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   Order number job is making parts for. (See JobProd.OrderNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

OrderNum pertains only to "make to order" requirements.  
Provides relationship to the JobProd for "make to order" requirements.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related Sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Related sales order release number.  """  
      self.TargetJobNum:str = obj["TargetJobNum"]
      """   Job that this job is making parts for. (See JobProd.TargetJobNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

TargetJobNum pertains only to "make to job" requirements.  
Provides relationship to the JobProd for "make to Job" requirements.  """  
      self.TargetAssemblySeq:int = obj["TargetAssemblySeq"]
      """  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.TargetMtlSeq:int = obj["TargetMtlSeq"]
      """  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  A description of the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Internal unit of measure.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.Visible:bool = obj["Visible"]
      """  Indicates if this MtlQueue is visible to the user on the Material Queue browse.  Set based on the users response to make a "move  request" when reporting quantities.  Set to true visible), if a move request is made.  This was implemented to keep track of labor quantity reported without making a move request.  The move request will then reflect the total quantity to move instead of what was reported on the labor transaction that requested the move.  Regardless of making a "Move Request" labor quantity reporting always creates/updates a MtlQueue record.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMAReceipt number of the related RMARcpt record.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMADisp number of the related RMADisp record.  """  
      self.NCTranID:int = obj["NCTranID"]
      """  The related NonConf.TranID number. Used to link the MtlQueue table to the NonConf table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the part.  """  
      self.Lock:bool = obj["Lock"]
      """  Indicates this record has been locked by a Advanced Shipping user and is not available for processing by any other user.  """  
      self.QueueID:str = obj["QueueID"]
      """  Used by Advanced Shipping to designate which queue this record is in.  Advanced Shipping queues can prioritize and process records.  """  
      self.QueuePickSeq:int = obj["QueuePickSeq"]
      """  Sequence of this record within an Advanced Shipping Queue.  """  
      self.ReleaseForPickingSeq:int = obj["ReleaseForPickingSeq"]
      """  This is an internal sequence number for grouping MtlQueue records.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group that was assigned to this transaction.  """  
      self.TranStatus:str = obj["TranStatus"]
      """   The status of the transaction of the material.  Valid values:
MGMT-LOCK - Manager locked, RELEASED - Released, HOLD - On Hold, USER-LOCK - Locked for a user, ORDER-HOLD - On Hold for Order Based Picking, QUALITY-HOLD - On Hold for Quality Control, and PICK-PACK - Three step allocation Pick-Pack Method  """  
      self.WaveNum:int = obj["WaveNum"]
      """  The Wave that was assigned during the allocation process.  """  
      self.Priority:int = obj["Priority"]
      """  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  One is the highest priority.  """  
      self.TranSource:str = obj["TranSource"]
      """  Transaction Source  """  
      self.LastMgrChangeEmpID:str = obj["LastMgrChangeEmpID"]
      """  When the TranStatus, AssignedToEmpID or Priority are modified, this value is updated with the ID of the Manager making the change.  """  
      self.AssignedToEmpID:str = obj["AssignedToEmpID"]
      """  Employee ID that was selected by the Warehouse Manager to process record from the queue.  """  
      self.TargetTFOrdNum:str = obj["TargetTFOrdNum"]
      """  Transfer Order for which Demand is being satisfied.  """  
      self.TargetTFOrdLine:int = obj["TargetTFOrdLine"]
      """  Transfer Order Line for which Demand is being satisfied.  """  
      self.PackStation:str = obj["PackStation"]
      """  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.LastUsedPCID:str = obj["LastUsedPCID"]
      """  Last Used PCID on the selected line.  """  
      self.FromPCID:str = obj["FromPCID"]
      """  The PCID from which the material movement will occur.  """  
      self.ToPCID:str = obj["ToPCID"]
      """  The PCID to which the material movement will occur.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      """  AttributeValueSeq  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.CustID:str = obj["CustID"]
      self.CustTerritoryID:str = obj["CustTerritoryID"]
      self.DisableTO:bool = obj["DisableTO"]
      """  Indicates whether Transfer Order Selector Flag should be disabled.  """  
      self.FromInv:bool = obj["FromInv"]
      """  From Inventory Selector Flag  """  
      self.FromJob:bool = obj["FromJob"]
      """  From Manufacturing Selector Flag  """  
      self.FromPO:bool = obj["FromPO"]
      """  From Purchasing Selector Flag  """  
      self.FromTO:bool = obj["FromTO"]
      """  From Transfer Order Selector Flag  """  
      self.FromWhseDesc:str = obj["FromWhseDesc"]
      self.FSAServiceOrderNumber:int = obj["FSAServiceOrderNumber"]
      """  Service Order Number from FSA. Only available in FSA Request Workbench.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource Num from FSA. Only available in FSA Request Workbench.  """  
      self.HoldStatus:bool = obj["HoldStatus"]
      self.LeadTime:int = obj["LeadTime"]
      self.MaxMfgLotSize:int = obj["MaxMfgLotSize"]
      self.MfgLeadTime:int = obj["MfgLeadTime"]
      self.MinMfgLotSize:int = obj["MinMfgLotSize"]
      self.NeedByTimeDisp:str = obj["NeedByTimeDisp"]
      self.NonStock:bool = obj["NonStock"]
      self.OkToProcess:bool = obj["OkToProcess"]
      """  Holds the result of checking sub-menu security.  NO indicates the current user does not have permission to carry out the indicated TranType.  """  
      self.OnHandQtySite:int = obj["OnHandQtySite"]
      self.OnHandQtyWhse:int = obj["OnHandQtyWhse"]
      self.PlantName:str = obj["PlantName"]
      self.PrimWhseCode:str = obj["PrimWhseCode"]
      self.PrimWhseDesc:str = obj["PrimWhseDesc"]
      self.RequestedByEmpName:str = obj["RequestedByEmpName"]
      self.RequestError:bool = obj["RequestError"]
      """  Indicates whether an error occured in processing.  """  
      self.RequestMsg:str = obj["RequestMsg"]
      """  Message used to return status information after processing.  """  
      self.SameWhseGroupEmp:bool = obj["SameWhseGroupEmp"]
      """  Is this material queue row part of the employees warehouse group  """  
      self.SelectedByEmpName:str = obj["SelectedByEmpName"]
      self.SelectedForProcessing:bool = obj["SelectedForProcessing"]
      """  Used by user to select rows for mass processing  """  
      self.ShipToCity:str = obj["ShipToCity"]
      self.ShipToCountry:str = obj["ShipToCountry"]
      self.ShipToName:str = obj["ShipToName"]
      """  Customer Ship To Name  """  
      self.ShipToNum:str = obj["ShipToNum"]
      self.ShipToState:str = obj["ShipToState"]
      self.ShipToZIP:str = obj["ShipToZIP"]
      self.SortByPriority:int = obj["SortByPriority"]
      """  Sort priority from highest to lowest (1,2,3,4,5,6,7,8,9,0)  """  
      self.SourceTypeDesc:str = obj["SourceTypeDesc"]
      """  Transfer, Sales Kit, Manufactured or Purchased.  """  
      self.ToWhseDesc:str = obj["ToWhseDesc"]
      self.TransferLeadTime:int = obj["TransferLeadTime"]
      self.TransferPlant:str = obj["TransferPlant"]
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Readable tran type (used in Replenishment Workbench)  """  
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.WaveRelated:bool = obj["WaveRelated"]
      """  Value is true if this mtlqueue record is related to a wave. False if it is not.  """  
      self.CustRegionCode:str = obj["CustRegionCode"]
      """  Customer Sales Territory Region Code  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Display (decimal) number of pieces for inventory tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumVendorID_:str = obj["VendorNumVendorID_"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName_:str = obj["VendorNumName_"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.WarehouseGroupCodeWhseGroupDesc:str = obj["WarehouseGroupCodeWhseGroupDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POSNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """  Serial Number base data type  """  
      self.SNFormat:str = obj["SNFormat"]
      """  Serial Number format  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Current Prefix setting  """  
      self.Plant:str = obj["Plant"]
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      self.SNMask:str = obj["SNMask"]
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POSelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SNPrefix:str = obj["SNPrefix"]
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask that was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment, needed here to keep POSelectedSerialNumbers in sync with SelectedSerialNumbers  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: needed here to keep POSelctedSerialNumbers in sync with SelectedSerialNumbers  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PackOutRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PackNum:int = obj["PackNum"]
      self.ShipViaCode:str = obj["ShipViaCode"]
      self.EntryPerson:str = obj["EntryPerson"]
      self.LabelComment:str = obj["LabelComment"]
      self.ShipComment:str = obj["ShipComment"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.CustNum:int = obj["CustNum"]
      self.PackLine:int = obj["PackLine"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.LineType:str = obj["LineType"]
      self.OurInventoryShipQty:int = obj["OurInventoryShipQty"]
      self.OurJobShipQty:int = obj["OurJobShipQty"]
      self.JobNum:str = obj["JobNum"]
      self.PartNum:str = obj["PartNum"]
      self.LineDesc:str = obj["LineDesc"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.ShipCmpl:bool = obj["ShipCmpl"]
      self.BinNum:str = obj["BinNum"]
      self.ShpConNum:int = obj["ShpConNum"]
      self.LotNum:str = obj["LotNum"]
      self.DimCode:str = obj["DimCode"]
      self.DUM:str = obj["DUM"]
      self.DimConvFactor:int = obj["DimConvFactor"]
      self.InvoiceComment:str = obj["InvoiceComment"]
      self.ShipStatus:str = obj["ShipStatus"]
      self.Stage:str = obj["Stage"]
      self.BTCustomerName:str = obj["BTCustomerName"]
      self.BTConNum:int = obj["BTConNum"]
      self.BTCustID:str = obj["BTCustID"]
      self.InvQty:int = obj["InvQty"]
      self.PackQty:int = obj["PackQty"]
      self.ShipAddr:str = obj["ShipAddr"]
      self.StockPart:bool = obj["StockPart"]
      self.CustName:str = obj["CustName"]
      self.KitPartNum:str = obj["KitPartNum"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.KitNumPartDescription:str = obj["KitNumPartDescription"]
      self.KitPartRev:str = obj["KitPartRev"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.TotRelQty:int = obj["TotRelQty"]
      self.PromptPartRev:bool = obj["PromptPartRev"]
      self.PromptKitRevision:bool = obj["PromptKitRevision"]
      self.PromptJobNum:bool = obj["PromptJobNum"]
      self.PromptOrderRel:bool = obj["PromptOrderRel"]
      self.PromptKit:bool = obj["PromptKit"]
      self.AutoQuantity:bool = obj["AutoQuantity"]
      self.PromptOrderLine:bool = obj["PromptOrderLine"]
      self.ToPlant:str = obj["ToPlant"]
      self.FromPlant:str = obj["FromPlant"]
      self.FromAddr:str = obj["FromAddr"]
      self.PackMode:str = obj["PackMode"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.BTCustNum:int = obj["BTCustNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.NumMatchs:int = obj["NumMatchs"]
      self.PackOutNum:int = obj["PackOutNum"]
      """  Unique identifer for the PackOut dataset  """  
      self.Plant:str = obj["Plant"]
      self.IsInvoiced:bool = obj["IsInvoiced"]
      self.MFTransNum:str = obj["MFTransNum"]
      self.TrackingNumber:str = obj["TrackingNumber"]
      self.MFCallTag:str = obj["MFCallTag"]
      self.MFPickUpNum:str = obj["MFPickUpNum"]
      self.MFZone:str = obj["MFZone"]
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      self.MFOversized:bool = obj["MFOversized"]
      self.MFTemplate:str = obj["MFTemplate"]
      self.MFDimWeight:int = obj["MFDimWeight"]
      self.ShipDate:str = obj["ShipDate"]
      self.VendorID:str = obj["VendorID"]
      self.Quantity:int = obj["Quantity"]
      self.TotPackedQty:int = obj["TotPackedQty"]
      self.RemainQty:int = obj["RemainQty"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.HasCartonLines:bool = obj["HasCartonLines"]
      """  Set from ShipHead.HasCartonLines  """  
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.PORelNum:int = obj["PORelNum"]
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  """  
      self.ShipStatusXlate:str = obj["ShipStatusXlate"]
      self.PkgCode:str = obj["PkgCode"]
      self.PkgClass:str = obj["PkgClass"]
      self.KitFlag:str = obj["KitFlag"]
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height of packaging  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  If zero the packaging height prompt is enabled.  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length of packaging  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Zero indicates the length is to be enabled.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width of packaging  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  Zero indicates the width prompt is enabled.  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      self.CODAmount:int = obj["CODAmount"]
      """  COD Amount  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Decared Insurance Amount  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  Logical indicating this pack has phantom cases.  Used by UI to disable phantom controlled fields.  """  
      self.Weight:int = obj["Weight"]
      """  Pack weight.  """  
      self.MasterpackPackNum:int = obj["MasterpackPackNum"]
      """  Masterpack PackID this pack is on.  """  
      self.EnableWhseBin:bool = obj["EnableWhseBin"]
      """  Enables the Warehouse and Bin fields on the UIApp  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      """  0 indicates Pkg Size UOM should be enabled  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      self.WeightUOM:str = obj["WeightUOM"]
      self.InventoryShipUOM:str = obj["InventoryShipUOM"]
      self.JobShipUOM:str = obj["JobShipUOM"]
      self.EnablePOSerialBtn:bool = obj["EnablePOSerialBtn"]
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer  """  
      self.EnablePackageControl:bool = obj["EnablePackageControl"]
      """  Boolean indicating if the package control functionality should be enabled.  """  
      self.PCID:str = obj["PCID"]
      self.ShipToWarning:str = obj["ShipToWarning"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      """  temp message to display newly created legal number  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number associated with pack  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID associated with Pack.  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  TranDocType Description associated with this Pack  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.KitAttributeSetID:int = obj["KitAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.KitAttributeSetDescription:str = obj["KitAttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.KitAttributeSetShortDescription:str = obj["KitAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for pack out  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      self.EnableReadyToInvoice:bool = obj["EnableReadyToInvoice"]
      """  Indicates if Ready to Invoice is enabled or not  """  
      self.ShipToInactive:bool = obj["ShipToInactive"]
      """  Indicates if the record is inactive.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PackOutTableset:
   def __init__(self, obj):
      self.PackOut:list[Erp_Tablesets_PackOutRow] = obj["PackOut"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.POSelectedSerialNumbers:list[Erp_Tablesets_POSelectedSerialNumbersRow] = obj["POSelectedSerialNumbers"]
      self.POSNFormat:list[Erp_Tablesets_POSNFormatRow] = obj["POSNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PackageControlPackVoidRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CustContainerPartNum:str = obj["CustContainerPartNum"]
      self.CustID:str = obj["CustID"]
      self.EDIShipToNum:str = obj["EDIShipToNum"]
      self.LineDesc:str = obj["LineDesc"]
      self.Name:str = obj["Name"]
      self.OurDock:str = obj["OurDock"]
      self.PackLine:int = obj["PackLine"]
      self.PackNum:int = obj["PackNum"]
      self.PartNum:str = obj["PartNum"]
      self.Plant:str = obj["Plant"]
      self.ShipComment:str = obj["ShipComment"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.ShipStatus:str = obj["ShipStatus"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number associated with the PackNum record.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  Description  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.PartTrackInventoryByRevision:bool = obj["PartTrackInventoryByRevision"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PackageControlPackVoidTableset:
   def __init__(self, obj):
      self.PackageControlPackVoid:list[Erp_Tablesets_PackageControlPackVoidRow] = obj["PackageControlPackVoid"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PickedOrdersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order Number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order Line number that this order release is linked to.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse picked item is located in.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin picked item is located in.  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job that is supplying the allocated quantity.  This is blank for a shipment from stock.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the parts that were picked.  """  
      self.Quantity:int = obj["Quantity"]
      """  Picked quantity.  Our units.  """  
      self.UOM:str = obj["UOM"]
      """  Unit of Measure that Quantity is specified in. Must be a valid UOM.  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Date which the item needs to be shipped by in order to meet the customers due date. Mirror image of OrderRel.ReqDate.  Duplicated here for sorting purposes.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum for sorting purposes.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """   ShipTo ID of sales order release.
Duplicated from OrderRel.ShipToNum for sorting purposes.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Ship Via ID duplicated from the OrderRel.ShipViaCode.  Used in the process of generating packing slips from the PickedOrder table.  Each PickedOrders record will become a ShipDtl.   A new Packing slip will be created for each break of Company/Site/Ship Da  """  
      self.PartNum:str = obj["PartNum"]
      """  The picked part number.  Normally this would be the same as what's on the related OrderDtl. However, it may be different to allow for substitute parts.  """  
      self.Complete:bool = obj["Complete"]
      """  Sales Order Release has been picked.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Populated from OrderHed.BTCustNum  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.HoldPrdInv:bool = obj["HoldPrdInv"]
      """  The Hold Product Invoices flag value for the Project  """  
      self.IsSelected:bool = obj["IsSelected"]
      self.IsVisible:bool = obj["IsVisible"]
      self.OTSAddr:str = obj["OTSAddr"]
      """  Contains OTS address  """  
      self.ParentPCID:str = obj["ParentPCID"]
      self.ProjectID:str = obj["ProjectID"]
      """  The ProjectID  """  
      self.ConInvMeth:str = obj["ConInvMeth"]
      """  The Invoicing Method of the Project  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReplicatedPacksRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company ID  """  
      self.PackNum:int = obj["PackNum"]
      """  Parent Pack ID that is used to create the replicated packs.  """  
      self.ReplicatedPackNum:int = obj["ReplicatedPackNum"]
      """  This is the pack num that was generated based upon the parent pack num.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat:str = obj["SNFormat"]
      """   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  """  
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesKitCompIssueRow:
   def __init__(self, obj):
      self.KitPartNum:str = obj["KitPartNum"]
      self.KitDescription:str = obj["KitDescription"]
      self.KitWarehouseCodeDesc:str = obj["KitWarehouseCodeDesc"]
      self.KitWarehouse:str = obj["KitWarehouse"]
      self.KitWhseList:str = obj["KitWhseList"]
      self.PackNum:int = obj["PackNum"]
      self.PackLine:int = obj["PackLine"]
      self.KitQtyFromInv:int = obj["KitQtyFromInv"]
      self.KitIUM:str = obj["KitIUM"]
      self.KitLotNum:str = obj["KitLotNum"]
      self.KitBinNum:str = obj["KitBinNum"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.KitBinNumEnabled:bool = obj["KitBinNumEnabled"]
      self.KitTrackLots:bool = obj["KitTrackLots"]
      self.KitSerialTracked:bool = obj["KitSerialTracked"]
      self.KitQtyFromInvEnabled:bool = obj["KitQtyFromInvEnabled"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsRow:
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The part number to which the serial numbers have been assigned.  """  
      self.quantity:int = obj["quantity"]
      """  The quantity of serial numbers that need to be selected.  """  
      self.whereClause:str = obj["whereClause"]
      """  whereClause for filtering available serial numbers  """  
      self.transType:str = obj["transType"]
      """  transType of this transaction  """  
      self.sourceRowID:str = obj["sourceRowID"]
      """  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  """  
      self.enableCreate:bool = obj["enableCreate"]
      """  Determines if serial numbers can be created.  """  
      self.enableSelect:bool = obj["enableSelect"]
      """  Determines if serial numbers can be selected.  """  
      self.enableRetrieve:bool = obj["enableRetrieve"]
      """  Determines if serial numbers can be retrieved.  """  
      self.allowVoided:bool = obj["allowVoided"]
      """  Specifies whether Voided serial numbers can be manually selected.  """  
      self.plant:str = obj["plant"]
      """  The Plant associated with this transaction  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      self.xrefPartType:str = obj["xrefPartType"]
      self.xrefCustNum:int = obj["xrefCustNum"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.attributeSetShortDescription:str = obj["attributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.revisionNum:str = obj["revisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsTableset:
   def __init__(self, obj):
      self.SelectSerialNumbersParams:list[Erp_Tablesets_SelectSerialNumbersParamsRow] = obj["SelectSerialNumbersParams"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SelectedIDNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.IDNumber:str = obj["IDNumber"]
      self.JobNum:str = obj["JobNum"]
      self.PackLine:int = obj["PackLine"]
      self.PackNum:int = obj["PackNum"]
      self.PartNum:str = obj["PartNum"]
      self.SeqNum:int = obj["SeqNum"]
      self.SerialNumber:str = obj["SerialNumber"]
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this ID number  """  
      self.TransType:str = obj["TransType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialMatchingParamsTableset:
   def __init__(self, obj):
      self.serialNumbersToMatch:list[Erp_Tablesets_serialNumbersToMatchRow] = obj["serialNumbersToMatch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ShipCOORow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.OrigCountry:int = obj["OrigCountry"]
      """  CountryNum for Country of Origin  """  
      self.QtyPerc:int = obj["QtyPerc"]
      """  Qty percent of this part which is from this country of origin.  """  
      self.ValuePerc:int = obj["ValuePerc"]
      """  Value percent of this part from this country of origin.  """  
      self.Primary:bool = obj["Primary"]
      """  Is this the primary country of origin for this part  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the country of origin is related. ?ShipDtl?, ?MscShpDt?, ?TFShipDtl?, and ?SubShipD?  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipDtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PackNum:int = obj["PackNum"]
      self.PackLine:int = obj["PackLine"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipDtlPackagingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PackNum:int = obj["PackNum"]
      self.PackLine:int = obj["PackLine"]
      self.ParentPkgNum:int = obj["ParentPkgNum"]
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeDesc:str = obj["TranDocTypeDesc"]
      self.PkgCode:str = obj["PkgCode"]
      self.PkgCodeDesc:str = obj["PkgCodeDesc"]
      self.PkgSerialNum:str = obj["PkgSerialNum"]
      self.PkgLength:int = obj["PkgLength"]
      self.PkgWidth:int = obj["PkgWidth"]
      self.PkgHeight:int = obj["PkgHeight"]
      self.SizeUOM:str = obj["SizeUOM"]
      self.Weight:int = obj["Weight"]
      self.WeightUOM:str = obj["WeightUOM"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.PartNum:str = obj["PartNum"]
      self.OurQty:int = obj["OurQty"]
      self.IUM:str = obj["IUM"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable, It is carried forward through from the ShipHead.OrderNum field.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this shipment detail line is linked to.  Must be valid in the OrderDtl file.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.OurInventoryShipQty:int = obj["OurInventoryShipQty"]
      """  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand.  This quantity is in the IUM unit of measure.  """  
      self.OurJobShipQty:int = obj["OurJobShipQty"]
      """  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This quantity is in the IUM unit of measure.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that supplied the quantity that was shipped. Defaulted from OrderRel.JobNum.  """  
      self.Packages:int = obj["Packages"]
      """  Number of Packages  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Description  """  
      self.IUM:str = obj["IUM"]
      """  Unit of measure...duplicated from the OrderDtl.IUM...Not user maintainable.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  """  
      self.ShipComment:str = obj["ShipComment"]
      """   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  """  
      self.ShipCmpl:bool = obj["ShipCmpl"]
      """  Indicates if this shipment should mark the order release as being shipped complete. Only one ShipDtl for a release can be marked as being complete. As the user toggles this field it also sets the OrderRel.ShipCmpl field and adjusts the PartBin.OnHand, PartWhse.AllocQty if necessary.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """   Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.

The default should be retrieved from the OrderDtl.WareHseCode. .  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.UpdatedInventory:bool = obj["UpdatedInventory"]
      """  Indicates if this transaction affected inventory at time of creation.  """  
      self.XPartNum:str = obj["XPartNum"]
      """   An optional field that is used if the customer has a different  Part number  than the users internal part number.
This field is defaulted from the OrderDtl.XPartNum.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the OrderDtl.XRevisionNum field.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table. This is duplicated from the OrderRel.ShpConNum.  """  
      self.TMBilling:bool = obj["TMBilling"]
      """  Indicates if this shipment line item will be invoiced for time and materials. This is not maintainable from within shipment entry. It is duplicated from the OrderDtl.TMBilling. The "Get Shipments" function of Invoice Entry uses this flag to automatically create invoices in a "On Hold" status. The idea is that these type of invoices need to be generated to act as a method of tracking invoice requirements, but they cannot yet be invoiced until all the costs are known. At which time the user will enter the appropriate charges, take it off "Hold" and complete the billing process.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  A flag which indicates "invoicing" status. This is a mirror image of ShipHead.Invoiced field. See ShipHead.Invoiced for further info.  """  
      self.WUM:str = obj["WUM"]
      """  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...). Defaulted from XASyst.DefaultWUM  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number is for Inventory Shipments.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  These comments will be copied into the Invoice detail.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the shipment is for.  Duplicated from ShipHead.CustNum.  Used to allow efficient browsing of the ShipDtl records for a specific customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The shipto number. Used for warranty validation.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  For Warranty shipments.  Defaults as Shiphead.shipdate. But can be maintained from the Service Call center.  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The # of days, months, years the material is covered by warranty  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The # of days, months, years the Labor is covered by warranty  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The # of days, months, years the Misc. Charges are covered by warranty  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Whether the duration of warranty  is for "Days", " Months", "years".  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Whether the duration of warranty  is "Days"," Months"," years".  """  
      self.MiscMod:str = obj["MiscMod"]
      """  Whether the duration of warranty  is for "Days"," Months"," years".  """  
      self.MaterialExpiration:str = obj["MaterialExpiration"]
      """  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.LaborExpiration:str = obj["LaborExpiration"]
      """  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.MiscExpiration:str = obj["MiscExpiration"]
      """  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.LastExpiration:str = obj["LastExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.Onsite:bool = obj["Onsite"]
      """  This warranty covers On site visits  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.Plant:str = obj["Plant"]
      """  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the Packing Slip is complete and ready for invoicing.  This is a mirror image of ShipHead.ReadyToInvoice.  """  
      self.SellingInventoryShipQty:int = obj["SellingInventoryShipQty"]
      """  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand. This quantity is a mirror of field OurInventoryShipQty except it is in the SUM unit of measure.  """  
      self.SellingJobShipQty:int = obj["SellingJobShipQty"]
      """  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This field is a mirror of OurJobShipQty except it is in the SUM unit of measure.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit of Measure...duplicated from the OrderDtl.SUM...Not user maintainable.  """  
      self.TotalNetWeight:int = obj["TotalNetWeight"]
      """  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  """  
      self.WIPWarehouseCode:str = obj["WIPWarehouseCode"]
      """   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  """  
      self.WIPBinNum:str = obj["WIPBinNum"]
      """   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.HeaderShipComment:str = obj["HeaderShipComment"]
      """  Packing slip comments.  These are comments off of the invoice header.  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  The packline of the kit parent  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.InventoryShipUOM:str = obj["InventoryShipUOM"]
      """  Unit of Measure of the quantity shipped from Inventory (OurInventoryShipQty). Must be a valid UOM. If Part is Multi-UOM tracking then only the Tracking UOMs are valid otherwise all UOM's of the Parts UOMClass are valid.  """  
      self.JobShipUOM:str = obj["JobShipUOM"]
      """  Unit of Measure of the quantity shipped from the Job (OurJobShipQty)  """  
      self.TrackSerialNum:bool = obj["TrackSerialNum"]
      """  Indicates whether the ShipDtl.PartNum is serial tracked. Required as a db field rather than using the link to PartNumTrackSerialNum to allow validations based on the ShipDtl table rather than the ttShipDtl table. Default is No.  """  
      self.JobLotNum:str = obj["JobLotNum"]
      """  Lot Number is for Job Shipments.  """  
      self.BinType:str = obj["BinType"]
      """  Identifies the type of Bin is being used (valid values are 'Std', 'Cust', 'Supp').  Associated with field ShipDtl.BinNum  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  Unit price discount percent.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item.  It can be zero.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.PickedAutoAllocatedQty:int = obj["PickedAutoAllocatedQty"]
      """  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Order.  This quantity is in the IUM unit of measure.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InDiscount:int = obj["InDiscount"]
      """  A flat discount amount for the line item includes taxes.  It can be zero.  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """  A flat discount amount for the line item includes taxes.  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reporting currency value of this field  """  
      self.InExtPrice:int = obj["InExtPrice"]
      """  Extended Price for the invoice line item including taxes.  """  
      self.DocInExtPrice:int = obj["DocInExtPrice"]
      """  Extended Price for the invoice line item including taxes.  """  
      self.Rpt1InExtPrice:int = obj["Rpt1InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtPrice:int = obj["Rpt2InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtPrice:int = obj["Rpt3InExtPrice"]
      """  Reporting currency value of this field  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """  Unit Price including taxes.  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Unit Price including taxes.  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.MFCustNum:int = obj["MFCustNum"]
      """  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  """  
      self.MFShipToNum:str = obj["MFShipToNum"]
      """  The ShipTo ID to be used for this record. This MUST BE VALID IN THE SHIPTO file.  """  
      self.UseOTMF:bool = obj["UseOTMF"]
      """  Indicates that the One Time Mark For information defined for this record should be used.  """  
      self.OTMFName:str = obj["OTMFName"]
      """  One Time Mark For Name of the ShipTo.  """  
      self.OTMFAddress1:str = obj["OTMFAddress1"]
      """  One Time Mark For first line of the ShipTo address.  """  
      self.OTMFAddress2:str = obj["OTMFAddress2"]
      """  One Time Mark For second line of the ShipTo address.  """  
      self.OTMFAddress3:str = obj["OTMFAddress3"]
      """  One Time Mark For third line of the ShipTo address.  """  
      self.OTMFCity:str = obj["OTMFCity"]
      """  City portion of the One Time Mark For address.  """  
      self.OTMFState:str = obj["OTMFState"]
      """  The state or province portion of the One Time Mark For address.  """  
      self.OTMFZIP:str = obj["OTMFZIP"]
      """  The zip or postal code portion of the One Time Mark For address.  """  
      self.OTMFContact:str = obj["OTMFContact"]
      """  One Time Mark For Contact Name  """  
      self.OTMFFaxNum:str = obj["OTMFFaxNum"]
      """  Fax number for the One Time Mark For.  """  
      self.OTMFPhoneNum:str = obj["OTMFPhoneNum"]
      """  Phone number for the One Time Mark For  """  
      self.OTMFCountryNum:int = obj["OTMFCountryNum"]
      """  Country number for the One Time Mark For  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.ShipOvers:bool = obj["ShipOvers"]
      """  ShipOvers  """  
      self.AllowedOvers:int = obj["AllowedOvers"]
      """  AllowedOvers  """  
      self.AllowedUnders:int = obj["AllowedUnders"]
      """  AllowedUnders  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NotAllocatedQty:int = obj["NotAllocatedQty"]
      """  This is the quantity being shipped that was not already previously allocated, and could not be auto allocated.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.PCIDItemSeq:int = obj["PCIDItemSeq"]
      """  PCID Item Sequence  """  
      self.DockingStation:str = obj["DockingStation"]
      """  The dockingstation of the shipto address.  For future use.  """  
      self.UseShipDtlInfo:bool = obj["UseShipDtlInfo"]
      """  For future use.  """  
      self.PkgCodePartNum:str = obj["PkgCodePartNum"]
      """  PkgCodePartNum  """  
      self.CustContainerPartNum:str = obj["CustContainerPartNum"]
      """  CustContainerPartNum  """  
      self.LabelType:str = obj["LabelType"]
      """  LabelType  """  
      self.WarrantySendToFSA:bool = obj["WarrantySendToFSA"]
      """  Indicates that the warranty will be sent to FSA  """  
      self.FSAEquipment:bool = obj["FSAEquipment"]
      """  When the shipment line is marked as "send as equipment", it will create an Installation in Epicor FSA.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.InventoryNumberOfPieces:int = obj["InventoryNumberOfPieces"]
      """  Number of pieces for this attribute set based on OurInventoryShipQty.  """  
      self.JobNumberOfPieces:int = obj["JobNumberOfPieces"]
      """  Number of pieces for this attribute set based on OurJobShipQty.  """  
      self.MXEstValue:int = obj["MXEstValue"]
      """  Estimated Value  """  
      self.MXEstValueCurrencyCode:str = obj["MXEstValueCurrencyCode"]
      """  Estimated Value Currency  """  
      self.MXHazardousShipment:bool = obj["MXHazardousShipment"]
      """  Hazardous Shipment  """  
      self.MXHazardousType:str = obj["MXHazardousType"]
      """  Hazardous Type  """  
      self.MXPackageType:str = obj["MXPackageType"]
      """  Package Type  """  
      self.CNDeclarationBillLine:int = obj["CNDeclarationBillLine"]
      """  CNDeclarationBillLine  """  
      self.JobNotAllocatedQty:int = obj["JobNotAllocatedQty"]
      """  This is the quantity being shipped from manufacturing that was not already previously allocated, and could not be auto allocated.  """  
      self.JobPickedAutoAllocatedQty:int = obj["JobPickedAutoAllocatedQty"]
      """  Quantity picked from manufacturing that was not manually allocated.  """  
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  Flag to indicate if Order/Line/Rel is Buy To Order  """  
      self.ChangeDateTime:str = obj["ChangeDateTime"]
      """  The date and time that the record was last changed  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DimCodeList:str = obj["DimCodeList"]
      """  Delimited list of available Dimension codes for line  """  
      self.DisplayInvQty:int = obj["DisplayInvQty"]
      """  OurInventoryShipQty * DimConvFactor - update inplace of OurInventoryShipQty  """  
      self.DocLineTax:int = obj["DocLineTax"]
      self.DropShip:bool = obj["DropShip"]
      """  Is Drop Shipment.  """  
      self.DtlError:bool = obj["DtlError"]
      """  Indicates if a detail line has errors to be corrected before leaving packing slip  """  
      self.EnableInvIDBtn:bool = obj["EnableInvIDBtn"]
      self.EnableInvSerialBtn:bool = obj["EnableInvSerialBtn"]
      self.EnableJobFields:bool = obj["EnableJobFields"]
      """  Logical indicating if receipt to a job is allowed.  This is determined by either the xasyst.shipnojob field or whether or not the sales order is linked to a job.  """  
      self.EnableKitIDBtn:bool = obj["EnableKitIDBtn"]
      self.EnableMfgIDBtn:bool = obj["EnableMfgIDBtn"]
      self.EnableMfgSerialBtn:bool = obj["EnableMfgSerialBtn"]
      self.EnableOBInvSerialBtn:bool = obj["EnableOBInvSerialBtn"]
      self.EnableOBMfgSerialBtn:bool = obj["EnableOBMfgSerialBtn"]
      self.EnablePackageControl:bool = obj["EnablePackageControl"]
      """  Boolean indicating if the package control functionality should be enabled.  """  
      self.EnablePOSerialBtn:bool = obj["EnablePOSerialBtn"]
      self.ExtJobNum:str = obj["ExtJobNum"]
      self.FSAInstallationCost:int = obj["FSAInstallationCost"]
      self.FSAInstallationOrderLine:int = obj["FSAInstallationOrderLine"]
      self.FSAInstallationOrderNum:int = obj["FSAInstallationOrderNum"]
      self.FSAInstallationRequired:bool = obj["FSAInstallationRequired"]
      """  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  """  
      self.FSAInstallationType:str = obj["FSAInstallationType"]
      self.GetLocIDNum:bool = obj["GetLocIDNum"]
      """  Equal to true if opening Location ID Diaglog  """  
      self.InvLegalNumber:str = obj["InvLegalNumber"]
      """  The invoice legal number.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  External field to be used in the SalesOrder Tracker to show the user the InvoiceNum linked to the shipment.  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      self.KitBinNum:str = obj["KitBinNum"]
      self.KitCompIssue:bool = obj["KitCompIssue"]
      self.KitCompShipComplete:bool = obj["KitCompShipComplete"]
      self.KitDescription:str = obj["KitDescription"]
      self.KitFlag:str = obj["KitFlag"]
      """  Sales Kit flag.  C = 'Component'  P = 'Parent'.  """  
      self.KitIUM:str = obj["KitIUM"]
      self.KitLotNum:str = obj["KitLotNum"]
      self.KitMassIssue:bool = obj["KitMassIssue"]
      self.KitParentIssue:bool = obj["KitParentIssue"]
      self.KitPartNum:str = obj["KitPartNum"]
      self.KitQtyFromInv:int = obj["KitQtyFromInv"]
      self.KitQtyFromInvEnabled:bool = obj["KitQtyFromInvEnabled"]
      self.KitSerialTracked:bool = obj["KitSerialTracked"]
      self.KitTrackLots:bool = obj["KitTrackLots"]
      self.KitWarehouse:str = obj["KitWarehouse"]
      self.KitWarehouseCodeDesc:str = obj["KitWarehouseCodeDesc"]
      self.KitWhseList:str = obj["KitWhseList"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.   This field comes directly from the table ShipHead.  """  
      self.LineContentValue:int = obj["LineContentValue"]
      """  Individual line content value that is used by the freight web service to calculate the total order value.  """  
      self.LineTax:int = obj["LineTax"]
      self.LinkMsg:str = obj["LinkMsg"]
      self.MarkForAddrList:str = obj["MarkForAddrList"]
      """  Contains the Mark For Address  """  
      self.MFCustID:str = obj["MFCustID"]
      self.OrderHold:bool = obj["OrderHold"]
      """  Indicates if Order is on Hold  """  
      self.OrderRelOurReqQty:int = obj["OrderRelOurReqQty"]
      self.OurJobShipIUM:str = obj["OurJobShipIUM"]
      self.OurJobShippedQty:int = obj["OurJobShippedQty"]
      self.OurRemainQty:int = obj["OurRemainQty"]
      self.OurRemainUM:str = obj["OurRemainUM"]
      self.OurReqQty:int = obj["OurReqQty"]
      self.OurReqUM:str = obj["OurReqUM"]
      self.OurShippedQty:int = obj["OurShippedQty"]
      self.OurShippedUM:str = obj["OurShippedUM"]
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      self.PackSlip:str = obj["PackSlip"]
      """  Packing slip for drop shipment.  """  
      self.PartAESExp:str = obj["PartAESExp"]
      """  Used by freight web service  """  
      self.PartCompany:str = obj["PartCompany"]
      self.PartECNNumber:str = obj["PartECNNumber"]
      """  Used by freight web service  """  
      self.PartExpLicNumber:str = obj["PartExpLicNumber"]
      """  Used by freight web service  """  
      self.PartExpLicType:str = obj["PartExpLicType"]
      """  Used by freight web service  """  
      self.PartHazClass:str = obj["PartHazClass"]
      """  Used by freight web service  """  
      self.PartHazGvrnmtID:str = obj["PartHazGvrnmtID"]
      """  Used by freight web service  """  
      self.PartHazItem:bool = obj["PartHazItem"]
      """  Used by freight web service  """  
      self.PartHazPackInstr:str = obj["PartHazPackInstr"]
      """  Used by freight web service  """  
      self.PartHazSub:str = obj["PartHazSub"]
      """  Used by freight web service  """  
      self.PartHazTechName:str = obj["PartHazTechName"]
      """  Used by freight web service  """  
      self.PartHTS:str = obj["PartHTS"]
      """  Used by freight web service  """  
      self.PartNAFTAOrigCountry:str = obj["PartNAFTAOrigCountry"]
      """  Used by freight web service  """  
      self.PartNAFTAPref:str = obj["PartNAFTAPref"]
      """  Used by freight web service  """  
      self.PartNAFTAProd:str = obj["PartNAFTAProd"]
      """  Used by freight web service  """  
      self.PartOrigCountry:str = obj["PartOrigCountry"]
      """  Used by freight web service  """  
      self.PartPartNum:str = obj["PartPartNum"]
      self.PartSchedBcode:str = obj["PartSchedBcode"]
      """  Used by freight web service  """  
      self.PartUseHTSDesc:bool = obj["PartUseHTSDesc"]
      """  Used by freight web service  """  
      self.PONum:str = obj["PONum"]
      self.ProjectID:str = obj["ProjectID"]
      """  Project of the related Order Line  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point ID.  """  
      self.RequestDate:str = obj["RequestDate"]
      self.Rpt1LineTax:int = obj["Rpt1LineTax"]
      self.Rpt2LineTax:int = obj["Rpt2LineTax"]
      self.Rpt3LineTax:int = obj["Rpt3LineTax"]
      self.SelectedLocationIDQty:int = obj["SelectedLocationIDQty"]
      self.SellingRemainQty:int = obj["SellingRemainQty"]
      self.SellingRemainUM:str = obj["SellingRemainUM"]
      self.SellingReqQty:int = obj["SellingReqQty"]
      self.SellingReqUM:str = obj["SellingReqUM"]
      self.SellingShipmentQty:int = obj["SellingShipmentQty"]
      self.SellingShipmentUM:str = obj["SellingShipmentUM"]
      self.SellingShippedQty:int = obj["SellingShippedQty"]
      self.SellingShippedUM:str = obj["SellingShippedUM"]
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  This field comes directly from the ShipHead table.  """  
      self.ShipToWarning:str = obj["ShipToWarning"]
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  This field comes directly from the ShipHead table.  """  
      self.StockPart:bool = obj["StockPart"]
      """  Indicates if Part is a stock Part  """  
      self.TrackID:bool = obj["TrackID"]
      self.TranLocationIDQty:int = obj["TranLocationIDQty"]
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier that drops shipped the good from their inventory to our customer.  """  
      self.WhseList:str = obj["WhseList"]
      self.KitAttributeSetID:int = obj["KitAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.KitAttributeSetDescription:str = obj["KitAttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.KitAttributeSetShortDescription:str = obj["KitAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.KitPartAttrClassID:str = obj["KitPartAttrClassID"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.MarkForAddrFormatted:str = obj["MarkForAddrFormatted"]
      """  Mark For address formatted for kinetic.  """  
      self.DispInventoryNumberOfPieces:int = obj["DispInventoryNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.DispJobNumberOfPieces:int = obj["DispJobNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.KitRevisionNum:str = obj["KitRevisionNum"]
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.CustNumSendToFSA:bool = obj["CustNumSendToFSA"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.DimensionDimCodeDescription:str = obj["DimensionDimCodeDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.LotPartLotDescription:str = obj["LotPartLotDescription"]
      self.MFShipToNumInactive:bool = obj["MFShipToNumInactive"]
      self.OrderLineProdCode:str = obj["OrderLineProdCode"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumPSCurrCode:str = obj["OrderNumPSCurrCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OTMFCountryDescription:str = obj["OTMFCountryDescription"]
      self.PackNumUseOTS:bool = obj["PackNumUseOTS"]
      self.PackNumShipStatus:str = obj["PackNumShipStatus"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumSendToFSA:bool = obj["PartNumSendToFSA"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumWarrantyCode:str = obj["PartNumWarrantyCode"]
      self.PartNumFSAEquipment:bool = obj["PartNumFSAEquipment"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PlantName:str = obj["PlantName"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.WarrantyCodeSendToFSA:bool = obj["WarrantyCodeSendToFSA"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.WIPWarehouseCodeDescription:str = obj["WIPWarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.PCID2_c:str = obj["PCID2_c"]
      self.PCID3_c:str = obj["PCID3_c"]
      self.PCID4_c:str = obj["PCID4_c"]
      self.PCID5_c:str = obj["PCID5_c"]
      self.PCIDType1_c:str = obj["PCIDType1_c"]
      self.PCIDType2_c:str = obj["PCIDType2_c"]
      self.PCIDType3_c:str = obj["PCIDType3_c"]
      self.PCIDType4_c:str = obj["PCIDType4_c"]
      self.PCIDType5_c:str = obj["PCIDType5_c"]
      pass

class Erp_Tablesets_ShipDtlTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  InvcDtl.TaxCode and InvcDtl/InvcMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount ((Qty*unitprice)-discount) or if this is for a InvcMisc record InvcMisc.Amount.  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  InvcDtl.TaxCode and InvcDtl/InvcMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount ((Qty*unitprice)-discount) or if this is for a InvcMisc record InvcMisc.Amount.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Reverse Charge.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution Date  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Tax Rate Date  """  
      self.DefTaxableAmt:int = obj["DefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.DocDefTaxableAmt:int = obj["DocDefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.Rpt1DefTaxableAmt:int = obj["Rpt1DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxableAmt:int = obj["Rpt2DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxableAmt:int = obj["Rpt3DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.DefTaxAmt:int = obj["DefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.DocDefTaxAmt:int = obj["DocDefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.Rpt1DefTaxAmt:int = obj["Rpt1DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxAmt:int = obj["Rpt2DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxAmt:int = obj["Rpt3DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.ManAdd:bool = obj["ManAdd"]
      """  This record was manually added (not in Liability) but will use the standard calculations  """  
      self.DedTaxAmt:int = obj["DedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.DocDedTaxAmt:int = obj["DocDedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.Rpt1DedTaxAmt:int = obj["Rpt1DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DedTaxAmt:int = obj["Rpt2DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DedTaxAmt:int = obj["Rpt3DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  """  
      self.FixedAmount:int = obj["FixedAmount"]
      """  Fixed Tax Amount  """  
      self.DocFixedAmount:int = obj["DocFixedAmount"]
      """  Document Fixed Tax Amount  """  
      self.Rpt1FixedAmount:int = obj["Rpt1FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2FixedAmount:int = obj["Rpt2FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3FixedAmount:int = obj["Rpt3FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the tax.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the tax converted to the customers currency.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DescCollectionType:str = obj["DescCollectionType"]
      self.TaxDescription:str = obj["TaxDescription"]
      self.TaxTotal:int = obj["TaxTotal"]
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      self.ChangeDateTime:str = obj["ChangeDateTime"]
      """  The date and time that the record was last changed  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.SalesTaxDescDescription:str = obj["SalesTaxDescDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PackNum:int = obj["PackNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipHeadInsuranceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing Slip  """  
      self.InsuranceSeq:int = obj["InsuranceSeq"]
      """  InsuranceSeq  """  
      self.Type:str = obj["Type"]
      """  Insurance Type  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Insurance Company Name  """  
      self.PolicyNum:str = obj["PolicyNum"]
      """  Insurance Policy Number  """  
      self.Premium:int = obj["Premium"]
      """  Insurance Premium  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  """  
      self.ShipLog:str = obj["ShipLog"]
      """  An optional field which can be used to enter a shipping log reference #.  """  
      self.LabelComment:str = obj["LabelComment"]
      """  An optional field that will be printed on the shipping labels for this packing slip.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Packing slip comments.  This will print on the Packing Slip.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Voided:bool = obj["Voided"]
      """  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External  ID  """  
      self.ICReceived:bool = obj["ICReceived"]
      """  Iinter Company Received flag  """  
      self.XRefPackNum:str = obj["XRefPackNum"]
      """  Cross reference Packing Slip number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Populated from OrderHed.BTCustNum.  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.ShipGroup:str = obj["ShipGroup"]
      """  Group the shipment belongs to for "Staging"  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Package Code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.VerbalConf:bool = obj["VerbalConf"]
      """  Verbal Confirmation required  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.MFTransNum:str = obj["MFTransNum"]
      """  Transaction Number returned by the Manifest Engine  """  
      self.MFCallTag:str = obj["MFCallTag"]
      """  Manifest Call Tag Number  """  
      self.MFPickupNum:str = obj["MFPickupNum"]
      """  Manifest Pickup Number  """  
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      """  Manifest Discount Freight Amount  """  
      self.MFTemplate:str = obj["MFTemplate"]
      """  Manifest Template Code  """  
      self.MFUse3B:bool = obj["MFUse3B"]
      """  Manifest flag to use 3 party billing  """  
      self.MF3BAccount:str = obj["MF3BAccount"]
      """  Manifest's 3rd Party Billing Account  """  
      self.MFDimWeight:int = obj["MFDimWeight"]
      """  Manifest Dimension Weight  """  
      self.MFZone:str = obj["MFZone"]
      """  Manifest Delivery Zone  """  
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      """  Manifest Published Freight Amount  """  
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      """  Manifest Other Amount  """  
      self.MFOversized:bool = obj["MFOversized"]
      """  Manifest Oversized flag  """  
      self.ServSatDelivery:bool = obj["ServSatDelivery"]
      """  Is a Service Saturday delivery acceptable  """  
      self.ServSatPickup:bool = obj["ServSatPickup"]
      """  Is a Service Saturday pickup available  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServPOD:bool = obj["ServPOD"]
      """  Service Auto POD flag  """  
      self.ServAOD:bool = obj["ServAOD"]
      """  AOD  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.PayFlag:str = obj["PayFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping, The city portion of the Payer main address.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  The state or province portion of the shipment payer main address.  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  The zip or postal code portion of the shipping payers main address.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  The country of the main shipping payers address.  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder Country portion of the address  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country portion of the address  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Payer Bill To Third Address line  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Payer Bill To Country Number  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Payer Bill To Phone Number  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View From Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  """  
      self.ReplicatedFrom:int = obj["ReplicatedFrom"]
      """  Pack ID of the pack this pack was replicated from.  This is used as a debugging tool and is not presented to the end user.  """  
      self.ReplicatedStat:str = obj["ReplicatedStat"]
      """  Informational field containing either Complete or Partial.  This is only popluated if the ReplicatedFrom field has a value.  This is used as a debugging tool and is not presented to the user.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.OTSOrderNum:int = obj["OTSOrderNum"]
      """  The Sales Order number which contains the One Time ShipTo data. The OTSOrderNum along with the values ShipToNum are used to find the OrderHed or OrderRel to obtain the OTS.  """  
      self.TaxCalculated:bool = obj["TaxCalculated"]
      """  Indicates whether or not the taxes for this shipment have been calculated.  This field is used to identify those situations where the tax engine was called but did not generate any taxes because none were needed.  """  
      self.TaxCalcDate:str = obj["TaxCalcDate"]
      """  Date the taxes were calculated.  Used for informational and audit tracking purposes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.OrderAmt:int = obj["OrderAmt"]
      """  Total order Amount. This field is an accumulation of the extended net amounts of the detail line items  """  
      self.DocOrderAmt:int = obj["DocOrderAmt"]
      """  Total order Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  """  
      self.Rpt1OrderAmt:int = obj["Rpt1OrderAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrderAmt:int = obj["Rpt2OrderAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrderAmt:int = obj["Rpt3OrderAmt"]
      """  Reporting currency value of this field  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.TotalWHTax:int = obj["TotalWHTax"]
      """   Order Total Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalWHTax:int = obj["DocTotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalWHTax:int = obj["Rpt1TotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalWHTax:int = obj["Rpt2TotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalWHTax:int = obj["Rpt3TotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """   Order Total Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.TotalTax:int = obj["TotalTax"]
      """   Order Total Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.TotalDiscount:int = obj["TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalDiscount:int = obj["Rpt1TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalDiscount:int = obj["Rpt2TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalDiscount:int = obj["Rpt3TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.DocTotalDiscount:int = obj["DocTotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.DeviceUOM:str = obj["DeviceUOM"]
      """  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.PBHoldNoInv:bool = obj["PBHoldNoInv"]
      """  Flag to indicate that project billing Hold Product Invoice flag is true, it prevents this pack slip from being selected for invoicing.  """  
      self.ReconcileQty:int = obj["ReconcileQty"]
      """  Reconciled quantity for the packing slip  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  Last trading partner demand schedule processed that affected this packing slip  """  
      self.CounterASN:int = obj["CounterASN"]
      """  Number of times the customer shipment has been shipped, that means it changed from non shipped status to shipped  """  
      self.OurBank:str = obj["OurBank"]
      """  Bank for Cash Receipts. Default is from 1) Sales Order 2)Bill To Customer 3) System Default(Company).  """  
      self.ERSOrder:bool = obj["ERSOrder"]
      """  It will be used to identify that the shipment will generate an invoice when it got shipped. If the first order release added to a pack belongs to an ERS order, then non ERS order releases will not be allowed in that pack and if the first order release added to a pack belongs to a non ERS order, then ERS order releases will not be allowed in that pack.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OrderDate:str = obj["OrderDate"]
      self.SlipStatus:str = obj["SlipStatus"]
      """  Comma delimited list of status types for lookup  """  
      self.AddrList:str = obj["AddrList"]
      """  Shipping Address  """  
      self.BillAddr:str = obj["BillAddr"]
      """  Billing Address  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates if Customer is on Credit Hold  """  
      self.OrderHold:bool = obj["OrderHold"]
      """  Indicates if Order is on Hold  """  
      self.MultipleShippers:bool = obj["MultipleShippers"]
      """  Flag indicating OrderRel's going to more than one shipTo  """  
      self.SendShipment:bool = obj["SendShipment"]
      """  Indicates whether to hide/view ExternalDeliveryNote field  """  
      self.BTCustID:str = obj["BTCustID"]
      """  CustID associated with ShipHeadHead.BTCustNum.  """  
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  CustName associated with ShipHead.BTCustNum.  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  Used by the manifest system.  Sum of the value of items in the carton.  Item price - discount + sales tax.  """  
      self.LastCartonFlag:bool = obj["LastCartonFlag"]
      """  Set to Y if the carton is the last one being shiped to the customer.  If the sum of the quantity packed does not equal the quantity ordered for each line in the carton the value is No.  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage Number.  """  
      self.EnableShipped:bool = obj["EnableShipped"]
      self.OrderNum:int = obj["OrderNum"]
      """  Order Number for new cartons.  """  
      self.HasCartonLines:bool = obj["HasCartonLines"]
      """  Indicates whether the Carton has lines or not.  """  
      self.StagingReq:bool = obj["StagingReq"]
      """  Displays the contents of XaSyst.StagingReq  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  """  
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  A zero indicates the Packing height is to be enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Indicates if package length is to be enabled.  If the value is zero the prompt is enabled.  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  A zero indicates the packaging width field is to be enabled.  """  
      self.CtnPkgCode:str = obj["CtnPkgCode"]
      """  Used to enable users to default the Carton Trk Dtl package settings.  Initial value defaults to the ShipHead.PkgCode.  However, this field does NOT have to be the same as the ShipHead.PkgCode.  """  
      self.ReplicateCount:int = obj["ReplicateCount"]
      """  Number of packs to replicate  """  
      self.PhantomCasesExist:bool = obj["PhantomCasesExist"]
      """  Logical indicating if CartonTrkDtl records exist for this pack.  Used by the UI for row rules.  """  
      self.EnablePhantom:bool = obj["EnablePhantom"]
      """  Logical indicating if the PhantomPack checkbox is to be enabled.  """  
      self.MasterpackPackNum:int = obj["MasterpackPackNum"]
      """  Pack ID of the Masterpack this shipment is on.  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for customer shipments  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Document Total tax amount from ShipDtl Tax for Collection type 'Invoice'  """  
      self.DocWithholdingTaxAmt:int = obj["DocWithholdingTaxAmt"]
      self.EnableTax:bool = obj["EnableTax"]
      """  Intended for internal UI use.  Identifies whether or not taxes are generated for shipdtls.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.DisplayInPrice:bool = obj["DisplayInPrice"]
      """  The flag to indicate if Tax Inclusive Pricing should be on display  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      """  Description of delivery type  """  
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.OurBankDescription:str = obj["OurBankDescription"]
      """  Full description of the bank account.  """  
      self.OurBankBankName:str = obj["OurBankBankName"]
      """  The Bank's full name.  """  
      self.PackToMasterpackDtlPackNum:int = obj["PackToMasterpackDtlPackNum"]
      """  Master pack packnum  """  
      self.ShipToCustName:str = obj["ShipToCustName"]
      """  The full name of the customer.  """  
      self.ShipToCustBTName:str = obj["ShipToCustBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.ShipToCustCustID:str = obj["ShipToCustCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      """  Full description for the Tax Region.  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipHeadListTableset:
   def __init__(self, obj):
      self.ShipHeadList:list[Erp_Tablesets_ShipHeadListRow] = obj["ShipHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ShipHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  """  
      self.ShipLog:str = obj["ShipLog"]
      """  An optional field which can be used to enter a shipping log reference #.  """  
      self.LabelComment:str = obj["LabelComment"]
      """  An optional field that will be printed on the shipping labels for this packing slip.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Packing slip comments.  This will print on the Packing Slip.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Voided:bool = obj["Voided"]
      """  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External  ID  """  
      self.ICReceived:bool = obj["ICReceived"]
      """  Iinter Company Received flag  """  
      self.XRefPackNum:str = obj["XRefPackNum"]
      """  Cross reference Packing Slip number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Populated from OrderHed.BTCustNum.  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.ShipGroup:str = obj["ShipGroup"]
      """  Group the shipment belongs to for "Staging"  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Package Code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.VerbalConf:bool = obj["VerbalConf"]
      """  Verbal Confirmation required  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.MFTransNum:str = obj["MFTransNum"]
      """  Transaction Number returned by the Manifest Engine  """  
      self.MFCallTag:str = obj["MFCallTag"]
      """  Manifest Call Tag Number  """  
      self.MFPickupNum:str = obj["MFPickupNum"]
      """  Manifest Pickup Number  """  
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      """  Manifest Discount Freight Amount  """  
      self.MFTemplate:str = obj["MFTemplate"]
      """  Manifest Template Code  """  
      self.MFUse3B:bool = obj["MFUse3B"]
      """  Manifest flag to use 3 party billing  """  
      self.MF3BAccount:str = obj["MF3BAccount"]
      """  Manifest's 3rd Party Billing Account  """  
      self.MFDimWeight:int = obj["MFDimWeight"]
      """  Manifest Dimension Weight  """  
      self.MFZone:str = obj["MFZone"]
      """  Manifest Delivery Zone  """  
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      """  Manifest Published Freight Amount  """  
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      """  Manifest Other Amount  """  
      self.MFOversized:bool = obj["MFOversized"]
      """  Manifest Oversized flag  """  
      self.ServSatDelivery:bool = obj["ServSatDelivery"]
      """  Is a Service Saturday delivery acceptable  """  
      self.ServSatPickup:bool = obj["ServSatPickup"]
      """  Is a Service Saturday pickup available  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServPOD:bool = obj["ServPOD"]
      """  Service Auto POD flag  """  
      self.ServAOD:bool = obj["ServAOD"]
      """  AOD  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.PayFlag:str = obj["PayFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping, The city portion of the Payer main address.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  The state or province portion of the shipment payer main address.  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  The zip or postal code portion of the shipping payers main address.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  The country of the main shipping payers address.  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder Country portion of the address  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country portion of the address  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Payer Bill To Third Address line  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Payer Bill To Country Number  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Payer Bill To Phone Number  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View From Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  """  
      self.ReplicatedFrom:int = obj["ReplicatedFrom"]
      """  Pack ID of the pack this pack was replicated from.  This is used as a debugging tool and is not presented to the end user.  """  
      self.ReplicatedStat:str = obj["ReplicatedStat"]
      """  Informational field containing either Complete or Partial.  This is only popluated if the ReplicatedFrom field has a value.  This is used as a debugging tool and is not presented to the user.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.OTSOrderNum:int = obj["OTSOrderNum"]
      """  The Sales Order number which contains the One Time ShipTo data. The OTSOrderNum along with the values ShipToNum are used to find the OrderHed or OrderRel to obtain the OTS.  """  
      self.TaxCalculated:bool = obj["TaxCalculated"]
      """  Indicates whether or not the taxes for this shipment have been calculated.  This field is used to identify those situations where the tax engine was called but did not generate any taxes because none were needed.  """  
      self.TaxCalcDate:str = obj["TaxCalcDate"]
      """  Date the taxes were calculated.  Used for informational and audit tracking purposes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.OrderAmt:int = obj["OrderAmt"]
      """  Total order Amount. This field is an accumulation of the extended net amounts of the detail line items  """  
      self.DocOrderAmt:int = obj["DocOrderAmt"]
      """  Total order Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  """  
      self.Rpt1OrderAmt:int = obj["Rpt1OrderAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrderAmt:int = obj["Rpt2OrderAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrderAmt:int = obj["Rpt3OrderAmt"]
      """  Reporting currency value of this field  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.TotalWHTax:int = obj["TotalWHTax"]
      """   Order Total Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalWHTax:int = obj["DocTotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalWHTax:int = obj["Rpt1TotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalWHTax:int = obj["Rpt2TotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalWHTax:int = obj["Rpt3TotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """   Order Total Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.TotalTax:int = obj["TotalTax"]
      """   Order Total Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.TotalDiscount:int = obj["TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalDiscount:int = obj["Rpt1TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalDiscount:int = obj["Rpt2TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalDiscount:int = obj["Rpt3TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.DocTotalDiscount:int = obj["DocTotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.DeviceUOM:str = obj["DeviceUOM"]
      """  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.PBHoldNoInv:bool = obj["PBHoldNoInv"]
      """  Flag to indicate that project billing Hold Product Invoice flag is true, it prevents this pack slip from being selected for invoicing.  """  
      self.ReconcileQty:int = obj["ReconcileQty"]
      """  Reconciled quantity for the packing slip  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  Last trading partner demand schedule processed that affected this packing slip  """  
      self.CounterASN:int = obj["CounterASN"]
      """  Number of times the customer shipment has been shipped, that means it changed from non shipped status to shipped  """  
      self.OurBank:str = obj["OurBank"]
      """  Bank for Cash Receipts. Default is from 1) Sales Order 2)Bill To Customer 3) System Default(Company).  """  
      self.ERSOrder:bool = obj["ERSOrder"]
      """  It will be used to identify that the shipment will generate an invoice when it got shipped. If the first order release added to a pack belongs to an ERS order, then non ERS order releases will not be allowed in that pack and if the first order release added to a pack belongs to a non ERS order, then ERS order releases will not be allowed in that pack.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.ShipOvers:bool = obj["ShipOvers"]
      """  ShipOvers  """  
      self.WIPackSlipCreated:bool = obj["WIPackSlipCreated"]
      """  WIPackSlipCreated  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAuthorizationCode:str = obj["AGAuthorizationCode"]
      """  AGAuthorizationCode  """  
      self.AGAuthorizationDate:str = obj["AGAuthorizationDate"]
      """  AGAuthorizationDate  """  
      self.AGCarrierCUIT:str = obj["AGCarrierCUIT"]
      """  AGCarrierCUIT  """  
      self.AGCOTMark:bool = obj["AGCOTMark"]
      """  AGCOTMark  """  
      self.AGDocumentLetter:str = obj["AGDocumentLetter"]
      """  AGDocumentLetter  """  
      self.AGInvoicingPoint:str = obj["AGInvoicingPoint"]
      """  AGInvoicingPoint  """  
      self.AGLegalNumber:str = obj["AGLegalNumber"]
      """  AGLegalNumber  """  
      self.AGPrintingControlType:str = obj["AGPrintingControlType"]
      """  AGPrintingControlType  """  
      self.AGTrackLicense:str = obj["AGTrackLicense"]
      """  AGTrackLicense  """  
      self.DispatchReason:str = obj["DispatchReason"]
      """  DispatchReason  """  
      self.AGShippingWay:str = obj["AGShippingWay"]
      """  AGShippingWay  """  
      self.OurSupplierCode:str = obj["OurSupplierCode"]
      """  Our Supplier Code  """  
      self.ASNPrintedDate:str = obj["ASNPrintedDate"]
      """  ASNPrintedDate  """  
      self.EDIShipToNum:str = obj["EDIShipToNum"]
      """  EDIShipToNum  """  
      self.MXIncoterm:str = obj["MXIncoterm"]
      """  MXIncoterm  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.DigitalSignature:str = obj["DigitalSignature"]
      """  DigitalSignature  """  
      self.SignedOn:str = obj["SignedOn"]
      """  SignedOn  """  
      self.SignedBy:str = obj["SignedBy"]
      """  SignedBy  """  
      self.FirstPrintDate:str = obj["FirstPrintDate"]
      """  FirstPrintDate  """  
      self.DocCopyNum:int = obj["DocCopyNum"]
      """  DocCopyNum  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      """  Declaration Bill  """  
      self.CNSample:bool = obj["CNSample"]
      """  Sample  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  Bonded  """  
      self.MXCertifiedTimestamp:str = obj["MXCertifiedTimestamp"]
      """  Creation date and time  """  
      self.MXCertificateSN:str = obj["MXCertificateSN"]
      """  Certificate Serial Number  """  
      self.MXCertificate:str = obj["MXCertificate"]
      """  Certificate  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  Fiscal Folio (UUID)  """  
      self.MXSATCertificateSN:str = obj["MXSATCertificateSN"]
      """  SAT Certificate Serial Number  """  
      self.MXDigitalSeal:str = obj["MXDigitalSeal"]
      """  Digital Seal  """  
      self.MXSATSeal:str = obj["MXSATSeal"]
      """  SAT Seal  """  
      self.MXOriginalString:str = obj["MXOriginalString"]
      """  Original String  """  
      self.MXOriginalStringTFD:str = obj["MXOriginalStringTFD"]
      """  TFD Original String  """  
      self.MXSerie:str = obj["MXSerie"]
      """  Serie  """  
      self.MXFolio:str = obj["MXFolio"]
      """  Folio  """  
      self.MXETD:str = obj["MXETD"]
      """  Estimated Date and Time of Departure  """  
      self.MXETA:str = obj["MXETA"]
      """  Estimated Date and Time of Arrival  """  
      self.MXDistance:int = obj["MXDistance"]
      """  Distance in Km  """  
      self.MXPermitType:str = obj["MXPermitType"]
      """  Permit Type  """  
      self.MXPermitNum:str = obj["MXPermitNum"]
      """  Permit Number  """  
      self.MXCartaPorteStatus:str = obj["MXCartaPorteStatus"]
      """  Carta Porte Status  """  
      self.VehicleLicensePlate:str = obj["VehicleLicensePlate"]
      """  Vehicle License Plate  """  
      self.VehicleType:str = obj["VehicleType"]
      """  Vehicle Type  """  
      self.VehicleYear:int = obj["VehicleYear"]
      """  Vehicle Year  """  
      self.DriverID:str = obj["DriverID"]
      """  Driver  """  
      self.MXCancelFiscalFolio:str = obj["MXCancelFiscalFolio"]
      """  MXCancelFiscalFolio  """  
      self.IncotermCode:str = obj["IncotermCode"]
      """  Incoterm Code  """  
      self.IncotermLocation:str = obj["IncotermLocation"]
      """  Incoterm Location  """  
      self.AddrList:str = obj["AddrList"]
      """  Shipping Address  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.BillAddr:str = obj["BillAddr"]
      """  Billing Address  """  
      self.BTCustID:str = obj["BTCustID"]
      """  CustID associated with ShipHeadHead.BTCustNum.  """  
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  CustName associated with ShipHead.BTCustNum.  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  Used by the manifest system.  Sum of the value of items in the carton.  Item price - discount + sales tax.  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage Number.  """  
      self.ChangeDateTime:str = obj["ChangeDateTime"]
      """  The date and time that the record was last changed  """  
      self.CheckOrderMessage:str = obj["CheckOrderMessage"]
      """  Internal field for temporary storage of check order messages.  """  
      self.CreditCardMessage:str = obj["CreditCardMessage"]
      """  This field temporarily holds certain message(s) returned by credit card processing logic for internal processing.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates if Customer is on Credit Hold  """  
      self.CtnPkgCode:str = obj["CtnPkgCode"]
      """  Used to enable users to default the Carton Trk Dtl package settings.  Initial value defaults to the ShipHead.PkgCode.  However, this field does NOT have to be the same as the ShipHead.PkgCode.  """  
      self.DisplayInPrice:bool = obj["DisplayInPrice"]
      """  The flag to indicate if Tax Inclusive Pricing should be on display  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Document Total tax amount from ShipDtl Tax for Collection type 'Invoice'  """  
      self.DocWithholdingTaxAmt:int = obj["DocWithholdingTaxAmt"]
      self.DoPostUpdate:bool = obj["DoPostUpdate"]
      """  Internal flag to indicate if post update processing should be done.  """  
      self.DspDigitalSignature:str = obj["DspDigitalSignature"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnablePackageControl:bool = obj["EnablePackageControl"]
      """  Logical indicating if the package control functionality should be enabled.  """  
      self.EnablePhantom:bool = obj["EnablePhantom"]
      """  Logical indicating if the PhantomPack checkbox is to be enabled.  """  
      self.EnableShipped:bool = obj["EnableShipped"]
      self.EnableTax:bool = obj["EnableTax"]
      """  Intended for internal UI use.  Identifies whether or not taxes are generated for shipdtls.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  """  
      self.FromMasterPack:bool = obj["FromMasterPack"]
      """  True if the update is being called from Master Pack (needed for validation)  """  
      self.HasCartonLines:bool = obj["HasCartonLines"]
      """  Indicates whether the Carton has lines or not.  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for customer shipments  """  
      self.LastCartonFlag:bool = obj["LastCartonFlag"]
      """  Set to Y if the carton is the last one being shiped to the customer.  If the sum of the quantity packed does not equal the quantity ordered for each line in the carton the value is No.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.MasterpackPackNum:int = obj["MasterpackPackNum"]
      """  Pack ID of the Masterpack this shipment is on.  """  
      self.MultipleShippers:bool = obj["MultipleShippers"]
      """  Flag indicating OrderRel's going to more than one shipTo  """  
      self.OrderDate:str = obj["OrderDate"]
      self.OrderHold:bool = obj["OrderHold"]
      """  Indicates if Order is on Hold  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order Number for new cartons.  """  
      self.PCID:str = obj["PCID"]
      self.PhantomCasesExist:bool = obj["PhantomCasesExist"]
      """  Logical indicating if CartonTrkDtl records exist for this pack.  Used by the UI for row rules.  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  A zero indicates the Packing height is to be enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Indicates if package length is to be enabled.  If the value is zero the prompt is enabled.  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  A zero indicates the packaging width field is to be enabled.  """  
      self.PostUpdMessage:str = obj["PostUpdMessage"]
      """  Internal field for temporary storage of post update messages.  """  
      self.QSUseBOL:bool = obj["QSUseBOL"]
      self.QSUseCO:bool = obj["QSUseCO"]
      self.QSUseIntl:bool = obj["QSUseIntl"]
      self.ReadyToInvoiceChanged:bool = obj["ReadyToInvoiceChanged"]
      """  Internal field for update processing that is true if ReadyToInvoice has been changed.  """  
      self.ReplicateCount:int = obj["ReplicateCount"]
      """  Number of packs to replicate  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      self.SendShipment:bool = obj["SendShipment"]
      """  Indicates whether to hide/view ExternalDeliveryNote field  """  
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.SlipStatus:str = obj["SlipStatus"]
      """  Comma delimited list of status types for lookup  """  
      self.StageShipped:bool = obj["StageShipped"]
      """  Carton Stage Ship Status  """  
      self.StagingReq:bool = obj["StagingReq"]
      """  Displays the contents of XaSyst.StagingReq  """  
      self.StatusChgMessage:str = obj["StatusChgMessage"]
      """  Internal field for temporary storage of status change messages.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      self.AutoInvoiceMessage:str = obj["AutoInvoiceMessage"]
      """  Internal field for temporary storage of auto invoicing messages.  """  
      self.ShipToAddressFormatted:str = obj["ShipToAddressFormatted"]
      """  Ship To address formatted for Kinetic.  """  
      self.SoldToAddressFormatted:str = obj["SoldToAddressFormatted"]
      """  Sold To address formatted  """  
      self.MXETADate:str = obj["MXETADate"]
      """  Estimated Date of Arrival  """  
      self.MXETATime:int = obj["MXETATime"]
      """  Estimated Time of Arrival  """  
      self.MXETDDate:str = obj["MXETDDate"]
      """  Estimated Date of Departure  """  
      self.MXETDTime:int = obj["MXETDTime"]
      """  Estimated Time of Departure  """  
      self.EnableIncotermLocation:bool = obj["EnableIncotermLocation"]
      """  Flag indicating whether to enable Incoterm Location  """  
      self.MXVehicleWeight:int = obj["MXVehicleWeight"]
      """  Vehicle Weight (in tons)  """  
      self.MXIdCCP:str = obj["MXIdCCP"]
      """  A unique Carta Porte identification number assigned by Epicor  """  
      self.MXCustomsRegime:str = obj["MXCustomsRegime"]
      """  Customs Regime for Export transaction  """  
      self.MXReverseLogistics:bool = obj["MXReverseLogistics"]
      """  Check box to specify the use of reverse logistic, collection or devolution services when shipping goods.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AGInvoicingPointDescription:str = obj["AGInvoicingPointDescription"]
      self.BTCustNumInactive:bool = obj["BTCustNumInactive"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CustomerSendToFSA:bool = obj["CustomerSendToFSA"]
      self.CustomerInactive:bool = obj["CustomerInactive"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      self.IncotermsDescription:str = obj["IncotermsDescription"]
      self.OurBankBankName:str = obj["OurBankBankName"]
      self.OurBankDescription:str = obj["OurBankDescription"]
      self.ShipToCustInactive:bool = obj["ShipToCustInactive"]
      self.ShipToCustBTName:str = obj["ShipToCustBTName"]
      self.ShipToCustCustID:str = obj["ShipToCustCustID"]
      self.ShipToCustName:str = obj["ShipToCustName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.Review_c:bool = obj["Review_c"]
      pass

class Erp_Tablesets_ShipHeadTrailerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing Slip  """  
      self.LicensePlate:str = obj["LicensePlate"]
      """  License Plate for Trailer  """  
      self.Type:str = obj["Type"]
      """  Type of Trailer  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipMiscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number of the ShipHead record that this record is related to.  """  
      self.PackLine:int = obj["PackLine"]
      """   The packing slip line number of the ShipDtl record that this record is related to.
NOTE: This is always zero.  Currently ShipMisc records are only related to the ShipHead record.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  An integer assigned by the system which is used as one of the components of the unique index for this record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. This will be printed on the Packing Slip and transferred over to invoice processing. The default is provided by MiscChrg.Description, but it's overrideable by the user. This can't be blank.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit. Can't be zero. Use MiscChrg.MiscAmt as a default.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.InMiscAmt:int = obj["InMiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit including taxes. Can't be zero. Use MiscChrg.MiscAmt as a default.  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.WIIsAutoCreatedMisc:bool = obj["WIIsAutoCreatedMisc"]
      """  WIIsAutoCreatedMisc  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  The amount of the MiscAmt converted to the ShipHead CurrencyCode  """  
      self.ChangeDateTime:str = obj["ChangeDateTime"]
      """  The date and time that the record was last changed  """  
      self.DspMiscAmt:int = obj["DspMiscAmt"]
      """  The amount of misc charge on display. If the Tax Liability is flagged as Tax Inclusive Pricing then this amount is InMiscAmount else this amount is MiscAmt.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.PackNumShipStatus:str = obj["PackNumShipStatus"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipTaxSumRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency display switch  """  
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency display symbol  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  DocDisplaySymbol  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  Document reportable amount.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Document taxable amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Document tax amount.  """  
      self.PackNum:int = obj["PackNum"]
      """  Pack ID  """  
      self.PackLIne:int = obj["PackLIne"]
      """  pack line  """  
      self.Percent:int = obj["Percent"]
      """  Percent  """  
      self.RateCode:str = obj["RateCode"]
      self.ReportableAmt:int = obj["ReportableAmt"]
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      self.TaxableAmt:int = obj["TaxableAmt"]
      self.TaxAmt:int = obj["TaxAmt"]
      self.TaxCode:str = obj["TaxCode"]
      self.TaxDescription:str = obj["TaxDescription"]
      self.RateCodeDesc:str = obj["RateCodeDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipUPSRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.UPSQVSeq:int = obj["UPSQVSeq"]
      """  UPS Quantum View Sequence  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  UPS Emailaddress  """  
      self.ShipmentNotify:bool = obj["ShipmentNotify"]
      """  Notify Emailaddress when shipped  """  
      self.FailureNotify:bool = obj["FailureNotify"]
      """  Logical indicating if the Email Address is to be notified of a failed shipment.  """  
      self.DeliveryNotify:bool = obj["DeliveryNotify"]
      """  Logical indicating if the Email Address is to be notified of delivery.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableQuantumView:bool = obj["EnableQuantumView"]
      """  Logical indicating if the UPS email fields are to be enabled.  """  
      self.ShipStatus:str = obj["ShipStatus"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtCustShipTableset:
   def __init__(self, obj):
      self.ShipHead:list[Erp_Tablesets_ShipHeadRow] = obj["ShipHead"]
      self.ShipHeadAttch:list[Erp_Tablesets_ShipHeadAttchRow] = obj["ShipHeadAttch"]
      self.CartonTrkDtl:list[Erp_Tablesets_CartonTrkDtlRow] = obj["CartonTrkDtl"]
      self.ShipDtl:list[Erp_Tablesets_ShipDtlRow] = obj["ShipDtl"]
      self.ShipDtlAttch:list[Erp_Tablesets_ShipDtlAttchRow] = obj["ShipDtlAttch"]
      self.ShipCOO:list[Erp_Tablesets_ShipCOORow] = obj["ShipCOO"]
      self.ShipDtlPackaging:list[Erp_Tablesets_ShipDtlPackagingRow] = obj["ShipDtlPackaging"]
      self.ShipDtlTax:list[Erp_Tablesets_ShipDtlTaxRow] = obj["ShipDtlTax"]
      self.ShipHeadInsurance:list[Erp_Tablesets_ShipHeadInsuranceRow] = obj["ShipHeadInsurance"]
      self.ShipMisc:list[Erp_Tablesets_ShipMiscRow] = obj["ShipMisc"]
      self.ReplicatedPacks:list[Erp_Tablesets_ReplicatedPacksRow] = obj["ReplicatedPacks"]
      self.ShipHeadTrailer:list[Erp_Tablesets_ShipHeadTrailerRow] = obj["ShipHeadTrailer"]
      self.ShipUPS:list[Erp_Tablesets_ShipUPSRow] = obj["ShipUPS"]
      self.LegalNumberGenerate:list[Erp_Tablesets_LegalNumberGenerateRow] = obj["LegalNumberGenerate"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SalesKitCompIssue:list[Erp_Tablesets_SalesKitCompIssueRow] = obj["SalesKitCompIssue"]
      self.SelectedIDNumbers:list[Erp_Tablesets_SelectedIDNumbersRow] = obj["SelectedIDNumbers"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.ShipTaxSum:list[Erp_Tablesets_ShipTaxSumRow] = obj["ShipTaxSum"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_serialNumbersToMatchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.SerialNumber:str = obj["SerialNumber"]
      self.validSerialNo:bool = obj["validSerialNo"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class ExpireDate_input:
   """ Required : 
   ExpirationDate
   EffectiveDAte
   Duration
   modifier
   """  
   def __init__(self, obj):
      self.ExpirationDate:str = obj["ExpirationDate"]
      self.EffectiveDAte:str = obj["EffectiveDAte"]
      self.Duration:int = obj["Duration"]
      self.modifier:str = obj["modifier"]
      pass

class ExpireDate_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ExpressShip_output:
   def __init__(self, obj):
      pass

class GenerateDigitalSignature_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class GenerateDigitalSignature_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GenerateLocationIDNum_input:
   """ Required : 
   ds
   ipPackNum
   ipPackLine
   ipFromMfg
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.ipPackNum:int = obj["ipPackNum"]
      """  PackNum  """  
      self.ipPackLine:int = obj["ipPackLine"]
      """  PackLine  """  
      self.ipFromMfg:bool = obj["ipFromMfg"]
      """  Called from Mfg  """  
      pass

class GenerateLocationIDNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GenerateSelectIDNumParams_input:
   """ Required : 
   SNList
   ipPartNum
   ipPackNum
   ipPackLine
   ipJobNum
   ipUom
   ipFromMfg
   """  
   def __init__(self, obj):
      self.SNList:str = obj["SNList"]
      self.ipPartNum:str = obj["ipPartNum"]
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipPackLine:int = obj["ipPackLine"]
      self.ipJobNum:str = obj["ipJobNum"]
      self.ipUom:str = obj["ipUom"]
      self.ipFromMfg:bool = obj["ipFromMfg"]
      pass

class GenerateSelectIDNumParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustShipTableset] = obj["returnObj"]
      pass

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.AvailTranDocTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   packNum
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustShipTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CustShipTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CustShipTableset] = obj["returnObj"]
      pass

class GetCartonPackaging_input:
   """ Required : 
   ipPkgCode
   """  
   def __init__(self, obj):
      self.ipPkgCode:str = obj["ipPkgCode"]
      pass

class GetCartonPackaging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPkgHeight:int = obj["parameters"]
      self.opPkgWidth:int = obj["parameters"]
      self.opPkgLength:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  ipTableName  """  
      self.fieldName:str = obj["fieldName"]
      """  ipFieldName  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCustShipOrdTrk_input:
   """ Required : 
   orderNum
   """  
   def __init__(self, obj):
      self.orderNum:int = obj["orderNum"]
      """  Order Number  """  
      pass

class GetCustShipOrdTrk_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustShipOrdTrkTableset] = obj["returnObj"]
      pass

class GetDisablePackOut_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetEnablePackageControl_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  bool  """  
      pass

class GetHeadOrderInfo_input:
   """ Required : 
   orderNum
   ds
   """  
   def __init__(self, obj):
      self.orderNum:int = obj["orderNum"]
      """  Proposed change to OrderNum  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class GetHeadOrderInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.creditMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetJobDtlInfo_input:
   """ Required : 
   ds
   packLine
   jobNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.packLine:int = obj["packLine"]
      """  Detail Line Number to update  """  
      self.jobNum:str = obj["jobNum"]
      """  Proposed change to JobNum field  """  
      pass

class GetJobDtlInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetJobInfo_input:
   """ Required : 
   jobNum
   ds
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  proposed JobNum change on ShipDtl  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class GetJobInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.creditMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetJobSupOpSeq_input:
   """ Required : 
   jobNum
   partNum
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  JobNum field  """  
      self.partNum:str = obj["partNum"]
      """  The part number to validate  """  
      pass

class GetJobSupOpSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.mtlSeq:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetLegalNumGenOpts_input:
   """ Required : 
   ipPackNum
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Packing Slip number  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class GetLegalNumGenOpts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.opPromptForNum:bool = obj["opPromptForNum"]
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
      self.returnObj:list[Erp_Tablesets_ShipHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetManifestInfo_input:
   """ Required : 
   ipSalesOrder
   ipPackNum
   ds
   """  
   def __init__(self, obj):
      self.ipSalesOrder:int = obj["ipSalesOrder"]
      self.ipPackNum:int = obj["ipPackNum"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class GetManifestInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCartonTrkDtl_input:
   """ Required : 
   ds
   shipmentType
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.shipmentType:str = obj["shipmentType"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewCartonTrkDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewOrdrShipDtl_input:
   """ Required : 
   ds
   packNum
   orderNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      """  Pack ID  """  
      self.orderNum:int = obj["orderNum"]
      """  Order number to default in the new record (optional)  """  
      pass

class GetNewOrdrShipDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewOrdrShipUPS_input:
   """ Required : 
   ds
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      """  Pack ID  """  
      pass

class GetNewOrdrShipUPS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewShipCOO_input:
   """ Required : 
   ds
   relatedToFile
   packNum
   packLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.packNum:int = obj["packNum"]
      self.packLine:int = obj["packLine"]
      pass

class GetNewShipCOO_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewShipDtlAttch_input:
   """ Required : 
   ds
   packNum
   packLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      self.packLine:int = obj["packLine"]
      pass

class GetNewShipDtlAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewShipDtlTax_input:
   """ Required : 
   ds
   packNum
   packLine
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      self.packLine:int = obj["packLine"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewShipDtlTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewShipDtl_input:
   """ Required : 
   ds
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewShipDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewShipHeadAttch_input:
   """ Required : 
   ds
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewShipHeadAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewShipHeadInsurance_input:
   """ Required : 
   ds
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewShipHeadInsurance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewShipHeadTrailer_input:
   """ Required : 
   ds
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewShipHeadTrailer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewShipHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class GetNewShipHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewShipMisc_input:
   """ Required : 
   ds
   packNum
   packLine
   seqNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      self.packLine:int = obj["packLine"]
      self.seqNum:int = obj["seqNum"]
      pass

class GetNewShipMisc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewShipUPS_input:
   """ Required : 
   ds
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewShipUPS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOrderInfo_input:
   """ Required : 
   orderNum
   ds
   """  
   def __init__(self, obj):
      self.orderNum:int = obj["orderNum"]
      """  Proposed change to OrderNum  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class GetOrderInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.creditMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOrderLineInfo_input:
   """ Required : 
   ds
   packLine
   orderLine
   subsPart
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.packLine:int = obj["packLine"]
      """  Detail Line Number to update  """  
      self.orderLine:int = obj["orderLine"]
      """  Proposed Orderline change  """  
      self.subsPart:str = obj["subsPart"]
      """  Proposed substitute PartNum  """  
      pass

class GetOrderLineInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOrderRelInfo_input:
   """ Required : 
   ds
   packLine
   orderRelNum
   allowNewShipTo
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.packLine:int = obj["packLine"]
      """  Detail Line Number to update  """  
      self.orderRelNum:int = obj["orderRelNum"]
      """  Proposed OrderRelease change  """  
      self.allowNewShipTo:bool = obj["allowNewShipTo"]
      """  Allow to take new ShipTo from release  """  
      pass

class GetOrderRelInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPOPackClass_input:
   """ Required : 
   ipPkgClass
   ds
   """  
   def __init__(self, obj):
      self.ipPkgClass:str = obj["ipPkgClass"]
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class GetPOPackClass_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPOPackaging_input:
   """ Required : 
   ipPkgCode
   ds
   """  
   def __init__(self, obj):
      self.ipPkgCode:str = obj["ipPkgCode"]
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class GetPOPackaging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPackClass_input:
   """ Required : 
   ipPkgClass
   ds
   """  
   def __init__(self, obj):
      self.ipPkgClass:str = obj["ipPkgClass"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class GetPackClass_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPackOutPartXRef_input:
   """ Required : 
   ds
   packLine
   partNum
   SysRowID
   rowType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      self.packLine:int = obj["packLine"]
      """  Detail Line Number to update  """  
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      pass

class GetPackOutPartXRef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      self.partNum:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class GetPackageControlPackVoid_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      pass

class GetPackageControlPackVoid_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PackageControlPackVoidTableset] = obj["returnObj"]
      pass

class GetPackaging_input:
   """ Required : 
   ipPkgCode
   ds
   """  
   def __init__(self, obj):
      self.ipPkgCode:str = obj["ipPkgCode"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class GetPackaging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartInfo_input:
   """ Required : 
   ds
   packLine
   partNum
   SysRowID
   rowType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.packLine:int = obj["packLine"]
      """  Detail Line Number to update  """  
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      pass

class GetPartInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.partNum:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      self.idWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPayBTFlagDefaults_input:
   """ Required : 
   ipOrderNum
   ipPayFlag
   ds
   """  
   def __init__(self, obj):
      self.ipOrderNum:int = obj["ipOrderNum"]
      self.ipPayFlag:str = obj["ipPayFlag"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class GetPayBTFlagDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPkgCodeQtyList_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      pass

class GetPkgCodeQtyList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPkgCodeList:list = obj[any]
      pass

      """  output parameters  """  

class GetQtyInfo_input:
   """ Required : 
   ds
   packLine
   displayInvQty
   ourJobShipQty
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.packLine:int = obj["packLine"]
      """  Detail Line Number to update  """  
      self.displayInvQty:int = obj["displayInvQty"]
      """  Proposed change to Inventory Qty field  """  
      self.ourJobShipQty:int = obj["ourJobShipQty"]
      """  Proposed change to OurJobShipQty field  """  
      pass

class GetQtyInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsContactTracker_input:
   """ Required : 
   whereClauseShipHead
   whereClauseShipHeadAttch
   whereClauseShipDtl
   whereClauseShipDtlAttch
   whereClauseShipMisc
   whereClauseSelectedSerialNumbers
   whereClauseSerialNumberSearch
   whereClauseSNFormat
   contactName
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseShipHead:str = obj["whereClauseShipHead"]
      """  Whereclause for ShipHead table.  """  
      self.whereClauseShipHeadAttch:str = obj["whereClauseShipHeadAttch"]
      """  Whereclause for ShipHeadAttch table.  """  
      self.whereClauseShipDtl:str = obj["whereClauseShipDtl"]
      """  Whereclause for ShipDtl table.  """  
      self.whereClauseShipDtlAttch:str = obj["whereClauseShipDtlAttch"]
      """  Whereclause for ShipDtlAttch table.  """  
      self.whereClauseShipMisc:str = obj["whereClauseShipMisc"]
      """  Whereclause for ShipMisc table.  """  
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      """  Whereclause for SelectedSerialNumbers table.  """  
      self.whereClauseSerialNumberSearch:str = obj["whereClauseSerialNumberSearch"]
      """  Whereclause for SerialNumberSearches table.  """  
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      """  Whereclause for SNFormat table.  """  
      self.contactName:str = obj["contactName"]
      """  Contact to return data for.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsContactTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustShipCustTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustomerTrackerAndSort_input:
   """ Required : 
   whereClauseShipHead
   whereClauseShipHeadAttch
   whereClauseShipDtl
   whereClauseShipDtlAttch
   whereClauseShipMisc
   whereClauseSelectedSerialNumbers
   whereClauseSerialNumberSearch
   whereClauseSNFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseShipHead:str = obj["whereClauseShipHead"]
      """  Whereclause for ShipHead table.  """  
      self.whereClauseShipHeadAttch:str = obj["whereClauseShipHeadAttch"]
      """  Whereclause for ShipHeadAttch table.  """  
      self.whereClauseShipDtl:str = obj["whereClauseShipDtl"]
      """  Whereclause for ShipDtl table.  """  
      self.whereClauseShipDtlAttch:str = obj["whereClauseShipDtlAttch"]
      """  Whereclause for ShipDtlAttch table.  """  
      self.whereClauseShipMisc:str = obj["whereClauseShipMisc"]
      """  Whereclause for ShipMisc table.  """  
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      """  Whereclause for SelectedSerialNumbers table.  """  
      self.whereClauseSerialNumberSearch:str = obj["whereClauseSerialNumberSearch"]
      """  Whereclause for SerialNumberSearch table.  """  
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      """  Whereclause for SNFormat table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsCustomerTrackerAndSort_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustShipCustTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustomerTracker_input:
   """ Required : 
   whereClauseShipHead
   whereClauseShipHeadAttch
   whereClauseShipDtl
   whereClauseShipDtlAttch
   whereClauseShipMisc
   whereClauseSelectedSerialNumbers
   whereClauseSerialNumberSearch
   whereClauseSNFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseShipHead:str = obj["whereClauseShipHead"]
      """  Whereclause for ShipHead table.  """  
      self.whereClauseShipHeadAttch:str = obj["whereClauseShipHeadAttch"]
      """  Whereclause for ShipHeadAttch table.  """  
      self.whereClauseShipDtl:str = obj["whereClauseShipDtl"]
      """  Whereclause for ShipDtl table.  """  
      self.whereClauseShipDtlAttch:str = obj["whereClauseShipDtlAttch"]
      """  Whereclause for ShipDtlAttch table.  """  
      self.whereClauseShipMisc:str = obj["whereClauseShipMisc"]
      """  Whereclause for ShipMisc table.  """  
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      """  Whereclause for SelectedSerialNumbers table.  """  
      self.whereClauseSerialNumberSearch:str = obj["whereClauseSerialNumberSearch"]
      """  Whereclause for SerialNumberSearches table.  """  
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      """  Whereclause for SNFormat table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsCustomerTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustShipCustTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsForCashReceipt_input:
   """ Required : 
   whereClauseShipHead
   whereClauseShipHeadAttch
   whereClauseCartonTrkDtl
   whereClauseShipDtl
   whereClauseShipDtlAttch
   whereClauseShipCOO
   whereClauseShipDtlPackaging
   whereClauseShipDtlTax
   whereClauseShipHeadInsurance
   whereClauseShipMisc
   whereClauseReplicatedPacks
   whereClauseShipHeadTrailer
   whereClauseShipUPS
   whereClauseLegalNumberGenerate
   whereClauseLegalNumGenOpts
   whereClauseSalesKitCompIssue
   whereClauseSelectedIDNumbers
   whereClauseSelectedSerialNumbers
   whereClauseShipTaxSum
   whereClauseSNFormat
   groupID
   headNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseShipHead:str = obj["whereClauseShipHead"]
      self.whereClauseShipHeadAttch:str = obj["whereClauseShipHeadAttch"]
      self.whereClauseCartonTrkDtl:str = obj["whereClauseCartonTrkDtl"]
      self.whereClauseShipDtl:str = obj["whereClauseShipDtl"]
      self.whereClauseShipDtlAttch:str = obj["whereClauseShipDtlAttch"]
      self.whereClauseShipCOO:str = obj["whereClauseShipCOO"]
      self.whereClauseShipDtlPackaging:str = obj["whereClauseShipDtlPackaging"]
      self.whereClauseShipDtlTax:str = obj["whereClauseShipDtlTax"]
      self.whereClauseShipHeadInsurance:str = obj["whereClauseShipHeadInsurance"]
      self.whereClauseShipMisc:str = obj["whereClauseShipMisc"]
      self.whereClauseReplicatedPacks:str = obj["whereClauseReplicatedPacks"]
      self.whereClauseShipHeadTrailer:str = obj["whereClauseShipHeadTrailer"]
      self.whereClauseShipUPS:str = obj["whereClauseShipUPS"]
      self.whereClauseLegalNumberGenerate:str = obj["whereClauseLegalNumberGenerate"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.whereClauseSalesKitCompIssue:str = obj["whereClauseSalesKitCompIssue"]
      self.whereClauseSelectedIDNumbers:str = obj["whereClauseSelectedIDNumbers"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseShipTaxSum:str = obj["whereClauseShipTaxSum"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForCashReceipt_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustShipTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsForInvoice_input:
   """ Required : 
   whereClauseShipHead
   whereClauseShipHeadAttch
   whereClauseCartonTrkDtl
   whereClauseShipDtl
   whereClauseShipDtlAttch
   whereClauseShipCOO
   whereClauseShipDtlPackaging
   whereClauseShipDtlTax
   whereClauseShipHeadInsurance
   whereClauseShipMisc
   whereClauseReplicatedPacks
   whereClauseShipHeadTrailer
   whereClauseShipUPS
   whereClauseLegalNumberGenerate
   whereClauseLegalNumGenOpts
   whereClauseSalesKitCompIssue
   whereClauseSelectedIDNumbers
   whereClauseSelectedSerialNumbers
   whereClauseShipTaxSum
   whereClauseSNFormat
   invoiceNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseShipHead:str = obj["whereClauseShipHead"]
      self.whereClauseShipHeadAttch:str = obj["whereClauseShipHeadAttch"]
      self.whereClauseCartonTrkDtl:str = obj["whereClauseCartonTrkDtl"]
      self.whereClauseShipDtl:str = obj["whereClauseShipDtl"]
      self.whereClauseShipDtlAttch:str = obj["whereClauseShipDtlAttch"]
      self.whereClauseShipCOO:str = obj["whereClauseShipCOO"]
      self.whereClauseShipDtlPackaging:str = obj["whereClauseShipDtlPackaging"]
      self.whereClauseShipDtlTax:str = obj["whereClauseShipDtlTax"]
      self.whereClauseShipHeadInsurance:str = obj["whereClauseShipHeadInsurance"]
      self.whereClauseShipMisc:str = obj["whereClauseShipMisc"]
      self.whereClauseReplicatedPacks:str = obj["whereClauseReplicatedPacks"]
      self.whereClauseShipHeadTrailer:str = obj["whereClauseShipHeadTrailer"]
      self.whereClauseShipUPS:str = obj["whereClauseShipUPS"]
      self.whereClauseLegalNumberGenerate:str = obj["whereClauseLegalNumberGenerate"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.whereClauseSalesKitCompIssue:str = obj["whereClauseSalesKitCompIssue"]
      self.whereClauseSelectedIDNumbers:str = obj["whereClauseSelectedIDNumbers"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseShipTaxSum:str = obj["whereClauseShipTaxSum"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.invoiceNum:int = obj["invoiceNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForInvoice_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustShipTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsForQuote_input:
   """ Required : 
   whereClauseShipHead
   whereClauseShipHeadAttch
   whereClauseCartonTrkDtl
   whereClauseShipDtl
   whereClauseShipDtlAttch
   whereClauseShipCOO
   whereClauseShipDtlPackaging
   whereClauseShipDtlTax
   whereClauseShipHeadInsurance
   whereClauseShipMisc
   whereClauseReplicatedPacks
   whereClauseShipHeadTrailer
   whereClauseShipUPS
   whereClauseLegalNumberGenerate
   whereClauseLegalNumGenOpts
   whereClauseSalesKitCompIssue
   whereClauseSelectedIDNumbers
   whereClauseSelectedSerialNumbers
   whereClauseShipTaxSum
   whereClauseSNFormat
   quoteNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseShipHead:str = obj["whereClauseShipHead"]
      self.whereClauseShipHeadAttch:str = obj["whereClauseShipHeadAttch"]
      self.whereClauseCartonTrkDtl:str = obj["whereClauseCartonTrkDtl"]
      self.whereClauseShipDtl:str = obj["whereClauseShipDtl"]
      self.whereClauseShipDtlAttch:str = obj["whereClauseShipDtlAttch"]
      self.whereClauseShipCOO:str = obj["whereClauseShipCOO"]
      self.whereClauseShipDtlPackaging:str = obj["whereClauseShipDtlPackaging"]
      self.whereClauseShipDtlTax:str = obj["whereClauseShipDtlTax"]
      self.whereClauseShipHeadInsurance:str = obj["whereClauseShipHeadInsurance"]
      self.whereClauseShipMisc:str = obj["whereClauseShipMisc"]
      self.whereClauseReplicatedPacks:str = obj["whereClauseReplicatedPacks"]
      self.whereClauseShipHeadTrailer:str = obj["whereClauseShipHeadTrailer"]
      self.whereClauseShipUPS:str = obj["whereClauseShipUPS"]
      self.whereClauseLegalNumberGenerate:str = obj["whereClauseLegalNumberGenerate"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.whereClauseSalesKitCompIssue:str = obj["whereClauseSalesKitCompIssue"]
      self.whereClauseSelectedIDNumbers:str = obj["whereClauseSelectedIDNumbers"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseShipTaxSum:str = obj["whereClauseShipTaxSum"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.quoteNum:int = obj["quoteNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForQuote_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustShipTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseShipHead
   whereClauseShipHeadAttch
   whereClauseCartonTrkDtl
   whereClauseShipDtl
   whereClauseShipDtlAttch
   whereClauseShipCOO
   whereClauseShipDtlPackaging
   whereClauseShipDtlTax
   whereClauseShipHeadInsurance
   whereClauseShipMisc
   whereClauseReplicatedPacks
   whereClauseShipHeadTrailer
   whereClauseShipUPS
   whereClauseLegalNumberGenerate
   whereClauseLegalNumGenOpts
   whereClauseSalesKitCompIssue
   whereClauseSelectedIDNumbers
   whereClauseSelectedSerialNumbers
   whereClauseShipTaxSum
   whereClauseSNFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseShipHead:str = obj["whereClauseShipHead"]
      self.whereClauseShipHeadAttch:str = obj["whereClauseShipHeadAttch"]
      self.whereClauseCartonTrkDtl:str = obj["whereClauseCartonTrkDtl"]
      self.whereClauseShipDtl:str = obj["whereClauseShipDtl"]
      self.whereClauseShipDtlAttch:str = obj["whereClauseShipDtlAttch"]
      self.whereClauseShipCOO:str = obj["whereClauseShipCOO"]
      self.whereClauseShipDtlPackaging:str = obj["whereClauseShipDtlPackaging"]
      self.whereClauseShipDtlTax:str = obj["whereClauseShipDtlTax"]
      self.whereClauseShipHeadInsurance:str = obj["whereClauseShipHeadInsurance"]
      self.whereClauseShipMisc:str = obj["whereClauseShipMisc"]
      self.whereClauseReplicatedPacks:str = obj["whereClauseReplicatedPacks"]
      self.whereClauseShipHeadTrailer:str = obj["whereClauseShipHeadTrailer"]
      self.whereClauseShipUPS:str = obj["whereClauseShipUPS"]
      self.whereClauseLegalNumberGenerate:str = obj["whereClauseLegalNumberGenerate"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.whereClauseSalesKitCompIssue:str = obj["whereClauseSalesKitCompIssue"]
      self.whereClauseSelectedIDNumbers:str = obj["whereClauseSelectedIDNumbers"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseShipTaxSum:str = obj["whereClauseShipTaxSum"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustShipTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetScale_input:
   """ Required : 
   workstationID
   """  
   def __init__(self, obj):
      self.workstationID:str = obj["workstationID"]
      """  Workstation ID  """  
      pass

class GetScale_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.scaleID:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetSelectIDNumbersParams_input:
   """ Required : 
   partNum
   shipQty
   shipUOM
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.shipQty:int = obj["shipQty"]
      self.shipUOM:str = obj["shipUOM"]
      pass

class GetSelectIDNumbersParams_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.convShipQty:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParams_input:
   """ Required : 
   ipPartNum
   ipAttributeSetID
   ipQuantity
   ipUOM
   ipPackNum
   ipPackLine
   ipTranType
   ipJobNum
   ipWhseCode
   ipBinNum
   ipLotNum
   ipFromPO
   ipOrderNum
   ipOrderLine
   ipOrderRelNum
   ipSysRowID
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      self.ipAttributeSetID:int = obj["ipAttributeSetID"]
      self.ipQuantity:int = obj["ipQuantity"]
      self.ipUOM:str = obj["ipUOM"]
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipPackLine:int = obj["ipPackLine"]
      self.ipTranType:str = obj["ipTranType"]
      self.ipJobNum:str = obj["ipJobNum"]
      self.ipWhseCode:str = obj["ipWhseCode"]
      self.ipBinNum:str = obj["ipBinNum"]
      self.ipLotNum:str = obj["ipLotNum"]
      self.ipFromPO:bool = obj["ipFromPO"]
      self.ipOrderNum:int = obj["ipOrderNum"]
      self.ipOrderLine:int = obj["ipOrderLine"]
      self.ipOrderRelNum:int = obj["ipOrderRelNum"]
      self.ipSysRowID:str = obj["ipSysRowID"]
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

class GetShipMiscDefaults_input:
   """ Required : 
   ds
   miscCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.miscCode:str = obj["miscCode"]
      """  Proposed Miscellaneous Code change  """  
      pass

class GetShipMiscDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetShipToAddr_input:
   """ Required : 
   ds
   shipToNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.shipToNum:str = obj["shipToNum"]
      """  Proposed ShipTo Number change  """  
      pass

class GetShipToAddr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetShipmentRelationshipMap_input:
   """ Required : 
   packNum
   maxNumOfCards
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      self.maxNumOfCards:int = obj["maxNumOfCards"]
      pass

class GetShipmentRelationshipMap_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetTranDocTypeID_input:
   """ Required : 
   ipTranDocTypeID
   ds
   """  
   def __init__(self, obj):
      self.ipTranDocTypeID:str = obj["ipTranDocTypeID"]
      """  TranDocTypeID supplied  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class GetTranDocTypeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetWarrantyInfo_input:
   """ Required : 
   ds
   warrantyCode
   orderLine
   orderRelNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.warrantyCode:str = obj["warrantyCode"]
      self.orderLine:int = obj["orderLine"]
      self.orderRelNum:int = obj["orderRelNum"]
      pass

class GetWarrantyInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetWhseInfo_input:
   """ Required : 
   ds
   packLine
   whseCode
   whseField
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.packLine:int = obj["packLine"]
      """  Detail Line Number to update  """  
      self.whseCode:str = obj["whseCode"]
      """  Proposed WarehouseCode change  """  
      self.whseField:str = obj["whseField"]
      """  Warehouse field that is being changed  """  
      pass

class GetWhseInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class HHCreateMassShipDtl_input:
   """ Required : 
   packNum
   orderNum
   ds
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      """  Pack Number to add new shipment lines to  """  
      self.orderNum:int = obj["orderNum"]
      """  Order Number to create shipment lines from  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class HHCreateMassShipDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class HHGetOrderInfo_input:
   """ Required : 
   orderNum
   ds
   """  
   def __init__(self, obj):
      self.orderNum:int = obj["orderNum"]
      """  Proposed change to OrderNum  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class HHGetOrderInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.creditMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class HHSetDtlDefaultValues_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class HHSetDtlDefaultValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
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

class MarkShipmentLines_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class MarkShipmentLines_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class NegativeInventoryTest_input:
   """ Required : 
   ipPartNum
   ipWarehouseCode
   ipBinNum
   ipLotNum
   ipAttributeSetID
   ipPCID
   ipDimCode
   ipDimConvFactor
   ipTranQty
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  ipPartNum  """  
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  ipWarehouseCode  """  
      self.ipBinNum:str = obj["ipBinNum"]
      """  ipBinNum  """  
      self.ipLotNum:str = obj["ipLotNum"]
      """  ipLotNum  """  
      self.ipAttributeSetID:int = obj["ipAttributeSetID"]
      """  ipAttributeSetID  """  
      self.ipPCID:str = obj["ipPCID"]
      """  ipPCID  """  
      self.ipDimCode:str = obj["ipDimCode"]
      """  ipDimCode  """  
      self.ipDimConvFactor:int = obj["ipDimConvFactor"]
      """  ipDimConvFactor  """  
      self.ipTranQty:int = obj["ipTranQty"]
      """  ipTranQty  """  
      pass

class NegativeInventoryTest_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opNegQtyAction:str = obj["parameters"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangePickeOrdersIsSelected_input:
   """ Required : 
   ipOrderNum
   ipOrderLine
   pickedOrderRowSysRowID
   oldIsSelected
   ds
   """  
   def __init__(self, obj):
      self.ipOrderNum:int = obj["ipOrderNum"]
      """  input order number  """  
      self.ipOrderLine:int = obj["ipOrderLine"]
      """  input order line  """  
      self.pickedOrderRowSysRowID:str = obj["pickedOrderRowSysRowID"]
      """  SysRowID of the PickedOrders row being changed  """  
      self.oldIsSelected:bool = obj["oldIsSelected"]
      """  New value for IsSelected  """  
      self.ds:list[Erp_Tablesets_CustShipPickedOrdersTableset] = obj["ds"]
      pass

class OnChangePickeOrdersIsSelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipPickedOrdersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeShipViaCode_input:
   """ Required : 
   shipViaCode
   ds
   """  
   def __init__(self, obj):
      self.shipViaCode:str = obj["shipViaCode"]
      """  New ShipVia Code  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class OnChangeShipViaCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeUPSQuantumView_input:
   """ Required : 
   ipPackNum
   ipQVEnable
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipQVEnable:bool = obj["ipQVEnable"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class OnChangeUPSQuantumView_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingAttributeSet_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class OnChangingAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingDispNumberOfPieces_input:
   """ Required : 
   numberOfPieces
   shippingFrom
   ds
   """  
   def __init__(self, obj):
      self.numberOfPieces:int = obj["numberOfPieces"]
      """  The proposed numberOfPieces  """  
      self.shippingFrom:str = obj["shippingFrom"]
      """  The Number of Pieces field that is changing (INVENTORY or JOB)  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class OnChangingDispNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingRevisionNumPackOut_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class OnChangingRevisionNumPackOut_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class OnChangingRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class POChangeStage_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class POChangeStage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class POChangeStatus_input:
   """ Required : 
   ipStatus
   ipResetCODCharges
   ipResetInsCharges
   ds
   """  
   def __init__(self, obj):
      self.ipStatus:str = obj["ipStatus"]
      """  Selected Status.
           Valid Options: Open, Close, Void, UnVoid, Freight, UnFreight, Stage  """  
      self.ipResetCODCharges:bool = obj["ipResetCODCharges"]
      """  Indicates if the CODAmount is to be reset to zero  """  
      self.ipResetInsCharges:bool = obj["ipResetInsCharges"]
      """  Indicates if the DeclaredAmt is to be reset to zero  """  
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class POChangeStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class POFindBufWhseBinLot_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class POFindBufWhseBinLot_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.found:int = obj["parameters"]
      self.rowident:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class POFindBuffer_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class POFindBuffer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.found:int = obj["parameters"]
      self.rowident:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class POGetDtlList_input:
   """ Required : 
   ipPackNum
   ipPCID
   ipOrderNum
   ipPackMode
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Pack Number  """  
      self.ipPCID:str = obj["ipPCID"]
      """  PCID  """  
      self.ipOrderNum:int = obj["ipOrderNum"]
      """  Order to get detail from  """  
      self.ipPackMode:str = obj["ipPackMode"]
      """  Pack Mode  """  
      pass

class POGetDtlList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PackOutTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.cWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class POGetLegalNumGenOpts_input:
   """ Required : 
   ipPackNum
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Packing Slip number  """  
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class POGetLegalNumGenOpts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      self.opPromptForNum:bool = obj["opPromptForNum"]
      pass

      """  output parameters  """  

class POGetNewWithDtl_input:
   """ Required : 
   ipOrderNum
   ipPackNum
   ipPCID
   ipPackMode
   """  
   def __init__(self, obj):
      self.ipOrderNum:int = obj["ipOrderNum"]
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipPCID:str = obj["ipPCID"]
      self.ipPackMode:str = obj["ipPackMode"]
      pass

class POGetNewWithDtl_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PackOutTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.pcWarningMsg:str = obj["parameters"]
      self.cWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class POGetNew_input:
   """ Required : 
   ipOrderNum
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipOrderNum:int = obj["ipOrderNum"]
      """  Order Number  """  
      self.ipPackNum:int = obj["ipPackNum"]
      """  Pack Num  """  
      pass

class POGetNew_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PackOutTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.pcWarningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class POGetShipTo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class POGetShipTo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class POUpdateAndDisplay_input:
   """ Required : 
   ipSourceRowID
   poLinkValues
   currLine
   ds
   """  
   def __init__(self, obj):
      self.ipSourceRowID:str = obj["ipSourceRowID"]
      """  RowIdent  """  
      self.poLinkValues:str = obj["poLinkValues"]
      """  poLinkValues  """  
      self.currLine:int = obj["currLine"]
      """  Pack Line  """  
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class POUpdateAndDisplay_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPackNum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      self.dspLegalNumMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class POUpdate_input:
   """ Required : 
   ipSourceRowID
   poLinkValues
   ds
   """  
   def __init__(self, obj):
      self.ipSourceRowID:str = obj["ipSourceRowID"]
      """  RowIdent  """  
      self.poLinkValues:str = obj["poLinkValues"]
      """  poLinkValues  """  
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class POUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPackNum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class POValidateOrderRel_input:
   """ Required : 
   ipPackNum
   ipOrderNum
   ipOrderLine
   ipOrderRelNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipOrderNum:int = obj["ipOrderNum"]
      self.ipOrderLine:int = obj["ipOrderLine"]
      self.ipOrderRelNum:int = obj["ipOrderRelNum"]
      pass

class POValidateOrderRel_output:
   def __init__(self, obj):
      pass

class POValidateOrder_input:
   """ Required : 
   ipCustNum
   ipOrderNum
   """  
   def __init__(self, obj):
      self.ipCustNum:int = obj["ipCustNum"]
      """  Customer Number  """  
      self.ipOrderNum:int = obj["ipOrderNum"]
      """  Order chose to add to carton  """  
      pass

class POValidateOrder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opVaildOrder:bool = obj["opVaildOrder"]
      pass

      """  output parameters  """  

class POValidatePart_input:
   """ Required : 
   ipPartNum
   ipOrderNum
   ds
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  Proposed part number.  """  
      self.ipOrderNum:int = obj["ipOrderNum"]
      """  Order number.  """  
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class POValidatePart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      self.opValidPart:bool = obj["opValidPart"]
      self.vMsgText:str = obj["parameters"]
      self.vSubAvail:bool = obj["vSubAvail"]
      self.vMsgType:str = obj["parameters"]
      pass

      """  output parameters  """  

class PackVerifyCalcPackPCIDCount_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  ipPackNum  """  
      pass

class PackVerifyCalcPackPCIDCount_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class PackVerifyPerformPackVerification_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  The Pack Number for the verification  """  
      pass

class PackVerifyPerformPackVerification_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opErrorMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class PartNumChangeUserPrompts_input:
   """ Required : 
   ds
   packLine
   partNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.packLine:int = obj["packLine"]
      """  Detail Line Number to update  """  
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      pass

class PartNumChangeUserPrompts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.idWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class PhantomStatusCheck_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      pass

class PhantomStatusCheck_output:
   def __init__(self, obj):
      pass

class PostUpdate_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Customer Shipment Number  """  
      pass

class PostUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreCreateMassShipDtl_input:
   """ Required : 
   packNum
   orderNum
   ds
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      """  Pack Number to add new shipment lines to  """  
      self.orderNum:int = obj["orderNum"]
      """  Order Number to create shipment lines from  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class PreCreateMassShipDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warnMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PrePickedOrders_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipPickedOrdersTableset] = obj["ds"]
      pass

class PrePickedOrders_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipPickedOrdersTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class PrintSlip_input:
   """ Required : 
   packNum
   printPreview
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      """  The Packing Slip Number to print  """  
      self.printPreview:bool = obj["printPreview"]
      """  Flag if print should be previewed.  """  
      pass

class PrintSlip_output:
   def __init__(self, obj):
      pass

class ProcessKitChildern_input:
   """ Required : 
   ipOrderNum
   ipOrderLine
   """  
   def __init__(self, obj):
      self.ipOrderNum:int = obj["ipOrderNum"]
      """  input order number  """  
      self.ipOrderLine:int = obj["ipOrderLine"]
      """  input order line  """  
      pass

class ProcessKitChildern_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ProcessMassShipKit_output:
   def __init__(self, obj):
      pass

class ProcessNegQtyTest_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  current pack number  """  
      pass

class ProcessNegQtyTest_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opWarnMessage:str = obj["parameters"]
      self.opAskMessage:str = obj["parameters"]
      self.opStopMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ProcessPickedOrderHH_input:
   """ Required : 
   pConsolidate
   skipDelete
   ds
   """  
   def __init__(self, obj):
      self.pConsolidate:bool = obj["pConsolidate"]
      """  Consolidates Orders in a single Carton.  """  
      self.skipDelete:bool = obj["skipDelete"]
      """  Skip Delete? (for testing purposes)  """  
      self.ds:list[Erp_Tablesets_CustShipPickedOrdersTableset] = obj["ds"]
      pass

class ProcessPickedOrderHH_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ShipHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_CustShipPickedOrdersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProcessPickedOrder_input:
   """ Required : 
   pConsolidate
   skipDelete
   ds
   """  
   def __init__(self, obj):
      self.pConsolidate:bool = obj["pConsolidate"]
      """  Consolidates Orders in a single Carton.  """  
      self.skipDelete:bool = obj["skipDelete"]
      """  Skip Delete? (for testing purposes)  """  
      self.ds:list[Erp_Tablesets_CustShipPickedOrdersTableset] = obj["ds"]
      pass

class ProcessPickedOrder_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ShipHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_CustShipPickedOrdersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RebuildShipUPS_input:
   """ Required : 
   ipPackNum
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class RebuildShipUPS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RemovePCID_input:
   """ Required : 
   ipSource
   ipPackNum
   ipPCID
   ds
   """  
   def __init__(self, obj):
      self.ipSource:str = obj["ipSource"]
      """  ipSource  """  
      self.ipPackNum:int = obj["ipPackNum"]
      """  ipPackNum  """  
      self.ipPCID:str = obj["ipPCID"]
      """  ipPCID  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class RemovePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.opPCIDCount:int = obj["parameters"]
      pass

      """  output parameters  """  

class SetShippedFromPackout_input:
   """ Required : 
   ds
   packNum
   shipped
   firstRun
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      """  Pack Number  """  
      self.shipped:bool = obj["shipped"]
      """  Indicates if the shipment is shipped or not  """  
      self.firstRun:bool = obj["firstRun"]
      """  Indicates if this is the first run. Will be false if the first run returned messages that required user input and the user chose to continue  """  
      pass

class SetShippedFromPackout_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      self.opReleaseMessage:str = obj["parameters"]
      self.opCompleteMessage:str = obj["parameters"]
      self.opShippingMessage:str = obj["parameters"]
      self.opInventoryMessage:str = obj["parameters"]
      self.opLockQtyMessage:str = obj["parameters"]
      self.opAllocationMessage:str = obj["parameters"]
      self.shipCreditMsg:str = obj["parameters"]
      self.cError:bool = obj["cError"]
      self.msg:str = obj["parameters"]
      self.opPostUpdMessage:str = obj["parameters"]
      self.updateComplete:bool = obj["updateComplete"]
      self.checkComplianceError:bool = obj["checkComplianceError"]
      pass

      """  output parameters  """  

class SetUPSQVEnable_input:
   """ Required : 
   ipQVEnable
   ds
   """  
   def __init__(self, obj):
      self.ipQVEnable:bool = obj["ipQVEnable"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class SetUPSQVEnable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetUPSQVShipStatus_input:
   """ Required : 
   ipShipStatus
   ds
   """  
   def __init__(self, obj):
      self.ipShipStatus:str = obj["ipShipStatus"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class SetUPSQVShipStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class StageWarning_input:
   """ Required : 
   iPackNum
   ipShipmentType
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      self.ipShipmentType:str = obj["ipShipmentType"]
      pass

class StageWarning_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.iWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class UndoShipAll_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class UndoShipAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCustShipTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCustShipTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateManifestChargeAmts_input:
   """ Required : 
   ipAmountType
   ipAction
   ds
   """  
   def __init__(self, obj):
      self.ipAmountType:str = obj["ipAmountType"]
      self.ipAction:bool = obj["ipAction"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class UpdateManifestChargeAmts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateMaster_input:
   """ Required : 
   ds
   doValidateCreditHold
   doCheckShipDtl
   doLotValidation
   doCheckOrderComplete
   doPostUpdate
   doCheckCompliance
   ipShippedFlagChanged
   ipPackNum
   ipBTCustNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.doValidateCreditHold:bool = obj["doValidateCreditHold"]
      self.doCheckShipDtl:bool = obj["doCheckShipDtl"]
      self.doLotValidation:bool = obj["doLotValidation"]
      self.doCheckOrderComplete:bool = obj["doCheckOrderComplete"]
      self.doPostUpdate:bool = obj["doPostUpdate"]
      self.doCheckCompliance:bool = obj["doCheckCompliance"]
      self.ipShippedFlagChanged:bool = obj["ipShippedFlagChanged"]
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipBTCustNum:int = obj["ipBTCustNum"]
      pass

class UpdateMaster_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      self.opReleaseMessage:str = obj["parameters"]
      self.opCompleteMessage:str = obj["parameters"]
      self.opShippingMessage:str = obj["parameters"]
      self.opLotMessage:str = obj["parameters"]
      self.opInventoryMessage:str = obj["parameters"]
      self.opLockQtyMessage:str = obj["parameters"]
      self.opAllocationMessage:str = obj["parameters"]
      self.opPartListNeedsAttr:str = obj["parameters"]
      self.opLotListNeedsAttr:str = obj["parameters"]
      self.shipCreditMsg:str = obj["parameters"]
      self.cError:bool = obj["cError"]
      self.compError:bool = obj["compError"]
      self.msg:str = obj["parameters"]
      self.opPostUpdMessage:str = obj["parameters"]
      self.updateComplete:bool = obj["updateComplete"]
      self.checkComplianceError:bool = obj["checkComplianceError"]
      self.changeStatusError:bool = obj["changeStatusError"]
      self.checkShipDtlAgain:bool = obj["checkShipDtlAgain"]
      pass

      """  output parameters  """  

class UpdateOrderRelOnKitChildren_input:
   """ Required : 
   ipPackNum
   ipPackLine
   ipOrderRelNum
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipPackLine:int = obj["ipPackLine"]
      self.ipOrderRelNum:int = obj["ipOrderRelNum"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class UpdateOrderRelOnKitChildren_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdatePackCODWithCarton_input:
   """ Required : 
   ipPackNum
   ipCaseNum
   ipOldCOD
   ipCOD
   ipFlag
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipCaseNum:int = obj["ipCaseNum"]
      self.ipOldCOD:int = obj["ipOldCOD"]
      self.ipCOD:int = obj["ipCOD"]
      self.ipFlag:bool = obj["ipFlag"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class UpdatePackCODWithCarton_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdatePackDeclaredWithCarton_input:
   """ Required : 
   ipPackNum
   ipCaseNum
   ipOldDeclared
   ipDeclared
   ipDeclaredFlag
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipCaseNum:int = obj["ipCaseNum"]
      self.ipOldDeclared:int = obj["ipOldDeclared"]
      self.ipDeclared:int = obj["ipDeclared"]
      self.ipDeclaredFlag:bool = obj["ipDeclaredFlag"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class UpdatePackDeclaredWithCarton_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdatePackWeightWithCarton_input:
   """ Required : 
   ipPackNum
   ipOldWeight
   ipWeight
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipOldWeight:int = obj["ipOldWeight"]
      self.ipWeight:int = obj["ipWeight"]
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class UpdatePackWeightWithCarton_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateBinCode_input:
   """ Required : 
   ipWhse
   ipBinNum
   """  
   def __init__(self, obj):
      self.ipWhse:str = obj["ipWhse"]
      self.ipBinNum:str = obj["ipBinNum"]
      pass

class ValidateBinCode_output:
   def __init__(self, obj):
      pass

class ValidateCreditHoldPO_input:
   """ Required : 
   ipOrderNum
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipOrderNum:int = obj["ipOrderNum"]
      self.ipPackNum:int = obj["ipPackNum"]
      pass

class ValidateCreditHoldPO_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCreditMessage:str = obj["parameters"]
      self.opAgingMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateCreditHoldSSC_input:
   """ Required : 
   ipPackNum
   ipShipmentType
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipShipmentType:str = obj["ipShipmentType"]
      pass

class ValidateCreditHoldSSC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCreditMessage:str = obj["parameters"]
      self.opcError:bool = obj["opcError"]
      pass

      """  output parameters  """  

class ValidateCreditHold_input:
   """ Required : 
   ipValPackNum
   ipValBTCustNum
   """  
   def __init__(self, obj):
      self.ipValPackNum:int = obj["ipValPackNum"]
      self.ipValBTCustNum:int = obj["ipValBTCustNum"]
      pass

class ValidateCreditHold_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCreditMessage:str = obj["parameters"]
      self.opcError:bool = obj["opcError"]
      pass

      """  output parameters  """  

class ValidateKitPart_input:
   """ Required : 
   packLine
   ds
   """  
   def __init__(self, obj):
      self.packLine:int = obj["packLine"]
      """  Detail Line Number to update  """  
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

class ValidateKitPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateLocationIDNumbers_input:
   """ Required : 
   IDNumList
   ipPartNum
   ipIDNumProposed
   ipPackNum
   ipPackLine
   """  
   def __init__(self, obj):
      self.IDNumList:str = obj["IDNumList"]
      self.ipPartNum:str = obj["ipPartNum"]
      self.ipIDNumProposed:str = obj["ipIDNumProposed"]
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipPackLine:int = obj["ipPackLine"]
      pass

class ValidateLocationIDNumbers_output:
   def __init__(self, obj):
      pass

class ValidatePackNum_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      pass

class ValidatePackNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self._success:bool = obj["_success"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   ipSerialNum
   ipPartNum
   ipAttributeSetID
   ipJobNum
   ipOurJobshipQty
   ipOurInvShipQty
   ipOrderNum
   ipOrderLine
   ipOrderRelNum
   ipShipFromWIP
   ipWarehouseCode
   ipBinNum
   """  
   def __init__(self, obj):
      self.ipSerialNum:str = obj["ipSerialNum"]
      self.ipPartNum:str = obj["ipPartNum"]
      self.ipAttributeSetID:int = obj["ipAttributeSetID"]
      self.ipJobNum:str = obj["ipJobNum"]
      self.ipOurJobshipQty:int = obj["ipOurJobshipQty"]
      self.ipOurInvShipQty:int = obj["ipOurInvShipQty"]
      self.ipOrderNum:int = obj["ipOrderNum"]
      self.ipOrderLine:int = obj["ipOrderLine"]
      self.ipOrderRelNum:int = obj["ipOrderRelNum"]
      self.ipShipFromWIP:bool = obj["ipShipFromWIP"]
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      self.ipBinNum:str = obj["ipBinNum"]
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isVoided:bool = obj["isVoided"]
      pass

      """  output parameters  """  

class VoidLegalNumber_input:
   """ Required : 
   ipPackNum
   ipVoidedReason
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Packing Slip number  """  
      self.ipVoidedReason:str = obj["ipVoidedReason"]
      """  Reason for the void  """  
      pass

class VoidLegalNumber_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustShipTableset] = obj["returnObj"]
      pass

class VoidPackSlip_input:
   """ Required : 
   packNum
   ds
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      self.ds:list[Erp_Tablesets_PackageControlPackVoidTableset] = obj["ds"]
      pass

class VoidPackSlip_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackageControlPackVoidTableset] = obj["ds"]
      pass

      """  output parameters  """  

