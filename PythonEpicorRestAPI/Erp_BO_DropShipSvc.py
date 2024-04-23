import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DropShipSvc
# Description: Business Object for Drop Shipment
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DropShips(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DropShips items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DropShips
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips",headers=creds) as resp:
           return await resp.json()

async def post_DropShips(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DropShips
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DropShipHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DropShipHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DropShips_Company_VendorNum_PurPoint_PackSlip(Company, VendorNum, PurPoint, PackSlip, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DropShip item
   Description: Calls GetByID to retrieve the DropShip item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DropShip
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DropShipHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DropShips_Company_VendorNum_PurPoint_PackSlip(Company, VendorNum, PurPoint, PackSlip, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DropShip for the service
   Description: Calls UpdateExt to update DropShip. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DropShip
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DropShipHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DropShips_Company_VendorNum_PurPoint_PackSlip(Company, VendorNum, PurPoint, PackSlip, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DropShip item
   Description: Call UpdateExt to delete DropShip item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DropShip
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")",headers=creds) as resp:
           return await resp.json()

async def get_DropShips_Company_VendorNum_PurPoint_PackSlip_DropShipDtls(Company, VendorNum, PurPoint, PackSlip, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DropShipDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DropShipDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/DropShipDtls",headers=creds) as resp:
           return await resp.json()

async def get_DropShips_Company_VendorNum_PurPoint_PackSlip_DropShipDtls_Company_VendorNum_PurPoint_PackSlip_PackLine(Company, VendorNum, PurPoint, PackSlip, PackLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DropShipDtl item
   Description: Calls GetByID to retrieve the DropShipDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DropShipDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DropShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/DropShipDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_DropShips_Company_VendorNum_PurPoint_PackSlip_DropShipHeadTrailers(Company, VendorNum, PurPoint, PackSlip, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DropShipHeadTrailers items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DropShipHeadTrailers1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipHeadTrailerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/DropShipHeadTrailers",headers=creds) as resp:
           return await resp.json()

async def get_DropShips_Company_VendorNum_PurPoint_PackSlip_DropShipHeadTrailers_Company_VendorNum_PurPoint_PackSlip_LicensePlate(Company, VendorNum, PurPoint, PackSlip, LicensePlate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DropShipHeadTrailer item
   Description: Calls GetByID to retrieve the DropShipHeadTrailer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DropShipHeadTrailer1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param LicensePlate: Desc: LicensePlate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DropShipHeadTrailerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/DropShipHeadTrailers(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + LicensePlate + ")",headers=creds) as resp:
           return await resp.json()

async def get_DropShips_Company_VendorNum_PurPoint_PackSlip_MXDropShipHeadInsurances(Company, VendorNum, PurPoint, PackSlip, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MXDropShipHeadInsurances items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MXDropShipHeadInsurances1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXDropShipHeadInsuranceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/MXDropShipHeadInsurances",headers=creds) as resp:
           return await resp.json()

async def get_DropShips_Company_VendorNum_PurPoint_PackSlip_MXDropShipHeadInsurances_Company_VendorNum_PurPoint_PackSlip_InsuranceSeq(Company, VendorNum, PurPoint, PackSlip, InsuranceSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MXDropShipHeadInsurance item
   Description: Calls GetByID to retrieve the MXDropShipHeadInsurance item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXDropShipHeadInsurance1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param InsuranceSeq: Desc: InsuranceSeq   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MXDropShipHeadInsuranceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/MXDropShipHeadInsurances(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + InsuranceSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DropShips_Company_VendorNum_PurPoint_PackSlip_DropShipHeadAttches(Company, VendorNum, PurPoint, PackSlip, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DropShipHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DropShipHeadAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/DropShipHeadAttches",headers=creds) as resp:
           return await resp.json()

async def get_DropShips_Company_VendorNum_PurPoint_PackSlip_DropShipHeadAttches_Company_VendorNum_PurPoint_PackSlip_DrawingSeq(Company, VendorNum, PurPoint, PackSlip, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DropShipHeadAttch item
   Description: Calls GetByID to retrieve the DropShipHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DropShipHeadAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DropShipHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/DropShipHeadAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DropShipDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DropShipDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DropShipDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipDtls",headers=creds) as resp:
           return await resp.json()

async def post_DropShipDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DropShipDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DropShipDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DropShipDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DropShipDtls_Company_VendorNum_PurPoint_PackSlip_PackLine(Company, VendorNum, PurPoint, PackSlip, PackLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DropShipDtl item
   Description: Calls GetByID to retrieve the DropShipDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DropShipDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DropShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DropShipDtls_Company_VendorNum_PurPoint_PackSlip_PackLine(Company, VendorNum, PurPoint, PackSlip, PackLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DropShipDtl for the service
   Description: Calls UpdateExt to update DropShipDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DropShipDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DropShipDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DropShipDtls_Company_VendorNum_PurPoint_PackSlip_PackLine(Company, VendorNum, PurPoint, PackSlip, PackLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DropShipDtl item
   Description: Call UpdateExt to delete DropShipDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DropShipDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_DropShipHeadTrailers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DropShipHeadTrailers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DropShipHeadTrailers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipHeadTrailerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadTrailers",headers=creds) as resp:
           return await resp.json()

async def post_DropShipHeadTrailers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DropShipHeadTrailers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DropShipHeadTrailerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DropShipHeadTrailerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadTrailers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DropShipHeadTrailers_Company_VendorNum_PurPoint_PackSlip_LicensePlate(Company, VendorNum, PurPoint, PackSlip, LicensePlate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DropShipHeadTrailer item
   Description: Calls GetByID to retrieve the DropShipHeadTrailer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DropShipHeadTrailer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param LicensePlate: Desc: LicensePlate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DropShipHeadTrailerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadTrailers(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + LicensePlate + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DropShipHeadTrailers_Company_VendorNum_PurPoint_PackSlip_LicensePlate(Company, VendorNum, PurPoint, PackSlip, LicensePlate, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DropShipHeadTrailer for the service
   Description: Calls UpdateExt to update DropShipHeadTrailer. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DropShipHeadTrailer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param LicensePlate: Desc: LicensePlate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DropShipHeadTrailerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadTrailers(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + LicensePlate + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DropShipHeadTrailers_Company_VendorNum_PurPoint_PackSlip_LicensePlate(Company, VendorNum, PurPoint, PackSlip, LicensePlate, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DropShipHeadTrailer item
   Description: Call UpdateExt to delete DropShipHeadTrailer item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DropShipHeadTrailer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadTrailers(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + LicensePlate + ")",headers=creds) as resp:
           return await resp.json()

async def get_MXDropShipHeadInsurances(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MXDropShipHeadInsurances items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MXDropShipHeadInsurances
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXDropShipHeadInsuranceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/MXDropShipHeadInsurances",headers=creds) as resp:
           return await resp.json()

async def post_MXDropShipHeadInsurances(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MXDropShipHeadInsurances
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MXDropShipHeadInsuranceRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MXDropShipHeadInsuranceRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/MXDropShipHeadInsurances", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MXDropShipHeadInsurances_Company_VendorNum_PurPoint_PackSlip_InsuranceSeq(Company, VendorNum, PurPoint, PackSlip, InsuranceSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MXDropShipHeadInsurance item
   Description: Calls GetByID to retrieve the MXDropShipHeadInsurance item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXDropShipHeadInsurance
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param InsuranceSeq: Desc: InsuranceSeq   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MXDropShipHeadInsuranceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/MXDropShipHeadInsurances(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + InsuranceSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MXDropShipHeadInsurances_Company_VendorNum_PurPoint_PackSlip_InsuranceSeq(Company, VendorNum, PurPoint, PackSlip, InsuranceSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MXDropShipHeadInsurance for the service
   Description: Calls UpdateExt to update MXDropShipHeadInsurance. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MXDropShipHeadInsurance
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param InsuranceSeq: Desc: InsuranceSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MXDropShipHeadInsuranceRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/MXDropShipHeadInsurances(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + InsuranceSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MXDropShipHeadInsurances_Company_VendorNum_PurPoint_PackSlip_InsuranceSeq(Company, VendorNum, PurPoint, PackSlip, InsuranceSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MXDropShipHeadInsurance item
   Description: Call UpdateExt to delete MXDropShipHeadInsurance item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MXDropShipHeadInsurance
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/MXDropShipHeadInsurances(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + InsuranceSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DropShipHeadAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DropShipHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DropShipHeadAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadAttches",headers=creds) as resp:
           return await resp.json()

async def post_DropShipHeadAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DropShipHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DropShipHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DropShipHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DropShipHeadAttches_Company_VendorNum_PurPoint_PackSlip_DrawingSeq(Company, VendorNum, PurPoint, PackSlip, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DropShipHeadAttch item
   Description: Calls GetByID to retrieve the DropShipHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DropShipHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DropShipHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DropShipHeadAttches_Company_VendorNum_PurPoint_PackSlip_DrawingSeq(Company, VendorNum, PurPoint, PackSlip, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DropShipHeadAttch for the service
   Description: Calls UpdateExt to update DropShipHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DropShipHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DropShipHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DropShipHeadAttches_Company_VendorNum_PurPoint_PackSlip_DrawingSeq(Company, VendorNum, PurPoint, PackSlip, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DropShipHeadAttch item
   Description: Call UpdateExt to delete DropShipHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DropShipHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + DrawingSeq + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/LegalNumGenOpts",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PendingDropShipDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PendingDropShipDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PendingDropShipDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PendingDropShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/PendingDropShipDtls",headers=creds) as resp:
           return await resp.json()

async def post_PendingDropShipDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PendingDropShipDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PendingDropShipDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PendingDropShipDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/PendingDropShipDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PendingDropShipDtls_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PendingDropShipDtl item
   Description: Calls GetByID to retrieve the PendingDropShipDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PendingDropShipDtl
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PendingDropShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/PendingDropShipDtls(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PendingDropShipDtls_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PendingDropShipDtl for the service
   Description: Calls UpdateExt to update PendingDropShipDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PendingDropShipDtl
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PendingDropShipDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/PendingDropShipDtls(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PendingDropShipDtls_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PendingDropShipDtl item
   Description: Call UpdateExt to delete PendingDropShipDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PendingDropShipDtl
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/PendingDropShipDtls(" + SysRowID + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SelectedSerialNumbers",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SelectedSerialNumbers", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SNFormats",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SNFormats", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDropShipHead, whereClauseDropShipHeadAttch, whereClauseDropShipDtl, whereClauseDropShipHeadTrailer, whereClauseMXDropShipHeadInsurance, whereClauseLegalNumGenOpts, whereClausePendingDropShipDtl, whereClauseSelectedSerialNumbers, whereClauseSNFormat, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseDropShipHead=" + whereClauseDropShipHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDropShipHeadAttch=" + whereClauseDropShipHeadAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDropShipDtl=" + whereClauseDropShipDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDropShipHeadTrailer=" + whereClauseDropShipHeadTrailer
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMXDropShipHeadInsurance=" + whereClauseMXDropShipHeadInsurance
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
   params += "whereClausePendingDropShipDtl=" + whereClausePendingDropShipDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(vendorNum, purPoint, packSlip, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "vendorNum=" + vendorNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "purPoint=" + purPoint
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "packSlip=" + packSlip

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_BuildCustomersToList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildCustomersToList
   Description: If the Order has releases to multiple Customer, this will return the list of available
Customers
   OperationID: BuildCustomersToList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildCustomersToList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildCustomersToList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildShipToCustList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildShipToCustList
   Description: Return a list of Ship To Customers.
Customers
   OperationID: BuildShipToCustList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildShipToCustList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildShipToCustList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDropShipDtlComplete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDropShipDtlComplete
   Description: Updates the Complete of DropShipDtl.
   OperationID: ChangeDropShipDtlComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDropShipDtlComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipDtlComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDropShipDtlIUM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDropShipDtlIUM
   Description: Updates the IUM of DropShipDtl.
   OperationID: ChangeDropShipDtlIUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDropShipDtlIUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipDtlIUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDropShipDtlLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDropShipDtlLotNum
   Description: Updates the LotNum of DropShipDtl.
   OperationID: ChangeDropShipDtlLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDropShipDtlLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipDtlLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDropShipDtlOurQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDropShipDtlOurQty
   Description: Updates the OurQty of DropShipDtl.
   OperationID: ChangeDropShipDtlOurQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDropShipDtlOurQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipDtlOurQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDropShipDtlPOLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDropShipDtlPOLine
   Description: Updates the POLine of DropShipDtl.
   OperationID: ChangeDropShipDtlPOLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDropShipDtlPOLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipDtlPOLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDropShipDtlPONum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDropShipDtlPONum
   Description: Updates the PONum of DropShipDtl.
   OperationID: ChangeDropShipDtlPONum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDropShipDtlPONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipDtlPONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDropShipDtlPORelNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDropShipDtlPORelNum
   Description: Updates the PORelNum of DropShipDtl.
   OperationID: ChangeDropShipDtlPORelNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDropShipDtlPORelNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipDtlPORelNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDropShipDtlVendorQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDropShipDtlVendorQty
   Description: Updates the VendorQty of DropShipDtl.
   OperationID: ChangeDropShipDtlVendorQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDropShipDtlVendorQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipDtlVendorQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDropShipHeadPONum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDropShipHeadPONum
   Description: Call this method when the PONum changes on the DropShipHead.
   OperationID: ChangeDropShipHeadPONum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDropShipHeadPONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipHeadPONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDropShipHeadShipToCustNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDropShipHeadShipToCustNum
   Description: Call this method when the ShipToCustNum changes on the DropShipHead.
   OperationID: ChangeDropShipHeadShipToCustNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDropShipHeadShipToCustNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipHeadShipToCustNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDropShipHeadShipToNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDropShipHeadShipToNum
   Description: Call this method when the ShipToCustNum changes on the DropShipHead.
   OperationID: ChangeDropShipHeadShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDropShipHeadShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipHeadShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingNumberOfPieces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new our qty
   OperationID: OnChangingNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateMassDropShipDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateMassDropShipDtl
   Description: The Create Mass Drop Ship method.
   OperationID: CreateMassDropShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateMassDropShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMassDropShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOrderShipments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOrderShipments
   Description: This method creates the data for the tables ShipDtl and DropShipDtl
   OperationID: GetOrderShipments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOrderShipments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderShipments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPendingDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPendingDtl
   Description: Updates PendingDropShipDtl.
   OperationID: GetPendingDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPendingDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPendingDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPOInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPOInfo
   Description: This method returns default information for the PO Number and the new Vendor ID
information.
   OperationID: GetPOInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPOInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMXCartaPortePOInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMXCartaPortePOInfo
   Description: Function to set Mexico Carta Porte fields default values
   OperationID: GetMXCartaPortePOInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMXCartaPortePOInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMXCartaPortePOInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPurPointInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPurPointInfo
   Description: This method returns default information for the Vendor Purchase Point.
   OperationID: GetPurPointInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPurPointInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPurPointInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipPartNum">ipPartNum</param><param name="ipAttributeSetID"></param><param name="ipQuantity">ipQuantity</param><param name="ipUOM">ipUOM</param><param name="ipVendNum">ipVendNum</param><param name="ipVendPP">ipVendPP</param><param name="ipPackSlip">ipPackSlip</param><param name="ipPackSlipLine">ipPackSlipLine</param><param name="ipPONum">PO Number</param><param name="ipPOLine">PO Line Number</param><param name="ipPORelNum">PO Release Number</param><returns></returns>
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetShipToAddressMultiKey(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetShipToAddressMultiKey
   Description: This method builds the ShipTo Address
   OperationID: GetShipToAddressMultiKey
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipToAddressMultiKey_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipToAddressMultiKey_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVendorInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendorInfo
   Description: This method returns default information for the Vendor.
   OperationID: GetVendorInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendorInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MarkShipmentLines(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MarkShipmentLines
   Description: This method sets all the temp-table records to be drop shipped (Ship all button selected)
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PostUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PostUpdate
   Description: This method will return a message if a credit card drop shipment was processed
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_processExtraCreditCharge(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method processExtraCreditCharge
   OperationID: processExtraCreditCharge
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/processExtraCreditCharge_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/processExtraCreditCharge_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreChangeDropShipDtlLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreChangeDropShipDtlLotNum
   Description: This method returns an error or question if the LotNum field does not exist
depending upon the security of the user
   OperationID: PreChangeDropShipDtlLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreChangeDropShipDtlLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreChangeDropShipDtlLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreCreateMassReceipt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreCreateMassReceipt
   Description: The Pre Create Mass Drop Ship method.
   OperationID: PreCreateMassReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreCreateMassReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreCreateMassReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdateDropShipDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdateDropShipDtl
   Description: This method is to be called right before the update method is called.
   OperationID: PreUpdateDropShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdateDropShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdateDropShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UndoShipAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UndoShipAll
   Description: This method re-sets all the temp-table records drop shipped (Undo Ship all button selected)
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSN
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipPartNum">Part Number</param><param name="ipAttributeSetID"></param><param name="ipSerialNo">Serial Number</param><param name="ipVendNum">Vendor Number</param><param name="ipPurPoint">Pur Point</param><param name="ipPackNum">Pack Number</param><param name="ipPONum">PO Number</param><param name="ipPOLine">PO Line Number</param><param name="ipPORelNum">PO Release Number</param>
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the drop shipment.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTranDocTypeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTranDocTypeID
   Description: Sets default values when the TranDocTypeID changes.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMultiKeySearchPONum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMultiKeySearchPONum
   Description: On Column Change MultiKeySearch PONum.
   OperationID: OnChangeMultiKeySearchPONum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMultiKeySearchPONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMultiKeySearchPONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildAddressField(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildAddressField
   Description: Build Address Field.
   OperationID: BuildAddressField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildAddressField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildAddressField_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InitializeMultiKeySearchData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InitializeMultiKeySearchData
   Description: Initialize MultiKeySearch Data.
   OperationID: InitializeMultiKeySearchData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InitializeMultiKeySearchData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitializeMultiKeySearchData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildShipToCustListWithOutputParameters(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildShipToCustListWithOutputParameters
   Description: Build ShipTo Customer List, with output parameters.
   OperationID: BuildShipToCustListWithOutputParameters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildShipToCustListWithOutputParameters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildShipToCustListWithOutputParameters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildShipToListWithParameters(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildShipToListWithParameters
   Description: Build ShipTo List, with out parameters.
   OperationID: BuildShipToListWithParameters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildShipToListWithParameters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildShipToListWithParameters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_buildShipToAddressFieldMultiKey(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method buildShipToAddressFieldMultiKey
   Description: build ShipTo Address.
   OperationID: buildShipToAddressFieldMultiKey
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/buildShipToAddressFieldMultiKey_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/buildShipToAddressFieldMultiKey_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteDropShipDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteDropShipDtl
   Description: Delete DropShipDtl method when dataset has several DropShipDtl records in state 'Added'.
   OperationID: DeleteDropShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteDropShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteDropShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateMassDropShipDtlWithoutComplete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateMassDropShipDtlWithoutComplete
   Description: Mass Drop Shipment functionality. Generates list without duplicated lines.
   OperationID: CreateMassDropShipDtlWithoutComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateMassDropShipDtlWithoutComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMassDropShipDtlWithoutComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDropShipHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDropShipHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDropShipHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDropShipHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDropShipHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDropShipHeadAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDropShipHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDropShipHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDropShipHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDropShipHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDropShipDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDropShipDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDropShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDropShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDropShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDropShipHeadTrailer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDropShipHeadTrailer
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDropShipHeadTrailer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDropShipHeadTrailer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDropShipHeadTrailer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMXDropShipHeadInsurance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMXDropShipHeadInsurance
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMXDropShipHeadInsurance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMXDropShipHeadInsurance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMXDropShipHeadInsurance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DropShipDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DropShipHeadAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DropShipHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DropShipHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadTrailerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DropShipHeadTrailerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXDropShipHeadInsuranceRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MXDropShipHeadInsuranceRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PendingDropShipDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PendingDropShipDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SNFormatRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["value"]
      pass

class Erp_Tablesets_DropShipDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  The unique identifier for the drop shipment.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order being drop shipped.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the purchase order being drop shipped.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  The release number of the purchase order being drop shipped.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Num defaulted from the PO release.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Supplier's part num. Defaulted from the PO release.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Defaulted from the PO release.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Defaulted from the PO release.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Defaulted from the PO release.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different Part number than the users internal part number. Defaulted from the SO release.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Field that contains the customer's revision.  """  
      self.OurQty:int = obj["OurQty"]
      """  This field will be automatically defaulted to the remaining quantity to be drop shipped. Receipt quantity in our unit of measure.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Holds any comments about the order line being shipped. This gets duplicated from the OrderDtl.ShipComment.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  These comments will be copied into the Invoice detail.  """  
      self.HeaderShipComment:str = obj["HeaderShipComment"]
      """  Packing slip comments.  These are comments off of the invoice header.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Complete:bool = obj["Complete"]
      """  This flag will be automatically set if the remaining quantity to be drop shipped equals to zero and will be automatically turned off if the remaining quantity is greater than zero.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier that drops shipped the good from their inventory to our customer.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point ID.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from PODetail LineDesc.  """  
      self.OurUnitCost:int = obj["OurUnitCost"]
      """  Unit cost base on our unit of measure. Default can be obtained from PODetail.UnitCost.  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  Item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.PUM:str = obj["PUM"]
      """  Vendor's selling Unit of Measure.  """  
      self.VendorUnitCost:int = obj["VendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the POdetail record.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt date. Mirror image of related DropShipHead.ReceiptDate.  """  
      self.APInvoiced:bool = obj["APInvoiced"]
      """  A\P invoice entry sets this to "Yes" when the drop ship detail line is invoiced.  """  
      self.ARInvoiced:bool = obj["ARInvoiced"]
      """  A\R invoice entry sets this to "Yes" when the receipt detail line is invoiced.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Invoice Number from corresponding APInvHed record.  """  
      self.APInvoiceLine:int = obj["APInvoiceLine"]
      """  Invoice Number Line from corresponding APInvDtl record.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  Invoice Number from corresponding InvcHead record.  """  
      self.ARInvoiceLine:int = obj["ARInvoiceLine"]
      """  Invoice Number Line from corresponding InvcDtl record.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  """  
      self.TranReference:str = obj["TranReference"]
      """  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.ReceivedShipped:bool = obj["ReceivedShipped"]
      """  Identifies a drop shipment line that is complete and ready to be invoiced.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  For Warranty drop shipments.  Defaults as DropShipHead.ReceiptDate. But can be maintained from the Service Call center.  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The # of days, months, years the Labor is covered by warranty  """  
      self.LaborExpiration:str = obj["LaborExpiration"]
      """  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Whether the duration of warranty  is "Days"," Months"," years".  """  
      self.LastExpiration:str = obj["LastExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The # of days, months, years the material is covered by warranty  """  
      self.MaterialExpiration:str = obj["MaterialExpiration"]
      """  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Whether the duration of warranty  is for "Days", " Months", "years".  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The # of days, months, years the Misc. Charges are covered by warranty  """  
      self.MiscExpiration:str = obj["MiscExpiration"]
      """  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.MiscMod:str = obj["MiscMod"]
      """  Whether the duration of warranty  is for "Days"," Months"," years".  """  
      self.Onsite:bool = obj["Onsite"]
      """  This warranty covers On site visits  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Warranty comments.  """  
      self.CustNum:int = obj["CustNum"]
      """  Duplicated from DropShipHead.CustNum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Duplicated from DropShipHead.ShipTotNum.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Duplicated from DropShipHead.ShipToCustNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  ProjProcessed  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.MXEstValue:int = obj["MXEstValue"]
      """  Estimated Value  """  
      self.MXEstValueCurrencyCode:str = obj["MXEstValueCurrencyCode"]
      """  Estimated Value Currency  """  
      self.MXTotalNetWeightKGM:int = obj["MXTotalNetWeightKGM"]
      """  Total Net Weight in kilograms  """  
      self.MXHazardousShipment:bool = obj["MXHazardousShipment"]
      """  Hazardous Shipment  """  
      self.MXHazardousType:str = obj["MXHazardousType"]
      """  Hazardous Type  """  
      self.MXPackageType:str = obj["MXPackageType"]
      """  Package Type  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.POComment:str = obj["POComment"]
      self.RemainingQty:int = obj["RemainingQty"]
      self.RemainingQtyUOM:str = obj["RemainingQtyUOM"]
      self.RequestedQty:int = obj["RequestedQty"]
      self.RequestedQtyUOM:str = obj["RequestedQtyUOM"]
      self.ShippedToDateQty:int = obj["ShippedToDateQty"]
      self.ShippedToDateQtyUOM:str = obj["ShippedToDateQtyUOM"]
      self.ThisShipmentQty:int = obj["ThisShipmentQty"]
      self.ThisShipmentQtyUOM:str = obj["ThisShipmentQtyUOM"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.CostPerFactor:int = obj["CostPerFactor"]
      """  Interger value of CostPerCode  """  
      self.BillToAddrFormatted:str = obj["BillToAddrFormatted"]
      """  The formatted bill to address  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AttributeSetIDDescription:str = obj["AttributeSetIDDescription"]
      self.AttributeSetIDShortDescription:str = obj["AttributeSetIDShortDescription"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DropShipHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PackSlip:str = obj["PackSlip"]
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

class Erp_Tablesets_DropShipHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  The unique identifier for the drop shipment.  """  
      self.PONum:int = obj["PONum"]
      """  The number of the purchase order that corresponds with the drop shipped goods.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier that drops shipped the good from their inventory to our customer.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point ID.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ship to num related to this drop shipment.  """  
      self.ReceivedShipped:bool = obj["ReceivedShipped"]
      """  Identifies a drop shipment that is complete and ready to be invoiced.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  The user who created the drop shipment. This field will be auto populated when a user saves a new drop shipment.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  The date when the drop shipment was created. This field will be auto populated when a user saves a new drop shipment.  """  
      self.ReceivePerson:str = obj["ReceivePerson"]
      """  The user who marked the drop shipment as Received/Shipped. This field will be auto populated when a user turns on the received/shipped flag.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Date when the drop shipment was marked as Received/Shipped. This field will be auto populated. This field will be auto populated when a user turns on the received/shipped flag.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The ship via used to ship the goods from our supplier to our customer. This field will be defaulted from the PO selected in the above.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  The tracking number used to track the shipment from our supplier to our customer.  """  
      self.APInvoiced:bool = obj["APInvoiced"]
      """  This flag will be set once the packing slip has been invoiced in AP Invoice.  """  
      self.ARInvoiced:bool = obj["ARInvoiced"]
      """  This flag will be set on once the packing slip has been invoiced in AR Invoice.  """  
      self.ShipmentPackNum:int = obj["ShipmentPackNum"]
      """  Pack Num of the regular shipment created when flag ReceivedShipped is set.  """  
      self.ReceiptPackSlip:str = obj["ReceiptPackSlip"]
      """  Packing Slip of the regular receipt created when flag ReceivedShipped is set.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Pack comments.  """  
      self.ReceiptComment:str = obj["ReceiptComment"]
      """  Contains comments about the overall Receipt.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer associated to the Drop Shioment.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer primary billing contact.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that drop shipment was made from/to  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.AddrList:str = obj["AddrList"]
      """  Address Information from Vendor or VendorPP  """  
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      """  Address Information from ShipToNum  """  
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.BillAddr:str = obj["BillAddr"]
      """  Address information for DropShipHead.CustNum  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.PurPointCity:str = obj["PurPointCity"]
      """  City portion of the address  """  
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      """  First address line  """  
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      """  Second address line  """  
      self.PurPointCountry:str = obj["PurPointCountry"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.PurPointState:str = obj["PurPointState"]
      """  State portion of the address  """  
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      """  Third address line  """  
      self.PurPointName:str = obj["PurPointName"]
      """  Purchase Point Name...can't be blank.  """  
      self.PurPointZip:str = obj["PurPointZip"]
      """  Postal Code or Zip code portion of the address  """  
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      """  The full name of the customer.  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
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
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DropShipHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  The unique identifier for the drop shipment.  """  
      self.PONum:int = obj["PONum"]
      """  The number of the purchase order that corresponds with the drop shipped goods.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier that drops shipped the good from their inventory to our customer.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point ID.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ship to num related to this drop shipment.  """  
      self.ReceivedShipped:bool = obj["ReceivedShipped"]
      """  Identifies a drop shipment that is complete and ready to be invoiced.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  The user who created the drop shipment. This field will be auto populated when a user saves a new drop shipment.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  The date when the drop shipment was created. This field will be auto populated when a user saves a new drop shipment.  """  
      self.ReceivePerson:str = obj["ReceivePerson"]
      """  The user who marked the drop shipment as Received/Shipped. This field will be auto populated when a user turns on the received/shipped flag.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Date when the drop shipment was marked as Received/Shipped. This field will be auto populated. This field will be auto populated when a user turns on the received/shipped flag.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The ship via used to ship the goods from our supplier to our customer. This field will be defaulted from the PO selected in the above.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  The tracking number used to track the shipment from our supplier to our customer.  """  
      self.APInvoiced:bool = obj["APInvoiced"]
      """  This flag will be set once the packing slip has been invoiced in AP Invoice.  """  
      self.ARInvoiced:bool = obj["ARInvoiced"]
      """  This flag will be set on once the packing slip has been invoiced in AR Invoice.  """  
      self.ShipmentPackNum:int = obj["ShipmentPackNum"]
      """  Pack Num of the regular shipment created when flag ReceivedShipped is set.  """  
      self.ReceiptPackSlip:str = obj["ReceiptPackSlip"]
      """  Packing Slip of the regular receipt created when flag ReceivedShipped is set.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Pack comments.  """  
      self.ReceiptComment:str = obj["ReceiptComment"]
      """  Contains comments about the overall Receipt.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer associated to the Drop Shioment.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer primary billing contact.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that drop shipment was made from/to  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
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
      """  Folio  """  
      self.MXFolio:str = obj["MXFolio"]
      """  Folio  """  
      self.MXETD:str = obj["MXETD"]
      """  Estimated Date and Time of Departure  """  
      self.MXETA:str = obj["MXETA"]
      """  Estimated Date and Time of Departure  """  
      self.MXDistance:int = obj["MXDistance"]
      """  Distance in Km  """  
      self.MXPermitType:str = obj["MXPermitType"]
      """  Permit Type  """  
      self.MXPermitNum:str = obj["MXPermitNum"]
      """  Permit Number  """  
      self.MXCartaPorteStatus:str = obj["MXCartaPorteStatus"]
      """  Carta Porte Status  """  
      self.MXVehicleLicensePlate:str = obj["MXVehicleLicensePlate"]
      """  Vehicle License Plate  """  
      self.MXVehicleType:str = obj["MXVehicleType"]
      """  Vehicle Type  """  
      self.MXVehicleYear:int = obj["MXVehicleYear"]
      """  Vehicle Year  """  
      self.MXDriverID:str = obj["MXDriverID"]
      """  Driver  """  
      self.MXCancelFiscalFolio:str = obj["MXCancelFiscalFolio"]
      """  MXCancelFiscalFolio  """  
      self.EDIShipReferenceType:str = obj["EDIShipReferenceType"]
      """  Name of the ship reference that is going to be stored.  """  
      self.EDIShipReferenceData:str = obj["EDIShipReferenceData"]
      """  Data this is going to be stored as ship reference.  """  
      self.EDIEstimatedDockDate:str = obj["EDIEstimatedDockDate"]
      """  Estimated time when the shipment will arrive.  """  
      self.AddrList:str = obj["AddrList"]
      """  Address Information from Vendor or VendorPP  """  
      self.BillAddr:str = obj["BillAddr"]
      """  Address information for DropShipHead.CustNum  """  
      self.CreditCardMessage:str = obj["CreditCardMessage"]
      """  This field temporarily holds certain message(s) returned by credit card processing logic for internal processing.  """  
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      """  Address Information from ShipToNum  """  
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.SupplierNameAddrFormatted:str = obj["SupplierNameAddrFormatted"]
      """  The formatted supplier name and address from AddrList  """  
      self.ShipToAddrFormatted:str = obj["ShipToAddrFormatted"]
      self.BillToAddrFormatted:str = obj["BillToAddrFormatted"]
      """  The formatted bill to address  """  
      self.MXETADate:str = obj["MXETADate"]
      """  Estimated Date of Arrival  """  
      self.MXETATime:int = obj["MXETATime"]
      """  Estimated Time of Arrival  """  
      self.MXETDDate:str = obj["MXETDDate"]
      """  Estimated Date of Departure  """  
      self.MXETDTime:int = obj["MXETDTime"]
      """  Estimated Time of Departure  """  
      self.MXVehicleWeight:int = obj["MXVehicleWeight"]
      """  Vehicle Weight (in tons)  """  
      self.MXIdCCP:str = obj["MXIdCCP"]
      """  A unique Carta Porte identification number assigned by Epicor  """  
      self.MXCustomsRegime:str = obj["MXCustomsRegime"]
      """  Customs Regime for Export transaction.  """  
      self.MXReverseLogistics:bool = obj["MXReverseLogistics"]
      """  Check box to specify the use of reverse logistic, collection or devolution services when shipping goods.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BTCustNumInactive:bool = obj["BTCustNumInactive"]
      self.CustNumInactive:bool = obj["CustNumInactive"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointState:str = obj["PurPointState"]
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      self.ShipToCustNumInactive:bool = obj["ShipToCustNumInactive"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DropShipHeadTrailerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor Number  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Supplier Purchase Point  """  
      self.PackSlip:str = obj["PackSlip"]
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

class Erp_Tablesets_MXDropShipHeadInsuranceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.PurPoint:str = obj["PurPoint"]
      """  PurPoint  """  
      self.PackSlip:str = obj["PackSlip"]
      """  PackSlip  """  
      self.InsuranceSeq:int = obj["InsuranceSeq"]
      """  InsuranceSeq  """  
      self.Type:str = obj["Type"]
      """  Type  """  
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

class Erp_Tablesets_PendingDropShipDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LineDesc:str = obj["LineDesc"]
      self.OurQuantity:int = obj["OurQuantity"]
      self.PartNum:str = obj["PartNum"]
      self.POLine:int = obj["POLine"]
      self.PONum:int = obj["PONum"]
      self.PurPoint:str = obj["PurPoint"]
      self.UOM:str = obj["UOM"]
      self.VendorNum:int = obj["VendorNum"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.PORelNum:int = obj["PORelNum"]
      self.PackSlip:str = obj["PackSlip"]
      self.RemainingQty:int = obj["RemainingQty"]
      """  The Remaining Qty between Supplier Qty and Received Qty  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  The Attribute Class for the part.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.RevisionNum:str = obj["RevisionNum"]
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




#########################################################################
# Custom Schemas:
#########################################################################
class AssignLegalNumber_input:
   """ Required : 
   ipVendorNum
   ipPurPoint
   ipPackSlip
   ds
   """  
   def __init__(self, obj):
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  Vendor No  """  
      self.ipPurPoint:str = obj["ipPurPoint"]
      """  Purchase point  """  
      self.ipPackSlip:str = obj["ipPackSlip"]
      """  Packing slip  """  
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class AssignLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.opLegalNumMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class BuildAddressField_input:
   """ Required : 
   ipString
   """  
   def __init__(self, obj):
      self.ipString:str = obj["ipString"]
      pass

class BuildAddressField_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class BuildCustomersToList_input:
   """ Required : 
   poNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      """  PO Number  """  
      pass

class BuildCustomersToList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.customersToList:str = obj["parameters"]
      pass

      """  output parameters  """  

class BuildShipToCustListWithOutputParameters_input:
   """ Required : 
   poNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      pass

class BuildShipToCustListWithOutputParameters_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.shipToCustList:str = obj["parameters"]
      self.firstCustomerNum:int = obj["parameters"]
      self.firstCustomerID:str = obj["parameters"]
      pass

      """  output parameters  """  

class BuildShipToCustList_input:
   """ Required : 
   poNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      """  PO Number  """  
      pass

class BuildShipToCustList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.shipToCustList:str = obj["parameters"]
      pass

      """  output parameters  """  

class BuildShipToListWithParameters_input:
   """ Required : 
   poNum
   custNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      self.custNum:int = obj["custNum"]
      pass

class BuildShipToListWithParameters_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.shipToList:str = obj["parameters"]
      self.firstShipToNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class BuildShipToList_input:
   """ Required : 
   poNum
   custNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      """  PO Number  """  
      self.custNum:int = obj["custNum"]
      """  Customer Number  """  
      pass

class BuildShipToList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.shipToList:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeDropShipDtlComplete_input:
   """ Required : 
   ds
   ipComplete
   ipPackLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.ipComplete:bool = obj["ipComplete"]
      """  The Complete value  """  
      self.ipPackLine:int = obj["ipPackLine"]
      """  Selected pack line  """  
      pass

class ChangeDropShipDtlComplete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeDropShipDtlIUM_input:
   """ Required : 
   ds
   ipIUM
   ipPackLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.ipIUM:str = obj["ipIUM"]
      """  The IUM value  """  
      self.ipPackLine:int = obj["ipPackLine"]
      """  Selected pack line  """  
      pass

class ChangeDropShipDtlIUM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.warnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeDropShipDtlLotNum_input:
   """ Required : 
   ds
   ipLotNum
   ipPackLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.ipLotNum:str = obj["ipLotNum"]
      """  The LotNum value  """  
      self.ipPackLine:int = obj["ipPackLine"]
      """  Selected pack line  """  
      pass

class ChangeDropShipDtlLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDropShipDtlOurQty_input:
   """ Required : 
   ds
   ipOurQty
   ipPackLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.ipOurQty:int = obj["ipOurQty"]
      """  The OurQty value  """  
      self.ipPackLine:int = obj["ipPackLine"]
      """  Selected pack line  """  
      pass

class ChangeDropShipDtlOurQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.warnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeDropShipDtlPOLine_input:
   """ Required : 
   ds
   ipPOLine
   ipPackLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.ipPOLine:int = obj["ipPOLine"]
      """  The POLine value  """  
      self.ipPackLine:int = obj["ipPackLine"]
      """  Selected pack line  """  
      pass

class ChangeDropShipDtlPOLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.serialWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeDropShipDtlPONum_input:
   """ Required : 
   ds
   ipPONum
   ipPackLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.ipPONum:int = obj["ipPONum"]
      """  The PONum value  """  
      self.ipPackLine:int = obj["ipPackLine"]
      """  Selected pack line  """  
      pass

class ChangeDropShipDtlPONum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDropShipDtlPORelNum_input:
   """ Required : 
   ds
   ipPORelNum
   ipPackLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.ipPORelNum:int = obj["ipPORelNum"]
      """  The PORelNum value  """  
      self.ipPackLine:int = obj["ipPackLine"]
      """  Selected pack line  """  
      pass

class ChangeDropShipDtlPORelNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDropShipDtlVendorQty_input:
   """ Required : 
   ds
   ipVendorQty
   ipPackLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.ipVendorQty:int = obj["ipVendorQty"]
      """  The VendorQty value  """  
      self.ipPackLine:int = obj["ipPackLine"]
      """  Selected pack line  """  
      pass

class ChangeDropShipDtlVendorQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.warnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeDropShipHeadPONum_input:
   """ Required : 
   ipPONum
   ds
   """  
   def __init__(self, obj):
      self.ipPONum:int = obj["ipPONum"]
      """  New PONum  """  
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class ChangeDropShipHeadPONum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDropShipHeadShipToCustNum_input:
   """ Required : 
   ipShipToCustNum
   ds
   """  
   def __init__(self, obj):
      self.ipShipToCustNum:int = obj["ipShipToCustNum"]
      """  New ShipToCustNum  """  
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class ChangeDropShipHeadShipToCustNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDropShipHeadShipToNum_input:
   """ Required : 
   ipShipToNum
   ds
   """  
   def __init__(self, obj):
      self.ipShipToNum:str = obj["ipShipToNum"]
      """  New ShipToNum  """  
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class ChangeDropShipHeadShipToNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateMassDropShipDtlWithoutComplete_input:
   """ Required : 
   ipVendorNum
   ipPurPoint
   ipPackSlip
   ipPONum
   ds
   """  
   def __init__(self, obj):
      self.ipVendorNum:int = obj["ipVendorNum"]
      self.ipPurPoint:str = obj["ipPurPoint"]
      self.ipPackSlip:str = obj["ipPackSlip"]
      self.ipPONum:int = obj["ipPONum"]
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class CreateMassDropShipDtlWithoutComplete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warnMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateMassDropShipDtl_input:
   """ Required : 
   ipVendorNum
   ipPurPoint
   ipPackSlip
   ipPONum
   ds
   """  
   def __init__(self, obj):
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  The VendorNum value  """  
      self.ipPurPoint:str = obj["ipPurPoint"]
      """  The PurPoint value  """  
      self.ipPackSlip:str = obj["ipPackSlip"]
      """  The PackSlip value  """  
      self.ipPONum:int = obj["ipPONum"]
      """  The PONum value  """  
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class CreateMassDropShipDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warnMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteDropShipDtl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class DeleteDropShipDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_DropShipDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  The unique identifier for the drop shipment.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order being drop shipped.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the purchase order being drop shipped.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  The release number of the purchase order being drop shipped.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Num defaulted from the PO release.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Supplier's part num. Defaulted from the PO release.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Defaulted from the PO release.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Defaulted from the PO release.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Defaulted from the PO release.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different Part number than the users internal part number. Defaulted from the SO release.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Field that contains the customer's revision.  """  
      self.OurQty:int = obj["OurQty"]
      """  This field will be automatically defaulted to the remaining quantity to be drop shipped. Receipt quantity in our unit of measure.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Holds any comments about the order line being shipped. This gets duplicated from the OrderDtl.ShipComment.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  These comments will be copied into the Invoice detail.  """  
      self.HeaderShipComment:str = obj["HeaderShipComment"]
      """  Packing slip comments.  These are comments off of the invoice header.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Complete:bool = obj["Complete"]
      """  This flag will be automatically set if the remaining quantity to be drop shipped equals to zero and will be automatically turned off if the remaining quantity is greater than zero.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier that drops shipped the good from their inventory to our customer.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point ID.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from PODetail LineDesc.  """  
      self.OurUnitCost:int = obj["OurUnitCost"]
      """  Unit cost base on our unit of measure. Default can be obtained from PODetail.UnitCost.  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  Item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.PUM:str = obj["PUM"]
      """  Vendor's selling Unit of Measure.  """  
      self.VendorUnitCost:int = obj["VendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the POdetail record.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt date. Mirror image of related DropShipHead.ReceiptDate.  """  
      self.APInvoiced:bool = obj["APInvoiced"]
      """  A\P invoice entry sets this to "Yes" when the drop ship detail line is invoiced.  """  
      self.ARInvoiced:bool = obj["ARInvoiced"]
      """  A\R invoice entry sets this to "Yes" when the receipt detail line is invoiced.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Invoice Number from corresponding APInvHed record.  """  
      self.APInvoiceLine:int = obj["APInvoiceLine"]
      """  Invoice Number Line from corresponding APInvDtl record.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  Invoice Number from corresponding InvcHead record.  """  
      self.ARInvoiceLine:int = obj["ARInvoiceLine"]
      """  Invoice Number Line from corresponding InvcDtl record.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  """  
      self.TranReference:str = obj["TranReference"]
      """  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.ReceivedShipped:bool = obj["ReceivedShipped"]
      """  Identifies a drop shipment line that is complete and ready to be invoiced.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  For Warranty drop shipments.  Defaults as DropShipHead.ReceiptDate. But can be maintained from the Service Call center.  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The # of days, months, years the Labor is covered by warranty  """  
      self.LaborExpiration:str = obj["LaborExpiration"]
      """  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Whether the duration of warranty  is "Days"," Months"," years".  """  
      self.LastExpiration:str = obj["LastExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The # of days, months, years the material is covered by warranty  """  
      self.MaterialExpiration:str = obj["MaterialExpiration"]
      """  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Whether the duration of warranty  is for "Days", " Months", "years".  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The # of days, months, years the Misc. Charges are covered by warranty  """  
      self.MiscExpiration:str = obj["MiscExpiration"]
      """  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.MiscMod:str = obj["MiscMod"]
      """  Whether the duration of warranty  is for "Days"," Months"," years".  """  
      self.Onsite:bool = obj["Onsite"]
      """  This warranty covers On site visits  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Warranty comments.  """  
      self.CustNum:int = obj["CustNum"]
      """  Duplicated from DropShipHead.CustNum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Duplicated from DropShipHead.ShipTotNum.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Duplicated from DropShipHead.ShipToCustNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  ProjProcessed  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.MXEstValue:int = obj["MXEstValue"]
      """  Estimated Value  """  
      self.MXEstValueCurrencyCode:str = obj["MXEstValueCurrencyCode"]
      """  Estimated Value Currency  """  
      self.MXTotalNetWeightKGM:int = obj["MXTotalNetWeightKGM"]
      """  Total Net Weight in kilograms  """  
      self.MXHazardousShipment:bool = obj["MXHazardousShipment"]
      """  Hazardous Shipment  """  
      self.MXHazardousType:str = obj["MXHazardousType"]
      """  Hazardous Type  """  
      self.MXPackageType:str = obj["MXPackageType"]
      """  Package Type  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.POComment:str = obj["POComment"]
      self.RemainingQty:int = obj["RemainingQty"]
      self.RemainingQtyUOM:str = obj["RemainingQtyUOM"]
      self.RequestedQty:int = obj["RequestedQty"]
      self.RequestedQtyUOM:str = obj["RequestedQtyUOM"]
      self.ShippedToDateQty:int = obj["ShippedToDateQty"]
      self.ShippedToDateQtyUOM:str = obj["ShippedToDateQtyUOM"]
      self.ThisShipmentQty:int = obj["ThisShipmentQty"]
      self.ThisShipmentQtyUOM:str = obj["ThisShipmentQtyUOM"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.CostPerFactor:int = obj["CostPerFactor"]
      """  Interger value of CostPerCode  """  
      self.BillToAddrFormatted:str = obj["BillToAddrFormatted"]
      """  The formatted bill to address  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AttributeSetIDDescription:str = obj["AttributeSetIDDescription"]
      self.AttributeSetIDShortDescription:str = obj["AttributeSetIDShortDescription"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DropShipHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PackSlip:str = obj["PackSlip"]
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

class Erp_Tablesets_DropShipHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  The unique identifier for the drop shipment.  """  
      self.PONum:int = obj["PONum"]
      """  The number of the purchase order that corresponds with the drop shipped goods.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier that drops shipped the good from their inventory to our customer.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point ID.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ship to num related to this drop shipment.  """  
      self.ReceivedShipped:bool = obj["ReceivedShipped"]
      """  Identifies a drop shipment that is complete and ready to be invoiced.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  The user who created the drop shipment. This field will be auto populated when a user saves a new drop shipment.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  The date when the drop shipment was created. This field will be auto populated when a user saves a new drop shipment.  """  
      self.ReceivePerson:str = obj["ReceivePerson"]
      """  The user who marked the drop shipment as Received/Shipped. This field will be auto populated when a user turns on the received/shipped flag.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Date when the drop shipment was marked as Received/Shipped. This field will be auto populated. This field will be auto populated when a user turns on the received/shipped flag.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The ship via used to ship the goods from our supplier to our customer. This field will be defaulted from the PO selected in the above.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  The tracking number used to track the shipment from our supplier to our customer.  """  
      self.APInvoiced:bool = obj["APInvoiced"]
      """  This flag will be set once the packing slip has been invoiced in AP Invoice.  """  
      self.ARInvoiced:bool = obj["ARInvoiced"]
      """  This flag will be set on once the packing slip has been invoiced in AR Invoice.  """  
      self.ShipmentPackNum:int = obj["ShipmentPackNum"]
      """  Pack Num of the regular shipment created when flag ReceivedShipped is set.  """  
      self.ReceiptPackSlip:str = obj["ReceiptPackSlip"]
      """  Packing Slip of the regular receipt created when flag ReceivedShipped is set.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Pack comments.  """  
      self.ReceiptComment:str = obj["ReceiptComment"]
      """  Contains comments about the overall Receipt.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer associated to the Drop Shioment.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer primary billing contact.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that drop shipment was made from/to  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.AddrList:str = obj["AddrList"]
      """  Address Information from Vendor or VendorPP  """  
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      """  Address Information from ShipToNum  """  
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.BillAddr:str = obj["BillAddr"]
      """  Address information for DropShipHead.CustNum  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.PurPointCity:str = obj["PurPointCity"]
      """  City portion of the address  """  
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      """  First address line  """  
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      """  Second address line  """  
      self.PurPointCountry:str = obj["PurPointCountry"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.PurPointState:str = obj["PurPointState"]
      """  State portion of the address  """  
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      """  Third address line  """  
      self.PurPointName:str = obj["PurPointName"]
      """  Purchase Point Name...can't be blank.  """  
      self.PurPointZip:str = obj["PurPointZip"]
      """  Postal Code or Zip code portion of the address  """  
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      """  The full name of the customer.  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
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
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DropShipHeadListTableset:
   def __init__(self, obj):
      self.DropShipHeadList:list[Erp_Tablesets_DropShipHeadListRow] = obj["DropShipHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DropShipHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  The unique identifier for the drop shipment.  """  
      self.PONum:int = obj["PONum"]
      """  The number of the purchase order that corresponds with the drop shipped goods.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier that drops shipped the good from their inventory to our customer.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point ID.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ship to num related to this drop shipment.  """  
      self.ReceivedShipped:bool = obj["ReceivedShipped"]
      """  Identifies a drop shipment that is complete and ready to be invoiced.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  The user who created the drop shipment. This field will be auto populated when a user saves a new drop shipment.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  The date when the drop shipment was created. This field will be auto populated when a user saves a new drop shipment.  """  
      self.ReceivePerson:str = obj["ReceivePerson"]
      """  The user who marked the drop shipment as Received/Shipped. This field will be auto populated when a user turns on the received/shipped flag.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Date when the drop shipment was marked as Received/Shipped. This field will be auto populated. This field will be auto populated when a user turns on the received/shipped flag.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The ship via used to ship the goods from our supplier to our customer. This field will be defaulted from the PO selected in the above.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  The tracking number used to track the shipment from our supplier to our customer.  """  
      self.APInvoiced:bool = obj["APInvoiced"]
      """  This flag will be set once the packing slip has been invoiced in AP Invoice.  """  
      self.ARInvoiced:bool = obj["ARInvoiced"]
      """  This flag will be set on once the packing slip has been invoiced in AR Invoice.  """  
      self.ShipmentPackNum:int = obj["ShipmentPackNum"]
      """  Pack Num of the regular shipment created when flag ReceivedShipped is set.  """  
      self.ReceiptPackSlip:str = obj["ReceiptPackSlip"]
      """  Packing Slip of the regular receipt created when flag ReceivedShipped is set.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Pack comments.  """  
      self.ReceiptComment:str = obj["ReceiptComment"]
      """  Contains comments about the overall Receipt.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer associated to the Drop Shioment.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer primary billing contact.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that drop shipment was made from/to  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
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
      """  Folio  """  
      self.MXFolio:str = obj["MXFolio"]
      """  Folio  """  
      self.MXETD:str = obj["MXETD"]
      """  Estimated Date and Time of Departure  """  
      self.MXETA:str = obj["MXETA"]
      """  Estimated Date and Time of Departure  """  
      self.MXDistance:int = obj["MXDistance"]
      """  Distance in Km  """  
      self.MXPermitType:str = obj["MXPermitType"]
      """  Permit Type  """  
      self.MXPermitNum:str = obj["MXPermitNum"]
      """  Permit Number  """  
      self.MXCartaPorteStatus:str = obj["MXCartaPorteStatus"]
      """  Carta Porte Status  """  
      self.MXVehicleLicensePlate:str = obj["MXVehicleLicensePlate"]
      """  Vehicle License Plate  """  
      self.MXVehicleType:str = obj["MXVehicleType"]
      """  Vehicle Type  """  
      self.MXVehicleYear:int = obj["MXVehicleYear"]
      """  Vehicle Year  """  
      self.MXDriverID:str = obj["MXDriverID"]
      """  Driver  """  
      self.MXCancelFiscalFolio:str = obj["MXCancelFiscalFolio"]
      """  MXCancelFiscalFolio  """  
      self.EDIShipReferenceType:str = obj["EDIShipReferenceType"]
      """  Name of the ship reference that is going to be stored.  """  
      self.EDIShipReferenceData:str = obj["EDIShipReferenceData"]
      """  Data this is going to be stored as ship reference.  """  
      self.EDIEstimatedDockDate:str = obj["EDIEstimatedDockDate"]
      """  Estimated time when the shipment will arrive.  """  
      self.AddrList:str = obj["AddrList"]
      """  Address Information from Vendor or VendorPP  """  
      self.BillAddr:str = obj["BillAddr"]
      """  Address information for DropShipHead.CustNum  """  
      self.CreditCardMessage:str = obj["CreditCardMessage"]
      """  This field temporarily holds certain message(s) returned by credit card processing logic for internal processing.  """  
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      """  Address Information from ShipToNum  """  
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.SupplierNameAddrFormatted:str = obj["SupplierNameAddrFormatted"]
      """  The formatted supplier name and address from AddrList  """  
      self.ShipToAddrFormatted:str = obj["ShipToAddrFormatted"]
      self.BillToAddrFormatted:str = obj["BillToAddrFormatted"]
      """  The formatted bill to address  """  
      self.MXETADate:str = obj["MXETADate"]
      """  Estimated Date of Arrival  """  
      self.MXETATime:int = obj["MXETATime"]
      """  Estimated Time of Arrival  """  
      self.MXETDDate:str = obj["MXETDDate"]
      """  Estimated Date of Departure  """  
      self.MXETDTime:int = obj["MXETDTime"]
      """  Estimated Time of Departure  """  
      self.MXVehicleWeight:int = obj["MXVehicleWeight"]
      """  Vehicle Weight (in tons)  """  
      self.MXIdCCP:str = obj["MXIdCCP"]
      """  A unique Carta Porte identification number assigned by Epicor  """  
      self.MXCustomsRegime:str = obj["MXCustomsRegime"]
      """  Customs Regime for Export transaction.  """  
      self.MXReverseLogistics:bool = obj["MXReverseLogistics"]
      """  Check box to specify the use of reverse logistic, collection or devolution services when shipping goods.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BTCustNumInactive:bool = obj["BTCustNumInactive"]
      self.CustNumInactive:bool = obj["CustNumInactive"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointState:str = obj["PurPointState"]
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      self.ShipToCustNumInactive:bool = obj["ShipToCustNumInactive"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DropShipHeadTrailerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor Number  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Supplier Purchase Point  """  
      self.PackSlip:str = obj["PackSlip"]
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

class Erp_Tablesets_DropShipTableset:
   def __init__(self, obj):
      self.DropShipHead:list[Erp_Tablesets_DropShipHeadRow] = obj["DropShipHead"]
      self.DropShipHeadAttch:list[Erp_Tablesets_DropShipHeadAttchRow] = obj["DropShipHeadAttch"]
      self.DropShipDtl:list[Erp_Tablesets_DropShipDtlRow] = obj["DropShipDtl"]
      self.DropShipHeadTrailer:list[Erp_Tablesets_DropShipHeadTrailerRow] = obj["DropShipHeadTrailer"]
      self.MXDropShipHeadInsurance:list[Erp_Tablesets_MXDropShipHeadInsuranceRow] = obj["MXDropShipHeadInsurance"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.PendingDropShipDtl:list[Erp_Tablesets_PendingDropShipDtlRow] = obj["PendingDropShipDtl"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
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

class Erp_Tablesets_MXDropShipHeadInsuranceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.PurPoint:str = obj["PurPoint"]
      """  PurPoint  """  
      self.PackSlip:str = obj["PackSlip"]
      """  PackSlip  """  
      self.InsuranceSeq:int = obj["InsuranceSeq"]
      """  InsuranceSeq  """  
      self.Type:str = obj["Type"]
      """  Type  """  
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

class Erp_Tablesets_OrderShipmentsRow:
   def __init__(self, obj):
      self.SellingShipmentQty:int = obj["SellingShipmentQty"]
      self.SellingShipmentUM:str = obj["SellingShipmentUM"]
      self.DisplayInvQty:int = obj["DisplayInvQty"]
      """  OurInventoryShipQty * DimConvFactor - update inplace of OurInventoryShipQty  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  External field to be used in the SalesOrder Tracker to show the user the InvoiceNum linked to the  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.   This field comes directly from the table ShipHead.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  This field comes directly from the ShipHead table.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  This field comes directly from the ShipHead table.  """  
      self.InvLegalNumber:str = obj["InvLegalNumber"]
      """  The invoice legal number.  """  
      self.OrderRelOurReqQty:int = obj["OrderRelOurReqQty"]
      self.PartCompany:str = obj["PartCompany"]
      self.PartPartNum:str = obj["PartPartNum"]
      self.KitFlag:str = obj["KitFlag"]
      """  Sales Kit flag. C = 'Component' P = 'Parent'.  """  
      self.KitCompIssue:bool = obj["KitCompIssue"]
      self.KitBackFlush:bool = obj["KitBackFlush"]
      self.KitCompShipComplete:bool = obj["KitCompShipComplete"]
      self.ExtJobNum:str = obj["ExtJobNum"]
      self.LinkMsg:str = obj["LinkMsg"]
      self.PONum:str = obj["PONum"]
      self.KitQtyFromInvEnabled:bool = obj["KitQtyFromInvEnabled"]
      self.KitParentIssue:bool = obj["KitParentIssue"]
      self.KitPartNum:str = obj["KitPartNum"]
      self.KitBinNum:str = obj["KitBinNum"]
      self.KitDescription:str = obj["KitDescription"]
      self.KitLotNum:str = obj["KitLotNum"]
      self.KitSerialTracked:bool = obj["KitSerialTracked"]
      self.KitTrackLots:bool = obj["KitTrackLots"]
      self.KitWarehouse:str = obj["KitWarehouse"]
      self.KitWarehouseCodeDesc:str = obj["KitWarehouseCodeDesc"]
      self.KitWhseList:str = obj["KitWhseList"]
      self.KitBinNumEnabled:bool = obj["KitBinNumEnabled"]
      self.PartAESExp:str = obj["PartAESExp"]
      """  Used by freight web service  """  
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
      """  Used by freight  web service  """  
      self.PartSchedBcode:str = obj["PartSchedBcode"]
      """  Used by freight web service  """  
      self.PartUseHTSDesc:bool = obj["PartUseHTSDesc"]
      """  Used by freight web service  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this shipment detail line is linked to.  Must be valid in the OrderDtl file.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  """  
      self.OurJobShipQty:int = obj["OurJobShipQty"]
      """  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This quantity is in the IUM unit of measure.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that supplied the quantity that was shipped. Defaulted from OrderRel.JobNum.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Generated from field LineDesc  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.  The default should be retrieved from the OrderDtl.WareHseCode. .  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The shipto number. Used for warranty validation.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the Packing Slip is complete and ready for invoicing.  This is a mirror image of ShipHead.ReadyToInvoice.  """  
      self.HeaderShipComment:str = obj["HeaderShipComment"]
      self.KitParentLine:int = obj["KitParentLine"]
      self.ChangedBy:str = obj["ChangedBy"]
      self.ChangeDate:str = obj["ChangeDate"]
      self.ChangeTime:int = obj["ChangeTime"]
      self.InventoryShipUOM:str = obj["InventoryShipUOM"]
      self.JobShipUOM:str = obj["JobShipUOM"]
      self.TrackSerialNum:bool = obj["TrackSerialNum"]
      self.JobLotNum:str = obj["JobLotNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.SysRevID:int = obj["SysRevID"]
      self.BinType:str = obj["BinType"]
      self.NotComplaint:bool = obj["NotComplaint"]
      """  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      self.Discount:int = obj["Discount"]
      self.DocDiscount:int = obj["DocDiscount"]
      self.PricePerCode:str = obj["PricePerCode"]
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      self.ExtPrice:int = obj["ExtPrice"]
      self.DocExtPrice:int = obj["DocExtPrice"]
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      self.UnitPrice:int = obj["UnitPrice"]
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      self.PickedAutoAllocatedQty:int = obj["PickedAutoAllocatedQty"]
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      self.OurRemainQty:int = obj["OurRemainQty"]
      self.KitMassIssue:bool = obj["KitMassIssue"]
      self.LineContentValue:int = obj["LineContentValue"]
      """  Individual line content value that is used by the freight web service to calculate the total order value.  """  
      self.EnableJobFields:bool = obj["EnableJobFields"]
      """  Logical indicating if receipt to a job is allowed.  This is determined by either the xasyst.shipnojob field or whether or not the sales order is linked to a job.  """  
      self.OrderHold:bool = obj["OrderHold"]
      """  Indicates if Order is on Hold  """  
      self.EnableInvSerialBtn:bool = obj["EnableInvSerialBtn"]
      self.EnableMfgSerialBtn:bool = obj["EnableMfgSerialBtn"]
      self.EnablePOSerialBtn:bool = obj["EnablePOSerialBtn"]
      self.LineTax:int = obj["LineTax"]
      self.DocLineTax:int = obj["DocLineTax"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.Rpt1LineTax:int = obj["Rpt1LineTax"]
      self.Rpt2LineTax:int = obj["Rpt2LineTax"]
      self.Rpt3LineTax:int = obj["Rpt3LineTax"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PackSlip:str = obj["PackSlip"]
      self.CustNumName:str = obj["CustNumName"]
      self.PackNumShipStatus:str = obj["PackNumShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """  This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The sales order number that this detail shipment line is linked to. This is not directly maintainable, It is carried forward through from the ShipHead.OrderNum field.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OrderShipmentsTableset:
   def __init__(self, obj):
      self.OrderShipments:list[Erp_Tablesets_OrderShipmentsRow] = obj["OrderShipments"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PendingDropShipDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LineDesc:str = obj["LineDesc"]
      self.OurQuantity:int = obj["OurQuantity"]
      self.PartNum:str = obj["PartNum"]
      self.POLine:int = obj["POLine"]
      self.PONum:int = obj["PONum"]
      self.PurPoint:str = obj["PurPoint"]
      self.UOM:str = obj["UOM"]
      self.VendorNum:int = obj["VendorNum"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.PORelNum:int = obj["PORelNum"]
      self.PackSlip:str = obj["PackSlip"]
      self.RemainingQty:int = obj["RemainingQty"]
      """  The Remaining Qty between Supplier Qty and Received Qty  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  The Attribute Class for the part.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.RevisionNum:str = obj["RevisionNum"]
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

class Erp_Tablesets_UpdExtDropShipTableset:
   def __init__(self, obj):
      self.DropShipHead:list[Erp_Tablesets_DropShipHeadRow] = obj["DropShipHead"]
      self.DropShipHeadAttch:list[Erp_Tablesets_DropShipHeadAttchRow] = obj["DropShipHeadAttch"]
      self.DropShipDtl:list[Erp_Tablesets_DropShipDtlRow] = obj["DropShipDtl"]
      self.DropShipHeadTrailer:list[Erp_Tablesets_DropShipHeadTrailerRow] = obj["DropShipHeadTrailer"]
      self.MXDropShipHeadInsurance:list[Erp_Tablesets_MXDropShipHeadInsuranceRow] = obj["MXDropShipHeadInsurance"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.PendingDropShipDtl:list[Erp_Tablesets_PendingDropShipDtlRow] = obj["PendingDropShipDtl"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DropShipTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DropShipTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DropShipTableset] = obj["returnObj"]
      pass

class GetLegalNumGenOpts_input:
   """ Required : 
   ipVendorNum
   ipPurPoint
   ipPackSlip
   ds
   """  
   def __init__(self, obj):
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  Vendor No  """  
      self.ipPurPoint:str = obj["ipPurPoint"]
      """  Purchase point  """  
      self.ipPackSlip:str = obj["ipPackSlip"]
      """  Packing slip  """  
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class GetLegalNumGenOpts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_DropShipHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMXCartaPortePOInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class GetMXCartaPortePOInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDropShipDtl_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      pass

class GetNewDropShipDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDropShipHeadAttch_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      pass

class GetNewDropShipHeadAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDropShipHeadTrailer_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      pass

class GetNewDropShipHeadTrailer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDropShipHead_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      pass

class GetNewDropShipHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMXDropShipHeadInsurance_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      pass

class GetNewMXDropShipHeadInsurance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOrderShipments_input:
   """ Required : 
   ds
   orderNum
   orderLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderShipmentsTableset] = obj["ds"]
      self.orderNum:int = obj["orderNum"]
      """  Order Number  """  
      self.orderLine:int = obj["orderLine"]
      """  Order Line  """  
      pass

class GetOrderShipments_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderShipmentsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPOInfo_input:
   """ Required : 
   ds
   poNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.poNum:int = obj["poNum"]
      """  Proposed Purchase Order Number  """  
      pass

class GetPOInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.vendorNum:int = obj["parameters"]
      self.purPoint:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPendingDtl_input:
   """ Required : 
   ds
   ipPONum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.ipPONum:int = obj["ipPONum"]
      """  The PO number  """  
      pass

class GetPendingDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPurPointInfo_input:
   """ Required : 
   ds
   purPoint
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.purPoint:str = obj["purPoint"]
      """  Proposed Purchase Point value  """  
      pass

class GetPurPointInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDropShipHead
   whereClauseDropShipHeadAttch
   whereClauseDropShipDtl
   whereClauseDropShipHeadTrailer
   whereClauseMXDropShipHeadInsurance
   whereClauseLegalNumGenOpts
   whereClausePendingDropShipDtl
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDropShipHead:str = obj["whereClauseDropShipHead"]
      self.whereClauseDropShipHeadAttch:str = obj["whereClauseDropShipHeadAttch"]
      self.whereClauseDropShipDtl:str = obj["whereClauseDropShipDtl"]
      self.whereClauseDropShipHeadTrailer:str = obj["whereClauseDropShipHeadTrailer"]
      self.whereClauseMXDropShipHeadInsurance:str = obj["whereClauseMXDropShipHeadInsurance"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.whereClausePendingDropShipDtl:str = obj["whereClausePendingDropShipDtl"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DropShipTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParams_input:
   """ Required : 
   ipPartNum
   ipAttributeSetID
   ipQuantity
   ipUOM
   ipVendNum
   ipVendPP
   ipPackSlip
   ipPackSlipLine
   ipPONum
   ipPOLine
   ipPORelNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      self.ipAttributeSetID:int = obj["ipAttributeSetID"]
      self.ipQuantity:int = obj["ipQuantity"]
      self.ipUOM:str = obj["ipUOM"]
      self.ipVendNum:int = obj["ipVendNum"]
      self.ipVendPP:str = obj["ipVendPP"]
      self.ipPackSlip:str = obj["ipPackSlip"]
      self.ipPackSlipLine:int = obj["ipPackSlipLine"]
      self.ipPONum:int = obj["ipPONum"]
      self.ipPOLine:int = obj["ipPOLine"]
      self.ipPORelNum:int = obj["ipPORelNum"]
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

class GetShipToAddressMultiKey_input:
   """ Required : 
   poNum
   custNum
   shipToNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      """  PO Num  """  
      self.custNum:int = obj["custNum"]
      """  Cust Num  """  
      self.shipToNum:str = obj["shipToNum"]
      """  Ship To Num  """  
      pass

class GetShipToAddressMultiKey_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.shipToListMult:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetTranDocTypeID_input:
   """ Required : 
   ipTranDocTypeID
   ds
   """  
   def __init__(self, obj):
      self.ipTranDocTypeID:str = obj["ipTranDocTypeID"]
      """  Transaction Document Type  """  
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class GetTranDocTypeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetVendorInfo_input:
   """ Required : 
   ds
   vendorID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.vendorID:str = obj["vendorID"]
      """  Proposed Vendor ID value  """  
      pass

class GetVendorInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.vendorNum:int = obj["parameters"]
      self.purPoint:str = obj["parameters"]
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

class InitializeMultiKeySearchData_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class InitializeMultiKeySearchData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MarkShipmentLines_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class MarkShipmentLines_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMultiKeySearchPONum_input:
   """ Required : 
   ipPONum
   ds
   """  
   def __init__(self, obj):
      self.ipPONum:int = obj["ipPONum"]
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class OnChangeMultiKeySearchPONum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class OnChangeShipViaCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingNumberOfPieces_input:
   """ Required : 
   numberOfPieces
   ipPackLine
   ds
   """  
   def __init__(self, obj):
      self.numberOfPieces:int = obj["numberOfPieces"]
      self.ipPackLine:int = obj["ipPackLine"]
      """  Selected pack line  """  
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class OnChangingNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.warnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class PostUpdate_input:
   """ Required : 
   ipPackSlip
   ipVendorNum
   ipPurPoint
   """  
   def __init__(self, obj):
      self.ipPackSlip:str = obj["ipPackSlip"]
      """  Drop Ship Pack Slip  """  
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  Supplier  """  
      self.ipPurPoint:str = obj["ipPurPoint"]
      """  Purchase Point  """  
      pass

class PostUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreChangeDropShipDtlLotNum_input:
   """ Required : 
   ds
   ipLotNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.ipLotNum:str = obj["ipLotNum"]
      """  The LotNum value  """  
      pass

class PreChangeDropShipDtlLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.questionMsg:str = obj["parameters"]
      self.errorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreCreateMassReceipt_input:
   """ Required : 
   ipVendorNum
   ipPurPoint
   ipPackSlip
   ipPONum
   ds
   """  
   def __init__(self, obj):
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  The VendorNum value  """  
      self.ipPurPoint:str = obj["ipPurPoint"]
      """  The PurPoint value  """  
      self.ipPackSlip:str = obj["ipPackSlip"]
      """  The PackSlip value  """  
      self.ipPONum:int = obj["ipPONum"]
      """  The PONum value  """  
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class PreCreateMassReceipt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warnMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreUpdateDropShipDtl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class PreUpdateDropShipDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      self.qMessageStr:str = obj["parameters"]
      self.sMessageStr:str = obj["parameters"]
      pass

      """  output parameters  """  

class UndoShipAll_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class UndoShipAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDropShipTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDropShipTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   ipPartNum
   ipAttributeSetID
   ipSerialNo
   ipVendNum
   ipPurPoint
   ipPackNum
   ipPONum
   ipPOLine
   ipPORelNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      self.ipAttributeSetID:int = obj["ipAttributeSetID"]
      self.ipSerialNo:str = obj["ipSerialNo"]
      self.ipVendNum:int = obj["ipVendNum"]
      self.ipPurPoint:str = obj["ipPurPoint"]
      self.ipPackNum:str = obj["ipPackNum"]
      self.ipPONum:int = obj["ipPONum"]
      self.ipPOLine:int = obj["ipPOLine"]
      self.ipPORelNum:int = obj["ipPORelNum"]
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

class VoidLegalNumber_input:
   """ Required : 
   ipVendorNum
   ipPurPoint
   ipPackSlip
   ipVoidedReason
   """  
   def __init__(self, obj):
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  Vendor No  """  
      self.ipPurPoint:str = obj["ipPurPoint"]
      """  Purchase point  """  
      self.ipPackSlip:str = obj["ipPackSlip"]
      """  Packing slip  """  
      self.ipVoidedReason:str = obj["ipVoidedReason"]
      """  Reason for the void  """  
      pass

class VoidLegalNumber_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DropShipTableset] = obj["returnObj"]
      pass

class buildShipToAddressFieldMultiKey_input:
   """ Required : 
   ipPONum
   ipShipToCustNum
   ipShipToNum
   ipAddrList
   """  
   def __init__(self, obj):
      self.ipPONum:int = obj["ipPONum"]
      self.ipShipToCustNum:int = obj["ipShipToCustNum"]
      self.ipShipToNum:str = obj["ipShipToNum"]
      self.ipAddrList:str = obj["ipAddrList"]
      pass

class buildShipToAddressFieldMultiKey_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class processExtraCreditCharge_input:
   """ Required : 
   docCmAmount
   depCheckRef
   lastInvoiceNum
   """  
   def __init__(self, obj):
      self.docCmAmount:int = obj["docCmAmount"]
      self.depCheckRef:str = obj["depCheckRef"]
      self.lastInvoiceNum:int = obj["lastInvoiceNum"]
      pass

class processExtraCreditCharge_output:
   def __init__(self, obj):
      pass

